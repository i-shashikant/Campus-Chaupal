from celery_app import celery


@celery.task
def test_task():
    print("Celery is working!")
    return "Celery is working!"