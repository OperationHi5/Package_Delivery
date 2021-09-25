import csv


def distance_reader():

    with open('distances.csv') as csv_file:
        read_distances = csv.reader(csv_file, delimiter=',')
        distance_list = list(read_distances)

        street_list = distance_list[0]

        all_distances = {}

        for row in distance_list[1:]:
            temp = {}
            for i in range(1, 28):
                temp[street_list[i]] = float(row[i])
            all_distances[row[0]] = temp

            print(row)

        return all_distances

