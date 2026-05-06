with open("story.txt", "r") as f: 
    story = f.read()

# set() is a list that only accepts unique elements
words=set()
start_of_word = -1
target_start = "<"
target_end = ">"

# enumereta will give us the position(i) and the element of the position(char)
for i,char in enumerate(story):
    if char == target_start:
        start_of_word = i 
    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1

answers = {}
for word in words: 
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
with open('your_stories', 'a') as f:
        f.write('"' + story + '"' + "\n")
        print(story)