#!/usr/bin/python3

"""
Fetches and displays information about an employee

API: https://jsonplaceholder.typicode.com/
"""
import requests
import sys

API = "https://jsonplaceholder.typicode.com"


def main(employee_id):
    """main function"""
    # get employee details
    response = requests.get(f"{API}/users/{employee_id}")
    if not response.ok:
        return 1
    employee_details = response.json()

    # get employee todos
    response = requests.get(f"{API}/todos?userId={employee_id}")
    if not response.ok:
        return 2
    employee_todos = response.json()

    # store details in variables
    name = employee_details.get('name')
    num_of_todos = len(employee_todos)
    completed_todos = tuple(
            todo for todo in employee_todos if todo.get('completed'))

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed_todos), num_of_todos
    ))
    for todo in completed_todos:
        print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    sys.exit(main(employee_id))
