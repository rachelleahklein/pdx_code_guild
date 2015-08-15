# This program takes a sentence and spits out the words in reverse order.

def user_input():
	sentence = raw_input("Please write a sentence: ")
	return sentence

def backwards(sentence):
	sentence_list = sentence.split()
	sentence_list.reverse()
	sentence_backwards = ' '.join(sentence_list)
	return sentence_backwards

def backwards_test():
	assert(backwards("I am a bike thief.") == "thief. bike a am I")

backwards_test()
sentence = user_input()
print backwards(sentence)
