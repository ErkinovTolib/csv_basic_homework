import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """

    column = []
    c = 0
    for i in data:
        column.append(i) 
    for j in column[0]:   
        c += 1
    return c
 
# Read the csv file
f = open('data.csv')
r = csv.reader(f)
print(find_number_of_columns(r))
