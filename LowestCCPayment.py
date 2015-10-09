# Problem Set 2 - 2nd Subset

# The following variables contain values as described below:

#    1.    balance - the outstanding balance on the credit card

#    2.    annualInterestRate - annual interest rate as a decimal



balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12.0
monthlyPayment = 0
updatedBalance = 5000

mthPaymentLowerBound = round(balance/12.0,2)
mthPaymentUpperBound = round((balance * ((1+monthlyInterestRate)**12)) / 12.0,2)

while True :
    updatedBalance = balance
    monthlyPayment = (mthPaymentLowerBound + mthPaymentUpperBound) / 2.0

    #print "LB : " + str(mthPaymentLowerBound)
    #print "UB : "  +str(mthPaymentUpperBound)
    #print "MP : " + str(monthlyPayment)    
            
    for month in range (1,13):
        
        monthlyUnpaidBalance = updatedBalance - monthlyPayment
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    #print "Upd Bal : " + str(updatedBalance)
    
    if ( int(updatedBalance) < 0 ):
        
        mthPaymentUpperBound = monthlyPayment
    
    elif ( int(updatedBalance) > 0 ):
        
        mthPaymentLowerBound = monthlyPayment
        
    else :
        
        print "Lowest Payment: " + str(round(monthlyPayment,2))
        break
    
