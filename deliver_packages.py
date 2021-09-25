from hashtable import *
from package_reader import *
from distance_reader import *
from truck import *
from datetime import *


def deliver_packages():
    package_table = package_reader()

    distances = distance_reader()

    truck1_list = [13, 14, 15, 16, 34, 19, 20, 21, 4, 40]

    truck2_list = [3, 18, 12, 36, 37, 38]

    delayed_packages = [6, 25, 28, 32]

    truck3_list = [6, 25, 26, 1, 28, 7, 29, 30, 31, 32]

    hub_address = "4001 South 700 East"

    update_time(package_table, truck1_list, time(8, 0))
    update_time(package_table, truck2_list, time(8, 0))
    update_time(package_table, truck3_list, time(8, 0))
    update_time(package_table, delayed_packages, time(9, 5))

    truck1_list = delivery_algo(truck1_list)

    truck1 = Truck(1, time(8, 0), truck1_list)

    truck1.current_location = hub_address

    print("------")
    print("Truck Schedule: ")
    print("------")
    print("Truck one leaves hub at", truck1.time)

    update_transport_time(package_table, truck1_list, time(8, 0))

    while truck1.package_list:
        package = package_table.get(truck1.package_list[0])
        distance_to_next = distances[truck1.current_location][package.address]
        truck1.miles += float(distance_to_next)
        truck1.current_location = package.address
        truck1.time = add_time(miles_to_time(distance_to_next), truck1.time)
        package.delivery_time = truck1.time
        package.truck_id = truck1.truck_id
        package_table.set(int(package.package_id), package)
        truck1.package_list.pop(0)
        if not truck1.package_list:
            truck1.miles += float(distances[truck1.current_location][hub_address])
            truck1.current_location = hub_address

    truck1.return_time = truck1.time

    print("Truck 1 Returns at: ", truck1.return_time)

    truck2_list = delivery_algo(truck2_list)

    truck2 = Truck(2, time(8, 0), truck2_list)

    truck2.current_location = hub_address

    print("Truck 2 leaves hub at", truck2.time)
    update_transport_time(package_table, truck2_list, time(8, 0))

    while truck2.package_list:
        package = package_table.get(truck2.package_list[0])
        distance_to_next = distances[truck2.current_location][package.address]
        truck2.miles += float(distance_to_next)
        truck2.current_location = package.address
        truck2.time = add_time(miles_to_time(distance_to_next), truck2.time)

        package.delivery_time = truck2.time
        package.truck_id = truck2.truck_id
        package_table.set(int(package.package_id), package)
        truck2.package_list.pop(0)
        if not truck2.package_list:
            truck2.miles += float(distances[truck2.current_location][hub_address])
            truck2.current_location = hub_address

    truck2.return_time = truck2.time
    print("Truck 1 Returns at: ", truck2.return_time)

    truck3_list = delivery_algo(truck3_list)
    truck3 = Truck(3, truck1.return_time, truck3_list)
    truck3.current_location = hub_address

    print("Truck 3 leaves hub at", truck3.time)

    update_transport_time(package_table, truck3_list, time(9, 5))

    while truck3.package_list:
        package = package_table.get(truck3.package_list[0])
        distance_to_next = distances[truck3.current_location][package.address]
        truck3.miles += float(distance_to_next)
        truck3.current_location = package.address
        truck3.time = add_time(miles_to_time(distance_to_next), truck3.time)
        package.delivery_time = truck3.time
        package.truck_id = truck3.truck_id
        package_table.set(int(package.package_id), package)
        truck3.package_list.pop(0)
        if not truck3.package_list:
            truck3.miles += float(distances[truck3.current_location][hub_address])
            truck3.current_location = hub_address

    truck3.return_time = truck3.time
    print("Truck 3 returns at:", truck3.return_time)

    truck1_list = [11, 22, 23, 24]
    truck1_list = delivery_algo(truck1_list)
    truck1.package_list = truck1_list
    truck1.current_location = hub_address
    truck1.time = truck2.return_time
    print("Truck 1 leaves hub again at", truck1.time)

    update_time(package_table, truck1_list, time(8, 0))
    update_transport_time(package_table, truck1_list, truck2.return_time)

    while truck1.package_list:
        package = package_table.get(truck1.package_list[0])
        distance_to_next = distances[truck1.current_location][package.address]
        truck1.miles += float(distance_to_next)
        truck1.current_location = package.address
        truck1.time = add_time(miles_to_time(distance_to_next), truck1.time)
        package.delivery_time = truck1.time
        package.truck_id = truck1.truck_id
        package_table.set(int(package.package_id), package)
        truck1.package_list.pop(0)
        if not truck1.package_list:
            truck1.miles += float(distances[truck1.current_location][hub_address])
            truck1.current_location = hub_address

    truck1.return_time = truck1.time
    print("Truck 1 returns again at:", truck1.return_time)

    truck2_list = [5, 8, 9, 10, 17, 2, 33, 39, 27, 35]
    truck2_list = delivery_algo(truck2_list)

    truck2.package_list = truck2.package_list
    truck2.current_location = hub_address
    truck2.time = truck3.return_time

    print("Truck 2 leaves hub again at", truck2.time)

    update_time(package_table, truck2_list, time(8, 0))
    update_transport_time(package_table, truck2_list, truck3.return_time)

    while truck2.package_list:
        package = package_table.get(truck2.package_list[0])
        distance_to_next = distances[truck2.current_location][package.address]
        truck2.miles += float(distance_to_next)
        truck2.current_location = package.address
        truck2.time = add_time(miles_to_time(distance_to_next), truck2.time)
        package.delivery_time = truck2.time
        package.truck_id = truck2.truck_id
        package_table.set(int(package.package_id), package)
        truck2.package_list.pop(0)
        if not truck2.package_list:
            truck2.miles += float(distances[truck2.current_location][hub_address])
            truck2.current_location = hub_address

    truck2.return_time = truck2.time
    print("Truck 2 returns again at:", truck2.return_time)

    all_mileage = truck1.miles + truck2.miles + truck3.miles
    print("------")
    print("Total Mileage for deliveries:", round(all_mileage, 2))
    print("------")
    print("All Packages Delivered")

    return package_table


def update_time(hash_table, truck_list, hub_time):
    for package_id in truck_list:
        package = hash_table.get(package_id)
        package.hub_time = hub_time
        hash_table.set(package_id, package)


def update_transport_time(hash_table, truck_list, transport_time):

    for package_id in truck_list:
        package = hash_table.get(package_id)
        package.transport_time = transport_time
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

    temp_date = date.today()
    converted_prev_time = datetime.combine(temp_date, prev_time)

    updated_time = (converted_prev_time + timedelta(minutes=minutes_to_add)).time()
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
