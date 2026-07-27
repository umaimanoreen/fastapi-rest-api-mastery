from fastapi import FastAPI
from fastapi import status
from app.models import Employee
app=FastAPI()
employee_list = []


@app.post("/employee", status_code=status.HTTP_201_CREATED)
def create_employee(employee: Employee):
   
    employee_list.append(employee)
    return {"message": "Employee created successfully", "employee": employee}

@app.get("/employees")
def get_employees():
    return {"employees": employee_list}


@app.put("/employee/{employee_id}")
def update_employee(employee_id:int, updated_employee : Employee):
    for index , employee in enumerate(employee_list):
        if employee.id == employee_id:
            employee_list[index] = updated_employee
            return {
                "message" :"Employee updated",
                "employee" : updated_employee
                   }

    
@app.delete("/employee/{employee_id}")
def delete_employee(employee_id:int ):   
    for index, employee in enumerate(employee_list):
        if employee.employee_id == employee_id:
            del employee_list[index]
            return {"message": "Employee deleted successfully"}
    return {"message": "Employee not found"
            }
    return Response(status_code=status.HTTP_204_NO_CONTENT)
        
@app.get ("/")
def home():
    return {"message":"welcome to the employee API"}

@app.get("/employee/{employee_id}")
def get_emplyee(employee_id:int):
    return{
        "employee_id":employee_id,
       
    }

@app.get("/employees")
def get_employees(
    department: str,
    city: str
):
    return {
        "department": department,
        "city": city
    }
@app.get("/books")
def search_books(title: str):
    return {
        "title": title
    }
@app.get("/products")
def search_products(
    brand: str,
    price: int
):
    return {
        "brand": brand,
        "price": price
    }
@app.get("/employees")
def get_employees(department: str = "All"):
    return {
        "department": department
    }
@app.get("/employees/{employee_id}")
def get_employee(
    employee_id: int,
    department: str = "All",
    city: str = "Islamabad"
):
    return {
        "employee_id": employee_id,
        "department": department,
        "city": city
    }