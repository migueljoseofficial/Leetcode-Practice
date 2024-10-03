from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True
        
        graph = defaultdict(list)


        #sucessfully created the graph!
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # lets try a dfs iterative approach

        seen = set()
        seen.add(source)

        frontier = []
        frontier.append(source)

        while frontier:
            node = frontier.pop()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    frontier.append(neighbor)
                if neighbor == destination:
                    return True

        return False
            

        



        



        