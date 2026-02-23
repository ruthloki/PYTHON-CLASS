# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount
#         print("deposited",amount)
#     def withdrawal(self,amount):
#         pass

#     def show_balance(self):
#         return self.balance

# class SavingsAcc(BankAccount):
#     def withdrawal(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print("withdrawn successfully")
#         else:
#             print("insufficient balance")

# class CurrentAcc(BankAccount):
#     def withdrawal(self,amount):
#         if amount<=self.balance+5000:
#             self.balance-=amount
#             print("withdraw (od)Withdraw")
#         else:
#             print("od limit exceeded")

# name=input("enter the name: ")
# balance=int(input("enter the opening balance: "))
# print("1.Savings")
# print("2.Current")
# ch=int(input("enter account type:"))
# if ch==1:
#     obj = SavingsAcc(name,balance)
# elif ch==2:
#     obj= CurrentAcc(name,balance)
# else:
#     print("invalid account type")

# # s=BankAccount(name,balance)

# pin_input=int(input("enter the pin: "))
# if pin_input==1840:    
#     while True:
#         print("\n1.deposit\n2.withdrawal\n3.show balance\n4.exit")
#         choice=int(input("enter your choice: "))
#         if choice==1:
#             amount=int(input("enter the amount to deposit: "))
#             obj.deposit(amount)
#         elif choice==2:
#             amount=int(input("enter the amount to withdraw: "))
#             obj.withdrawal(amount)
#         elif choice==3:
#             obj.show_balance()
#         elif choice==4:
#             print("exiting...")
#             break
#         else:
#             print("invalid choice")
# else:    
#     print("invalid pin")



from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, number, total_seats):
        self.number = number
        self.total_seats = total_seats

    @abstractmethod
    def calculate_fare(self):
        pass

    def show_details(self):
        print(f"Bus No: {self.number}")
        print(f"Total Seats: {self.total_seats}")

class LuxuryBus(Vehicle):
    def calculate_fare(self):
        return 500

class OrdinaryBus(Vehicle):
    def calculate_fare(self):
        return 200

class SeatManager:
    def __init__(self, total_seats):
        self.__total = total_seats
        self.__booked = []

    def book_seat(self):
        if len(self.__booked) < self.__total:
            seat = len(self.__booked) + 1
            self.__booked.append(seat)
            return seat
        return None

    def cancel_seat(self, seat):
        if seat in self.__booked:
            self.__booked.remove(seat)
            return True
        return False

    def available_seats(self):
        return self.__total - len(self.__booked)

    def booked_seats(self):
        return self.__booked

class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Ticket:
    def __init__(self, passenger, bus, seat, fare):
        self.passenger = passenger
        self.bus = bus
        self.seat = seat
        self.fare = fare

    def show_ticket(self):
        print("\n--- BUS TICKET ---")
        self.passenger.show()
        print(f"Bus No: {self.bus.number}")
        print(f"Seat: {self.seat}")
        print(f"Fare: Rs.{self.fare}")
        print("------------------")

def main():

    print("1. Luxury (500)\n2. Ordinary (200)")
    choice = int(input("Choose bus: "))

    bus = LuxuryBus("KL-01", 5) if choice == 1 else OrdinaryBus("KL-02", 5)
    bus.show_details()

    manager = SeatManager(bus.total_seats)

    tickets = []

    while True:
        print("\n1.Available  2.Book  3.Cancel  4.Show  5.Exit")
        option = int(input("Enter choice: "))

        if option == 1:
            print("Available:", manager.available_seats())

        elif option == 2:
            seat = manager.book_seat()
            if seat is None:
                print("Bus Full!")
            else:
                name = input("Name: ")
                age = int(input("Age: "))
                passenger = Passenger(name, age)
                fare = bus.calculate_fare()  
                ticket = Ticket(passenger, bus, seat, fare)
                tickets.append(ticket)
                ticket.show_ticket()

        elif option == 3:
            seat_no = int(input("Seat to cancel: "))
            if manager.cancel_seat(seat_no):
                tickets = [t for t in tickets if t.seat != seat_no]
                print("Cancelled!")
            else:
                print("Invalid seat!")

        elif option == 4:
            if not tickets:
                print("No tickets booked.")
            else:
                for t in tickets:
                    t.show_ticket()

        elif option == 5:
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()