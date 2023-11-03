#user input variables
name = input("Enter client name: ")
address = input("Enter address of property: ")
purchase = int(input("Enter purchase price: "))

#minimum down payment amount
#minimum down payment percentage
#mortgage if/else statement
if purchase <= 500000:
    #minimum calculations
    min_down_payment = purchase * 0.05
    min_total = (min_down_payment/purchase) * 100
elif purchase > 500000 and purchase <= 1000000:
    #minimum calculations
    remainder = purchase - 500000
    min_down_payment = (500000 * 0.05) + (remainder * 0.10)
    min_total = (min_down_payment/purchase) * 100
elif purchase > 1000000:
    #minimum calculations
    min_down_payment = purchase * 0.2
    min_total = (min_down_payment/purchase) * 100
else:
    print("Please enter a valid purchase amount.")

down_payment_input = float(input(f"Enter down payment percentage (minimum {round(min_total, 3)}): "))

down_payment_percent = down_payment_input/100
down_payment_total = down_payment_percent * purchase
print(f"Down payment total: {round(down_payment_total, 1)}")

#insurance calculation
#premium insurance rates
insurance_rate1 = 0.04
insurance_rate2 = 0.031
insurance_rate3 = 0.028


if down_payment_input >= 5  and down_payment_input < 10:
    insurance_cost = (purchase - down_payment_total) * insurance_rate1 / 100
    principal_amount = purchase - down_payment_total + insurance_cost
   
    print(f"Mortgage insurance price is {insurance_cost}")
    print(f"Total mortgage amount is ${round(principal_amount, 1)}")

elif down_payment_input >= 10 and down_payment_input < 15:
    insurance_cost = (purchase - down_payment_total) * insurance_rate2 / 100
    principal_amount = purchase - down_payment_total + insurance_cost
    
    print(f"Mortgage insurance price is {insurance_cost}")
    print(f"Total mortgage amount is ${round(principal_amount, 1)}") 

elif down_payment_input >= 15 and down_payment_input < 20:
    insurance_cost = (purchase - down_payment_total) * insurance_rate3 / 100
    principal_amount = purchase - down_payment_total + insurance_cost
    
    print(f"Mortagage insurance price {insurance_cost}")
    print(f"Total mortgage amount is ${round(principal_amount, 1)}")

else:
    insurance_cost = 0
    principal_amount = purchase - down_payment_total + insurance_cost
    
    print(f"Mortgage Insurance price is {insurance_cost}")
    print(f"Total mortgage amount is ${round(principal_amount, 1)}")

#mortgage term calculations
while True:
    mortgage_term = input("Enter mortgage term (1, 2, 3, 5, or 10): ")
    if mortgage_term == "1":
        intrest_rate = 0.0595
        break
    elif mortgage_term == "2":
        intrest_rate = 0.059
        break
    elif mortgage_term == "3":
        intrest_rate = 0.056
        break
    elif mortgage_term == "5":
        intrest_rate = 0.0529
        break
    elif mortgage_term == "10":
        intrest_rate = 0.06
        break
    else:
        print("Please enter a valid choice")

def calc_monthly_rate(interest_rate):
    calc1 = (1 + interest_rate) /2
    calc2 = calc1**2
    calc3 = calc2**(1/12) - 1
    return calc3

effective_monthly_rate = calc_monthly_rate(intrest_rate)

# def effective_monthly_rate(interest_rate):
#     one_plus_a = 1 + interest_rate
#     power_of_two = one_plus_a ** 2
#     power_of_twelve = power_of_two ** 1/12
#     annual_mortgage_interest_rate = power_of_twelve - 1
#     return annual_mortgage_interest_rate
# emr = int(effective_monthly_rate(intrest_rate))


while True:
    mortgage_amortization = input("Enter mortgage amortization period (5, 10, 15, 20, 25): ")
    if mortgage_amortization == "5":
        mortgage_amortization_term = 5
        break
    elif mortgage_amortization == "10":
        mortgage_amortization_term = 10
        break
    elif mortgage_amortization == "15":
        mortgage_amortization_term = 15

        break
    elif mortgage_amortization == "20":
        mortgage_amortization_term = 20

        break
    elif mortgage_amortization == "25":
        mortgage_amortization_term = 25

        break
    else:
        print("Please enter a valid choice")
annual_intrest_rate = intrest_rate * 100
print(f"Intrest rate for the term will be {round(annual_intrest_rate, 3)}%") 

#num_payments = number of payments
num_payments = int(mortgage_term) * 12

def calculate_monthly_payment(num_payments, principal_amount, effective_monthly_rate):

    calc1 = effective_monthly_rate**num_payments
    calc2 = effective_monthly_rate * (1 + calc1)

    calc3 = (1 + effective_monthly_rate)**num_payments
    calc4 = calc3 - 1

    full_calc = principal_amount * (calc2 / calc4)
    return full_calc

monthly_payment = calculate_monthly_payment(num_payments, principal_amount, effective_monthly_rate)

print(f"Your monthly payments will be {round(monthly_payment, 2)} per month")

schedule = input("Would you like to see the amortization schedule? (Y/N): ").lower()

if schedule == "y":
    print(f"Month\t\tOpening Bal\t\tPayment\t\t\tPrincipal\tInterest\t\tClosing Bal")
    months = 0
    total_interest = 0
    total_principal = 0
    while months < num_payments:
        monthly_interest = principal_amount * effective_monthly_rate
        monthly_principal = monthly_payment - monthly_interest
        closing_balance = principal_amount - monthly_principal + monthly_interest
        total_principal += monthly_principal
        total_interest += monthly_interest
        principal_amount -= monthly_principal
        months += 1
        print(f"{months:.2f}\t\t{principal_amount:.2f}\t\t{monthly_payment:.2f}\t\t{total_principal:.2f}\t\t{total_interest:.2f}\t\t{closing_balance:.2f}")
        
elif schedule == "n":
    print()