def is_fraudulenttransaction():
    txn_amnt=100
    tresh_hold=50
    if txn_amnt >tresh_hold:
        print ('fraud')
    else: 
        print('no')

is_fraudulenttransaction()


