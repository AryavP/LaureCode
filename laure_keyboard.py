# Store a keyboard in a binary tree and store autocomplete options in another tree

# Set up autocomplete 0.0.104 for predictive text

import autocomplete
autocomplete.load()

import datetime

class Conversation:
	# conversation had on certain date and time
	
	def __init__(self,DateTimeStamp,sentence_list,word_list,letter_list,num_sentences,num_words,first_run):
		self.num_sentences = 0
		self.num_words = 0
		self.sentence_list = []
		self.word_list = []
		self.letter_list = []
		self.first_run = 1
		self.DateTimeStamp = datetime.datetime.now()
		self.last_sentence = "Started Conversation at:"+self.DateTimeStamp
		self.add_sentence(sentence_list,last_sentence,num_sentences,num_words)

	def add_sentence(self,sentence_list,last_sentence,num_sentences,num_words,first_run):
		self.sentence_list.append(self.last_sentence)
		self.num_sentences = self.num_sentences+1
		return self.sentence_list
		#self.num_words = self.num_words + len(self.last_sentence)
	
	def add_word(self, word_list, last_word, num_words):
		self.word_list.append(self.last_word)
		self.num_words = self.num_words+1
		return self.word_list

	def add_letter(self, letter_list, last_letter):
		self.letter_list.append(self.last_letter)
		return self.letter_list	

	def start_sentence(self):
                if self.first_run == 0:
                        self.destroy_words()
                self.word_choice = 0
                self.word_choice_list = ['i','t','m']
                self.sentence_list = []
                self.wordlabel_list = []
                self.start_word()

        def start_word(self):
                if self.first_run == 0:
                        self.destroy_letters()
                self.word_list = []
                self.letterlabel_list = []
                self.first_run = 0

class EmptyTree():

	def isEmpty(self):
		return True

	def __str__(self):
		return strHelper(self,0)

	def strHelper(self,level):
		return ""

	def print_tree(self,level,right):
		return ""

class BinaryTree():
	# binary tree that will store keyboard letters or predicted words.
	
	EMPTY_TREE = EmptyTree()

	def __init__(self,rootid):
		self.left = BinaryTree.EMPTY_TREE
		self.right = BinaryTree.EMPTY_TREE
		self.rootid = rootid

	def isEmpty(self):
		return False

	def get_left_child(self):
		return self.left

	def get_right_child(self):
		return self.right

	def set_nodeValue(self,value):
		self.rootid = value

	def get_nodeValue(self):
		return self.rootid

	def insert_nodeValue(self,rootid):
		#print rootid,self.rootid
		if rootid[1] < self.rootid[1]:
			if self.left == BinaryTree.EMPTY_TREE:
				self.left = BinaryTree(rootid)
			else:
				self.left.insert_nodeValue(rootid)
		else:
			if self.right == BinaryTree.EMPTY_TREE:
				self.right = BinaryTree(rootid)
			else:
				self.right.insert_nodeValue(rootid)

	def __str__(self):
		"""Returns a string representation of the tree
        	rotated 90 degrees to the left."""
		return self.strHelper(level = 0)

	def strHelper(self, level):
            	result = ""
            	if not self.isEmpty():
			result += str(self.get_nodeValue()) + "\n"
			right_tree = self.get_right_child()
			left_tree = self.get_left_child()
			result += "\ " + "\n"
               		result += right_tree.strHelper(level)
               		#result += "\ " * level
			result += "/ " + "\n"
               		#result += str(self.get_nodeValue()) + "\n"
               		result += left_tree.strHelper(level)
          	return result
		return strHelper(self,0)
	
	def print_tree(self,level,right):
		print level
		blank = ""
		if level > 0:
			numspaces = pow(2,level-1)
			#print numspaces
			for i in range(1,numspaces):
				blank += " "
				#print i, blank
			if right == 0:
				keyboard = blank + str(self.get_nodeValue()[0])
			else:
				keyboard = str(self.get_nodeValue()[0]) + blank
			print keyboard
			right_level = level - 1
			right_tree = self.get_right_child()
			left_tree = self.get_left_child()
			left_level = level - 1
			left_tree.print_tree(left_level, 0)
			right_tree.print_tree(right_level, 1)
		else:
			return			
			
					

class Keyboard():
	
	def __init__(self):
		keylist = [" ",".","'","?","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",chr(127)]		
		#self.keylist = ["m","e","u","a","i","q","y",".","c","g","k","o","s","w","'"," ","?","b","d","f","h","j","l","n","p","r","t","v","x","z",chr(127)]
		self.keylist = self.sequence_keys(keylist, 32)
		self.kb_size = len(self.keylist)
		self.tree = self.make_keyboardTree()

	def sequence_keys(self, keylist, maxkeys):
		N = len(keylist)
		startindex = 0
		new_keylist = list(keylist)
		for i in range(0,5):
			ksum = 0
			for k in range(0, i):
				ksum = ksum + pow(2,k)
			n = (N - ksum)/pow(2,(i+1))
			num = pow(2,i)
			quotient = maxkeys/num
			endindex = startindex  + num
			for index in range(startindex, endindex):
				oldindex = (index - startindex)*quotient+n
				new_keylist[index] = keylist[oldindex]
			startindex = endindex
		print new_keylist
		return new_keylist

	def make_keyboardTree(self):
		keyvalue_list = []
		for key in self.keylist:
			keyvalue = ord(key)
			pair = [key, keyvalue]
			keyvalue_list.append(pair)
		#print keyvalue_list
		self.keyboardTree = BinaryTree(keyvalue_list[0])
		newlist = keyvalue_list[1:len(keyvalue_list)]
		#print newlist
		#print self.keyboardTree.__str__()
		for kv in newlist:
			print kv
			self.keyboardTree.insert_nodeValue(kv)
		return self.keyboardTree

		


class WordChoices():

	def __init__(self, word, prev_word, num_choices):
		if prev_word is None:
			word_list = autocomplete.predict_currword(word,num_choice)
		else:
			tmp_wordlist1 = autocomplete.predict_currword(word,num_choice)
			tmp_wordlist2 = autocomplete.predict_currword_given_lastword(prev_word, word, num_choice)
			if len(tmp_wordlist1) > len(tmp_wordlist2):
				word_list = tmp_wordlist1
			else:
				word_list = tmp_wordlist2	
		self.w_size = len(word_list)
		for i in range(0, len(word_list)-1):
			(word_list[i])[1] = (len(word_list)/2 - 1)+((-1)^(i+1))*i
		self.make_wordTree(word_list)

	def make_wordTree(self, wordlist):
		self.wordTree = BinaryTree(wordlist[0])
		newwordlist = wordlist[-0]
		for word in newwordlist:
			self.wordTree.insert_nodeValue(word)


if __name__ == "__main__":
	BigKeyboard = Keyboard()
	#print BigKeyboard.tree.__str__()
	BigKeyboard.tree.print_tree(level=5,right=0)

		
		

		

	
