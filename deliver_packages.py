from distance_reader import *
from format_time import *
from package_reader import *
from truck import *


def deliver_packages():
    package_table = package_reader()

    distances = distance_reader()

    truck1_list = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

    truck2_list = [2, 3, 6, 18, 25, 26, 27, 28, 32, 36, 38]

    truck3_list = [4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 33, 35, 39]

    hub_address = "4001 South 700 East"

    truck1_list = delivery_algo(truck1_list)

    truck1 = Truck(1, 480, truck1_list)

    truck1.current_location = hub_address

    print("------")
    print("Truck Schedule: ")
    print("------")
    print("Truck 1 leaves hub at", format_minutes(truck1.time))

    update_transport_time(package_table, truck1_list, 480, 'En Route')

    while truck1.package_list:
        package = package_table.get(truck1.package_list[0])
        distance_to_next = distances[truck1.current_location][package.address]
        truck1.miles += float(distance_to_next)
        truck1.current_location = package.address
        truck1.time = add_time(miles_to_time(distance_to_next), truck1.time)
        package.delivery_time = truck1.time
        package.truck_id = truck1.truck_id
        package.status = 'Delivered'
        package_table.set(int(package.package_id), package)
        truck1.package_list.pop(0)
        if not truck1.package_list:
            truck1.miles += float(distances[truck1.current_location][hub_address])
            truck1.current_location = hub_address

    truck1.return_time = truck1.time

    print("Truck 1 Returns at: ", format_minutes(truck1.return_time))

    truck2_list = delivery_algo(truck2_list)

    truck2 = Truck(2, 545, truck2_list)

    truck2.current_location = hub_address

    print("Truck 2 leaves hub at", format_minutes(truck2.time))
    update_transport_time(package_table, truck2_list, truck2.time, 'En Route')

    while truck2.package_list:
        package = package_table.get(truck2.package_list[0])
        distance_to_next = distances[truck2.current_location][package.address]
        truck2.miles += float(distance_to_next)
        truck2.current_location = package.address
        truck2.time = add_time(miles_to_time(distance_to_next), truck2.time)
        package.delivery_time = truck2.time
        package.truck_id = truck2.truck_id
        package.status = 'Delivered'
        package_table.set(int(package.package_id), package)
        truck2.package_list.pop(0)
        if not truck2.package_list:
            truck2.miles += float(distances[truck2.current_location][hub_address])
            truck2.current_location = hub_address

    truck2.return_time = truck2.time
    print("Truck 2 Returns at: ", format_minutes(truck2.return_time))

    truck3_list = delivery_algo(truck3_list)
    truck3 = Truck(3, 620, truck3_list)
    truck3.current_location = hub_address

    print("Truck 3 leaves hub at", format_minutes(truck3.time))

    update_transport_time(package_table, truck3_list, truck3.time, 'En Route')

    while truck3.package_list:
        package = package_table.get(truck3.package_list[0])
        distance_to_next = distances[truck3.current_location][package.address]
        truck3.miles += float(distance_to_next)
        truck3.current_location = package.address
        truck3.time = add_time(miles_to_time(distance_to_next), truck3.time)
        package.delivery_time = truck3.time
        package.truck_id = truck3.truck_id
        package.status = 'Delivered'
        package_table.set(int(package.package_id), package)
        truck3.package_list.pop(0)
        if not truck3.package_list:
            truck3.miles += float(distances[truck3.current_location][hub_address])
            truck3.current_location = hub_address

    truck3.return_time = truck3.time
    print("Truck 3 returns at:", format_minutes(truck3.return_time))

    all_mileage = truck1.miles + truck2.miles + truck3.miles
    print("------")
    print("Total Mileage for deliveries:", round(all_mileage, 2))
    print("------")
    print("All Packages Delivered")
    print("------")

    return package_table


def update_time(hash_table, truck_list, hub_time, status):
    for package_id in truck_list:
        package = hash_table.get(package_id)
        package.hub_time = hub_time
        package.status = status
        hash_table.set(package_id, package)


def update_transport_time(hash_table, truck_list, transport_time, status):

    for package_id in truck_list:
        package = hash_table.get(package_id)
        package.transport_time = transport_time
        package.status = status
        hash_table.set(package_id, package)


def update_delivery_time(hash_table, package_id, delivery_time):
    package = hash_table.get(package_id)
    package.delivery_time = delivery_time
    hash_table.set(package_id, package)


def update_truck(hash_table, truck_list, truck_id):
    for package_id in truck_list:
        package = hash_table.get(package_id)
        package.truck_id = truck_id
        hash_table.set(package_id, package)


def miles_to_time(miles):

    converted_time = round(float(miles) / 0.3)
    return converted_time


def add_time(minutes_to_add, prev_time):
    # print(minutes_to_add)
    # print(prev_time)
    updated_time = minutes_to_add + int(prev_time)
    # print(updated_time)
    return updated_time


def delivery_algo(package_list):

    hub_address = "4001 South 700 East"
    current_address = hub_address

    package_table = package_reader()
    distances = distance_reader()
    organized_list = []

    while package_list:
        shortest_first = []
        shortest_distance = None
        for package_id in package_list:
            package = package_table.get(int(package_id))
            distance = distances[current_address][package.address]
            if shortest_distance is not None:
                if float(distance) < float(shortest_distance):
                    shortest_distance = float(distance)
                    shortest_first.insert(0, int(package.package_id))
                else:
                    shortest_first.append(int(package.package_id))
            else:
                shortest_distance = float(distance)
                shortest_first.append(int(package.package_id))

        current_package = package_table.get(shortest_first[0])
        current_address = current_package.address
        organized_list.append(shortest_first[0])
        package_list.remove(shortest_first[0])

    return organized_list
