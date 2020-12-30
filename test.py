stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def slice_wrap(mylist, start, end):
    start %= len(mylist)
    end %= len(mylist)
    if end > start: return mylist[start: end]
    else: return mylist[start:] + mylist[:end]

def del_wrap(mylist, start, end):
    start %= len(mylist)
    end %= len(mylist)
    if end > start: del mylist[start: end]
    else: 
        del mylist[start:] 
        del mylist[:end]

print(slice_wrap(stuff, 1, 4))
del_wrap(stuff, 1, 4)
print(stuff)