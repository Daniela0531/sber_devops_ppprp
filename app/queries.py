from flask import Flask, request

from datetime import datetime

app = Flask(__name__)

statistics_num = 0

@app.route('/')
def main() -> str:
    return "<h1>Hello there!!! I am here!!! aaaaa</h1>"

@app.route('/time')
def time() -> str:
    global statistics_num
    now = datetime.now()
    statistics_num += 1
    return "<h1>Current Time = {}</h1>".format(now.strftime("%H:%M:%S"))

@app.route('/statistics')
def statistics() -> str:
    return "<h1>Statistics number = {}</h1>".format(statistics_num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
