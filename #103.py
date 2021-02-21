#103. Binary Tree Zigzag Level Order Traversal
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root==None):
            return None
        if(root.left==None and root.right==None):
            return [[root.val]]
        que = []
        holder=[]
        que.append(root)
        while(len(que)!=0):
            tempholder=[]
            for i in range(len(que)):
                valh = que.pop(0)
                tempholder.append(valh.val) 
                
                if(valh.left!=None):
                    que.append(valh.left)
                if(valh.right!=None):
                    que.append(valh.right)
            if(len(holder)%2!=0):
                holder.append(reversed(tempholder))
            else:
                holder.append(tempholder)
        return holder
                
