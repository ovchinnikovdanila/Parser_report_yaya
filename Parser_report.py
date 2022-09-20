import csv
import re

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
				print(row[0])
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
						print("da2")
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
		print(bak_object[i].type_id + " " + bak_object[i].type_of_profile + " " + bak_object[i].type_of_direction + " среднее по 1 вопросу: " + str(bak_object[i].avgqwn1))
	for i in range(count_mag):
		print(mag_object[i].type_id + " " + mag_object[i].type_of_profile + " " + mag_object[i].type_of_direction + " среднее по 1 вопросу: " + str(mag_object[i].avgqwn1))

class use_normal_string:
	def __init__(self, text):
		self.m = text.split("***")

	def bak(self):
		for i in range(count_bak):
			if self.m[1] == bak_object[i].type_of_profile and self.m[2] == bak_object[i].type_of_direction:
				print("da")
				bak_object[i].change_culc(self.m[3],self.m[4],self.m[5],self.m[6])  #ИНДЕКСЫ М ПО ПОРЯДКУ ВОПРОСОВ
	def mag(self):
		for i in range(count_mag):
			if self.m[1] == mag_object[i].type_of_profile and self.m[2] == mag_object[i].type_of_direction:
				mag_object[i].change_culc(self.m[3],self.m[4],self.m[5],self.m[6])
	def spec(self):
		for i in range(count_spec):
			if self.m[1] == spec_object[i].type_of_profile and self.m[2] == spec_object[i].type_of_direction:
				spec_object[i].change_culc(self.m[3],self.m[4],self.m[5],self.m[6])

class Bakalavriat:
	def __init__(self, name_id):
		self.name_id = name_id
		self.type_id = "Бакалавриат"
		self.type_of_profile = ""
		self.type_of_direction = ""
		self.counter = 0
		self.qwn1 = 0					#Тут индекы вопросов
		self.qwn2 = 0
		self.qwn3 = 0
		self.qwn4 = 0
		self.avgqwn1 = 0				#ТУТ СРЕДНИЕ МЕЖДУ КАКИМИ
		self.avgqwn2 = 0
		self.avgqwn3 = 0
		self.avgqwn4 = 0
		self.avgqwn1_2 = 0
		self.avgqwn3_4 = 0

	def change_culc(self, q1, q2, q3, q4):    #Добавить количествог вопросов ДОПИСАТЬ КУШКИ
		self.counter += 1
		self.qwn1 += int(q1)
		self.qwn2 += int(q2)
		self.qwn3 += int(q3)
		self.qwn4 += int(q4)
		self.avgqwn1 = self.qwn1 / self.counter
		self.avgqwn2 = self.qwn2 / self.counter
		self.avgqwn3 = self.qwn3 / self.counter
		self.avgqwn4 = self.qwn4 / self.counter
		self.avgqwn1_2 = self.avgqwn1 + self.avgqwn2
		self.avgqwn3_4 = self.avgqwn3 + self.avgqwn4

class Magistratura(Bakalavriat):
	def __init__(self, name_id):
		self.name_id = name_id
		self.type_id = "Магистратура"
		self.type_of_profile = ""
		self.type_of_direction = ""
		self.counter = 0
		self.qwn1 = 0
		self.qwn2 = 0
		self.qwn3 = 0
		self.qwn4 = 0
		self.avgqwn1 = 0
		self.avgqwn2 = 0
		self.avgqwn3 = 0
		self.avgqwn4 = 0
		self.avgqwn1_2 = 0
		self.avgqwn3_4 = 0
		
class Specialitet(Bakalavriat):
	def __init__(self, name_id):
		self.name_id = name_id
		self.type_id = "Специалитет"
		self.type_of_profile = ""
		self.type_of_direction = ""
		self.counter = 0
		self.qwn1 = 0
		self.qwn2 = 0
		self.qwn3 = 0
		self.qwn4 = 0
		self.avgqwn1 = 0
		self.avgqwn2 = 0
		self.avgqwn3 = 0
		self.avgqwn4 = 0
		self.avgqwn1_2 = 0
		self.avgqwn3_4 = 0

init_class_objects("n_list.csv")
reader("input.csv")
output()
