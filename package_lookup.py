from format_time import *


def package_lookup(selected_package, selected_time):
    statement = '\nID: ' + selected_package.package_id + ' Address: ' + selected_package.address + \
                ' City: ' + selected_package.city + ' Postal Code: ' + selected_package.zipcode + \
                ' Delivery Deadline: ' + format_minutes(selected_package.deadline) + \
                ' Weight: ' + selected_package.weight + ' Status: '
    if selected_package is not None:
        if selected_time < 480:

            statement1 = statement + 'At Hub'

            return statement1

        elif selected_package.delivery_time > selected_time > selected_package.departure_time:

            statement2 = statement + 'En Route'

            return statement2

        elif selected_time >= selected_package.delivery_time:
            statement3 = statement + selected_package.status + ' At ' + format_minutes(selected_package.delivery_time)

            return statement3


def all_package_search(package_table, selected_time):
    for i in range(1, 41):
        package = package_table.get(i)
        statement = '\nID: ' + package.package_id + ' Address: ' + package.address + \
                    ' City: ' + package.city + ' Postal Code: ' + package.zipcode + \
                    ' Delivery Deadline: ' + format_minutes(package.deadline) + \
                    ' Weight: ' + package.weight + ' Status: '
        if package is not None:
            if selected_time < 480 or selected_time < package.departure_time:

                statement1 = statement + 'At Hub'

                print(statement1)

            elif package.delivery_time > selected_time > package.departure_time:

                statement2 = statement + 'En Route'

                print(statement2)

            elif selected_time >= package.delivery_time:
                statement3 = statement + package.status + ' At ' + format_minutes(package.delivery_time)

                print(statement3)
