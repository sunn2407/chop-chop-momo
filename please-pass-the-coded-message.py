arry = []
total = 0
result = []


def recursiveCombinations(arry, temp, start, end, index, r):
    global result
    global total
    if(index == r):
        if(sum(arry)-sum(temp)) % 3 == 0:
            if(sum(temp) < total):
                total = sum(temp)
                return temp
        else:
            return []

    for i in range(start, end+2):
        if(end-i+1 >= r-index):
            temp[index] = arry[i]
            result = recursiveCombinations(arry, temp, i+1, end, index+1, r)
            if(result != None and len(result) > 0):
                return result


def getCombinations(r):
    global total
    total = 9*len(arry)
    return (recursiveCombinations(arry, [None for i in range(r)], 0, len(arry)-1, 0, r))


def getLargestNumb(temp, pickOut, original):
    if(pickOut == len(arry)):
        return 0
    if(pickOut > 0 and pickOut <= (len(arry)-1)):
        if(getCombinations(pickOut) != None):
            remove = getCombinations(pickOut)
            for i in remove:
                original.remove(i)
            original.reverse()
            return joinList(original)
    if(sum(temp) % 3 == 0):
        temp.reverse()
        return joinList(temp)
    finalRes = getLargestNumb(temp, pickOut+1, original)
    if(finalRes != None):
        return finalRes


def joinList(l):
    s = [str(i) for i in l]
    return int("".join(s))


def solution(l):
    global arry
    l.sort()
    arry = l
    if(len(l) > 0):
        if(len(l) == 1 and l[0] % 3 != 0):
            return 0
        return (getLargestNumb(l, 0, l))
    return 0


solution([1, 4])
