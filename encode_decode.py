import pickle

def encode(readable_w : str):
	with open('word_str.pickle', 'rb') as f:
		lst_of_words = pickle.load(f)

	to_print = ''
	for char in readable_w:
		if char in lst_of_words:
			to_print += str(lst_of_words.index(char)) + ' '
		else:
			lst_of_words.append(char)
			to_print += str(lst_of_words.index(char)) + ' '

	with open('word_str.pickle', 'wb') as f:
		pickle.dump(lst_of_words, f)

	print(to_print.strip())


def decode(coded_w : str):
	with open('word_str.pickle', 'rb') as f:
		lst_of_words = pickle.load(f)

	lst_of_indices = coded_w.split()
	readable_w = ''
	for i in lst_of_indices:
		readable_w += lst_of_words[int(i)]

	print(readable_w)
