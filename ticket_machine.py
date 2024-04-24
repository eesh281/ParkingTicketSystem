from parking_system import ParkingSystem
from token_generator import TokenGenerator
from payment_processor import PaymentProcessor

class TicketMachine:
    def __init__(self, parking_system, token_generator, payment_processor):
        self.parking_system = parking_system
        self.token_generator = token_generator
        self.payment_processor = payment_processor

    def issue_ticket(self):
        spot_id = self.parking_system.park_car()
        if spot_id:
            token = self.token_generator.generate_token(spot_id)
            print(f"Token generated: {token}")
            return token
        return None

    def process_payment(self, token):
        # Assume fixed parking fee for simplicity
        amount = 10  # $10 for parking
        self.payment_processor.process_payment(amount)
        self.parking_system.remove_car(int(token.split("_")[1]))
