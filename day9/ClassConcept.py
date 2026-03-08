class HDFC:
    branch = "Nanganallur"
    Gold_ROI = 10

    def __init__(self):
        print("Iam Constructor")

    def create_customer(self):
        print("Creating customer")

    def check_balance(self):
        print("Checking balance")

    def check_payment(self):
        print("Checking payment")

    def get_OTP(self):
        print("Getting OTP")

    @staticmethod
    def get_aadhar():
        print("Getting aadhar")


obj = HDFC()
obj.create_customer()
print(obj.branch)

HDFC.get_aadhar()