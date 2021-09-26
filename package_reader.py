import csv
from package import *
from hashtable import *


def package_reader():
    """
    This function takes a csv file, opens it, and adds the data to a list. It then iterates through
    each row of the list and adds each row to the hash table. It returns a hash table that contains
    organized data from the csv file.

    Algorithmic Complexity: O(N). Loops over n elements in the dictionary, each row is a line from the csv.
    Each line of code in the loop runs at O(1) complexity
    """

    # Opens the package csv file so the data can be accessed
    with open('packages.csv') as csv_file:
        # Creates a list with the CSV data
        read_packages = csv.reader(csv_file, delimiter=",")

        # Creates an empty hash table to hold packages
        package_table = HashTable()

        # Iterates through each row in the list
        for row in read_packages:
            # Creates package objects using the data from the list
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            # Adds the package to the hash table and sets the package_id as an int
            # to be used as a key in the hash table
            package_table.set(int(package.package_id), package)

        return package_table
