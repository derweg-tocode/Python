fname = input("Enter file: ")

if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        di[w] = di.get(w, 0) + 1


largest = -1
thewords = None
for k,v in di.items():
    if v > largest:
        largest = v
        theword = k
    print(theword, largest)

