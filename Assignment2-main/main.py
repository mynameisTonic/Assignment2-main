#user input variables
name = input("Enter client name: ")
address = input("Enter address of property: ")
purchase = int(input("Enter purchase price: "))

#minimum down payment amount
min_down_payment = 0
#minimum down payment percentage
min_total = 0
#mortgage if/else statement
if purchase <= 500000:
    #minimum calculations
    min_down_payment = purchase * 0.05
    min_total = (min_down_payment/purchase) * 100
elif purchase > 500000 or purchase <= 1000000:
    #minimum calculations
    remainder = purchase - 500000
    min_down_payment = (500000 * 0.05) + (remainder * 0.10)
    min_total = (min_down_payment/purchase) * 100
elif purchase > 1000000:
    #minimum calculations
    min_down_payment = purchase * 0.20
    min_total = (min_down_payment/purchase) * 100
else:
    print("Please enter a valid purchase amount.")

down_payment_input = float(input(f"Enter down payment percentage (minimum {min_total}): "))

down_payment_percent = down_payment_input/100
down_payment_total = down_payment_percent * purchase
print(down_payment_total)

#insurance calculation
#premium insurance rates
insurance_rate1 = 0.04
insurance_rate2 = 0.031
insurance_rate3 = 0.028
insurance_rate4 = 0

if down_payment_input >= 5  and down_payment_percent < 10:
    insurance_cost = (purchase - down_payment_total) * insurance_rate1 / 100
    principal_amount = purchase - down_payment_total + insurance_cost
    print(f"Mortgage insurance price is {insurance_cost}")
    print(f"The principal amount is {principal_amount}")
elif down_payment_input >= 10 and down_payment_percent < 15:
    insurance_cost = (purchase - down_payment_total) * insurance_rate2 / 100
    principal_amount = purchase - down_payment_total + insurance_cost
    print(f"Mortgage insurance price is {insurance_cost}")
    print(f"The principal amount is {principal_amount}")    
elif down_payment_input >= 15 and down_payment_percent < 20:
    insurance_cost = (purchase - down_payment_total) * insurance_rate3 / 100
    principal_amount = purchase - down_payment_total + insurance_cost
    print(f"Mortagage insurance price {insurance_cost}")
    print(f"The principal amount is {principal_amount}")
else:
    insurance_cost = (purchase - down_payment_total) * insurance_rate4 / 100
    principal_amount = purchase - down_payment_total + insurance_cost
    print(f"Mortgage Insurance price is {insurance_cost}")
    print(f"The principal amount is {principal_amount}")

intrest = 0

#mortgage term calculations
while True:
    mortgage_term = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))

    if mortgage_term == 1:
        intrest_rate = (intrest + 0.0595)

        break
    elif mortgage_term == 2:
        intrest_rate = (intrest + 0.059)

        break
    elif mortgage_term == 3:
        intrest_rate = (intrest + 0.056)

        break
    elif mortgage_term == 5:
        intrest_rate = (intrest + 0.0529)

        break
    elif mortgage_term == 10:
        intrest_rate = (intrest + 0.06)

        break
    else:
        print("Please enter a valid choice")

annual_intrest_rate = (intrest_rate * 100)

    #while intrest_rate == 0:
        #print("Please enter a valid choice")
        #if intrest_rate < 1:
            #break
# LINES above failed attempt at making loop

effective_monthly_rate = (((1+(annual_intrest_rate)/2)**2)**(1/12) - 1)

effective_monthly_rate = int()

#num_payments = number of payments
num_payments = mortgage_term*12

principal_amount = purchase - down_payment_total

monthly_payment = principal_amount * (effective_monthly_rate * (1 + effective_monthly_rate)**num_payments) / ((1 + effective_monthly_rate)**num_payments - 1)

mortgage_amortization = input("Enter mortgage amortization period (5, 10, 15, 20, 25): ")