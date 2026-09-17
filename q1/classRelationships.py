class MusicalInstrument:
    def __init__(self, name: str, type: str, primary_material: str, price: int):
        self.name = name
        self.type = type
        self.primary_material = primary_material
        self.__price = price
    def play(self, song_title: str) -> str:
        return f"The {self.name} is now beautifully playing '{song_title}'!"
    def apply_discount(self, discount_amount: int):
        if discount_amount > 0 and discount_amount < self.__price:
            self.__price -= discount_amount
            print(f"[Success] Applied a ${discount_amount} discount to the {self.name}.")
        else:
            print(f"[Error] Invalid discount amount for the {self.name}.")
    def get_details(self) -> str:
        return f"{self.name} ({self.type}, made of {self.primary_material}) - Price: ${self.__price}"
class Musician:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
        self.instrument = None
    def assign_instrument(self, instrument):
        self.instrument = instrument
    def play(self, instrument):
        return instrument.play("Hotel California")
if __name__ == "__main__":
    instrument = MusicalInstrument("Guitar", "String", "Wood", 1200)
    musician = Musician("Alex", 30000)
    print("--- BEFORE RELATIONSHIP ---")
    print("Musician:", musician.name)
    print("Instrument:", musician.instrument)
    print("\n--- BUILDING RELATIONSHIP ---")
    musician.assign_instrument(instrument)
    print("Instrument assigned.")
    print("\n--- AFTER RELATIONSHIP ---")
    print("Musician:", musician.name)
    print("Instrument:", musician.instrument.name)
    print("\n--- ACCESSING DATA THROUGH RELATIONSHIP ---")
    print(musician.instrument.get_details())
    print(musician.play(musician.instrument))
