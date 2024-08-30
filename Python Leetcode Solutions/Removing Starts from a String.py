class Solution:
    def removeStars(self, s: str) -> str:
        #create an array
        ans=[]
        #loop through the string
        for i in s:
            #if i is a star, then remove from string
            if i=="*":
                ans.pop()
            else:
                #add it to the new ans
                ans+=[i]
        #returns the array as a string
        return "".join(ans)

        