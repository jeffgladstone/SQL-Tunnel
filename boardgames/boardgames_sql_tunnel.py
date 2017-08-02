
"""
    Filename: boardgames_sql_tunnel.py
    Author: Jeff Gladstone
    Date: 8/2/2017
    Description:
    This Python program manipulates
    a boardgames database using SQL queries
    and then outputs the result set
    to a CSV file.

    The result set shows the most recent boardgames
    with an average rating above 8/10.

    Boardgames database source: https://github.com/amrith8/BoardGamesDataAnalysis
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
			writer.writerow({fieldnames[0]: row[0], fieldnames[1]: row[1], fieldnames[2]: row[2]})

# Sample Execution
fieldnames = ['name', 'yearpublished', 'average_rating']
query = '''SELECT ''' + fieldnames[0] + ',' + fieldnames[1] + ',' + fieldnames[2] + ''' FROM boardgame_data
	WHERE ''' + fieldnames[2] + ''' > 8 ORDER BY ''' + fieldnames[1] + ''' DESC LIMIT 100;'''
output_list = execute_sql('boardgame_data.db', query)
output_csv(fieldnames, output_list, 'boardgames_output.csv')