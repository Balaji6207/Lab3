import employee_info

print ("Test employee info")

def test_get_employees_by_age_range():
     result_arr = [
          {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
          {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
          {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
      ]
     output = employee_info.get_employees_by_age_range(26,36)
     assert(result_arr==output)


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