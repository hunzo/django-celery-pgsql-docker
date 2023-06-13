from celery import shared_task
# from celery.contrib.abortable import AbortableTask
# from celery.contrib.abortable import AbortableAsyncResult
from time import sleep
from celery_progress.backend import ProgressRecorder

from core.celery import app



# @shared_task(bind=True, base=AbortableTask)
# @shared_task(bind=True, ignore_result=True)
@shared_task(bind=True)
def Counter(self, counter):

    print(self.request.id)
    progress_recorder = ProgressRecorder(self)

    for i in range(counter):
        i += 1
        print(i)
        sleep(0.5)
        progress_recorder.set_progress(i + 1, counter)
    
    return "done"


def CeleryGetTask():
    try:
        i = app.control.inspect().active()

    except Exception as e:
        i = {}

    celery_host = i.keys()
    # hostname =  for k in i

    hostname = ""
    for x in celery_host:
        hostname = x


    # get task id
    tasks = []
    for t in i[hostname]:
        tasks.append(t['id'])
    # print(tasks)

    return tasks
