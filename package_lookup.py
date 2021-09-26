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
