from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

# Routes for various pages
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
