i = 0
a = 0
b = 1
c=0
d=0
fib=list()
while c < 4000000:
    if i <= 1:
        c = i
    else:
        c = a + b
        a = b
        b = c
    i = i+1
    if c % 2 == 0:
        d += c
    if c < 4000000:
        print(c)

print("Sum of evens is:",d)
