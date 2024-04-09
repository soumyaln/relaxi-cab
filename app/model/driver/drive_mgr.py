from app.store import driverStore


class DriverManager:
    DriverManagerInst = None

    def __init__(self):
        self.driverStore = driverStore.driver_map

    @staticmethod
    def get_instance():
        if not DriverManager.DriverManagerInst:
            DriverManager.DriverManagerInst = DriverManager()
        return DriverManager.DriverManagerInst

    def add_driver(self, driver_name, driver_object):
        self.driverStore[driver_name] = driver_object

    def get_driver(self, driver_name):
        return self.driverStore[driver_name]

    def get_driver_map(self):
        return self.driverStore






