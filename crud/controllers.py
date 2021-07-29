def doTask(first, second):
    char = kapital(first.replace(' ', ''))
    freq = [char.count(i) for i in char]
    pair = list(zip(char, freq))
    dic = {}
    
    for j,k in pair:
        if j not in dic:
            dic[j] = k

    test = set(kapital(second.replace(' ', '')))
    match = 0

    for i in dic:
        if i in test:
            match += dic[i]
    return str(round(match/len(char)*100, 2)) + '%'

def kapital(lst):
    lst = list(lst)
    for i in range(len(lst)):
        try:
            lst[i] = lst[i].upper()
        except:
            pass
    return lst

