def calculate_price(weight, distance, eco_mode=False):
    base_price = 50
    price_per_km = 10
    price_per_kg = 20

    price = base_price + (price_per_km * distance) + (price_per_kg * weight)

    if eco_mode:
        price *= 0.9  # 10% discount for green delivery

    return round(price, 2)
