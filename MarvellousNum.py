def CheckPrime(no):
    if no>1:
        for i in range(2,no):
            if (no %i)==0:
                return False
        else:
            return True
               
