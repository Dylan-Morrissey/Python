num = 23456789
num = str(num)

n = 4
start_pos = 0


def nvalues(num, n):
    if n == 0:
        return 1
    else:
        return int(num[i]) * nvalues(num[1:], n-1)



for i in range(start_pos,len(num)):
    try:
        val = nvalues(num, n)
        print val

    except IndexError:
        break