import os
from celery import Celery
from datetime import datetime

app=Celery()
app

@app.task
def user_task():
    print("def work")



#butefuelsoup