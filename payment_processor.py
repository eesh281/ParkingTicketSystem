class PaymentProcessor:
    """This class will process payment with proper info, this method can be modified using different mode of payment like credit, cash, etc"""
    def process_payment(self, amount):
        print(f"Payment processed for ${amount}.")
