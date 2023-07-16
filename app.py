from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloWorld():
    return 'Hello World'

@app.route('/aboutus', methods=['GET'])
def aboutWorld():
    return 'About Us all'


if __name__=="__main__":
    app.run(port=3000, debug=True)