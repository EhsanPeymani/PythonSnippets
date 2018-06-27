import records
import os

connection_string = 'sqlite:///chinook.db'
print(connection_string)

db = records.Database(connection_string)
rows = db.query('SELECT * FROM employees WHERE EmployeeId < 6')

print('List of Employees:')
for employee in rows:
    print('Id {}: {} {}'.format(employee['EmployeeId'],
                                employee['FirstName'],
                                employee['LastName']))

print('')
print(rows[0].export('json'))