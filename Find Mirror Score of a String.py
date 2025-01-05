class Solution:
    def calculateScore(self, s: str) -> int:
        mirror_map = {chr(i): chr(219 -  i) for i in range (ord('a'), ord('z') + 1)}
        char_indices = {c: [] for c in mirror_map.keys()}
        score = 0
        for i, char in enumerate(s):
            mirror_char = mirror_map[char]
            if char_indices[mirror_char]:
                j = char_indices[mirror_char].pop()
                score += i - j
            else:
                char_indices[char].append(i)
        return score
        ©leetcode
