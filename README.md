#NOC Shift manager

An application that is supposed to get user input in the form of shift blocks (shifts they cannot work at),
and output a valid weekly shift schedule.

Things the app will consider:
* Global rule handling (no two shift in a row, no more than two nights a week, etc...)
* Worker specific rules (doesnt work nights, doesnt work weekends, etc...)
* Equal spread in the salary between the workers


version control:
- ver 0.01: Made initial packages.
 Classes will contain the WorkWeek and Worker classes.
 Rules will contain the rule handler, and the Global rules and Worker specific rules in json form.
- ver 0.02: Completed the WorkWeek class for now. it has an id, a start and end dates, and the weekly schedule
that starts empty. Made two methods: get_last_sunday() and get_next_saturday(), that do what they say on the tin.
Made an initial Worker class.
- ver 0.03: Started work on the Worker class. it will enable control over the workers.json file.
the goal is to be able to create new workers and add them to the json file,remove them from it and edit their rules and properties.
- ver 0.04: Restructured the project. The Rules package is now the Database package.
 It's purpose is to host the database and the db_interactions module that is responsible to interact with the databases.