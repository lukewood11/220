"""
Name: Luke Wood
Interest.py

Problem: this program illustrates a hello function

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    annual_interest = eval(input("Enter annual interest"))
    bill_cycle = eval(input("Enter days in the billing cycle"))
    net_balance = eval(input("Enter credit card statement"))
    amount_paid = eval(input("Enter amount paid"))
    date_payment = eval(input("Enter date of payment"))
    step_1 = net_balance * bill_cycle
    step_2 = amount_paid * (bill_cycle - date_payment)
    step_3 = step_1 - step_2
    step_4 = step_3 / bill_cycle
    step_5 = ((annual_interest/100) / 12) * step_4
    print(round(step_5, 2))





