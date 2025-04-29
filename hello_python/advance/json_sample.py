import json
from datetime import datetime
from typing import List

# 1. 基本数据类型序列化
data = {
    "name": "辽宁产串红小番茄",
    "price": 12.8,
    "in_stock": True,
    "varieties": ["串红", "樱桃番茄", "黄珍珠"],
    "weight_grams": None,
    "harvest_date": "2023-10-15"
}

# 序列化为JSON字符串
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print("基本序列化结果:")
print(json_str)

# 从JSON字符串反序列化
parsed_data = json.loads(json_str)
print("\n反序列化后数据:", parsed_data)

# 2. 处理日期等特殊对象
class Product:
    def __init__(self, name: str, expiry_date: datetime):
        self.name = name
        self.expiry_date = expiry_date

# 自定义编码器
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, Product):
            return {"name": obj.name, "expiry_date": obj.expiry_date}
        return super().default(obj)

# 使用自定义编码器
tomato = Product("辽宁串红番茄", datetime(2023, 12, 31))
product_list = {
    "product": tomato,
    "update_time": datetime.now()
}

json_with_date = json.dumps(product_list, cls=CustomEncoder, indent=2)
print("\n含自定义对象的序列化:")
print(json_with_date)

# 3. 从文件读写JSON
# 写入文件
with open('data/tomato.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 从文件读取
with open('data/tomato.json', 'r', encoding='utf-8') as f:
    file_data = json.load(f)
print("\n从文件读取的数据:", file_data)

# 4. 处理复杂结构（嵌套对象/集合）
class Variety:
    def __init__(self, name: str, sugar_content: float):
        self.name = name
        self.sugar_content = sugar_content

class TomatoProduct:
    def __init__(self, name: str, varieties: List[Variety]):
        self.name = name
        self.varieties = varieties

def variety_encoder(obj):
    if isinstance(obj, Variety):
        return {"variety_name": obj.name, "sugar": obj.sugar_content}
    elif isinstance(obj, TomatoProduct):
        return {"product_name": obj.name, "varieties": obj.varieties}
    return obj

product = TomatoProduct(
    "辽宁精品礼盒",
    [Variety("串红", 8.5), Variety("黄珍珠", 7.2)]
)

# 使用default参数处理复杂对象
complex_json = json.dumps(product, default=variety_encoder, indent=2)
print("\n复杂对象序列化结果:")
print(complex_json)


# use ujson library sample
import ujson

# 示例数据 (与之前的例子相同)
data = {
    "name": "辽宁串红小番茄",
    "origin": "辽宁",
    "category": "生鲜",
    "subcategory": "小番茄",
    "variety": "串红",
    "price": 9.99,
    "unit": "500g",
    "specifications": {
        "size": "中等",
        "color": "鲜红",
        "sweetness": "高"
    },
    "packaging": ["盒装", "袋装"],
    "is_organic": False,
    "seasonal": True,
    "available_months": ["6月", "7月", "8月", "9月"],
    "related_products": ["圣女果", "千禧果"],
    "supplier": {
        "name": "辽宁番茄种植合作社",
        "contact": "张先生"
    }
}

# 1. 将 Python 对象序列化为 JSON 字符串
json_string = ujson.dumps(data, ensure_ascii=False, indent=4)  # ensure_ascii=False 支持中文，indent=4 美化输出

print("JSON 字符串:\n", json_string)

# 2. 将 JSON 字符串写入文件 (ujson 没有直接写入文件的方法，需要手动写入)
with open("data/tomato_ujson.json", "w", encoding="utf-8") as f:
    f.write(json_string)
    print("数据已写入 tomato_ujson.json 文件")

# 3. 从 JSON 字符串反序列化为 Python 对象
loaded_data = ujson.loads(json_string)

print("\n反序列化后的 Python 对象:\n", loaded_data)
print("番茄品种:", loaded_data["variety"])

# 4. 从 JSON 文件反序列化为 Python 对象
with open("data/tomato_ujson.json", "r", encoding="utf-8") as f:
    json_string_from_file = f.read() # 先读取文件内容
    loaded_data_from_file = ujson.loads(json_string_from_file)

print("\n从文件反序列化后的 Python 对象:\n", loaded_data_from_file)
print("供应商名称:", loaded_data_from_file["supplier"]["name"])

#  更复杂的例子，包含嵌套列表和对象
complex_data = {
    "product": "辽宁串红小番茄",
    "variations": [
        {
            "grade": "一级",
            "price": 12.99,
            "packaging": "精装礼盒"
        },
        {
            "grade": "二级",
            "price": 9.99,
            "packaging": "普通盒装"
        }
    ],
    "farm_details": {
        "location": "辽宁大连",
        "area": "100亩",
        "certifications": ["绿色食品认证", "无公害农产品认证"]
    }
}

complex_json_string = ujson.dumps(complex_data, ensure_ascii=False, indent=4)
print("\n复杂数据JSON字符串:\n", complex_json_string)

complex_loaded_data = ujson.loads(complex_json_string)
print("\n复杂数据反序列化后的Python对象:\n", complex_loaded_data)
print("一级品价格:", complex_loaded_data["variations"][0]["price"])
