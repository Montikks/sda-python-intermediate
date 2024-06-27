class Vehicle:
    def __init__(self, brand, model, color, number_of_wheels, seat_capacity, max_speed=None):
        """
        Konstruktor třídy Vehicle inicializuje atributy vozidla.

        :param brand: Značka vozidla
        :param model: Model vozidla
        :param color: Barva vozidla
        :param number_of_wheels: Počet kol vozidla
        :param seat_capacity: Počet sedadel ve vozidle
        :param max_speed: Maximální rychlost vozidla (není povinný pro všechny)
        """
        self.brand = brand
        self.model = model
        self.color = color
        self.number_of_wheels = number_of_wheels
        self.seat_capacity = seat_capacity
        self.max_speed = max_speed

    def start(self):
        """Vypíše zprávu o startu vozidla."""
        print(f"{self.brand} {self.model} is starting.")

    def get_color(self):
        """Vrátí barvu vozidla."""
        return self.color

    def is_possible_to_reach(self, speed):
        """
        Zjistí, zda vozidlo může dosáhnout zadané rychlosti.

        :param speed: Požadovaná rychlost
        :return: True, pokud může dosáhnout rychlosti, jinak False
        """
        if self.max_speed is None:
            print("Max speed is not defined for this vehicle.")
            return False
        return speed <= self.max_speed


class Motorcycle(Vehicle):
    def __init__(self, brand, model, color, seat_capacity, max_speed):
        """
        Konstruktor třídy Motorcycle inicializuje atributy motocyklu.

        :param brand: Značka motocyklu
        :param model: Model motocyklu
        :param color: Barva motocyklu
        :param seat_capacity: Počet sedadel na motocyklu
        :param max_speed: Maximální rychlost motocyklu
        """
        super().__init__(brand, model, color, 2, seat_capacity, max_speed)


class Car(Vehicle):
    def __init__(self, brand, model, color, seat_capacity, max_speed):
        """
        Konstruktor třídy Car inicializuje atributy automobilu.

        :param brand: Značka automobilu
        :param model: Model automobilu
        :param color: Barva automobilu
        :param seat_capacity: Počet sedadel v automobilu
        :param max_speed: Maximální rychlost automobilu
        """
        super().__init__(brand, model, color, 4, seat_capacity, max_speed)


class Bus(Vehicle):
    def __init__(self, brand, model, color, seat_capacity):
        """
        Konstruktor třídy Bus inicializuje atributy autobusu.

        :param brand: Značka autobusu
        :param model: Model autobusu
        :param color: Barva autobusu
        :param seat_capacity: Počet sedadel v autobusu
        """
        # Max speed je pevně stanovena pro autobusy na 80 km/h
        super().__init__(brand, model, color, 6, seat_capacity, 80)


# Příklady použití
def main():
    # Vytvoření objektů
    bike = Motorcycle("Yamaha", "MT-07", "Blue", 2, 200)
    car = Car("Tesla", "Model S", "Red", 5, 250)
    bus = Bus("Mercedes", "Citaro", "White", 30)

    # Volání metod na objektech
    bike.start()  # Yamaha MT-07 is starting.
    print(bike.get_color())  # Blue
    print(bike.is_possible_to_reach(150))  # True
    print(bike.is_possible_to_reach(250))  # False

    car.start()  # Tesla Model S is starting.
    print(car.get_color())  # Red
    print(car.is_possible_to_reach(200))  # True
    print(car.is_possible_to_reach(300))  # False

    bus.start()  # Mercedes Citaro is starting.
    print(bus.get_color())  # White
    print(bus.is_possible_to_reach(70))  # True
    print(bus.is_possible_to_reach(100))  # False


if __name__ == "__main__":
    main()
