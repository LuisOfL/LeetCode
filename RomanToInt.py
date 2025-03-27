def romanToInt(s):
    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    tot = 0
    for x in range(len(s)):
        if x + 1 < len(s) and dic[s[x]] < dic[s[x + 1]]:
            tot -= dic[s[x]]
        else:
            tot += dic[s[x]]
    return tot

s = input("Dame el valor del número romano: ")
res = romanToInt(s)
print(f"El valor en decimal es {res}")
