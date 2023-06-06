

class Flight:
    def __init__(self, flight_number, route, departure_time, price):
        self.flight_number = flight_number
        self.route = route
        self.departure_time = departure_time
        self.price = price


flights = [
    Flight(1, "Израиль - Ирак", "12:00", 500),
    Flight(2, "Багдат - Нью-Йорк", "14:30", 1000),
    Flight(3, "Токио - Сидней", "10:45", 800),
]

def display_flights():
    print("Список доступных перелетов:")
    for flight in flights:
        print(f"Номер рейса: {flight.flight_number}")
        print(f"Маршрут: {flight.route}")
        print(f"Время вылета: {flight.departure_time}")
        print(f"Цена: {flight.price}")
        print("")

def make_payment(flight_number):
    flight = next((flight for flight in flights if flight.flight_number == flight_number), None)
    if flight:
        print(f"Выбран рейс: {flight.flight_number}")
        fio = input("Введите свое ФИО: ")
        payment = float(input("Введите сумму оплаты: "))
        if payment == flight.price:
            print("Оплата успешно завершена!")
            print(f"Номер рейса: {flight.flight_number}")
            print(f"ФИО: {fio}")
            print(f"Маршрут: {flight.route}")
            print(f"Время вылета: {flight.departure_time}")
        elif payment > flight.price:
            change = payment - flight.price
            print("Оплата успешно завершена!")
            print(f"Сдача: {change}")
            print(f"Номер рейса: {flight.flight_number}")
            print(f"ФИО: {fio}")
            print(f"Маршрут: {flight.route}")
            print(f"Время вылета: {flight.departure_time}")
        else:
            print("Недостаточно средств для оплаты!")
    else:
        print("Неверный номер рейса!")

try:
    display_flights()
    flight_number = int(input("Введите номер рейса: "))
    make_payment(flight_number)
except ValueError:
    print("Ошибка ввода!")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
