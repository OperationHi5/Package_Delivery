from distance_reader import *
from format_time import *
from package_reader import *
from truck import *


def deliver_packages():
    """
    This function is the main algorithm. It initializes the distance dictionary and the package hash table.
    It initializes and updates truck data, loads the packages into the truck. It initializes and updates the
    package_table hash table, organizes the packages into the proper order, delivers the packages, and then returns
    the hash table so the data can be accessed after being ran

    Algorithmic Complexity: O(N^2). The delivery of the packages is linear which gives a complexity of O(N), but
    since each truck requires the delivery_algo to be ran, and delivery_algo has a complexity of O(N^2), it gives
    deliver_packages a complexity of O(N^2).
    """

    # initializes a hash table with every package
    package_table = package_reader()

    # initializes a dictionary with all locations and distances
    distances = distance_reader()

    # manually loading the packages in each truck
    # Truck 1 contains all of the "early" delivery packages except for 6, and all of the packages that
    # are required to be delivered together
    truck1_list = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

    # Truck 2 contains all of the packages that are delayed
    truck2_list = [2, 3, 6, 18, 25, 26, 27, 28, 32, 36, 38]

    # Truck 3 contains the remaining packages
    truck3_list = [4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 33, 35, 39]

    # Initializes a string variable for the hub address
    hub_address = "4001 South 700 East"

    # Runs the delivery algorithm to sort the package list in the most efficient manner
    truck1_list = delivery_algo(truck1_list)

    # Initializes the Truck Object to hold the packages and sets it to 8:00 AM and loads the sorted packages
    truck1 = Truck(1, 480, truck1_list)

    # Sets the truck's location to the hub
    truck1.current_location = hub_address

    print("------")
    print("Truck Schedule: ")
    print("------")
    print("Truck 1 leaves hub at", format_minutes(truck1.time))

    # Truck leaves the hub, and updates the packages on the truck to being 'En Route' to their destination
    update_transport_time(package_table, truck1_list, 480, 'En Route')

    # Delivers packages one by one until there are no remaining packages, then returns to the hub
    while truck1.package_list:
        package = package_table.get(truck1.package_list[0])
        distance_to_next = distances[truck1.current_location][package.address]
        truck1.miles += float(distance_to_next)
        truck1.current_location = package.address
        # Adds the time to the next address to the current truck time
        truck1.time = add_time(miles_to_time(distance_to_next), truck1.time)
        # Sets the package's delivery time to the current time
        package.delivery_time = truck1.time
        package.truck_id = truck1.truck_id
        package.status = 'Delivered'
        package_table.set(int(package.package_id), package)
        truck1.package_list.pop(0)
        if not truck1.package_list:
            truck1.miles += float(distances[truck1.current_location][hub_address])
            truck1.current_location = hub_address

    # Sets the time that the truck returns to the current time
    truck1.return_time = truck1.time

    print("Truck 1 Returns at: ", format_minutes(truck1.return_time))

    # Runs the delivery algorithm to sort the package list in the most efficient manner
    truck2_list = delivery_algo(truck2_list)

    # Initializes the Truck Object to hold the packages and sets it to 8:00 AM and loads the sorted packages
    truck2 = Truck(2, 545, truck2_list)

    # Sets the truck's location to the hub
    truck2.current_location = hub_address

    print("Truck 2 leaves hub at", format_minutes(truck2.time))

    # Truck leaves the hub, and updates the packages on the truck to being 'En Route' to their destination
    update_transport_time(package_table, truck2_list, truck2.time, 'En Route')

    # Delivers packages one by one until there are no remaining packages, then returns to the hub
    while truck2.package_list:
        package = package_table.get(truck2.package_list[0])
        distance_to_next = distances[truck2.current_location][package.address]
        truck2.miles += float(distance_to_next)
        truck2.current_location = package.address
        # Adds the time to the next address to the current time
        truck2.time = add_time(miles_to_time(distance_to_next), truck2.time)
        # Sets the package's delivery time to the current time
        package.delivery_time = truck2.time
        package.truck_id = truck2.truck_id
        package.status = 'Delivered'
        package_table.set(int(package.package_id), package)
        truck2.package_list.pop(0)
        if not truck2.package_list:
            truck2.miles += float(distances[truck2.current_location][hub_address])
            truck2.current_location = hub_address

    # Sets the time that the truck returns to the current time
    truck2.return_time = truck2.time
    print("Truck 2 Returns at: ", format_minutes(truck2.return_time))

    # Runs the delivery algorithm to sort the package list in the most efficient manner
    truck3_list = delivery_algo(truck3_list)

    # Initializes the Truck Object to hold the packages and sets it to 8:00 AM and loads the sorted packages
    truck3 = Truck(3, 620, truck3_list)

    # Sets the truck's location to the hub
    truck3.current_location = hub_address

    print("Truck 3 leaves hub at", format_minutes(truck3.time))

    # Truck leaves the hub, and updates the packages on the truck to being 'En Route' to their destination
    update_transport_time(package_table, truck3_list, truck3.time, 'En Route')

    # Delivers packages one by one until there are no remaining packages, then returns to the hub
    while truck3.package_list:
        package = package_table.get(truck3.package_list[0])
        distance_to_next = distances[truck3.current_location][package.address]
        truck3.miles += float(distance_to_next)
        truck3.current_location = package.address
        # Adds the time to the next address to the current time
        truck3.time = add_time(miles_to_time(distance_to_next), truck3.time)
        # Sets the package's delivery time to the current time
        package.delivery_time = truck3.time
        package.truck_id = truck3.truck_id
        package.status = 'Delivered'
        package_table.set(int(package.package_id), package)
        truck3.package_list.pop(0)
        if not truck3.package_list:
            truck3.miles += float(distances[truck3.current_location][hub_address])
            truck3.current_location = hub_address

    # Sets the time that the truck returns to the current time
    truck3.return_time = truck3.time
    print("Truck 3 returns at:", format_minutes(truck3.return_time))

    # Adds up the total mileage traveled for all three trucks
    all_mileage = truck1.miles + truck2.miles + truck3.miles
    print("------")
    print("Total Mileage for deliveries:", round(all_mileage, 2))
    print("------")
    print("All Packages Delivered")
    print("------")

    return package_table


def update_transport_time(hash_table, truck_list, transport_time, status):
    """
    This method takes a hash table, list, time, and status as arguments. For each package id in the list of packages,
    it takes the package out of the table and updates when it leaves the hub, updates the status to 'En Route' and
    sets the hash table key to a new value

    Algorithmic Complexity: O(n). Each item in the truck list is iterated over, and because the hash table doesn't
    need to resize and each key only has one element associated with it, the complexity stays O(n).
    """
    for package_id in truck_list:
        package = hash_table.get(package_id)
        package.departure_time = transport_time
        package.status = status
        hash_table.set(package_id, package)


def update_delivery_time(hash_table, package_id, delivery_time):
    """
    This method takes a hash table, package id, and time as arguments. For the selected package id, is searches
    the hash table for the package with that id, and updates the package's delivery time with the inputted delivery
    time.

    Algorithmic Complexity: O(1). This function in this program will run at O(1) because it's only updating a single
    item
    """
    package = hash_table.get(package_id)
    package.delivery_time = delivery_time
    hash_table.set(package_id, package)


def miles_to_time(miles):
    """
    This function takes the number of miles between locations and converts it into minutes based on the
    speed of the delivery trucks, which is 18 miles per hour.

    Algorithmic Complexity: O(1).
    """
    converted_time = round(float(miles) / 0.3)
    return converted_time


def add_time(minutes_to_add, prev_time):
    """
    This function takes the amount of time in minutes and adds the minutes of the trip from one location to the
    next to get an accurate representation of where each package is and when it was delivered

    Algorithmic Complexit: O(1).
    """
    updated_time = minutes_to_add + int(prev_time)
    return updated_time


def delivery_algo(package_list):
    """
    delivery_algo:
    implements a greedy algorithm that starts at the hub and then moves to the next closest
    address. It repeats that until every address has been visited, and then returns back to the hub address. It
    takes a list of packages as input to determine the order of delivery, then organizes the package list in
    to the appropriate order and returns a hash table.

    Algorithmic Complexity: O(n^2). This greedy algorithm is polynomial in time. It has a loop
    that iterates over every package id found in a list, and within that loop there is a for loop that iterates
    over every package id in the package list.
    """

    # initializes the hub address variable to the starting address
    hub_address = "4001 South 700 East"
    current_address = hub_address

    # creates a hash table that contains all of the package data
    package_table = package_reader()

    # creates a dictionary with all of the locations and distances
    distances = distance_reader()

    # initializes a list that will hold all of the sorted package ids
    sorted_list = []

    # starting a the hub, it creates a circuit graph where each vertex of the graph is weighted
    # then determines which one has the lowest weight. The weights are equal to the number of miles between
    # addresses
    while package_list:
        shortest_first = []
        shortest_distance = None
        for package_id in package_list:
            package = package_table.get(int(package_id))
            # retrieves the distance from the current location to the next location
            distance = distances[current_address][package.address]
            if shortest_distance is not None:
                if float(distance) < float(shortest_distance):
                    # Checks to see if the distance is smaller than the shortest distance from the current location
                    shortest_distance = float(distance)
                    shortest_first.insert(0, int(package.package_id))
                else:
                    shortest_first.append(int(package.package_id))
            else:
                shortest_distance = float(distance)
                shortest_first.append(int(package.package_id))

        current_package = package_table.get(shortest_first[0])
        current_address = current_package.address
        sorted_list.append(shortest_first[0])
        package_list.remove(shortest_first[0])

    return sorted_list
