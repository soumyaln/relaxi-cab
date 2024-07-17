from fastapi import FastAPI, HTTPException, Body
from models.customer_mgr import CustomerManager
from models.customer import Customer



app = FastAPI()

@app.post("/customer/signup")
async def signup(name: str = Body(...), email: str = Body(...), phone_number: str = Body(...), password: str = Body(...)):

    cusMgrsInst = CustomerManager.get_instance()

    customer = cusMgrsInst.get_customer(phone_number)
    

    if not customer:
        customer = Customer(name,password,phone_number,email)
        cusMgrsInst.add_customer(phone_number,customer)
        return {"userID":str(customer.customer_id),"UserCreatedAt":str(customer.creationTime)}
    else:
        raise HTTPException(status_code=409,detail="User with phone alraedy exists")


@app.post("/customer/login")
async def login(login_id: str = Body(...), password: str = Body(...)):
    
    cusMgrsInst = CustomerManager.get_instance()

    customersMap = cusMgrsInst.get_customer_map()

    if login_id not in customersMap:
        return {"error": "User not found"}

    customerObj = customersMap[login_id]

    if not customerObj.verify_password(password):
        return {"error": "Incorrect password"}

    return {"message": "Successfully logged in!","lastLoginAt":str(customerObj.loginTime)}

@app.get("/health-check")
async def health_check():

    state_healthy = True
    # ...
    if state_healthy: 
        return {"status": "no issues reported"}
    else:
        return {"status": "issues reported"}

@app.get("/")
async def root():
    return {"message": "Hello !"}
