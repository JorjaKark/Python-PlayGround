def preorder(tree):
    if tree is None:
        return []
    else:
        value, left, right = tree
        return [value] + preorder(left) + preorder(right)
