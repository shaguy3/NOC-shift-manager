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
        emps_this = emps_last
    os.chdir(cwd)
    return False


os.chdir(os.path.join('..', 'Database'))
test_week = work_week.WorkWeek(1, date.fromordinal(dbi.get_last_sunday().toordinal() - 7),
                               date.fromordinal(dbi.get_next_saturday().toordinal() - 7))
test_week_2 = work_week.WorkWeek(2, dbi.get_last_sunday(), dbi.get_next_saturday().toordinal())
shamil = dbi.load_employee('Guy Shamilyan')
yarden = dbi.load_employee('Yarden Yefet')
heli = dbi.load_employee('Heli Kanade')

test_week[20].append(shamil)
test_week_2[0].append(yarden)
test_week_2[0].append(heli)
test_week_2[1].append(shamil)

print(test_week[20])
print(test_week_2[0])
print(test_week_2[1])

print(has_adjacent_shifts(test_week, test_week_2))
