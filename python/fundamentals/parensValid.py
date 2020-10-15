def parensValid(parentStr):
    while len(parentStr) > 0:
        if len(parentStr) <= 1:
            return False
        # print(parentStr, "WHYYYY")
        if parentStr[0] == "(":
            parentStr.pop(0)
        else:
            return False
        for i in range(len(parentStr)):
            if parentStr[i] == ")":
                # print(parentStr)
                parentStr.pop(i)
                # print(i)
                break
            if i == len(parentStr)-1:
                return False
    return True

print(parensValid(list(")()()()")))