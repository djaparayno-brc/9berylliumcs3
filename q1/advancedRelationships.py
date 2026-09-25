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
class Guitar(MusicalInstrument):
    def __init__(self, name: str, type: str, primary_material: str, price: int, number_of_strings: int):
        super().__init__(name, type, primary_material, price)
        self.number_of_strings = number_of_strings
    def guitar_details(self) -> str:
        return f"{self.get_details()} - {self.number_of_strings} strings"
class Musician:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
        self.instrument = None
    def assign_instrument(self, instrument):
        self.instrument = instrument
    def play(self):
        if self.instrument:
            return self.instrument.play("Hotel California")
        return "No instrument assigned."
if __name__ == "__main__":
    guitar = Guitar(
        "Stratocaster Guitar",
        "String",
        "Alder Wood",
        1200,
        6
    )
    print("--- TEST 1: INHERITANCE ---")
    print("Guitar:", guitar.name)
    print("Material:", guitar.primary_material)
    print("Price:", guitar.get_details())
    print("Strings:", guitar.number_of_strings)
    print("\n--- TEST 2: AGGREGATION ---")
    musician = Musician("Alex", 30000)
    instrument = MusicalInstrument("Silver Flute", "Woodwind", "Silver", 800)
    musician.assign_instrument(instrument)
    print("Musician:", musician.name)
    print("Assigned Instrument:", musician.instrument.name)
    print("Instrument Details:", musician.instrument.get_details())
    print("\n--- TEST 3: USAGE ---")
    print(musician.play())
