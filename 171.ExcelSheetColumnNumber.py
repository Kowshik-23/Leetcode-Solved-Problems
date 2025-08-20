class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1  # Convert letter to number
            result = result * 26 + value      # Shift previous digits and add new one
        return result
            