class Patient:
  def __init__ (self, name: str, bill_amount: float):
    self.name = name
    self.bill_amount = bill_amount

  def get_name (self):
    return self.name

  def set_name (self, name: str):
    self.name = name

  def get_bill_amount (self):
    return self.bill_amount

  def set_bill_amount (self, bill_amount: float):
    self.bill_amount = bill_amount

  def calculate_bill (self, bill_amount: float):
    return self.bill_amount

  def display_patient_type (self):
    print("Regular Patient")
    
class SeniorPatient(Patient):
  def __init__(self, name: str, bill_amount: float):
    super().__init__()
    self.number_of_pages = number_pages 
  def get_number_of_pages(self):
      return self.number_of_pages
   def set_number_of_pages(self, number_pages):
      if isinstance(number_pages, int) and number_pages > 0:
            self.number_of_pages = number_pages
      else:
            print("Number of pages must not be negative. Try again, it must not be negative this time.") #reply to wrong input
  
