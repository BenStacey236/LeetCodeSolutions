# Medium Solution
# Problem 151

def reverseWords(s: str) -> str:
        return ' '.join([word for word in reversed(s.split()) if word != ' '])