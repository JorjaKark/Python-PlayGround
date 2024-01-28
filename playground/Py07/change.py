def change(money):
    new_value = 0
    result_dict = {2.0: 0, 1.0: 0, 0.5:0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    for key, value in result_dict.items():
        new_value = money//key
        money = money - (new_value*key)
        money = round(money,2)
        result_dict[key] = new_value
    return result_dict

