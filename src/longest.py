def _longest(tree):
    if tree is None:
        return 0, -1
    l1, d1 = _longest(tree.left)
    l2, d2 = _longest(tree.right)
    return max(d1 + d2 + 2, l1, l2), max(d1, d2) + 1

longest = lambda tree: _longest(tree)[0]

class Tree(object):
    __slots__ = "left", "right"
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

print longest(Tree(Tree(Tree(), Tree(Tree(), Tree())), Tree()))
