from parking_spot import ParkingSpot

class ParkingSystem:
    """This class will be responsible for parking and removing car from parking area.
    Attr:
        max_spots: This instance is for max number of spots.
        available_spots: This instance is for max number of available spots.
        parking_spots: This instance is for parked spots.
    """
    def __init__(self, max_spots):
        """Initializes the Parking System with the instances max spots, avaiable spots & parked spots."""
        self.max_spots = max_spots
        self.available_spots = max_spots
        self.parking_spots = [ParkingSpot(i) for i in range(1, max_spots + 1)]
     
    def park_car(self):
        """This method will check available spot and return spot_id."""
        if self.available_spots > 0:
            for spot in self.parking_spots:
                if not spot.occupied:
                    spot.occupy_spot()
                    self.available_spots -= 1
                    print(f"Car parked successfully at spot {spot.spot_id}.")
                    return spot.spot_id
        print("There is no available spot in this area")
        return None
   
    def remove_car(self, spot_id):
        """This method will remove car with proper spot_id"""
        for spot in self.parking_spots:
            if spot.spot_id == spot_id:
                spot.free_spot()
                self.available_spots += 1
                print(f"Car removed from the parking spot {spot_id}.")
                return
        print("Invalid spot ID")
