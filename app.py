from flask import Flask
app = Flask(__name__)
# Temporary in-memory database
cars = []

@app.route('/')
def home():
    return render_template('index.html', cars=cars)

@app.route('/add_car', methods=['POST'])
def add_car():
    brand = request.form.get('brand')
    model = request.form.get('model')
    year = request.form.get('year')
    price = request.form.get('price')
    
    # Save car details in the list
    cars.append({
        'brand': brand,
        'model': model,
        'year': year,
        'price': price
    })
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
