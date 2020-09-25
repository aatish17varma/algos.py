class Solution:
    def __init__(self):
        self.traversedNodes = set()

    def findCycles(self, graph):
        for node in graph:
            answer = self.helper(graph, node, None)
            if answer:
                return True
        return False

    def helper(self, graph, node, parent):
        if node in self.traversedNodes:
            return False 
        self.traversedNodes.add(node)
        for neighbor in graph[node]:
            if (neighbor in self.traversedNodes and neighbor != parent) or self.helper(graph,neighbor,node):
                return True

        return False

graph = {
        '1' : ['0','2'],
        '0' : ['1','2', '3'],
        '2' : ['0','1'],
        '3' : ['0',],
}

print(Solution().findCycles(graph))
