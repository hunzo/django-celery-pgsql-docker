from django.shortcuts import render, redirect
from django.contrib import messages

from app.tasks import CeleryGetTask, Counter


def Home(request):

    try:
        tasks = CeleryGetTask()
    except:
        tasks = []

    if request.method == "POST":
        code = request.POST.get("code")

        if not code.isnumeric():
            messages.error(request, f"Please enter number")
            return redirect("home")

        ret = Counter.delay(int(code))
        # ret = Counter.apply_async(args=(int(code),))

        print(ret.task_id)

        messages.success(request, f"count: {code}")
        return redirect("home")

    
    context = {
        "tasks": tasks
    }
    return render(request, "index.html", context)


from core.celery import my_revoke

def CancelTask(request, task_id):
    print(f"Task Cancel: {task_id}")
    # task = Counter.AsyncResult(task_id).revoke(terminate=True)
    # task = Counter.AsyncResult(task_id)

    # app.task.control.revoke(task_id)
    # task.revoke(terminate=True, signal='SIGKILL')
    # task.abort()

    # print(task.)

    
    # print(task)

    my_revoke(task_id)
    messages.error(request, "task revoke")
    return redirect('home')
