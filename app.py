from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def shop():
	whales = ["Blue Whale - 10,000,000£", "Sperm Whale - 12,500,000£", "White Whale - 13,400,000£"]
	return render_template("shop.html", whales = whales)

if __name__ == '__main__':
   app.run(debug = True)