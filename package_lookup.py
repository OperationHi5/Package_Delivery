from format_time import *


def package_lookup(selected_package, selected_time):
    """
    This function takes a package and a time as input, and then returns a string that displays
    information of all of the attributes of the package at the designated time.

    Algorithmic Complexity: O(1). Searching and printing data for a single item in a 1 to 1 mapped hash table is O(1)
    in complexity
    """
    statement = '\nID: ' + selected_package.package_id + ' Address: ' + selected_package.address + \
                ' City: ' + selected_package.city + ' Postal Code: ' + selected_package.zipcode + \
                ' Delivery Deadline: ' + format_minutes(selected_package.deadline) + \
                ' Weight: ' + selected_package.weight + ' Status: '
    # Ensures that a package is selected
    if selected_package is not None:
        # Because no trucks can leave the hub before 8:00 AM, all packages should have this status before 8:00 AM
        if selected_time < 480:
            # Appends the proper status to the statement string
            statement1 = statement + 'At Hub'
            return statement1

        elif selected_package.delivery_time > selected_time > selected_package.departure_time:
            # If the desired time is before the delivery time, but after the package has left on the truck
            # Appends the proper status to the statement string
            statement2 = statement + 'En Route'
            return statement2

        elif selected_time >= selected_package.delivery_time:
            # If the desired time is after the delivery time
            # Appends the proper status and delivery time to the statement string
            statement3 = statement + selected_package.status + ' At ' + format_minutes(selected_package.delivery_time)

            return statement3


def all_package_search(package_table, selected_time):
    """
    This function takes a hash table and a time as input, and iterates through all items in the hash table
    to display the attributes for every package in the table at the designated time.

    Algorithmic Complexity: O(N). Since n items are being searched through, the complexity is only O(N). Would
    be higher in a situation where there were multiple elements associated with a single key.
    """
    for i in range(1, 41):
        package = package_table.get(i)
        statement = '\nID: ' + package.package_id + ' Address: ' + package.address + \
                    ' City: ' + package.city + ' Postal Code: ' + package.zipcode + \
                    ' Delivery Deadline: ' + format_minutes(package.deadline) + \
                    ' Weight: ' + package.weight + ' Status: '
        if package is not None:
            # Ensures that a package is selected
            if selected_time < 480 or selected_time < package.departure_time:
                # If the time is before 8:00 AM or before the package's departure time
                # Certain Packages can't leave until a certain time
                # Appends the proper status to the statement string
                statement1 = statement + 'At Hub'

                print(statement1)

            elif package.delivery_time > selected_time > package.departure_time:
                # If the desired time is before the delivery time, but after the package has left on the truck
                # Appends the proper status to the statement string
                statement2 = statement + 'En Route'

                print(statement2)

            elif selected_time >= package.delivery_time:
                # If the desired time is after the delivery time
                # Appends the proper status and delivery time to the statement string
                statement3 = statement + package.status + ' At ' + format_minutes(package.delivery_time)

                print(statement3)
