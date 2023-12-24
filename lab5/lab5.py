class Person:
    def __init__(self, full_name, driving_experience):
        self.full_name = full_name
        self.driving_experience = driving_experience

    def __str__(self):
        return f"{self.full_name}, опыт вождения: {self.driving_experience} лет"


class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

    def __str__(self):
        return f"Двигатель: Мощность {self.power} л.с., Производитель: {self.manufacturer}"


class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Остановка")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def __str__(self):
        return f"Автомобиль: {self.brand}, Класс: {self.car_class}, Вес: {self.weight} кг\n" \
               f"Водитель: {self.driver}\n" \
               f"{self.engine}"

class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine, payload_capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.payload_capacity = payload_capacity

    def __str__(self):
        return super().__str__() + f"\nГрузоподъемность: {self.payload_capacity} кг"


class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f"\nМаксимальная скорость: {self.max_speed} км/ч"


# Пример использования классов
driver1 = Person("Иван Иванов", 5)
engine1 = Engine(200, "Производитель Япония")
car1 = Car("Тойота Камри", "Седан", 1500, driver1, engine1)

driver2 = Person("Петр Петров", 10)
engine2 = Engine(300, "Производитель Швеция")
lorry1 = Lorry("Вольво FH", "Грузовик", 8000, driver2, engine2, 5000)

driver3 = Person("Анна Сидорова", 3)
engine3 = Engine(400, "Производитель Италия")
sport_car1 = SportCar("Феррари 488", "Спорткар", 1200, driver3, engine3, 300)

print(car1)
print("\n" + "-" * 50 + "\n")
print(lorry1)
print("\n" + "-" * 50 + "\n")
print(sport_car1)
