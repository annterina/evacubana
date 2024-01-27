from celery.app import Celery

app = Celery(__name__, broker='sqs://')
app.conf.broker_transport_options = {'region': 'eu-north-1'}


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, test.s(), name='test every 60')
    sender.add_periodic_task(30.0, hello.s(), name='hello every 30')


@app.task
def test():
    print("annterina is testing!")
    return 'annterina is testing!'


@app.task
def hello():
    print("Hello annterina!")
    return 'Hello annterina!'
