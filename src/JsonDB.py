import json
def read_json(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        data= json.load(f)
        f.close()
    return data
    
def write_json(filename, data):
    with open(filename, 'w',encoding='utf-8') as f:
        json.dump(data, f,ensure_ascii=False)
        f.close()