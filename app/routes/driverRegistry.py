from app.model.driver.driver import Driver
from app.model.driver.drive_mgr import DriverManager

from fastapi import APIRouter, Response

router = APIRouter(prefix='/api/v1/driver')


class DriverService:

    @router.post('/register')
    def register(self, **kwargs):
        """
        This route registers a new driver
        """
        driver_name = kwargs["name"]
        driver_email = kwargs["email"]
        driver_phone = kwargs["phone"]

        driver_mgr_instance = DriverManager.get_instance()

        try:
            driver_obj = Driver(driver_name, driver_email, driver_phone)
            driver_mgr_instance.add_driver(driver_name, driver_obj)

            return {"message": "Driver registered", "status": 200}
        except Exception:
            return {"message": "unable to register driver", "status": 500}
