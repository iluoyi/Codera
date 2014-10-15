def _shortest(tree, x, y):
    ''' return (lca_node,) if both are found, or x if only x is found, or y if only y is found,
    or None if neither is found in the current subtree'''
    if tree is None:
        return None
    left = _shortest(tree.left, x, y)
    if type(left) is tuple:
        return left
    right = _shortest(tree.right, x, y)
    if type(right) is tuple:
        return right
    found_x = (tree is x) or (left is x) or (right is x)
    found_y = (tree is y) or (left is y) or (right is y)
    return (tree,) if found_x and found_y else x if found_x else y if found_y else None

shortest = lambda tree, x, y: _shortest(tree, x, y)[0]

class Tree(object):
    __slots__ = "left", "right"
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

t = Tree(Tree(), Tree(Tree(None, Tree()), Tree()))
print shortest(t, t.right.left.right, t.left) is t
print shortest(t, t.right.left.right, t.right.right) is t.right
print shortest(t, t.right.left.right, t.right) is t.right # lca == y
print shortest(t, t.right.left, t.right.left) is t.right.left # x == y
