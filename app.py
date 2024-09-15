from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    pass
    return render_template('home.html')


@app.route('/transportation_prices')
def service():
    return render_template('transportation_prices.html')


@app.route('/about')
def route():
    return render_template('about.html')


@app.route('/big_cars')
def big_cars():
    return render_template('big_cars.html')


@app.route('/small_cars')
def small_cars():
    return render_template('small_cars.html')


@app.route('/contacts')
def contact():
    return render_template('contact.html')


if '__main__' == __name__:
    app.run(debug=True)
