class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        choc_prices = {}
        two_pieces = []

        for price in prices:
            if price not in  choc_prices:
                choc_prices[price] = 1
            else:
                choc_prices[price] += 1
        

        for i in range(2):
            min_price = float("inf")
            for price in prices:
                if choc_prices[price] != 0:
                    min_price = min(price, min_price)
            two_pieces.append(min_price)
            choc_prices[min_price] -= 1
        

        cost = two_pieces[0] + two_pieces[1]

        if cost > money:
            return money
        else:
            return money - cost

        