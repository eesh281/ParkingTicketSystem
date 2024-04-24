from parking_spot import ParkingSpot

class ParkingSystem:
    def __init__(self, max_spots):
        self.max_spots = max_spots
        self.available_spots = max_spots
        self.parking_spots = [ParkingSpot(i) for i in range(1, max_spots + 1)]

    def park_car(self):
        if self.available_spots > 0:
            for spot in self.parking_spots:
                if not spot.occupied:
                    spot.occupy_spot()
                    self.available_spots -= 1
                    print(f"Car parked successfully at spot {spot.spot_id}.")
                    return spot.spot_id
        print("No available spots. Please try again later.")
        return None

    def remove_car(self, spot_id):
        for spot in self.parking_spots:
            if spot.spot_id == spot_id:
                spot.free_spot()
                self.available_spots += 1
                print(f"Car removed from the parking spot {spot_id}.")
                return
        print("Invalid spot ID. Car not found.")
