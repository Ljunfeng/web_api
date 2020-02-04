import json

data = {'id':1,'name':'woia','passowrd':'666'}

print(type(data))

#将python类型转化json类型
json_str = json.dumps(data)
print(type(json_str))
print(json_str)

#将json类型转陈成python类型
json_load = json.loads(json_str)
print(type(json_load))


#json文件处理。
#写入json数据到文件
with open('data.json','w') as f :
    json.dump(json_str,f)


#读取json数据文件
with open('data.json','r') as f1:
    data = json.load(f1)
    print(data)