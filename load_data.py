import json
str1=''
with open("output_1.json", "r", encoding='utf-8') as file:
    str1=file.read()
l =  json.loads(str1) # ДеСериализация
print(l)