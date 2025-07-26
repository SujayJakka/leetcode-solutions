class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        distances = [float("inf")] * n
        distances[src] = 0
        temp = []

        def relax(edge):
            src, des, price = edge[0], edge[1], edge[2]

            if distances[src] + price < temp[des]:
                temp[des] = distances[src] + price
        
        for i in range(k+1):
            temp = distances.copy()
            for flight in flights:
                relax(flight)
            distances = temp.copy()
        

        return -1 if distances[dst] == float("inf") else distances[dst]


            