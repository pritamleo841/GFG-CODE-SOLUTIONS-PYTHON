class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.strip().split()
        result=[]
        for word in words:
            stack=list(word)
            reversed_word=''
            while stack:
                reversed_word+=stack.pop()
            result.append(reversed_word)
        return ' '.join(result)