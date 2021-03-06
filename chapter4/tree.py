#Question 1
import collections
from chapter4.basicds import linkedlist

class graph:
    def __init__(self, gdict, left, right):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        self.left = left
        self.right = right

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
        

#Question 2
#idea is to find the root first then build left n right subtrees
    def arr_toBST(self, arr):
        if not arr:
            return None

        mid = len(arr) // 2

        root = self.gdict[arr[mid]]
        root.left = self.arr_toBST(arr[:mid])
        root.right = self.arr_toBST(arr[mid+1:])

        return root

#Question 3
    def listDepth(root):
        #BFS
        levels = {}
        queue = [root]

        while queue:
            node,level = queue.pop(0)

            if level not in levels:
                levels[level] = linkedlist()

            #add nodes each level
            levels[level].add(node)

            #push node into queue/ adj nodes into queue
            if node.left:
                queue.append(node.left)
                level += 1

            if node.right:
                queue.append(node.right)
                level += 1

        return levels

            











        



        

        
