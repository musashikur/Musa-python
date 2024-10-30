def calculate_morgage (principal,rate,term):
    MonthlyRate=rate/12
    Month=term*12
    Monthly_payment=principal*(MonthlyRate*(MonthlyRate+1)**Month)/((1+MonthlyRate)**Month-1)
    return Monthly_payment
payment=calculate_morgage(1000000,0.12,25)
print(payment)



def is_fraudulent)transaction(txn_amnt,tresh_hold):
    txn_amnt=input("enter txn amnt")
    tresh_hold=input("enter txn amnt")
    IF txn_amnt>tresh_hold
    print ('fraud')
    else print('no')



