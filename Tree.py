class Tree:
  def __init__(self, val_ = None, left_ = None, right_ = None):
    self.val = val_
    self.left = left_
    self.right = right_

  def insert(self, val):
    # make it a binary serach tree
    if self.val:
        if val < self.val:
            if self.left is None:
            	self.left = Tree(val)
            else:
            	self.left.insert(val)
        elif val > self.val:
            if self.right is None:
              self.right = Tree(val)
            else:
              self.right.insert(val)
    else:
        self.val = val

  def inorder(self):
    # Note: inorder visit a BST results in an ascending array
    if self.left:
        self.left.inorder()
    print(self.val)
    if self.right:
        self.right.inorder()

class Solution:
    def MinimumDepth(self,root:[Tree]):
        
        def findDepth(node, level):
            if not node:
                return level
            
            left = findDepth(node.left, level+1)

            right = findDepth(node.right, level+1)

            return min(left, right)
        
        return findDepth(root, 0)
        
    def BiuldTreeFromPreAndIn(self, preorder, inorder):
        # preorder: List[int], inorder: List[int] -> Optional[TreeNode]
        if preorder == None:
            return
        if len(preorder) == 1:
            return Tree(preorder[0])
        
        root = Tree(preorder[0])
        rootindex = inorder.index(preorder[0])
        
        root.left = self.BiuldTreeFromPreAndIn(preorder[1: 1+rootindex], inorder[: rootindex]) 
        root.right = self.BiuldTreeFromPreAndIn(preorder[1+rootindex: ], inorder[1+rootindex: ])
        
        return root
BST = Tree(20)
BST.left = Tree(18)
BST.right = Tree(22)
BST.insert(19)
BST.insert(23)
BST.insert(5)
BST.insert(21)

#BST.inorder()


s = Solution()
print(s.MinimumDepth(BST))

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = s.BiuldTreeFromPreAndIn(preorder, inorder)
root.inorder()