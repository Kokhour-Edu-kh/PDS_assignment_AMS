
#Electricity Bill with Progressive Tiers



def findmoney(kwh):
    if kwh < 0:
        print("Invalid consumption!")
    else:
        if kwh <= 50:
            elec_cost = kwh * 480

        elif kwh <= 200:
            elec_cost = 50 * 480 + (kwh - 50) * 610

        else:
            elec_cost = ( 50 * 480 + 150 * 610 + (kwh - 200) * 730)

        service_fee =2000
        subtotal =elec_cost + service_fee
        vat =subtotal * 0.10
        total_real =subtotal + vat
        total_dollar =total_real /4100
    return int(total_real), total_dollar

ele_month =[0, 35, 50, 120, 200, 350]

for kwh in ele_month:
    kh,dollar =findmoney(kwh)

    print(f"\t{kwh} Kwh ->  {kh} Real  (=  {dollar:2f} USD)")

