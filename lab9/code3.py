def calculate_shipping(country, weight):
    if country == "USA":
        if weight < 5:
            return 10
        else:
            return 20
    elif country == "Canada":
        if weight < 5:
            return 15
        else:
            return 25
    else:
        if weight < 5:
            return 30
        else:
            return 50




shipping_prices = {
    "USA": (10, 20),
    "Canada": (15, 25),
    "Other": (30, 50)
}


def calculate_shipping(country, weight):
    prices = shipping_prices.get(country, shipping_prices["Other"])
    if weight < 5:
        return prices[0]
    return prices[1]
