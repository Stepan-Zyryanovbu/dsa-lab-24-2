def calculate_tax(income):
    if income <= 10000:
        return income * 0.1
    elif income <= 20000:
        return income * 0.15
    else:
        return income * 0.2



LOW_LIMIT = 10000
MID_LIMIT = 20000

LOW_RATE = 0.1
MID_RATE = 0.15
HIGH_RATE = 0.2


def calculate_tax(income):
    # налог для низкого дохода
    if income <= LOW_LIMIT:
        return income * LOW_RATE
    # налог для среднего дохода
    elif income <= MID_LIMIT:
        return income * MID_RATE
    # налог для высокого дохода
    else:
        return income * HIGH_RATE
