import Lab2.bmi as bmi
print("Test_Lab2 bmi")

def test_bmi_normal_weight():
    input_height = 1.73
    input_weight = 57
    test_bmi_range = 0
    result = bmi.calculate_bmi(input_height, input_weight)  # Call calculate_bmi from Lab2 module
    assert (result == test_bmi_range)
    print("0")
def test_bmi_over_weight():
    input_height = 1.73
    input_weight = 80
    test_bmi_range = 1
    result = bmi.calculate_bmi(input_height, input_weight)  # Call calculate_bmi from Lab2 module
    assert (result == test_bmi_range)
    print("1")
def test_bmi_under_weight():
    input_height = 1.73
    input_weight = 50
    test_bmi_range = -1
    result = bmi.calculate_bmi(input_height, input_weight)  # Call calculate_bmi from Lab2 module
    assert (result == test_bmi_range)
    print("-1")
