quoSum = 0

def solution(m, f):
    return (getParent(int(m), int(f)))

def getParent(x, y):
    global quoSum
    if(x <= 0 or y <= 0):
        quoSum = 'impossible'
        return (quoSum)

    if(x == 1 or y == 1):
        quoSum = quoSum+(x*y)-1
        return str(quoSum)
        
    if(x > y):
        x_ = x % y
        y_ = y
        quoSum = quoSum+int(x/y)

    if(y > x):
        y_ = y % x
        x_ = x
        quoSum = quoSum+int(y/x)

    getParent(x_, y_)
    return str(quoSum)
