test_dict = {"boop":4,"koop":10,"snoop":7,"kloop":1}

yo = sorted(test_dict, key=test_dict.get)

print(yo)