from flask import *

	
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>WELCOME TO THE API  SIDRAELEZZ TELEGRAM : @SidraTools</h1>"

if __name__ == "__main__":
	app.run(debug=True)
    
