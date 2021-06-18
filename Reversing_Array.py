import math


def reverseArray(a):
    # Declaring the new array

    newarr = []

    # Defining the array size and size constraint

    n = len(a)
    x = pow(10,3)

    # Conditioning the array size

    if n<1:
        return False

    elif n > x:
        return False

    else:

        # Defining the array element size constraint

        y = pow(10, 4)

        for i in range(n-1, -1, -1):
            if a[i] < 1:
                return False

            elif a[i] > y:
                return False

            else:
                newarr.append(a[i])

        return newarr


exarray = [4,10001,3,5,6,54]
print(reverseArray(exarray))


