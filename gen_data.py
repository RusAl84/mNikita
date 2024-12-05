
import json
l=[]
l.append('Отзывчивость')
l.append('Честность')
l.append('Дисциплинированность') 
l.append('Умение')
l.append('Верность')
l.append('Добрата')
l.append('Ласка')
l.append('Радость')
l.append('Нежность')
l.append('Точным')
str1 = json.dumps(l, ensure_ascii=False) # Сериализация
print(str1)
with open("output_1.json", "w", encoding="UTF-8") as file_out:
    n = file_out.write(str1)

        # with open(filename, "r", encoding='utf-8') as file:
        #     self.data = file.read()