import re
import csv
import os


def reader(filename):
		need_report = 1
		with open(filename, "r", encoding="utf-8") as f:
			for row in csv.reader(f):
				if any(field.strip() for field in row):
					id_fe = check_obr_prog(row[5])
					match id_fe:
						case "1":
							obr_prog_num_1.change_culc(row[8], row[9], row[10], row[12])
						case "2":
							obr_prog_num_2.change_culc(row[8], row[9], row[10], row[12])
						case _:			
							need_report = 0
			if need_report == "1"	
				create_report_docx()


def check_obr_prog(group)
	match group:
		case "404М", "400":
			return 1
		case "500", "600":
			return 2
		case _:
			return none

def create_report_docx()

class Obr_progs()
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

	def change_culc(q1, q2, q3, q4)
		self.counter += 1
		self.qwn1 += q1
		self.qwn2 += q2
		self.qwn3 += q3
		self.qwn4 += q4
		self.avgqwn1 /= counter
		self.avgqwn2 /= counter
		self.avgqwn3 /= counter
		self.avgqwn4 /= counter
		self.avgqwn1_2 = avgqwn1 + avgqwn2
		self.avgqwn3_4 = avgqwn3 + avgqwn4


