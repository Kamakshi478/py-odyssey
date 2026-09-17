class solution:
    # function to print pattern 6
    def pattern6(self, N):
        # loop for rows     
        for i in range(N):
                for j in range(N, i, -1):
                    print(N-j+1, end=" ")
                print()
            

if __name__ == "__main__":
               #create solution object
               sol=solution()
               #define N
               N=5
               # call the function pattern6
               sol.pattern6(N)



         