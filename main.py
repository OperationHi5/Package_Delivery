#  Jacob Clingler - Student ID: 000968521

import csv
import re
from deliver_packages import *
from hashtable import *
from package import *
from distance_reader import *
from truck import *
from datetime import *


# def package_lookup(selected_package, selected_time):
#     statement = '\nID: ' + str(selected_package.id) + ' Address: ' + str(selected_package.address) + \
#                 ' City: ' + str(selected_package.city) + ' Postal Code: ' + str(selected_package.postal_code) + \
#                 ' Delivery Deadline: ' + str(format_minutes(selected_package.deadline)) + \
#                 ' Weight: ' + str(selected_package.weight) + ' Status: '
#     if selected_package is not None:
#         if selected_time < selected_package.departure_time:
#
#             statement1 = statement + 'At Hub'
#
#             return statement1
#
#         elif selected_package.delivery_time > selected_time > selected_package.departure_time:
#
#             statement2 = statement + 'En Route'
#
#             return statement2
#
#         elif selected_time >= selected_package.delivery_time:
#             statement3 = statement + selected_package.status + ' At ' + format_minutes(selected_package.delivery_time)
#
#             return statement3

class Main:

    while True:
        print("Welcome: ")
        print("\n 1. Run Program \n 2. Package Lookup \n 3. Print All Package Status \n 4. Exit \n")
        input1 = input('Please Select a Menu Option: ')

        if input1 == '1':
            deliver_packages()
        # elif input1 == '2':
        #     while True:
        #         package_id = int(input("\nPlease enter the ID (1-40) of the Package you would like to look up"
        #                                "or Enter '0' to Exit: \n"))
        #         selected_package = hashtable.get(int(package_id))
        #
        #         if package_id == 0:
        #             print("\nExiting Lookup\n")
        #             break
        #
        #         elif selected_package is not None:
        #             while True:
        #                 status_time = input("Please Enter the Time You Would Like The Status At: "
        #                                     "(Example: 10:00 AM or 3:00 PM) \n")
        #                 format_check = re.match("[0-9][0-9]:[0-9][0-9] [A-Z][A-Z]", status_time)
        #                 if bool(format_check):
        #                     status_time = time_to_minutes(status_time)
        #                     print(package_lookup(selected_package, status_time))
        #                     break
        #                 else:
        #                     print("Please Enter Time in the Correct Format (HH:MM AM)")
        #
        #         else:
        #             print('Please select a valid package ID...\n')
        #
        # elif input1 == '3':
        #     status1 = 540
        #     status2 = 600
        #     status3 = 780
        #     print('\n---------\n')
        #     print('All Package Status at ' + format_minutes(status1) + '\n')
        #     for i in range(1, 41):
        #         print(package_lookup(hashtable.get(i), status1))
        #
        #     print('\n---------\n')
        #     print('All Package Status at ' + format_minutes(status3) + '\n')
        #     for i in range(1, 41):
        #         print(package_lookup(hashtable.get(i), status2))
        #
        #     print('\n---------\n')
        #     print('All Package Status at ' + format_minutes(status3) + '\n')
        #     for i in range(1, 41):
        #         print(package_lookup(hashtable.get(i), status3))

        elif input1 == '4':
            print('Exiting Program, Goodbye!\n')
            break

        else:
            print('\nPlease Select a Valid Option...\n')

