def even_odd():
    a = [1, 2, 2, 1]
    a1 = [1, 3, 2]

    for i in range(1,len(a)):

        if (i) % 2 == 0:  #even should be greater
            if a[i] > a[i-1]:
                a[i],a[i-1] = a[i-1],a[i]
                print("even",i,i-1)
        else:
            if a[i] < a[i-1]:
                a[i],a[i-1] = a[i-1] ,a[i]
                print("odd",i,i-1)

    return a

b = even_odd()
print(b)