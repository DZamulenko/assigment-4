def convert_to_uah(amount, rate=41.5):
    amount/=rate
    return abs(round(amount,2))
print(f"{convert_to_uah(-200,40)}")