while True:
    n = input("\nРешето Эратосфена\nEnter \'exit\' or num: ")
    if n != "exit":
        n = int(n)
        a = []
        for i in range(n + 1):
            a.append(i)
        a[1] = 0
        i = 2
        while i**2 <= n:
            if a[i] != 0:
                j = i**2
                while j <= n:
                    a[j] = 0
                    j += i
            i += 1
        a = set(a)
        a.remove(0)
        a = list(a)
        a.sort()
        print(a)
    else:
        break