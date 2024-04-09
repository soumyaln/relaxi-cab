from app.model.customer.customer import Customer
from app.model.customer.customer_mgr import CustomerManager
from app.utils.utils import generate_user_ids
from app.utils.common import Rating

from fastapi import APIRouter, Response

router = APIRouter(prefix='/api/v1/customer')


class CustomerService:

    def __init__(self):
        self.custIDs = []

    @router.post('/register')
    def register(self, name: str, email: str, phone: str):
        """
        This route registers a new customer
        """
        cus_name = name
        cus_email = email
        cus_phone = phone
        cus_id = "cus"+generate_user_ids()
        cus_rating = Rating.UNASSIGNED

        while cus_id in self.custIDs:
            cus_id = generate_user_ids()

        cus_mgr_instance = CustomerManager.get_instance()

        try:
            cus_obj = Customer(cus_name, cus_email, cus_phone)
            cus_obj.customer_id = cus_id
            cus_obj.rating = cus_rating
            cus_mgr_instance.add_customer(cus_name, cus_obj)
            self.custIDs = cus_id
            return {"message": "Customer registered", "status": 200}
        except KeyError:
            return {"message": "Invalid request parameters", "status": 400}
        except Exception as e:
            return {"message": f"Unable to register customer: {str(e)}", "status": 500}

