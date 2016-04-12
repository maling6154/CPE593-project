import os
import math
import FileWords
from numpy import *


class FileOp:
	"""deal with files"""
	def __init__(self,filepath):
		self.filepath = filepath
		self.file_list = None
		self.all_words = None
		self.get_file_lists()
		self.get_filepath_words()

	def get_file_lists(self):
		"""get all files from the filepath
		"""
		self.file_list = []
		for root,dirs,files in os.walk(self.filepath):
			for file in files:
				self.file_list.append(os.path.join(root,file))
		return self.file_list

	def get_filepath_words(self):
		"""get all words from the files of a filepath
		"""
		self.all_words = []
		for file in self.file_list:
			self.all_words.extend(FileWords.words(file))



class LogisticRegression:
	"""implement Logistic Regression"""
	def __init__(self,ham_list,spam_list,ham_words,spam_words):
		self.ham_list = ham_list
		self.spam_list = spam_list
		self.all_words = list(set(ham_words + spam_words))
		self.X = []
		self.Y = []
		self.generate_X_Y()

	def file_to_x(self,file):
		"""generate vector x for a file"""
		file_words = FileWords.words(file)
		x = [1] #added for w0
		for i in self.all_words:
			x.append(file_words.count(i))
		return x

	def generate_X_Y(self):
		"""generate X and Y, list form"""
		for file in self.spam_list:
			self.X.append(self.file_to_x(file))
		for file in self.ham_list:
			self.X.append(self.file_to_x(file))
		#notcie 0 is used for spam
		self.Y = [0] * len(spam_list) + [1] * len(ham_list)

	def sigmoid(self,X):
		"""compute sigmoid, notice exp is Numpy function"""
		return 1.0 / (1 + exp(-X))

	def grad_ascent(self,X,Y,lmda = 0,max_iter = 500):
		"""compute weights W using grad ascent"""
		#convert list to Numpy matrix
		X_mat = mat(X)
		Y_mat = mat(Y).transpose()
		rows, cols = shape(X_mat)
		alpha = 0.001
		W = ones((cols,1))

		for i in range(max_iter):
			h = self.sigmoid( X_mat * W )
			error = (Y_mat - h )
			W += alpha * X_mat.transpose() * error - alpha * lmda * W
		return W

	def is_spam(self,file,W):
		"""classify if a file is spam"""
		x = self.file_to_x(file)
		x = mat(x)
		if x*W > 0:
			return 0
		return 1

	def spam_count(self,file_list,W):
		"""return the count of spam"""
		count = 0
		for file in file_list:
			if self.is_spam(file,W):
				count += 1
		return count



#prepare all_words
train_ham = FileOp('./train/ham')
ham_words = train_ham.all_words
ham_list = train_ham.file_list

train_spam = FileOp('./train/spam')
spam_words = train_spam.all_words
spam_list = train_spam.file_list


#prepare test lists
test_ham = FileOp('./test/ham')
test_ham_list = test_ham.file_list

test_spam = FileOp('./test/spam')
test_spam_list = test_spam.file_list






#using logistic regression without stopwords
logis = LogisticRegression(ham_list,spam_list,ham_words,spam_words)
W = logis.grad_ascent(logis.X,logis.Y)


count = logis.spam_count(test_ham_list,W)
print('Logistic Regression without stop words ./test/ham lambda = {} rate = {:.2%}'.format(0,1- count/len(test_ham_list)))

count = logis.spam_count(test_spam_list,W)
print('Logistic Regression without stop words ./test/spam lambda = {} rate = {:.2%}'.format(0,count/len(test_spam_list)))
