/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

 /*
    - use dfs to reach the deepest node
    - return the left and right nodes 
    - change the left for the right
    - change the right for the left
 */

public class Solution {
    public TreeNode InvertTree(TreeNode root) {
        return Dfs(root);
    }

    public TreeNode Dfs(TreeNode root){
        if(root == null) return null;

        var nodeLeft = Dfs(root.left);
        var nodeRight = Dfs(root.right);

        root.left = nodeRight;
        root.right = nodeLeft;

        return root;
    }
}
