from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Маршруты
@app.route('/')
def home():
    return render_template('index.html', title="Главная страница")

@app.route('/about')
def about():
    return render_template('about.html', title="О нас")

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('result.html', name=name)
    return render_template('form.html', title="Форма ввода данных")

# Обработка ошибок
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Страница не найдена"), 404

if __name__ == '__main__':
    app.run(debug=True)
