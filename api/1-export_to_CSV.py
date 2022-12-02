#!/usr/bin/python3
"""returns information about his/her TODO list progress"""
import urllib.request
import json
import sys
import csv


if __name__ == '__main__':

    uId = int(sys.argv[1])
    rows = []
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
                strUID = f'"{uId}"'
                row = [strUID, userName]
                rows.append(row)


    with open(f'./{uId}.csv', 'w+') as file:
        writer = csv.writer(file)
        for roww in rows:
            writer.writerow(roww)
