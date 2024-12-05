from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/<int:num>")
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
    s= f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Заголовок страницы</title>
        <link rel="stylesheet" href="./styles/style.css">

        <meta property="og:title" content="Заголовок страницы в OG">
        <meta property="og:description" content="Описание страницы в OG">
        <meta property="og:image" content="https://example.com/image.jpg">
        <meta property="og:url" content="https://example.com/">
    </head>
    <body>
        <header>
        <h1>Дорогой друг ты: {s}</h1>
        <p>Который сделан на основе готового шаблона</p>
        <nav>
            <ul>
            <li><a href="index.html">Эта страница</a></li>
            <li><a href="catalog.html">Другая страница</a></li>
            </ul>
        </nav>
        </header>
        <main>
        <article>
            <section>
            <h2> {s}</h2>
            <p>Она обо мне</p>
            <img src="images/image.png" alt="Человек и пароход">
            <p>Но может быть и о семантике, я пока не решил.</p>
            </section>
            <section>
            <h2>Вторая секция</h2>
            <p>Она тоже обо мне</p>
            </section>
            <section>
            <h2>И третья</h2>
            <p>Вы уже должны были начать догадываться.</p>
            </section>
        </article>
        </main>
        <footer>
        <p>Сюда бы я вписал информацию об авторе и ссылки на другие сайты</p>
        </footer>
        <!-- сюда можно подключить jquery <script src="scripts/app.js" defer></script> -->
    </body>
    </html>
        """
    

    # return f"Дорогой друг ты: {s} "
    return s


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run()