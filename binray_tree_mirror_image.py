'''
Mirror(Tree)

(1)  Call Mirror for left-subtree    i.e., Mirror(left-subtree)
(2)  Call Mirror for right-subtree  i.e., Mirror(right-subtree)
(3)  Swap left and right subtrees.
          temp = left-subtree
          left-subtree = right-subtree
          right-subtree = temp
'''


def mirror_Tree(self,root):
    if root.left:
        self.mirror_Tree(root.left)
    if root.right:
        self.mirror_Tree(root.right)
    if root.left or root.right:
        temp=root.left
        root.left=root.right
        root.right=temp
    return root
