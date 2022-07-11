import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   row = []
   for rows in data:
       row.append(rows)
   
   return row[0]

# Read the csv file
f = open('data.csv')
row = csv.reader(f)
print(get_first_row(row))