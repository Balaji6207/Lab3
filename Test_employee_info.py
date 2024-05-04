import employee_info

print ("Test employee info")

def test_calculate_average_salary():
     result = (50000+60000+56000+70000+65000+60000)/6
     output = employee_info.calculate_average_salary()
     assert(result==output)