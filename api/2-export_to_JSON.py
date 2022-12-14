#!/usr/bin/python3
"""returns information about his/her TODO list progress"""
import urllib.request
import json
import sys


if __name__ == '__main__':
    uId = int(sys.argv[1])
    userDict = {}
    taskList = []
    with urllib.request.urlopen('https://jsonplaceholder'
                                '.typicode.com/users') as response:
        users = json.loads(response.read().decode())
        for user in users:
            if user['id'] == uId:
                userName = user['username']

    with urllib.request.urlopen('https://jsonplaceholder'
                                '.typicode.com/todos') as response:
        jsonDict = json.loads(response.read().decode())
        for line in jsonDict:
            if line['userId'] == uId:
                tempDict = {"task": line['title'], "completed": line['completed'], "username": userName}
                taskList.append(tempDict)
            userDict[uId] = taskList


    with open(f'./{uId}.json', 'w+') as file:
        file.write(json.dumps(userDict))
