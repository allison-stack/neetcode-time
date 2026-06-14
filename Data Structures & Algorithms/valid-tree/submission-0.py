class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # input: number of nodes and edges
        # output: if valid tree
        # tree: has no cycles and all nodes are connected (can be visited)
        # create adj list from edges
        # check for cycles - dfs on neighbor nodes
        adj=[[] for _ in range(n)]
        visited=set()
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor==parent:
                    continue
                if not dfs(neighbor,node):
                    return False
            return True
        return dfs(0,-1) and len(visited)==n
        