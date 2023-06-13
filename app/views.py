from django.shortcuts import render, redirect
from django.contrib import messages

from app.tasks import CeleryGetTask, Counter

from celery.result import AsyncResult


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



def CancelTask(request, task_id):
    print(f"task Cancel id: {task_id}")

    AsyncResult(task_id).revoke(terminate=True)

    messages.error(request, f"task id: {task_id} has been revoke")
    return redirect('home')
