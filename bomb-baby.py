def getBigger(m, n):
    if(m > n):
        return m
    return n


def getSmaller(m, n):
    if(m > n):
        return n
    return m


def solution(m, f):
    return (getParent(int(m), int(f)))


quoSum = 0


def getParent(x, y):
    global generation
    global quoSum
    # print(generation)
    print(x, y, 'X AND Y')

    if(x <= 0 or y <= 0):
        quoSum = 'impossible'
        # print('Impossible')
        return (quoSum)

    big = getBigger(x, y)
    small = getSmaller(x, y)
    diff = big-small

    # print(big, small, diff)

    quo = big/small
    rem = big % small
    # print('importantt')
    quoSum = quoSum+int(quo)

    if(x == 1 or y == 1):
        # print(f'{x}M {y}F')
        # generation=generation+1
        # print(generation, 'terminating condition')
        quoSum = quoSum-1

        return str(quoSum)

    if(x == getBigger(x, y)):
        x_ = rem
        y_ = small
    if(y == getBigger(x, y)):
        y_ = rem
        x_ = small
    # print(f'{x_},{y_} X_ Y_')
    getParent(x_, y_)
    # print(generation)
    # getParent(smallX,thenY)
    return str(quoSum)


print(solution('9999999999999999999990', '6667646'))
