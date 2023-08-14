from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def show_time():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Current time: {current_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8282)

