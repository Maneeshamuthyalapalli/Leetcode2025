class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        prime_count = 0
        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            if is_prime(set_bits):
                prime_count += 1
        return prime_count

        
