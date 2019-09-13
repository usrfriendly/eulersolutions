Euler=600851475143

print(Euler)

import sys

for i in range(2,600851475143,1):
    if Euler % i == 0:
        for n in range (1,i):
            if i % n != 0:
                print(i)
