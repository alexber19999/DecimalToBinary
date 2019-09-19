def decToBin(num):
    binNumRaw = ""
    while(num > 0):
        binNumRaw += str(num % 2)
        num = num // 2
    binNum = ''.join(reversed(binNumRaw))
    print(binNum)

decToBin(12)


def binToDec(num):
    decNum = 0
    power = 0
    while(num != 0):
        binDigit = num % 10
        decNum += binDigit * pow(2, power)
        num = num // 10
        power += 1
    print(decNum)


binToDec(10101)










