# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:55:36 2016

@author: lakinlv
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
from sys import path

#添加工作目录
#path.append('C:\\Users\\lakinlv\\Documents\\pwranalytics\\')


class fillNa:

    #gap是设备产生数据间隔(注意：输入的单位是分钟)
    #根据不同的时间间隔，生成字符串
    #def gen_gap_str(self, gap):
    #    p=24*60/gap
    #    f=str(gap) + 'T'
    #    tp=pd.timedelta_range(start='0 days', periods = p, freq= f)
    #    tp_str=list(tp)
    #    tp_str=[str(i)[7:12] for i in tp_str]
    #    return tp,tp_str
        
    #输入path, filename, sheetname
    #读取excel中单独的指定的一个sheet
    #def read_excel(self, path, fileName, sheetName):
    #    data=pd.read_excel(open(self.path+self.file, 'rb'), sheetname=sheetName)
    #    return data
    
    #定义一个从KWn 到deltatime的转换map
    #def map_kw_ts(self, kw, gap = 15):
    #    kw =  pd.DataFrame({'KW':pd.unique(kw)})
    #    kw['SEQ'] = kw['KW'].str.replace('KW','').astype('int') -1
	# 
    #    ts_gap =  pd.DataFrame({'TGap': self.gen_gap_str(gap)[0]})
    #    ts_gap['SEQ'] = ts_gap.index
	#
    #    kw_ts_map =  pd.merge(kw, ts_gap, on = 'SEQ')
    #    kw_ts_map = kw_ts_map.drop(['SEQ'], axis = 1)
    #    return kw_ts_map
    
	
	#缺失值处理策略
	#填充根据
    #定义一个不包括0的计算均值的方法
    def filiNa_mean_noZero(self,arr):
        return arr[arr!=0].mean()
    #定义一个不包括0的计算均值的方法
    def filiNa_median_noZero(self,arr):
        return arr[arr!=0].median()
        
    #定义分组   
    #返回每一天对应的工作日类型
    def map_get_dateType(self,arr):
        #conver to weekday
        arr = pd.to_datetime(arr)
        #arr = pd.Series(pd.unique(arr))
        wkday = arr.dt.weekday + 1
        #create date map
        weekday_dic = {1:'workday',
                     2:'workday',
                     3:'workday',
                     4:'workday',
                     5:'workday',
                     6:'weekend',
                     7:'weekend'}
        return wkday.map(weekday_dic) #map用在大规模的数据集上很慢
        #daily_wkday = pd.DataFrame({'Date': arr,
        #                            'Weekday': wkday.map(wkday_dic)})
        #return daily_wkday
        
    #返回每一天对应的是一年用电季节峰谷(arr would be ts format)
    def map_peak_valley_season(self, arr):
       arr = pd.to_datetime(arr)
       #arr = pd.Series(pd.unique(arr))
       month = arr.dt.month
       pvs_map = {}
       for i in range(len(month)):
           if 6 <= month[i] <= 8:
               pvs_map[arr[i]] = 'peak'
           else: 
               pvs_map[arr[i]] = 'valley'
       return arr.map(pvs_map)
       #daily_seasonPV = pd.DataFrame({'Date': arr,
       #                                'season_PV': arr.map(pvs_map)})        
       #return daily_seasonPV
       
     #返回每小时对应的是一天内用电的峰谷
    def map_peak_valley_hour(self, arr):
        #提取整点信息
        arr = pd.to_datetime(arr)
        #arr = pd.Series(pd.unique(arr))
        hour = arr.dt.hour
        #定义peak & valley
        pvh_map = {}
        for i in range(len(arr)):
            if 8 <= hour[i] <= 23:
                pvh_map[arr[i]] = 'peak'
            else: 
                pvh_map[arr[i]] = 'valley'
        return arr.map(pvh_map)
        #hourly_dailyPV = pd.DataFrame({'Hour': arr,
        #                               'dailyPV': arr.map(pvh_map)})
        #return hourly_dailyPV                               
    #输入不同分组条件，输出填充后结果
    def fillna_group(self, df, groupList = []):
        grouped = df.groupby(groupList)
        fill_func = lambda g: g.fillna(self.filiNa_median_noZero(g))
        fill_na = grouped.apply(fill_func)
        fill_na.index = np.arange(len(fill_na))
        print 'before fill, the number cells of null is:', df.isnull().sum().sum()
        print 'after fill, the number cells of null is:', fill_na.isnull().sum().sum() 
        return fill_na
        
    #输入不同分组条件，输出填充后结果
    def long_to_wide(self, df, value = [], index = [], column = []):
        wideDF = pd.pivot_table(df, values = value, 
                                index = index, 
                                columns = column)
        wideDF = wideDF.reset_index()
        return wideDF
      
    

