class MusicalInstrument:
    def __init__(self, name: str, type: str, primary_material: str, price: int):
        """Initializes a new musical instrument object."""
        self.name = name
        self.type = type
        self.primary_material = primary_material
        self.__price = price
    def play(self, song_title: str) -> str:
        return f"🎶 The {self.name} is now beautifully playing '{song_title}'!"
    def apply_discount(self, discount_amount: int):
        if discount_amount > 0 and discount_amount < self.__price:
            self.__price -= discount_amount
            print(f"[Success] Applied a ${discount_amount} discount to the {self.name}.")
        else:
            print(f"[Error] Invalid discount amount for the {self.name}.")
    def get_details(self) -> str:
        return f"{self.name} ({self.type}, made of {self.primary_material}) - Price: ${self.__price}"
if __name__ == "__main__":
    instrument1 = MusicalInstrument("Stratocaster Guitar", "String", "Alder Wood", 1200)
    instrument2 = MusicalInstrument("Silver Flute", "Woodwind", "Silver", 800)
    print("--- BEFORE ---")
    print(f"Object 1: {instrument1.get_details()}")
    print(f"Object 2: {instrument2.get_details()}")
    print("-" * 40)
    print("Performing actions on Object 1...")
    print(instrument1.play("Hotel California"))
    instrument1.apply_discount(150)
    print("-" * 40)
    print("--- AFTER ---")
    print(f"Object 1 (Updated):   {instrument1.get_details()}")
    print(f"Object 2 (Unchanged): {instrument2.get_details()}")
