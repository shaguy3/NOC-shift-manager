#NOC Shift manager

An application that is supposed to get user input in the form of shift blocks (shifts they cannot work at),
and output a valid weekly shift schedule.

Things the app will consider:
* Global rule handling (no two shift in a row, no more than two nights a week, etc...)
* Worker specific rules (doesnt work nights, doesnt work weekends, etc...)
* Equal spread in the salary between the workers
* 