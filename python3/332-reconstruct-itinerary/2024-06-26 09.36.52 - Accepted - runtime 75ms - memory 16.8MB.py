class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets = sorted(tickets)[::-1]
        res = []
        edges = defaultdict(list)

        for ticket in tickets:
            arrival, destination = ticket
            edges[arrival].append(destination)
        
        def dfs(city):

            while edges[city]:
                destination = edges[city].pop()
                dfs(destination)
            res.append(city)
        
        dfs("JFK")
        return res[::-1]


        