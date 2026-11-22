word=input("Enter a word :") or "python"
print(word)
print("Length of word:",len(word))
print("Type of word:",type(word))
Characters=list(word)
print("Characters in the word:",Characters)
pairs=list(zip(Characters,Characters[1:]))
print("adjacentpairs",pairs)
