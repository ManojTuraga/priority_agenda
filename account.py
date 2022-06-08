from datetime import date
from time import strptime
from heaps import MaxHeap
from task import Task

class Account:
    def __init__(self, user_name, password):
        self._usr_name = user_name
        self._pswd = password
        self._tasks = MaxHeap()

    def add_task(self, title, info, due_date, weight, date_created = str(date.today().strftime("%m/%d/%Y"))):
        new_task = Task(title, info, due_date, weight, date_created)
        self._tasks.add(new_task)

    def remove_task(self):
        test = self._tasks.remove()
        return test.get_title()

    def get_username(self):
        return self._usr_name

    def get_password(self):
        return self._pswd

    def get_task(self):
        return self._tasks.peek_root()

    def get_tasks(self):
        return self._tasks.get_heap()

    def set_tasks(self, new_maxheap):
        self._tasks = new_maxheap

    def __lt__(self, other):
        if isinstance(other, Account):
            return self._usr_name < other._usr_name

        if isinstance(other, str):
            return self._usr_name < other

    def __gt__(self, other):
        if isinstance(other, Account):
            return self._usr_name > other._usr_name

        if isinstance(other, str):
            return self._usr_name > other

    def __eq__(self, other):
        if isinstance(other, Account):
            return self._usr_name == other._usr_name

        if isinstance(other, str):
            return self._usr_name == other

    def __str__(self):
        return f'{self._usr_name};\t{self._pswd}{self._tasks}'

        
