import csv


def distance_reader():
    """
    This function takes and opens a csv file and uses that file to generate a list of street names, then creates
    a dictionary to hold a connected graph of the addresses and their distances from each other. It iterates
    through every row in the dictionary and adds that data to another dictionary that combines the distances
    with a list of streets, then returns dictionary with the organized Address:Distance Data

    Algorithmic Complexity: 0(n^2). Each element is iterated over multiple times to create a fully connected graph of
    the data.
    """
    with open('distances.csv') as csv_file:
        # Initializes a list with the CSV data
        read_distances = csv.reader(csv_file, delimiter=',')

        # Initializes a list of street names
        distance_list = list(read_distances)

        street_list = distance_list[0]

        # Initializes a dictionary that holds the dictionaries of the streets and their distances from each other
        all_distances = {}

        for row in distance_list[1:]:
            # Initializes a temporary dictionary that holds key/value pairs of the streets and distances
            temp = {}
            for i in range(1, 28):
                temp[street_list[i]] = float(row[i])
            all_distances[row[0]] = temp

        return all_distances

