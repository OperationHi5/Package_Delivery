import csv
from package import *
from hashtable import *


def package_reader():
    with open('packages.csv') as csv_file:
        read_packages = csv.reader(csv_file, delimiter=",")
        package_table = HashTable()

        for row in read_packages:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            package_table.set(int(package.package_id), package)

        return package_table
