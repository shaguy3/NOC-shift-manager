
# os.chdir(os.path.join('..', 'Database'))
# test_week = work_week.WorkWeek(1, date.fromordinal(dbi.get_last_sunday().toordinal() - 7),
#                                date.fromordinal(dbi.get_next_saturday().toordinal() - 7))
# test_week_2 = work_week.WorkWeek(2, dbi.get_last_sunday(), dbi.get_next_saturday().toordinal())
# shamil = dbi.load_employee('Guy Shamilyan')
# yarden = dbi.load_employee('Yarden Yefet')
# heli = dbi.load_employee('Heli Kanade')
#
# test_week[20].append(shamil)
# test_week_2[0].append(yarden)
# test_week_2[0].append(heli)
# test_week_2[1].append(yarden)
#
# print(test_week[20])
# print(test_week_2[0])
#
# print(has_adjacent_shifts(test_week, test_week_2))