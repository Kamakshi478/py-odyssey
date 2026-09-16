class solution:
    # function to print pattern 3 
    def pattern3(self, N):
        # loop for rows     
        for i in range(1, N+1):
                for j in range(1,i+1):
                    print(j, end=" ")
                print()
            

if __name__ == "__main__":
               #create solution object
               sol=solution()
               #define N
               N=5
               # call the function pattern3 
               sol.pattern3(N)



         