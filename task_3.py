def process_prices(discount_percent,*prices):
    discount_percent=discount_percent/100+1
    new_prs=[]
    for i in prices[0]:
        if i>0:
            new_prs.append(round(i*discount_percent))
    return new_prs
old_prices=[1000, -50,300, 0, 500]
print(f"{process_prices(20,old_prices)}")