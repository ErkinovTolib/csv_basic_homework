import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    first = []
    for column in data:
        first.append(column[0])
    return first
    
# Read the csv file
f = open('data.csv')
data = csv.reader(f)
print(get_first_column(data))