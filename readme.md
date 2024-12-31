## for tests run broker
 - docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management

## add task with producer
 - python producer.py

## run worker 
 - celery -A worker_tasks worker --loglevel=INFO
