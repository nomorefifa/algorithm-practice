# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        # 1. 종료 조건: 만약 현재 노드(root)가 빈자리라면 0 반환
        if not root:
            return 0
        
        # 2. 왼쪽 부하 직원에게 깊이 물어보기 (재귀 호출)
        left_depth = self.maxDepth(root.left)
        
        # 3. 오른쪽 부하 직원에게 깊이 물어보기 (재귀 호출)
        right_depth = self.maxDepth(root.right)
        
        # 4. 결론: 왼쪽과 오른쪽 중 더 큰 값에 '나 자신(1)'을 더해서 반환
        return max(left_depth, right_depth) + 1