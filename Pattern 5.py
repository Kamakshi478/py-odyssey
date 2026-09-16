class solution:
    # function to print pattern 4 
    def pattern4(self, N):
        # loop for rows     
        for i in range(N):
                for j in range(N, i, -1):
                    print("*", end=" ")
                print()
            

if __name__ == "__main__":
               #create solution object
               sol=solution()
               #define N
               N=5
               # call the function pattern4
               sol.pattern4(N)



         