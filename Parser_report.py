import csv
import re
import report_in_docx as re_docx

def init_class_objects(filename):
	global count_bak
	global count_mag
	global count_spec
	global bak_object
	global mag_object
	global spec_object
	count_bak=0
	count_mag=0
	count_spec=0
	with open(filename,"r", encoding="UTF-8") as f:
		for row in csv.reader(f, delimiter=";"):
			if any(field.strip() for field in row):
				match row[0]:
					case "Бакалавриат":
						count_bak += 1
					case "Магистратура":
						count_mag += 1
					case "Специалитет":
						count_spec += 1
					case _:
						print("warring2")
		bak_object = [Bakalavriat(f"{i}") for i in range(count_bak)]
		mag_object = [Magistratura(f"{i}") for i in range(count_mag)]
		spec_object = [Specialitet(f"{i}") for i in range(count_spec)]
	with open(filename,"r", encoding="UTF-8") as f:
		cb = 0
		cm = 0
		cs = 0
		for row in csv.reader(f, delimiter=";"):
			if any(field.strip() for field in row):
				match row[0]:
					case "Бакалавриат":
						bak_object[cb].type_of_profile = row[1]
						bak_object[cb].type_of_direction = row[2]
						cb += 1
					case "Магистратура":
						mag_object[cm].type_of_profile = row[1]
						mag_object[cm].type_of_direction = row[2]
						cm += 1
					case "Специалитет":
						spec_object[cs].type_of_profile = row[1]
						spec_object[cs].type_of_direction = row[2]
						cs += 1
					case _:
						print("warring3")


def reader(filename):
	with open(filename, "r", encoding="UTF-8") as f:
		for row in csv.reader(f, delimiter=";"):
			if any(field.strip() for field in row):
				normal_string=""
				match row[0]:
					case "Бакалавриат":
						for item in row:
							if any(field.strip() for field in item):
								normal_string += item + "***"
						bakalavr = use_normal_string(normal_string)
						bakalavr.bak()
					case "Магистратура":
						for item in row:
							if any(field.strip() for field in item):
								normal_string += item + "***"
						magister = use_normal_string(normal_string)
						magister.mag()
					case "Специалитет":
						for item in row:
							if any(field.strip() for field in item):
								normal_string += item + "***"
						specialist = use_normal_string(normal_string)
						specialist.spec()
					case _:
						print("warring1")

def output():
	for i in range(count_bak):
		percent_answers = 80
		re_docx.reporting(bak_object[i].counter, percent_answers,
						  bak_object[i].type_id,
						  bak_object[i].type_of_profile,
						  bak_object[i].type_of_direction,
						  bak_object[i].avgqwn)

		print(bak_object[i].type_id + " "
			  + bak_object[i].type_of_profile + " "
			  + bak_object[i].type_of_direction
			  + " среднее по 1 вопросу: " + str(bak_object[i].avgqwn[0])
			  + " в опросе приняло участие: " + str(bak_object[i].counter))
	for i in range(count_mag):
		print(mag_object[i].type_id + " "
			  + mag_object[i].type_of_profile + " "
			  + mag_object[i].type_of_direction
			  + " среднее по 1 вопросу: " + str(mag_object[i].avgqwn[0])
			  + " в опросе приняло участие: " + str(mag_object[i].counter))

	for i in range(count_spec):
		print(spec_object[i].type_id + " "
		+ spec_object[i].type_of_profile + " "
		+ spec_object[i].type_of_direction \
		+ " среднее по 1 вопросу: " + str(spec_object[i].avgqwn[0])
		+ " в опросе приняло участие: " + str(spec_object[i].counter))


class use_normal_string:
	def __init__(self, text):
		self.m = text.split("***")

	def bak(self):
		for i in range(count_bak):
			if self.m[1] == bak_object[i].type_of_profile and self.m[2] == bak_object[i].type_of_direction:
				questions = []
				for item in self.m:
					if item.replace(" ","").isdigit():
						questions.append(item)
				bak_object[i].change_culc(questions)  #ИНДЕКСЫ М ПО ПОРЯДКУ ВОПРОСОВ

	def mag(self):
		for i in range(count_mag):
			if self.m[1] == mag_object[i].type_of_profile and self.m[2] == mag_object[i].type_of_direction:
				questions = []
				for item in self.m:
					if item.replace(" ", "").isdigit():
						questions.append(item)
				mag_object[i].change_culc(questions)  # ИНДЕКСЫ М ПО ПОРЯДКУ ВОПРОСОВ

	def spec(self):
		for i in range(count_spec):
			if self.m[1] == spec_object[i].type_of_profile and self.m[2] == spec_object[i].type_of_direction:
				questions = []
				for item in self.m:
					if item.replace(" ", "").isdigit():
						questions.append(item)
				spec_object[i].change_culc(questions)  # ИНДЕКСЫ М ПО ПОРЯДКУ ВОПРОСОВ

class Bakalavriat:
	def __init__(self, name_id):
		self.name_id = name_id
		self.type_id = "Бакалавриат " + self.name_id
		self.type_of_profile = ""
		self.type_of_direction = ""
		self.init_questions_0()

	def init_questions_0(self):
		self.counter = 0
		self.qwns = []
		self.avgqwn = []
		for i in range(9):
			self.qwns.append(0)
			self.avgqwn.append(0.5)

	def change_culc(self, q):    #Добавить количествог вопросов ДОПИСАТЬ КУШКИ
		self.counter += 1
		for i in range(len(q)):
			self.qwns[i] += int(q[i])
			self.avgqwn[i] = self.qwns[i] / self.counter

class Magistratura(Bakalavriat):
	def __init__(self, name_id):
		self.name_id = name_id
		self.type_id = "Магистратура " + self.name_id
		self.type_of_profile = ""
		self.type_of_direction = ""
		self.init_questions_0()

class Specialitet(Bakalavriat):
	def __init__(self, name_id):
		self.name_id = name_id
		self.type_id = "Специалитет " + self.name_id
		self.type_of_profile = ""
		self.type_of_direction = ""
		self.init_questions_0()

init_class_objects("n_list.csv")
reader("input.csv")
output()
