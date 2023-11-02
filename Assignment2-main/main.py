#user input variables
name = input("Enter client name: ")
address = input("Enter address of property: ")
purchase = int(input("Enter purchase price: "))

#minimum down payment variables
min_down_payment = 0
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