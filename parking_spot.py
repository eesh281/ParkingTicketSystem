
class ParkingSpot:
    '''This class responsible for checking parking spot is occupied or free spot. 
spot_id will be used in the constructor to determine if that spot is occupied or free'''
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.occupied = False

    def occupy_spot(self):
        self.occupied = True

    def free_spot(self):
        self.occupied = False
