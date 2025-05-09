class Solution:
    # def isPalindrome(self, x: int) -> bool:
        
    #     #음수 처리
    #     if x < 0: 
    #         return False

    #     x = str(x)
    #     front = 0
    #     back = len(x) - 1

    #     while front<=back :
    #         if x[front] != x[back]:
    #             return False
    #         else:
    #             front += 1
    #             back -= 1
    #     return True

    # 숫자가 문자보다 계산이 빠름
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            #10으로 나눠서 나머지를 계속 더해감으로 증가시킴
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10