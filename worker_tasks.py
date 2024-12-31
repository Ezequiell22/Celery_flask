from celery import Celery
import sqlite3

app = Celery(
  main = 'worker_tasks',
  broker='pyamqp//:guest@localhost//',
  backend='db+sqlite:///celery.sqlite'
)

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