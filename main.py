import string
from collections import Counter
import matplotlib.pyplot as plt

# read text file
text = open("text.txt", encoding="utf-8").read()

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# NLP Algorithm Steps
emotion_list = []
emotion_dict = {}
# Open the emotion file
with open("emotions.txt", "r") as file:
    # Loop through each line and clear it
    for line in file:
        clear_line = line.replace("\n", '').replace("'", '').replace(",", '').strip()
        word, emotion = clear_line.split(":")
        emotion_dict[word] = emotion

# If word is present in the dictionary, add the emotion to the emotion_list
for word in final_words:
    if word in emotion_dict:
        emotion_list.append(emotion_dict[word])

# Count each emotion in the emotion_list
word_counter = Counter(emotion_list)

print(word_counter)

# Plotting the emotions on the graph
fig, ax1 = plt.subplots()
ax1.bar(word_counter.keys(), word_counter.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

