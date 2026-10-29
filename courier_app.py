class Parcel:
    def __init__(self, parcel_id, status, location):
        self.parcel_id = parcel_id
        self.status = status
        self.location = location

    def update_status(self, new_status, new_location):
        self.status = new_status
        self.location = new_location

    def display(self):
        print(f"Parcel ID: {self.parcel_id}")
        print(f"Status: {self.status}")
        print(f"Location: {self.location}")


parcel = Parcel("PT-1001", "In transit", "City Hub")
parcel.display()

parcel.update_status("Out for delivery", "Main Street")
print("\nUpdated information:")
parcel.display()
