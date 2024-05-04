from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "<p>Bedankt voor de opleiding Peter!</p>"

if __name__ == '__main__':
    app.run(port=5000,debug=True)