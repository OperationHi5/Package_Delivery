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
            print("At What Time Would You Like To Check The Status of All Packages?")
            status_time = input("\n 1. 9:00 AM \n 2. 10:00 AM \n 3. 1:00 PM \n Select An Option: ")
            if status_time != 1 or status_time != 2 or status_time != 3:
                print("Please Select a Valid Option")

            if status_time == '1':
                hashtable = deliver_packages()
                all_package_search(hashtable, 540)
            elif status_time == '2':
                hashtable = deliver_packages()
                all_package_search(hashtable, 600)
            elif status_time == '3':
                hashtable = deliver_packages()
                all_package_search(hashtable, 780)

        elif input1 == '4':
            print('Exiting Program, Goodbye!\n')
            break

        else:
            print('\nPlease Select a Valid Option...\n')

