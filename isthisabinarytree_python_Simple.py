def Maxroot(root):
    if root is None:
        return -100000
    leftmax=Maxroot(root.left)
    rightmax=Maxroot(root.right)
    return max(root.data,leftmax,rightmax)
def Minroot(root):
    if root is None:
        return 100000
    leftmin=Minroot(root.left)
    rightmin=Minroot(root.right)
    return min(root.data,leftmin,rightmin)
def check_binary_search_tree_(root):
    if root is None:
        return True
    leftMax=Maxroot(root.left)
    rightMin=Minroot(root.right)
    if root.data>=rightMin or root.data<=leftMax:
        return False
    isleft=check_binary_search_tree_(root.left)
    isright=check_binary_search_tree_(root.right)
    return isleft and isright
