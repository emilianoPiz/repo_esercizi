a=[1,28,-4,]
def linked_list_max_min(p,_max,_min):
    _max = p.key if _max == None else max(_max,p.key)
    _min = p.key if _min == None else min(_min,p.key)

    if p.next == None:
        return _max,_min
    else:
        return linked_list_max_min(p.next,_max,_min)