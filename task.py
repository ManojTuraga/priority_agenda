from datetime import date
from time import strptime

class Task:
    def __init__(self, title, info, due_date, weight, date_created = str(date.today().strftime("%m/%d/%Y"))):
        self._title = title
        self._info = info
        self._date_created = date_created
        self._due_date = due_date
        self._weight = weight

    def get_title(self):
        return self._title

    def set_title(self, new_value):
        self._title = new_value

    def get_info(self):
        return self._info

    def set_info(self, new_value):
        self._info = new_value

    def get_due_date(self):
        return self._due_date

    def set_due_date(self, new_date):
        self._due_date = new_date

    def get_date_created(self):
        return self._date_created

    def set_date_created(self, new_date):
        self._date_created = new_date

    def get_weight(self):
        return self._weight

    def set_weight(self, new_weight):
        self._weight = new_weight

    def __lt__(self, other):
        self_date_created = strptime(self._date_created, "%m/%d/%Y")
        other_date_created = strptime(other._date_created, "%m/%d/%Y")
        self_due_date = strptime(self._due_date, "%m/%d/%Y")
        other_due_date = strptime(other._due_date, "%m/%d/%Y")

        if self_due_date > other_due_date:
            return True

        elif self_due_date == other_due_date and self_date_created > other_date_created:
            return True

        elif self_due_date == other_due_date and self_date_created == other_date_created and self._weight < other._weight:
            return True

        else:
            return False

    def __gt__(self, other):
        self_date_created = strptime(self._date_created, "%m/%d/%Y")
        other_date_created = strptime(other._date_created, "%m/%d/%Y")
        self_due_date = strptime(self._due_date, "%m/%d/%Y")
        other_due_date = strptime(other._due_date, "%m/%d/%Y")

        if self_due_date < other_due_date:
            return True

        elif self_due_date == other_due_date and self_date_created < other_date_created:
            return True

        elif self_due_date == other_due_date and self_date_created == other_date_created and self._weight > other._weight:
            return True

        else:
            return False

    def __eq__(self, other):
        self_date_created = strptime(self._date_created, "%m/%d/%Y")
        other_date_created = strptime(other._date_created, "%m/%d/%Y")
        self_due_date = strptime(self._due_date, "%m/%d/%Y")
        other_due_date = strptime(other._due_date, "%m/%d/%Y")

        return (self_date_created == other_date_created and self_due_date == other_due_date and self._weight == other._weight)

    def __str__(self):
        return f'{self._title},\t{self._info},\t{self._due_date},\t{self._weight},\t{self._date_created}'
