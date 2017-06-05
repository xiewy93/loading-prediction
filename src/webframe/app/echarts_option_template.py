# -*- coding: utf-8 -*-
from __future__ import division

bar_option1 = {
            'title': {
                'text': '测试'
            },
            'tooltip': {},
            'legend': {
                'data':['负荷']
            },
            'xAxis': {
                'data': ["周末","非周末","节假日","工作日","非工作日","夏天"]
            },
            'yAxis': {},
            'series': [{
                'name': '负荷量',
                'type': 'bar',
                'data': [5, 20, 36, 10, 10, 20]
            }]
        }
def create_line_option(df,n):
    option_dict=dict()
    option_dict = {
    'title' : {	
        'text': '某用户四季的负荷比较',
        'left':'center'
    },
    'tooltip' : {
        'trigger': 'axis'
    },
    'legend': {
        'data':list(df.columns),
        'y':'bottom'
    },
    'toolbox': {
        'show' : 'true',
        'feature' : {
            'mark' : {'show': 'true'},
            'dataView' : {'show': 'true', 'readOnly': 'false'},
            'magicType' : {'show': 'true', 'type': ['line', 'bar', 'stack', 'tiled']},
            'restore' : {'show': 'true'},
            'saveAsImage' : {'show': 'true'}
        }
    },
    'calculable' : 'true',
    'xAxis' : [
        {
            'type' : 'category',
            'name' : '时间',
            'boundaryGap' : 'false',
            'data' : list(df.index)
        }
    ],
    'yAxis' : [
        {
            'type' : 'value',
            'name' : '负荷 单位(KW)',
            'axisLabel': {
            'formatter': '{value}'
            }
        }
    ]}
    tempt = []
    for i in range(n):
        tempt.append({
        'name':list(df.columns)[i],
        'type':'line',
        'data':list(df[list(df.columns)[i]])
        })
    option_dict['series'] = tempt
    return option_dict
    
    

#bar_option = create_line_option(df,4)
#if_holidays_option = create_line_option(df1,2)
#weekday_type_option = create_line_option(df2,2)
#holidays_option = create_line_option(df3,7)



line_option = {
    'title': {
        'text': '未来一周走势',
        'subtext': '纯属虚构'
    },
    'tooltip': {
        'trigger': 'axis'
    },
    'legend': {
        'data':['真实负荷','预测负荷']
    },
    'toolbox': {
        'show': True,
        'feature': {
            'dataZoom': {
                'yAxisIndex': 'none'
            },
            'dataView': {'readOnly': False},
            'magicType': {'type': ['line', 'bar']},
            'restore': {},
            'saveAsImage': {}
        }
    },
    'xAxis':  {
        'type': 'category',
        'boundaryGap': False,
        'data': ['周一','周二','周三','周四','周五','周六','周日']
    },
    'yAxis': {
        'type': 'value',
        'axisLabel': {
            'formatter': '{value} °C'
        }
    },
    'series': [
        {
            'name':'真实负荷',
            'type':'line',
            'data':[11, 11, 15, 13, 12, 13, 10]
        },
        {
            'name':'预测负荷',
            'type':'line',
            'data':[1, -2, 2, 5, 3, 2, 0]
        }
    ]
}