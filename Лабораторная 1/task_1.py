# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Car:
    def __init__(self, current_velocity: int, model: str):
        """
        :param current_velocity: текущая скорость автомобиля
        :param model: марка автомобиля

        примеры:
        >>> car_1 = Car(50, "Москвич")
"""
        ...
        if not isinstance(current_velocity, int):
            raise TypeError("скорость должна быть округленной до целого числа")
        if current_velocity <= 0:
            raise ValueError("скорость должна быть положительным числом")
        if current_velocity > 400:
            raise ValueError("скорость должна быть менее 400 км/ч")
        self.current_velocity = current_velocity

        if not isinstance(model, str):
            raise TypeError("название марки должно быть str")
        self.model = model

    def is_foreign_car(self) -> bool:
        """
               Функция, которая проверяет то, что является ли машина иномаркой

               :return: Является ли машина иномаркой

               Примеры:
               >>> car_1 = Car(50, "Москвич")
               >>> car_1.is_foreign_car()
               """
        ...

    def speed_limit(self) -> bool:
        """
               Функция проверяет, превышает ли машина разрешенную скорость
                :return: превышена ли скорость
               Примеры:
               >>> car_2 = Car(60, 'Лада')
               >>> car_2.speed_limit()
               """



class Phone:
    def __init__(self, price: int, camera_type: str,memory_in_gb: int):
        """
        :param price: стоимость телефона в рублях
        :param camera_type: тип камеры телефона
        :memory_in_gb: количество памяти телефона в гигабайтах

        примеры:
        >>> phone_1 = Phone(30000, "4k", 64)
"""
        ...
        if not isinstance(price, int):
            raise TypeError("значения должны быть целыми числами")
        if price <= 0:
            raise ValueError("значения должны быть положительными числами")
        if memory_in_gb < 5:
            raise ValueError("слишком низкий объем памяти")
        self.price = price
        self.memory_in_gb = memory_in_gb
        self.camera_type = camera_type

    def change_price(self) -> None:
        """
               Функция изменения цены

               :return: измененная цена телефона

               Примеры:
               >>> phone_1 = Phone(30000, "4k", 64)
               >>> phone_1.change_price()
               """
        ...

    def expand_memory(self) -> None:
        """
               Функция увеличивает базовую память телефона
                :return: измененный объем памяти
               Примеры:
               >>> phone_2 = Phone(40000, "2k", 32)
               >>> phone_2.expand_memory()
               """


class Ticket:
    def __init__(self, movie: str, time: str,date: str, room: int):
        """
        :param movie: название фильма, на который куплен билет
        :param time: время начала сеанса
        :param date: дата сеанса
        :param room: комната, в которой показывают фильм

        примеры:
        >>> ticket_1 = Ticket("Чебурашка", "12:00", "10.12.2023", 5)

"""
        ...
        if not isinstance(room, int):
            raise TypeError("номер комнаты должен быть целым числом")
        if room <= 0:
            raise ValueError("номер комнаты должен быть положительным числом")
        self.movie = movie
        self.time = time
        self.date = date
        self.room = room

    def change_room(self) -> None:
        """
               Функция изменяет локацию показа фильма

               :return: измененная комната показа фильма

               Примеры:
               >>> ticket_1 = Ticket("Чебурашка", "12:00", "10.12.2023", 5)
               >>> ticket_1.change_room()
               """
        ...

    def is_expired_ticket(self) -> bool:
        """
               Функция проверяет, просрочен ли билет
                :return: Является ли билет просроченным
               Примеры:
               >>> ticket_2 = Ticket("Иван Царевич и Серый Волк", "10:00", "1.10.2022", 3)
               >>> ticket_2.is_expired_ticket()
               """




if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации

    pass

