class Solution:
    def pattern1(self, N):
        for i in range(N):
            for j in range(N):
                print(" * ", end=" ")
            print()
s= Solution()
s.pattern1(3)