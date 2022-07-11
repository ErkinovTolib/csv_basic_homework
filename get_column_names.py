#Define function,Get coloumn names from a csv file
import csv
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    names = []
    col = []
    for i in data:
        col.append(i)
    for j in col[0]:
        names.append(j)

    return names
    
# Read the csv file
f = open('data.csv')
name = csv.reader(f)
print(get_column_names(name))