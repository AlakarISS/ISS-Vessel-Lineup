from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler import util

# def start_schedular():
#     scheduler = BackgroundScheduler()
#     scheduler.add_jobstore(DjangoJobStore(), "default")

#     from App.task import move_sailed_data

#     scheduler.add_job(
#         move_sailed_data,
#         'cron',
#         hour=12,
#         minute=30,
#         id="append",
#         replace_existing=True,
#     )

#     try:
#         scheduler.start()
#     except KeyboardInterrupt:
#         scheduler.shutdown()