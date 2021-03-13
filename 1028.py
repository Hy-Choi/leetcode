# leetcode 1028. Recover a Tree From Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        nodeDict = []
        c = 0
        value = S[0]
        # dList = [idx for idx, i in enumerate(S) if i == "-"]
        # print(dList)
        
        for idx in range(1, len(S)):
            curr = S[idx]
            fast = S[idx-1]
            
            if curr == "-":
                if fast != "-":
                    nodeDict.append([value, c])
                    value = ""
                    c = 0
                c+=1
            else:
                value += curr
                
            if idx == (len(S)-1):
                nodeDict.append([value, c])
        
        if len(S) == 1:
            nodeDict.append([value, 0])
        # print(nodeDict)
        
        pending = [TreeNode(int(nodeDict[0][0]))]
        for g in nodeDict[1:]:
            depth = g[1]
            val = int(g[0])
            # print("\nddd : ", depth, val)
            if depth >= len(pending):
                # print("if", pending)
                pending[-1].left = TreeNode(val)
                pending.append(pending[-1].left)
            else:
                # print("else", pending)
                del pending[depth:]
                pending[-1].right = TreeNode(val)
                pending.append(pending[-1].right)
                # print(pending)
                
        return pending[0]

    