from abc import ABC, abstractmethod

# Product A
class IPayment(ABC):
    @abstractmethod
    def pay(self):
        pass


# Product B
class IReceipt(ABC):
    @abstractmethod
    def download(self):
        pass


# Concrete Products - Stripe
class StripePayment(IPayment):
    def pay(self):
        print("Stripe Pay")


class StripeReceipt(IReceipt):
    def download(self):
        print("Stripe Download")


# Concrete Products - Crypto
class CryptoPayment(IPayment):
    def pay(self):
        print("Crypto Pay")


class CryptoReceipt(IReceipt):
    def download(self):
        print("Crypto Download")


# Abstract Factory
class IPaymentFactory(ABC):
    @abstractmethod
    def create_payment(self):
        pass

    @abstractmethod
    def create_receipt(self):
        pass


# Concrete Factory 1
class StripeFactory(IPaymentFactory):
    def create_payment(self):
        return StripePayment()

    def create_receipt(self):
        return StripeReceipt()


# Concrete Factory 2
class CryptoFactory(IPaymentFactory):
    def create_payment(self):
        return CryptoPayment()

    def create_receipt(self):
        return CryptoReceipt()


# Client
class Checkout:
    def __init__(self, factoryabs: IPaymentFactory):
        self._payment = factoryabs.create_payment()
        self._receipt = factoryabs.create_receipt()

    def process(self):
        self._payment.pay()
        self._receipt.download()


# Main
if __name__ == "__main__":
    # Select Stripe family
    factory = StripeFactory()
    checkout = Checkout(factory)
    checkout.process()

    print()

    # Switch to Crypto family
    factory = CryptoFactory()
    checkout = Checkout(factory)
    checkout.process()