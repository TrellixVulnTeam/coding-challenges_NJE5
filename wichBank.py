banks=[1,2,3,4,5,6,7,8,9,10]
cost=15


def wichBankToBreak(banks, cost):
    biggest=max(banks)
    seen=[False for i in range(0,biggest+1)]
    for bank1 in banks:
        bank2 = cost - bank1
        if bank2 in seen:
            print("Bank1: {} | Bank2: {}".format(str(bank1), str(bank2)))
        seen.append(bank1)

wichBankToBreak(banks,cost)