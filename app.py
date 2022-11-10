from flask import Flask

app = Flask(__name__)

if __name__ == "__main__": # True is executed directly, False if imported
    app.run(debug=True, host ="0.0.0.0")