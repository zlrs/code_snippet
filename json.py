import json
dic = {'id': '1003', 'inital': '65'}

# Writing data to str or file
# json.dumps()
# json.dump()
json_str = json.dumps(dic, indent=4, separators=(',', ': '), ensure_ascii=False)
print(json_str)
with open('data.json', 'w') as f:
    json.dump(dic, f)

# Reading data back
# json.loads()
# json.load()
data = json.loads(json_str)
with open('data.json', 'r') as f:
    data = json.load(f)
    
# output:
# {
#     "id": "1003",
#     "inital": "65"
# }

# tutorial:
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html
