def numToBinary(number, bit):
    strNum = ""
    for i in range(bit):
        if number % 2 == 0:
            strNum = "0" + strNum
        else:
            strNum = "1" + strNum
        number //= 2

    return strNum

def negativeToBinary(number, bits):
    number = abs(number)

    binary = ""
    for i in range(bits):
        binary = ("1" if number % 2 else "0") + binary
        number //= 2

    flipped = ""
    for bit in binary:
        flipped += "0" if bit == "1" else "1"

    result = ""
    carry = 1
    for i in range(bits - 1, -1, -1):
        if flipped[i] == "1" and carry == 1:
            result = "0" + result
            carry = 1
        elif flipped[i] == "0" and carry == 1:
            result = "1" + result
            carry = 0
        else:
            result = flipped[i] + result

    return result

def main():
    bit = 8
    number = -5

    numInBinerry = "00000000"

    if (number == 0):
        print(numInBinerry)
    elif (number > 0):
        numInBinerry = numToBinary(number, bit)
        print("המספר בבינארי: ", numInBinerry)
    else:
        numInBinerry = negativeToBinary(number, bit)
        print("המספר בבינארי לפני משלים ל2: ", numInBinerry)


if __name__ == "__main__":
    main()