class solution:
    # function to print pattern 2 
    def pattern2(self, N):
        # loop for rows     
        for i in range(N):
            #prints stars in each row 
            print("*"* (i+1))

if __name__ == "__main__":
               #create solution object
               sol=solution()
               #define N
               N=5
               # call the function pattern2 
               sol.pattern2(N)



         