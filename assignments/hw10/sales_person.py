"""
Name: Luke Wood

sales_person.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """ encapsulates data for a sales person"""
    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = str(name)
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if sum(self.sales) >= quota:
            return True

        return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1

        if other.total_sales() < self.total_sales():
            return 1

        return 0

    def __str__(self):
        if self.employee_id is not None and self.name is not None and \
                self.total_sales() is not None:
            return str(self.employee_id) + "-" + self.name + ":" + str(self.total_sales())
        return None



