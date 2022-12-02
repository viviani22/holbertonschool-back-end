#!/usr/bin/python3
"""returns information about his/her TODO list progress"""
import urllib.request
import json


if __name__ == '__main__':
    userDict = {}
    taskList = []
    with urllib.request.urlopen('https://jsonplaceholder'
                                '.typicode.com/users') as response:
        users = json.loads(response.read().decode())

    with urllib.request.urlopen('https://jsonplaceholder'
                                '.typicode.com/todos') as response:
        jsonDict = json.loads(response.read().decode())
        for user in users:
            for line in jsonDict:
                if line['userId'] == user['id']:
                    tempDict = {"username": user['username'], "task": line['title'], "completed": line['completed']}
                    taskList.append(tempDict)
            userDict[user['id']] = taskList


    with open(f'./todo_all_employees.json', 'w+') as file:
        file.write(json.dumps(userDict))
