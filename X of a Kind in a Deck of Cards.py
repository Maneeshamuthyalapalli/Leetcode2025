class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)
        counts = list(freq.values())
        gcd_all = reduce(gcd, counts)
        return gcd_all > 1
