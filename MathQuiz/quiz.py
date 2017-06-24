import datetime
import random

from questions import Add, Multiply, Substract


class Quiz:
	questions = []
	answers = []
	
	def __init__(self):
		# question_types = (Add, Multiply)
		count = 0
		range_num1 = int(input("Enter 1st number: "))
		range_num2 = int(input("Enter 2nd number: "))
		question_count = int(input("How many questions would you like: "))
		# Generate 10 random questsions with numbers from 1 to 10
		while count < question_count:
			num1 = random.randint(range_num1, range_num2)
			num2 = random.randint(range_num1, range_num2)
			question_add = Add(num1, num2)
			self.questions.append(question_add)
			count += 1
			num1 = random.randint(range_num1, range_num2)
			num2 = random.randint(range_num1, range_num2)
			question_mult = Multiply(num1, num2)
			self.questions.append(question_mult)
			count += 1
			num1 = random.randint(range_num1, range_num2)
			num2 = random.randint(range_num1, range_num2)
			question_subs = Substract(num1, num2)
			self.questions.append(question_subs)
			count += 1
			
		# add these questions into self.questions
		
	#def ask(self, question):
		
		
	def take_quiz(self):
		self.total_correct = 0
		# log the start time
		self.quiz_startTime = datetime.datetime.now()
		# ask all the questions
		# log the start time
		question_startTime = datetime.datetime.now()
		# capture the answer
		for question in self.questions:
			answer = input("Question No{}: {}".format((self.questions.index(question) + 1), question.text) + ("\nYour answer: "))
			try:
				int(answer) and len(answer) > 0
			except ValueError:
				answer = (input("Please enter a number:"))
		# check the answer
		# if the answer is right send back True
			if answer == str(question.answer):
				correct = True
				self.total_correct += 1
			# otherwise send back False
			else:
				correct = False
				
			self.answers.append(correct)
			
		# log the end time
			question_endTime = datetime.datetime.now()
		
		# send back the elapsed time, too
			elapsed_time = (question_endTime - self.quiz_startTime).seconds
			print ("Your time so far is {} seconds.".format(elapsed_time))
			#print (self.answers)
			#print (question.answer)
			#print (answer)
			#print (self.total_correct)
		# log if they got the question right
		
		# log the end time
		self.quiz_endTime = datetime.datetime.now()
		# show a summary
		return self.summary()
		
		
	def summary(self):
		# print how many you got right and the total # of questions. 5/10
		print ("You answered correctly {} out of {} questions!".format(self.total_correct, len(self.questions)))
		# print the total time for the quiz: 30 seconds!
		print ("Your total time was {} seconds".format((self.quiz_endTime - self.quiz_startTime).seconds))
		
Quiz().take_quiz()