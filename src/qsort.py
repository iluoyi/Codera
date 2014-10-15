def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left  = [x for x in a if x < pivot ]
        right = [x for x in a[1:] if x >= pivot]
        return  sort(left)  + [pivot] +  sort(right)

def sort2(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left  = [x for x in a if x < pivot ]
        right = [x for x in a[1:] if x >= pivot]
        return  [sort2(left)]  + [pivot] +  [sort2(right)]

def inorder(t):
    if t == []:
        return []
    left, node, right = t
    return inorder(left) + [node] + inorder(right)

def pp((left, node, right), lev=0):
    if right != []:
        pp(right, lev+1)
    print "\t" * lev, node
    if left != []:
        pp(left, lev+1)

if __name__ == "__main__":
    a = [4, 2, 5, 1, 6, 8, 0, 7, 3]
    t = sort2(a)
    print t
    print inorder(t)
    pp(t)
