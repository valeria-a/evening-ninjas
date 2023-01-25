class Branch:

    def __init__(self, branch_id, name, address, city):
        self.branch_id = branch_id
        self.name = name
        self.address = address
        self.city = city

    def set_address(self, new_address):
        self.address = new_address
