# coding: utf-8
import datetime
import os
import pandas as pd
import random

# - [ ] Study for Applied Information Technology Engineer Examination.
# - [ ] Study JMAM.
# - [ ] Study of machine learning.

def tooMany(value1, value2):
    if value1 + value2 > 60:
        return True
    else:
        return False

def just(value):
    if 45 < value < 55:
        return True
    else:
        return False

def createTodoList(task_list):
    todo_list = []
    total = 0
    while not just(total):
        one = task_list[random.randint(1, len(task_list)-1)]
        if not tooMany(one[2], total):
            todo_list.append(one)
            total += one[2]
    return sorted(todo_list)

def createDocument(todo_list):
    str = '''## Purpose!
This file is my day's logging.
You should write your day's tasks result.

## Daylog
'''

    for todo in todo_list:
        task = '- [ ] ' + todo[0] + ' : ' + todo[1] + '\n'
        str += task

    return str

today = datetime.datetime.today()
filename = 'daylog_' + today.strftime('%Y-%m%d') + '.md'

if not os.path.exists(filename):
    with open(filename, 'w', encoding='utf-8') as file:

        tasks_pd = pd.read_csv('tasks.csv')
        task_list = tasks_pd.values.tolist()
        file.write(createDocument(createTodoList(task_list)))

        print('create today\'s daylog!\nfile name is', filename)
        os.system('atom ' + filename)
else:
    print('Today\'s daylog is already exist!')
