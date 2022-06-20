import collections
import heapq

class Graph:
    '''
    self.graph_list:[[node1,node2,weight],[node1,node3,weight]...]
    self.graph_dict: {'node1': [(node2,weight), (node3,weight) ...],
                     'node2': [(node3,weight), (node4,weight),...],
                     ...}
    '''
    def __init__(self, _graph_list):
        if _graph_list == None:
            _graph_list = []
        self.graph_list = _graph_list
        self.graph_dict = collections.defaultdict(list)
        self.vertex = set()
        
        if self.graph_list:
            for (u,v,w) in self.graph_list:
                self.graph_dict[u].append((v, w))
                self.vertex.add(u)
                self.vertex.add(v)
                 
    def add_edge(self, node1, node2, weight=float('inf')):
        self.graph_list.append([node1,node2,weight])
        self.graph_dict[node1].append((node2, weight))
        self.vertex.add(u)
        self.vertex.add(v)
    
    def create_matrix(self):
        n = len(self.vertex)
        matrix = [[0]*n for i in range(n)]
        for (u,v,w) in self.graph_list:
            matrix [u][v] = w
        return matrix
        
    def print_adj_list(self):
        for key in self.graph_dict.keys():
            print("node", key, ": ", self.graph_dict[key])
        
            
            
    # ——————————————————————————————Algorithm—————————————————————————————————
    def Dijkstra(self, src):
        '''
        Time complexity: O(V^2) 
        
        Parameters
        src : String/Int
            indicating source node.

        Returns
        shortest_path: dic
        '''
        shortest_path = dict()
        edges = self.graph_dict
        if len(edges) < 2:
            return
        
        visited = set()
        h = [(0, src)]
        
        while (h):
            (w1 , n1) = heapq.heappop(h)
            if n1 in visited:
                continue
            visited.add(n1)
            shortest_path[n1] = w1
            
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(h, (w1 + w2 ,n2))
            
        return shortest_path
    
    
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])

    # Connects subtrees containing nodes `x` and `y`
    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1
            
    def kruskals_mst(self):
        '''
        Time complexity: O(V*log(V))

        '''
        # Resulting tree
        result = []
        
        # Iterator
        i = 0
        # Number of edges in MST
        e = 0
    
        # Sort edges by their weight
        self.graph_list = sorted(self.graph_list, key=lambda item: item[2])
        
        # Auxiliary arrays
        parent = []
        subtree_sizes = []
    
        # Initialize `parent` and `subtree_sizes` arrays
        for node in range(len(self.vertex)):
            parent.append(node)
            subtree_sizes.append(0)
    
        # Important property of MSTs
        # number of egdes in a MST is 
        # equal to (len(self.vertex) - 1)
        while e < (len(self.vertex) - 1):
            # Pick an edge with the minimal weight
            node1, node2, weight = self.graph_list[i]
            i = i + 1
    
            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)
    
            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)
        
        # Print the resulting MST
        for node1, node2, weight in result:
            print("%d - %d: %d" % (node1, node2, weight))
            
    def prims_mst(self):
        '''
        Time complexity: O(V^2)

        '''
        matrix = self.create_matrix()
        # Defining a really big number, that'll always be the highest weight in comparisons
        postitive_inf = float('inf')
    
        # This is a list showing which nodes are already selected 
        # so we don't pick the same node twice and we can actually know when stop looking
        selected_nodes = [False for node in range(len(self.vertex))]
    
        # Matrix of the resulting MST
        result = [[0 for column in range(len(self.vertex))] 
                    for row in range(len(self.vertex))]
        
        indx = 0
        for i in range(len(self.vertex)):
            print(matrix[i])
        
        print(selected_nodes)
    
        # While there are nodes that are not included in the MST, keep looking:
        while(False in selected_nodes):
            # We use the big number we created before as the possible minimum weight
            minimum = float('inf')
    
            # The starting node
            start = 0
    
            # The ending node
            end = 0
    
            for i in range(len(self.vertex)):
                # If the node is part of the MST, look its relationships
                if selected_nodes[i]:
                    for j in range(len(self.vertex)):
                        # If the analyzed node have a path to the ending node AND its not included in the MST (to avoid cycles)
                        if (not selected_nodes[j] and matrix[i][j]>0):  
                            # If the weight path analized is less than the minimum of the MST
                            if matrix[i][j] < minimum:
                                # Defines the new minimum weight, the starting vertex and the ending vertex
                                minimum = matrix[i][j]
                                start, end = i, j
            
            # Since we added the ending vertex to the MST, it's already selected:
            selected_nodes[end] = True
    
            # Filling the MST Adjacency Matrix fields:
            result[start][end] = minimum
            
            if minimum == float('inf'):
                result[start][end] = 0
    
            print("(%d.) %d - %d: %d" % (indx, start, end, result[start][end]))
            indx += 1
            
            result[end][start] = result[start][end]
    
        # Print the resulting MST
        # for node1, node2, weight in result:
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))
        
# Create a graph G        
G = Graph([[0,1,6],[0,2,2],[2,1,1],[2,3,7],[1,3,1]])

# Dijkstra
shortest_path = G.Dijkstra(0)
print(shortest_path)
G.kruskals_mst()
G.prims_mst()