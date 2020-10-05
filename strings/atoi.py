class Solution:
    '''
    This new solution is O(N) time and O(N) space.
    It is O(N) space because we are restricting the total to be at most 32 bits. With the previous approach, we kept on adding total
    without restricting it. This is only possible in Python because ints are unbounded. However, this flexibility allows total to grow arbitrarily large
    making the space complexity O(N) 
    '''
    def myAtoi(self, str):
        intRepresentation = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, }
        i = 0
        sign = 1
        total = 0
        while i < len(str):

            if str[i] == " ":
                i += 1
                continue

            if str[i] == "-" or str[i] == "+":
                sign = 1 if str[i] == "+" else -1 
                i += 1                 
                total = self.compute(i, str, total,sign,intRepresentation)
                break

            if str[i] not in intRepresentation:
                return 0 

            if str[i] in intRepresentation:
                total = self.compute(i,str,total,sign,intRepresentation)
                break

        total *= sign

        if -pow(2,31) > total:
            return -pow(2,31)

        elif total > pow(2,31) - 1:
            return pow(2,31) - 1

        return total

    def compute(self,i, str, total, sign,intRepresentation):
        while i < len(str) and str[i] in intRepresentation:
            if sign == 1:
                if total == (pow(2,32) - 1) //  10:
                    if intRepresentation[str[i]] > (pow(2,32) - 1) % 10:
                        return pow(2,32) - 1
                    else:
                        total = total * 10 + intRepresentation[str[i]]
                elif total > (pow(2,32) - 1) //  10:
                    return pow(2,32) - 1
                else:
                    total = total * 10 + intRepresentation[str[i]]

            elif sign == -1:
                if total == (pow(2,32) //  10):
                    if intRepresentation[str[i]] > pow(2,32) % 10:
                        return (pow(2,32))
                    else:
                        total = total * 10 + intRepresentation[str[i]]
                elif total >= (pow(2,32) // 10):
                    return (pow(2,32))
                else:
                    total = total * 10 + intRepresentation[str[i]]
            i += 1
        return total


one = Solution()
print(one.myAtoi("3.14159"))
print(one.myAtoi("   -42"))
print(one.myAtoi("42"))
print(one.myAtoi("4193 with words"))
print(one.myAtoi("words and 987"))
print(one.myAtoi("-91283472332"))
print(one.myAtoi("21474836460"))
