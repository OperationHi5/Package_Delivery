class Truck:
    """
    The Truck class is used to create truck objects that can in turn hold packages for delivery. It has attributes
    that can hold data about the truck's current location as well as where it needs to go. It also holds the total
    mileage of the truck throughout its delivery journey.
    """

    # Sets the init method for the Truck class so that it can be used for the trucks data and to hold packages
    # and address, location, and mileage information
    def __init__(self, truck_id, time, package_list):
        self.truck_id = truck_id
        self.package_list = package_list
        self.time = time
        self.departure_time = 0
        self.return_time = None
        self.miles = 0.0
        self.current_location = ""
        self.next_location = ""
