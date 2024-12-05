from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/nikita/<int:num>")
def Getnikita(num):
    l=[]

    import json
    str1=''
    with open("output_1.json", "r", encoding='utf-8') as file:
        str1=file.read()
    l =  json.loads(str1) # ДеСериализация
    print(l)
    print(num)    
    # return f"Никита не съел {num} ёжиков"
    s=l[num%10]
    return f"Дорогой друг ты: {s} "


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run()