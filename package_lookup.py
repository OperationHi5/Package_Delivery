def package_lookup(selected_package, selected_time):
    statement = '\nID: ' + str(selected_package.id) + ' Address: ' + str(selected_package.address) + \
                ' City: ' + str(selected_package.city) + ' Postal Code: ' + str(selected_package.postal_code) + \
                ' Delivery Deadline: ' + str(format_minutes(selected_package.deadline)) + \
                ' Weight: ' + str(selected_package.weight) + ' Status: '
    if selected_package is not None:
        if selected_time < selected_package.departure_time:

            statement1 = statement + 'At Hub'

            return statement1

        elif selected_package.delivery_time > selected_time > selected_package.departure_time:

            statement2 = statement + 'En Route'

            return statement2

        elif selected_time >= selected_package.delivery_time:
            statement3 = statement + selected_package.status + ' At ' + format_minutes(selected_package.delivery_time)

            return statement3