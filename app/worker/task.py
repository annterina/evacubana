from celery.app import Celery

app = Celery(__name__, broker='sqs://')
app.conf.broker_transport_options = {'region': 'eu-north-1'}


@app.task
def dummy_task():
    print("Hello annterina!")
    return 'Hello annterina!'
