class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return str(self.name)

class Edge(object):
    def __init__(self, src, dest):
        self.src = src #Type Node
        self.dest = dest #Type Node
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src.getName()) + ' -> ' + str(self.dest.getName())
    
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src.getName()) + ' -> ' + str(self.dest.getName()) + " (" + self.weight + ")"


class Digraph(object):
    def __init__(self):
        self.edges = {}

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + ' -> ' + dest.getName() + '\n'
        return result[:-1]

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def _DFS(self, start, end, path, shortest):
        path = path + [start]
        if start == end:
            return path
        for node in self.childrenOf(start):
            if node not in path:
                if shortest == None or len(path) < len(shortest):
                    newPath = self._DFS(node, end, path, shortest)
                    if newPath != None:
                        shortest = newPath
                    else:
                        return
        return shortest

    def printPath(self, path):
        result = ''
        for i in range(len(path)):
            result = result + str(path[i].getName())
            if i != len(path) - 1:
                result = result + ' -> '
        return result

    def shortestPathDFS(self, start, end):
        path = self._DFS(start, end, [], None)
        if path == None:
            return
        else:
            return self.printPath(path)

    def BFS(self, start, end):
            initPath = [start]
            pathQueue = [initPath]
            while len(pathQueue) != 0:
                tmpPath = pathQueue.pop(0)
                lastNode = tmpPath[-1]
                if lastNode == end:
                    return tmpPath
                for nextNode in graph.childrenOf(lastNode):
                    if nextNode not in tmpPath:
                        newPath = tmpPath + [nextNode]
                        pathQueue.append(newPath)
            return None

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)