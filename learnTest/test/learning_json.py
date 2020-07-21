import json

data="""
{
"hours":[
                {
                    "hours":"08时",
                    "wea":"晴",
                    "tem":"20",
                    "win":"东风",
                    "win_speed":"<3级"
                },
                {
                    "hours":"09时",
                    "wea":"晴",
                    "tem":"21",
                    "win":"南风",
                    "win_speed":"<3级"
                },
                {
                    "hours":"10时",
                    "wea":"晴",
                    "tem":"25",
                    "win":"西南风",
                    "win_speed":"<3级"
                },
                {
                    "hours":"11时",
                    "wea":"晴",
                    "tem":"28",
                    "win":"东风",
                    "win_speed":"<3级"
                },
                {
                    "hours":"12时",
                    "wea":"晴",
                    "tem":"30",
                    "win":"东北风",
                    "win_speed":"<3级"
                },
                {
                    "hours":"13时",
                    "wea":"晴",
                    "tem":"31",
                    "win":"东北风",
                    "win_speed":"3-4级"
                },
                {
                    "hours":"14时",
                    "wea":"晴",
                    "tem":"33",
                    "win":"东风",
                    "win_speed":"<3级"
                }
            ]
}

"""


weather=json.loads(data)
list1=weather.get('hours')
print(list1)
for item in list1:
    print(item.get('hours'))
    pass