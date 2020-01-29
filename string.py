def untilq():
    a=input("ENTER STRING")
    while(a.lower()!='q'):
        print(a)
        untilq()
        break
    untilq()
