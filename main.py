class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
            self,
            max_speed,
            efficiency,
            load_weight,
            bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        base_cost = super().get_trip_cost(distance, food_price)
        return base_cost + (self.load_weight * 0.01)

    def get_cargo_volume(self):
        return self.bed_area * 2


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume

def main():
    catapult = Catapult(5,3,7)
    battering_ram = BatteringRam(3,4,2, 2)
    print(f"For Catapult Cargo volume: {catapult.get_cargo_volume()}, Trip_cost: {catapult.get_trip_cost(5,5)}")
    print(f"{battering_ram.get_cargo_volume()} Battering Ram")

main()