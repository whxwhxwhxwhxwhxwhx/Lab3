import price_info

print("Test_price_info")
input_price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }
input_quantity_list={'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}

def test_total_cost_shopping():
    
        test_total_cost=46.75

        result=price_info.total_cost_shopping(input_price_list, input_quantity_list)

        assert(result==test_total_cost)

def test_cost_of_fruit():
    
    test_fruit='apple'
    test_quantity_list=10
    test_cost=12

    result = price_info.cost_of_fruits(test_fruit, test_quantity_list, input_price_list)

    assert (result == test_cost)