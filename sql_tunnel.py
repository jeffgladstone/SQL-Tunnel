
"""
    Filename: sql_tunnel.py
    Author: Jeff Gladstone
    Date: 8/2/2017
    Description:
    This Python program manipulates
    a database file using SQL queries
    and then outputs the result set
    to a CSV file.
"""

# Initial imports
import sqlite3 #import sqlite3 the python library to interact with sqlite databases
import csv

# SQL query execution function
def execute_sql(input_db, query):
	conn = sqlite3.connect(input_db)
	c = conn.cursor()
	output_list = []
	for row in c.execute(query):
		output_list.append(row)
	return output_list

# Output function
def output_csv(fieldnames, output_list, output_csv_name):
	with open(output_csv_name, "w") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
		writer.writeheader()
		for row in output_list:
			writer.writerow({fieldnames[0]: row[0]})

# Sample Execution
fieldnames = ['---first field name---', '---second field name---']
query = '''SELECT ''' + fieldnames[0] + ',' + fieldnames[1] + ''' FROM boardgame_data;'''
output_list = execute_sql('---input db file ---', query)
output_csv(fieldnames, output_list, '---output csv name---')