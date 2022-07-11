import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    c = 0
    x = []
    for row in r:
        x.append(row)
        c += 1
    return c

# Read the csv file
f = open('data.csv')
r = csv.reader(f)
print(find_number_of_rows('r'))


