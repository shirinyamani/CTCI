#Question 1
class graph:
    def __init__(self, gdict):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addedge(self,vertex, edge):
        self.gdict[vertex].append(edge)


    def is_route(self, start,end):
        queue = [start]
        visited = [start]
        path = False

        while queue:
            node_deq = queue.pop(0)
            for adj in self.gdict[node_deq]:
                if adj not in visited:
                    if adj == end:
                        path == True
                        break
                    else:
                        visited.append(adj)
                        queue.append(node_deq)

            return path
        


        
