"""
Name: Luke Wood

sales_force.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from hw10.sales_person import SalesPerson


class SalesForce:
    """ encapsulates data for a sales person"""
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, 'r')
        for line in infile:
            t_list = (line.split(","))
            emp_id = t_list[0]
            name = t_list[1].strip()
            data = t_list[2].strip()
            data = (data.split(" "))
            data = [float(x) for x in data]
            worker = SalesPerson(emp_id, name)
            for i in data:
                worker.enter_sale(i)
            self.sales_people.append(worker)

    def quota_report(self, quota):
        q_report = []
        for person in self.sales_people:
            id = person.get_id()
            name = person.get_name()
            sales = person.total_sales()
            quota = person.met_quota(quota)
            list = [id, name, sales, quota]
            q_report.append(list)
        return q_report

    def top_seller(self):
        sellers = []
        self.sales_people.sort(reverse=True, key=SalesPerson.total_sales)
        sellers.append(self.sales_people[0])
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales == sellers[0].total_sales:
                sellers.append(self.sales_people[i])
        return sellers

    def individual_sales(self, employee_id):
        for thing in self.sales_people:
            if thing.get_id() == employee_id:
                return thing
        return None




