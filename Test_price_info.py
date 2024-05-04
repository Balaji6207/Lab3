import price_info

print ("Test price info")


def test_total_cost_shopping():
     result = 46.75
     output = price_info.total_cost_shopping()
     assert(result==output)

def test_cost_of_fruits():
     result = 12.0
     output = price_info.cost_of_fruits('apple', 10)
     assert(result==output)
