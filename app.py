from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for popular destinations (could be retrieved from a database)
popular_destinations = [
    {"city": "New York", "image": "new_york.jpg", "description": "Explore furnished apartments in New York"},
    {"city": "Lviv", "image": "lviv.jpg", "description": "Find your next home in Lviv"},
    {"city": "Dubai", "image": "dubai.jpg", "description": "Discover premium stays in Dubai"}
]

@app.route('/')
def index():
    return render_template('index.html', destinations=popular_destinations)

@app.route('/search', methods=['POST'])
def search():
    location = request.form.get('location')
    move_in_date = request.form.get('move_in_date')
    length_of_stay = request.form.get('length_of_stay')

    # Process the search query (for now just print the data)
    print(f"Location: {location}, Move-in Date: {move_in_date}, Length of Stay: {length_of_stay}")

    # In a real application, this data would be used to search the database
    return render_template('search_results.html', location=location)

if __name__ == '__main__':
    app.run(debug=True)
