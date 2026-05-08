import pickle

with open('compressed.bin', 'rb') as f:
    data = pickle.load(f)

unique_words = data['unique_words']
indices = data['indices']

original_words = [unique_words[i] for i in indices]
fileName_text = " ".join(original_words)

with open('fileName.txt', 'w', encoding='utf-8') as f:
    f.write(fileName_text)

print(fileName_text)
