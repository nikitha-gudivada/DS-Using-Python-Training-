annual_income=int(input("Annual Income"))
hra=int(input("HRA"))
deductions=int(input("Deductions"))
tax=annual_income-(12*hra)-deductions-300000
if(300000<tax<600000):
    tax_amount=0.1*tax
    print(tax_amount)
elif(600000<tax<1000000):
    tax_amount=0.15*tax
    print(tax_amount)
elif(tax>1000000):
    tax_amount=0.2*tax
    print(tax_amount)
else:
    print("No tax")
