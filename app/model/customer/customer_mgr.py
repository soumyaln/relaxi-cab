from app.store import customerStore


class CustomerManager:
    CustomerManagerInst = None

    def __init__(self):
        self.customerStore = customerStore.customer_map

    @staticmethod
    def get_instance():
        if not CustomerManager.CustomerManagerInst:
            CustomerManager.CustomerManagerInst = CustomerManager()
        return CustomerManager.CustomerManagerInst

    def add_customer(self, customer_name, customer_object):
        self.customerStore[customer_name] = customer_object

    def get_customer(self, customer_name):
        return self.customerStore[customer_name]

    def get_customer_map(self):
        return self.customerStore




