
from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        adjList = [[] for i in range(V)]
        #for undirected graph,both side nodes are included
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        return adjList
        


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        V, E = IntArray().Input()

        edges = IntMatrix().Input(E, 2)

        obj = Solution()
        res = obj.printGraph(V, edges)

        empty = True
        for i in range(V):
            if res[i]:
                empty = False
                break

        # If all are empty, print []
        if empty:
            print("[]")
        else:
            # Print sorted, unique adjacency lists in the required format
            for i in range(V):
                st = sorted(set(res[i]))  # Sort and remove duplicates
                print("[", end="")
                for j in range(len(st)):
                    print(st[j], end="")
                    if j < len(st) - 1:
                        print(" ", end="")
                print("]")
        print("~")

# } Driver Code Ends