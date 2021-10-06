from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from articleUpdater import feederapi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(feederapi.update_data, 'interval', minutes=2)
    scheduler.start() 