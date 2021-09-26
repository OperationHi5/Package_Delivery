# creating a Truck class to create Truck objects
class Truck:
    def __init__(self, truck_id, time, package_list):
        self.truck_id = truck_id
        self.package_list = package_list
        self.time = time
        self.departure_time = 0
        self.return_time = None
        self.miles = 0.0
        self.current_location = ""
        self.next_location = ""
