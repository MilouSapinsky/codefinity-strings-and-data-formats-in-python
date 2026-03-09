def substring_between_chars(text, char):
    firstIndex = text.find(char)
    lastIndex = text.rfind(char)
    if firstIndex == -1 and firstIndex == lastIndex:
        return ""
    else:
        return text[firstIndex+1 : lastIndex]
            

# Sample calls
print(substring_between_chars("abracadabra", "a"))  # Expected: "bracadabr"
print(substring_between_chars("hello world", "l"))  # Expected: "lo wor"
print(substring_between_chars("test", "x"))         # Expected: ""