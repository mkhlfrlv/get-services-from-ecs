import atexit
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)
app.config.from_object(__name__)


def scheduled_task():
    print("This task is running every minute.")


@app.route('/services', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_task, 'interval', minutes=1)
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())

    app.run()
