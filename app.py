from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("fireball123.html")

if __name__ == '__main__':
    app.run(debug=True)

