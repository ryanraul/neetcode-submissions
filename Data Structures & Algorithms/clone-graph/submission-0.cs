/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}


// DFS 
    - stop criterea -> node == null

    cloneNode = new Node(node.val);
    foreach(neighbor in node.neighbors)
        cloneNeighbour = dfs(neighbor)
        cloneNode.neighbors.Add(cloneNeighbour)
    
    return cloneNode;

    [1][2]
    [2][1,3]
    [1] => retorna o obj do hash
    [3][2]
    [2] => retorn o obj do hash
    [2][1,3]
    [1][2]



*/



public class Solution {
    private Dictionary<Node, Node> cloneReferences = new Dictionary<Node, Node>();

    public Node CloneGraph(Node node) {
        return dfs(node);
    }

    public Node dfs(Node node){
        if(node == null) return null;

        if(cloneReferences.ContainsKey(node)) return cloneReferences[node];
        
        var cloneNode = new Node(node.val);
        cloneReferences[node] = cloneNode;

        foreach(var neighbor in node.neighbors){
            var cloneNeighbor = dfs(neighbor);
            cloneNode.neighbors.Add(cloneNeighbor);
        }

        return cloneNode;
    }
}
