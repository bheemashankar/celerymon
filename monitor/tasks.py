from monitor.celery_app import app

@app.task
def debug_task():
    try:
        i = app.control.inspect()
        print(i.stats())
    except Exception as e:
        print("Full block error....:: %s" % e)
