#  Jacob Clingler - Student ID: 000968521

import re

from deliver_packages import *
from package_lookup import *


class Main:

    while True:
        print("Welcome: ")
        print("\n 1. Run Program \n 2. Package Lookup \n 3. Print All Package Status \n 4. Exit \n")
        input1 = input('Please Select a Menu Option: ')

        if input1 == '1':
            deliver_packages()
        elif input1 == '2':
            while True:
                all_packages = deliver_packages()
                package_id = int(input("\nPlease enter the ID (1-40) of the Package you would like to look up"
                                       "or Enter '0' to Exit: \n"))
                if package_id < 1 or package_id > 40:
                    print("\nPlease Select a Valid Package ID\n")
                    break
                else:
                    selected_package = all_packages.get(package_id)
                    while True:
                        status_time = input("Please Enter the Time You Would Like The Status At: "
                                            "(Example: 10:00 AM or 3:00 PM) \n")
                        format_check = re.match("[0-9][0-9]:[0-9][0-9] [A-Z][A-Z]", status_time)
                        if bool(format_check):
                            status_time = convert_to_minutes(status_time)
                            print(package_lookup(selected_package, status_time))
                            break
                        else:
                            print("Please Enter Time in the Correct Format (HH:MM AM)")

        elif input1 == '3':
            status1 = 540
            status2 = 600
            status3 = 780
            print('\n---------\n')
            print('All Package Status at ' + format_minutes(status1) + '\n')
            for i in range(1, 41):
                print(package_lookup(hashtable.get(i), status1))

            print('\n---------\n')
            print('All Package Status at ' + format_minutes(status3) + '\n')
            for i in range(1, 41):
                print(package_lookup(hashtable.get(i), status2))

            print('\n---------\n')
            print('All Package Status at ' + format_minutes(status3) + '\n')
            for i in range(1, 41):
                print(package_lookup(hashtable.get(i), status3))

        elif input1 == '4':
            print('Exiting Program, Goodbye!\n')
            break

        else:
            print('\nPlease Select a Valid Option...\n')

