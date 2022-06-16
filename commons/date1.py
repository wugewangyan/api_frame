import json
from datetime import datetime


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


dic = {'time': datetime.now()}
print(dic)
dic_str = json.dumps(dic, cls=DateEncoder)
print(dic_str)