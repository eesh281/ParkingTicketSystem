class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.occupied = False

    def occupy_spot(self):
        self.occupied = True

    def free_spot(self):
        self.occupied = False
