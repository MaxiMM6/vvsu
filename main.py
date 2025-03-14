class Solution:
    
    def convertDateToBinary(self, date: str) -> str:

        result = date.split('-')
        bin_list = []
        
        for i in range(len(result)):
            result[i] = int(result[i])
            bin_list.append(bin(result[i])[2:])

        
        
        return '-'.join(bin_list)



solution = Solution()
print(solution.convertDateToBinary("2080-02-29"))