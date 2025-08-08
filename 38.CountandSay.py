class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
    
        for _ in range(n - 1):
            current = ""
            count = 1
            
            # Go through the string and apply run-length encoding
            for i in range(1, len(result) + 1):
                if i < len(result) and result[i] == result[i - 1]:
                    count += 1
                else:
                    current += str(count) + result[i - 1]
                    count = 1
            
            result = current  # Move to next term
        
        return result
            