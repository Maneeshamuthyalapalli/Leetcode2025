class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
        ranks = [""] * len(score)
    
        for rank, (idx, _) in enumerate(sorted_scores):
            if rank == 0:
                ranks[idx] = "Gold Medal"
            elif rank == 1:
                ranks[idx] = "Silver Medal"
            elif rank == 2:
                ranks[idx] = "Bronze Medal"
            else:
                ranks[idx] = str(rank + 1)
        return ranks



        
