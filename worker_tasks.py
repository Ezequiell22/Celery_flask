from celery import Celery
import sqlite3
from celery.schedules import crontab

app = Celery(
  main = 'worker_tasks',
  broker='pyamqp//:guest@localhost//',
  backend='db+sqlite:///celery.sqlite'
)

#agendamento
app.conf.beat_schedule = {
  'sc-stock-every-minute' : {
    'task' : 'task_x',
    'schedule' : crontab(minute='*'),
    'args' : ('teste 1', )
  }
}

app.conf.timezone = 'America/Sao_Paulo'

@app.task
def task_x(name):
  message = f'Ola, {name}'

  with sqlite3.connect('data.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
      '''
        create table if not exists stocks (
        id integer primary key autoincrement,
        stock_name text,
        price real
        )    
      ''')

    cursor.execute('''
    insert or ignore into stocks(stock_name, price)
    values(?,?)
    ''', (name, 21))

    conn.commit()

  return message