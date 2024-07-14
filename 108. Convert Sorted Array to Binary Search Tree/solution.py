# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        ##base case once nums is empty
        if not nums:
            return None

        #find middle
        midpoint = len(nums) // 2
        
        #creates tree!
        root = TreeNode(nums[midpoint])

        #divide and conquer/recursion
        root.left = self.sortedArrayToBST(nums[:midpoint])
        root.right = self.sortedArrayToBST(nums[midpoint+1:])

        return root
        