# creating a package class that will create package objects
class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.hub_time = None
        self.delivery_time = None
        self.departure_time = None
        self.truck_id = 0
