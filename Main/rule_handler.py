from Database import db_interactions as dbi
from Classes import employee, work_week
from datetime import date
import os


def no_adjacent_shifts(last_week, this_week):
    """documentation"""
    # last_week = dbi.load_last_week()      When the rule handling is complete, this line will be relevant.
    for emp_last in last_week[20]:
        for emp_this in this_week[0]:
            if emp_last == emp_this:
                return False
    for shift in this_week:
        if shift == this_week[0]:
            emps_last = shift
        else:
            emps_this = shift
            for emp_last in emps_last:
                for emp_this in emps_this:
                    if emp_last == emp_this:
                        return False
        emps_last = shift
    return True


def at_least_one_operator_in_each_shift(this_week):
    """documentation"""
    for shift in this_week:
        if not shift:
            return False
    return True


def no_night_after_morning(this_week):
    this_morning = this_week[0]
    for i in range(1, 21):
        if i % 3 == 0:
            this_morning = this_week[i]
        elif i % 3 == 2:
            for emp_morning in this_morning:
                for emp_this in this_week[i]:
                    if emp_morning == emp_this:
                        return False
    return True


def no_more_than_maximum_shifts(this_week):
    """documentation"""
    max_shifts = dbi.load_global_rule('Maximum number of shifts')
    shift_counters = {}
    for shift in this_week:
        for emp in shift:
            if not str(emp.id) in shift_counters.keys():
                shift_counters[str(emp.id)] = 1
            else:
                shift_counters[str(emp.id)] += 1
            if shift_counters[str(emp.id)] > max_shifts:
                return False
    return True


# TODO: "Soft rules handling
def no_8_8_8(this_week):
    pass


if __name__ == '__main__':
    pass
