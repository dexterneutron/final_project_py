from flask import Flask, jsonify
from lib.storedata import get_data,store_data
from flask_apscheduler import APScheduler

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route("/api/feed", methods = ['GET'])
def retrive_data():
    data = get_data()
    return jsonify(data)

@scheduler.task('interval', id='update_from_api', seconds=60, misfire_grace_time=900)
def update_from_api():
    try:
        store_data()
        print('Data stored sucessfully')
    except:
        print('Error fetching data')

if __name__ == '__main__':
    app.run()
