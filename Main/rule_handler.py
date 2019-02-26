from Database import db_interactions as dbi
from Classes import employee, work_week
from datetime import date
import os


def has_adjacent_shifts(last_week, this_week, cwd=os.getcwd()):
    os.chdir(os.path.join('..', 'Database'))
    # last_week = dbi.load_last_week()
    for emp_last in last_week[20]:
        for emp_this in this_week[0]:
            if emp_last == emp_this:
                os.chdir(cwd)
                return True
    for shift in this_week:
        if shift == this_week[0]:
            emps_last = shift
        else:
            emps_this = shift
            for emp_last in emps_last:
                for emp_this in emps_this:
                    if emp_last == emp_this:
                        os.chdir(cwd)
                        return True
        emps_last = emps_this
    os.chdir(cwd)
    return False


# TODO: "at least one operator at each shift" handling

# TODO: "Night after morning" handling

# TODO: "Maximum number of shifts" handling

# TODO: "Sof rules handling
