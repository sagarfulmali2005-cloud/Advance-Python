class UPI:
    def pay(self, amount):
        print("Payment of Rs.", amount, "made through UPI.")


class CreditCard:
    def pay(self, amount):
        print("Payment of Rs.", amount, "made through Credit Card.")


class DebitCard:
    def pay(self, amount):
        print("Payment of Rs.", amount, "made through Debit Card.")


class NetBanking:
    def pay(self, amount):
        print("Payment of Rs.", amount, "made through Net Banking.")


class PaymentProcessor:

    def __init__(self, method):
        self.method = method

    def set_payment_method(self, method):
        self.method = method

    def process_payment(self, amount):
        if amount <= 0:
            print("Invalid payment amount.")
            return

        self.method.pay(amount)


def main():

    print("Payment Processing System")
    print("-------------------------")

    payment = PaymentProcessor(UPI())
    payment.process_payment(1200)

    payment.set_payment_method(CreditCard())
    payment.process_payment(2500)

    payment.set_payment_method(DebitCard())
    payment.process_payment(1800)

    payment.set_payment_method(NetBanking())
    payment.process_payment(3500)


if __name__ == "__main__":
    main()

    