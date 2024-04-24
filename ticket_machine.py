from parking_system import ParkingSystem
from token_generator import TokenGenerator
from payment_processor import PaymentProcessor

class TicketMachine:
    """This  class represents a ticket machine for issuing parking tickets.
    Attr:
        parking_system: This instance is for managing parking spots.
        token_generator: This instance is for generating tokens.
        payment_processor:This instance is for processing payments.
    """
    def __init__(self, parking_system, token_generator, payment_processor):
        """Initializes a TicketMachine with the provided parking system, token generator,
        and payment processor."""
        self.parking_system = parking_system
        self.token_generator = token_generator
        self.payment_processor = payment_processor

    def issue_ticket(self):
        """Issues a parking ticket & returns generated token if parking is successful, otherwise None."""
        spot_id = self.parking_system.park_car()
        if spot_id:
            token = self.token_generator.generate_token(spot_id)
            print(f"Token generated: {token}")
            return token
        return None

    def process_payment(self, token):
        """Processes payment for a parking ticket.
        Args:
            token (str): Token associated with the parking ticket.
        """
        # Assume fixed parking fee for simplicity
        amount = 10  # $10 for parking
        self.payment_processor.process_payment(amount)
        self.parking_system.remove_car(int(token.split("_")[1]))
