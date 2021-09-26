class Package:
    """
    Package class allows the creation of package objects. Stores all of the relevant information of the package
    so that packages can be loaded into trucks and delivered, with attributes that can be updated throughout
    the process of delivery. Package objects hold data that is pulled from the packages.csv file. After the
    object is created it is added to a hash table for easy/quick access.
    """

    # Sets the init method so that package objects can be created and hold package data
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.hub_time = 0
        self.transport_time = 0
        self.delivery_time = 0
        self.departure_time = 0
        self.truck_id = 0
        self.status = ' '
