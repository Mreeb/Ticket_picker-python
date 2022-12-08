import pandas as pd
import random

class Ticket_picker:
    def __init__(self):
        self.df = None
        self.students_list = None
        self.ticket = None
        self.total_tickets = None
        self.Tickets = []
        self.draw = None
        flag = None

    def Read(self):
        self.df = pd.read_excel("ROSTER 1st140.xlsx")

    def working(self):
        self.input()
        choice = input('D to Draw ticket or q to exit: ').upper()
        while choice == 'D':
            self.draw = random.randint(1, self.total_tickets)
            start = 0
            stop = 0
            for i in range(len(self.students_list)):
                stop += self.Tickets[i]
                if self.draw in range(start, stop):
                    print("{} Wins!!!".format(self.students_list[i]))
                    start = stop
            choice = input('Draw again or q to exit: ').upper()

    def input(self):
        self.Read()
        # print(self.df)
        self.students_list = self.df["Students"].to_list()
        for student in self.students_list:
            try:
                self.ticket = int(input("Enter tickets for {}: ".format(student)))
            except ValueError:
                print("\nPlease only use integers")
                self.ticket = int(input("Enter tickets for {}: ".format(student)))
            self.Tickets.append(self.ticket)

        self.total_tickets = 0
        for tickets in self.Tickets:
            self.total_tickets += tickets


if __name__ == "__main__":
    print(20*"=", "Ticket Picker", 20*"=")
    obj = Ticket_picker()
    obj.working()
