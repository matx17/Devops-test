PriceLists_Operators = {
    'A': {
        '1': 0.9,
        '268': 5.1,
        '46': 0.17,
        '4620': 0.0,
        '468': 0.15,
        '4631': 0.15,
        '4673': 0.9,
        '46732': 1.1
    },
    'B': {
        '1': 0.92,

        '44': 0.5,
        '46': 0.2,
        '467': 1.0,
        '48': 1.2,



    }
}

def getPrefixPriceRate(Prefix, OperatorPriceList):
    PrefixLength = len(Prefix)
    if(PrefixLength == 0):
        return None
    PrefixRate = OperatorPriceList.get(Prefix)
    ##print(Prefix, PrefixRate)
    if PrefixRate != None:
        return PrefixRate
    return getPrefixPriceRate(Prefix[0:PrefixLength - 1], OperatorPriceList)
    
def getCheapestOperator(telNo):
    CheapestRate = 0
    CheapestRateOperator = None
    firstOperator = True
    
    for operator, pricelist in PriceLists_Operators.items():
        Rate = getPrefixPriceRate(telNo, pricelist)
        if (Rate < CheapestRate or firstOperator == True):
            CheapestRate = Rate
            CheapestRateOperator = operator
            firstOperator = False
            
    return CheapestRateOperator


print(getCheapestOperator('4612345678'))
