# 10진수 2진화
def DtoB(dec):
    if dec == 0: return "0"
    bin = ''
    while dec:
        bin = bin + str(dec%2)
        dec = dec // 2
    return bin[::-1]

# 2진수 10진화
# 입력 예 : (2진수) 1010 >> (10진수) 10
def BtoD(bin):
    dec = 0
    key = 1
    for i in range(len(bin)-1, -1, -1):
        dec = dec + int(bin[i]) * key
        key = key * 2
    return dec