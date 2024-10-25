class Solution:
    def isValid(self, s: str) -> bool:

        # intiate the stack
        stack = [] 

        #initate the dictionary  
        hashmap = {')': '(', ']':'[','}':'{'}

        # iteratre through the string
        for i in s:
            # if i is not in the hash map push it to the stack
            if i not in hashmap:
                stack.append(i)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != hashmap[i]:
                    return False



        # check if stack is empty
        return not stack