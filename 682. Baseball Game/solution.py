class Solution:
    def calPoints(self, operations: List[str]) -> int:
    
        # empty record is empty stack?
        record = []

        for op in operations:
        
            #if + add up the last two
            if op == "+":
                record.append(record[-1] + record[-2])
            #elif d double it
            elif op == "D":
                record.append(record[-1]*2)
            #elif c invaliate the last record or we pop it from the stack
            elif op == "C":
                record.pop()   
            #else we just add it to the stack cuz it's a number
            else:
                record.append(int(op))

        #we wanna return the sum of the total record now
        return(sum(record))