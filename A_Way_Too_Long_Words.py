for i in range(int(input())):
    s = input()
    n = len(s)
    if n > 10:
        print (s[0] + str(n-2) + s[-1])
    else :
        print (s)