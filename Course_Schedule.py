
class Solution:

    def _init_(self):
        self.adjacencyMatrix = []
        self.visitedMap = {}

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        res = [True]

        self.adjacencyMatrix = [[0 for i in range(numCourses)] for j in range(numCourses)]
        self.visitedMap = {}
        
        for i in range(numCourses):
            self.visitedMap[i] = 0

        for i in range(len(prerequisites)):
            self.adjacencyMatrix[prerequisites[i][1]][prerequisites[i][0]] = 1
        
        for i in range(numCourses):
            if(self.visitedMap[i] == 0):
                path = set()
                self.DFSVisit(i, res, path)
            
            if(res[0] == False):
                return False
        
        return True
            
    def DFSVisit(self, index, res, path):
        self.visitedMap[index] = 1
        path.add(index)

        for j in range(len(self.adjacencyMatrix[index])):

            if self.adjacencyMatrix[index][j] == 1:
                if(self.visitedMap[j] == 0):
                    self.DFSVisit(j, res, path)
                elif(j in path):
                    res[0] = False
        
        path.remove(index)

        
        

                




