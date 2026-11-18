class Patient: # A class called Patient is created:
    def __init__(self, name: str, bill_amount: float):  # self, name, and bill_amount were initialized with their data typed specified
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self) -> str:    # Function to get the name of patient
        return self.__name

    def set_name(self, name: str): # function to set the name of the patient
        self.__name = name

    def get_bill_amount(self) -> float: # function to get the bill amount for the patient
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: float): # function to set how much the bill amount is
        self.__bill_amount = bill_amount

    def calculate_bill(self) -> float: # function to calculate how much the patient needs to pay, including discounts
        return self.__bill_amount 

    def display_patient_type(self): # function to get the patient type
        print("Patient Type: Regular Patient")
# The regular patient does not have a discount.

class SeniorPatient(Patient):
    # the methods are polymorphed
    def calculate_bill(self) -> float:
        return self.get_bill_amount() * 0.80 # apply the senior citizen discount of 20%

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilHealthPatient(Patient):
    # the methods are polymorphed
    def calculate_bill(self) -> float:
        return self.get_bill_amount() * 0.85 # apply the philhealth member discount of 15%

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


# This is the main code where the functions are called out
if __name__ == "__main__":
    print("Hospital Billing System")
    print("-------------------------")
    print()

    # For the regular patient:
    pat1 = Patient("Dexter Josue A. Parayno", 67000.00)
    print(f"Patient Name: {pat1.get_name()}")
    pat1.display_patient_type()
    print(f"Original bill: ₱{pat1.get_bill_amount():,.2f}")
    print(f"Final bill: ₱{pat1.calculate_bill():,.2f}")
    print()

    # for the Senior Citizen Patient:
    pat2 = SeniorPatient("Bato Dela Rosa", 600000.00)
    print(f"Patient Name: {pat2.get_name()}")
    pat2.display_patient_type()
    print(f"Original bill: ₱{pat2.get_bill_amount():,.2f}")
    print(f"Final bill: ₱{pat2.calculate_bill():,.2f}")
    print()

    # for the PhilHealth Patient
    pat3 = PhilHealthPatient("Harry Potter", 9340.00)
    print(f"Patient Name: {pat3.get_name()}")
    pat3.display_patient_type()
    print(f"Original bill: ₱{pat3.get_bill_amount():,.2f}")
    print(f"Final bill: ₱{pat3.calculate_bill():,.2f}")
