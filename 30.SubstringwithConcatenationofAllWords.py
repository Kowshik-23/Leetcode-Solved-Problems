class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        wordLen = len(words[0])
        wordCount = Counter(words)
        numWords = len(words)
        totalLen = wordLen * numWords
        n = len(s)
        
        res = []
        
        
        for i in range(wordLen):
            left = i
            seen = Counter()
            count = 0  
            
            for j in range(i, n - wordLen + 1, wordLen):
                word = s[j:j + wordLen]
                
                if word in wordCount:
                    seen[word] += 1
                    count += 1
                    
                    while seen[word] > wordCount[word]:
                        leftWord = s[left:left + wordLen]
                        seen[leftWord] -= 1
                        left += wordLen
                        count -= 1
                    
                    if count == numWords:
                        res.append(left)
                        
                        leftWord = s[left:left + wordLen]
                        seen[leftWord] -= 1
                        left += wordLen
                        count -= 1
                        
                else:
                    seen.clear()
                    count = 0
                    left = j + wordLen
        
        return res
        