import employee_info

print ("Test employee info")

def test_calculate_average_salary():
     result = (50000+60000+56000+70000+65000+60000)/6
     output = employee_info.calculate_average_salary()
     assert(result==output)

def test_get_employees_by_dept():
     result_arr = [ 
          {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
          {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000},
      ]
   
     output = employee_info.get_employees_by_dept("Sales")
     assert(result_arr==output)