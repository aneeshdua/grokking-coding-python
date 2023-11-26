#https://leetcode.com/problems/backspace-string-compare/description/
class Solution:
    def backspaceCompare(self, str1: str, str2: str) -> bool:
        #In place soln
        def getNextValidIndex(string:str,index:int) -> int:
            bpCount=0
            while(index>=0):
                if(string[index] == '#'):
                    bpCount+=1
                elif (bpCount>0):
                    bpCount-=1
                else:
                    break
                index-=1
            return index

        index1 = len(str1)-1
        index2 = len(str2)-1

        while(index1 >=0 or index2 >=0):
            i1 = getNextValidIndex(str1,index1)
            i2 = getNextValidIndex(str2,index2)

            if (i1<0 and i2<0):
                return True

            if i1<0 or i2<0:
                return False
            
            if (str1[i1]!=str2[i2]):
                return False
            
            index1 = i1-1
            index2 = i2-1
        
        return True

        

        
        #################################################
        #Extra space soln
        # stack1=[]
        # stack2=[]

        # for char in s:
        #     print(char)
        #     if char!='#':
        #         stack1.append(char)
        #     elif (len(stack1)>0):
        #         stack1.pop()
        
        # for char in t:
        #     if char!='#':
        #         stack2.append(char)
        #     elif (len(stack2)>0):
        #         stack2.pop()
        # print("s1",stack1)
        # print("s2",stack2)
        # if(stack1==stack2):
        #     return True
        # else:
        #     return False
        