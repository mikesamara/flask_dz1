'''
Создать базовый шаблон для интернет-магазина, содержащий общие
элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для
страниц категорий товаров и отдельных товаров. Например, создать
страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world'


@app.route('/main/')
def main():
    content = {'title': 'Главная'}
    return render_template('main.html', **content)


@app.route('/shoes/')
def shoes():
    content = [{
        'id': '123',
        'name': 'puma3310',
        'brand': 'Puma',
        'price': '100.00',
        'size': '42'
    }, {
        'id': '158',
        'name': 'nike3310',
        'brand': 'Nike',
        'price': '150.00',
        'size': '42'
    }]
    tittle = {'title': 'Страница с обувью'}
    return render_template('shoes.html', users=content, **tittle)


@app.route('/clothes/')
def clothes():
    content = [{
        'id': '13',
        'type': 'Платье',
        'price': '188.00',
        'size': '36'
    }, {
        'id': '23',
        'type': 'Джинсы',
        'price': '99.99',
        'size': '38'
    }]
    tittle = {'title': 'Страница с одеждой'}
    return render_template('clothes.html', users1=content, **tittle)


if __name__ == '__main__':
    app.run()
