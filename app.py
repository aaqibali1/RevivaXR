from flask import Flask, render_template, url_for

# Create the Flask application
app = Flask(__name__)

# Homepage Route
@app.route('/')
def home():
    return render_template('index.html')

# About Page Route
@app.route('/about')
def about():
    return render_template('about.html')

# Run the Flask web application
if __name__ == '__main__':
    app.run(debug=True)

