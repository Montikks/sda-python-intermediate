from dataclasses import dataclass, field
from typing import List

@dataclass
class Item:
    name: str
    unit_price: float
    quantity: int

    def get_price(self) -> float:
        """Vypočítá a vrátí celkovou cenu položky."""
        return self.unit_price * self.quantity

@dataclass
class WeightedItem(Item):
    weight: float

    def __post_init__(self):
        self.quantity = 1  # Vždy nastaveno na 1 pro vážené položky

    def get_price(self) -> float:
        """Vypočítá a vrátí celkovou cenu vážené položky."""
        return self.unit_price * self.weight

@dataclass
class Basket:
    items: List[Item] = field(default_factory=list)

    def add_item(self, item: Item):
        """Přidá položku do košíku."""
        self.items.append(item)

    def print_basket(self) -> str:
        """Vrátí seznam položek v košíku ve formě stringu."""
        return '\n'.join(f"{item.name}: {item.get_price():.2f} Kč" for item in self.items)

    def calculate_price(self) -> float:
        """Vypočítá celkovou cenu položek v košíku."""
        total_price = sum(item.get_price() for item in self.items)
        return round(total_price, 2)

    def ask_and_add_item(self, item: Item):
        """Zeptá se uživatele na množství položky a přidá ji do košíku."""
        if isinstance(item, WeightedItem):
            item.weight = float(input(f"Zadejte váhu pro {item.name} (kg): "))
        else:
            item.quantity = int(input(f"Zadejte množství pro {item.name}: "))
        self.add_item(item)

# Příklad použití:
if __name__ == "__main__":
    # Předdefinované položky
    bananas = WeightedItem('banan', 27.90, 1, 0)
    avocado = Item('avokado', 32, 0)
    batteries = Item('baterky', 89.90, 0)

    # Vytvoření košíku
    basket = Basket()

    # Zeptání se na množství a přidání do košíku
    for item in [bananas, avocado, batteries]:
        basket.ask_and_add_item(item)

    # Výpis položek v košíku a celkové ceny
    print("Obsah košíku:")
    print(basket.print_basket())
    print(f"Celková cena: {basket.calculate_price()} Kč")
