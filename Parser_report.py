import csv


def reader(filename):
		with open(filename, "r") as f:
			for row in csv.reader(f, delimiter=";"):
				if any(field.strip() for field in row):
					numer_of_n = str(check_obr_prog(row[5]))
					match numer_of_n:
						case "1":
							eform1.change_culc(row[8], row[9], row[12], row[13])
						case "2":
							eform2.change_culc(row[8], row[9], row[12], row[13])
						case _:			
							print("unnoun")
			create_report_docx()


def check_obr_prog(group):
	match group:
		case "404" | "400":
			return 1
		case "500" | "600":
			return 2
		case _:
			return 3

def create_report_docx():
	print(str(eform1.avgqwn1))
	print(str(eform2.avgqwn2))

class Obr_progs():
	counter = 0
	qwn1 = 0
	qwn2 = 0
	qwn3 = 0
	qwn4 = 0
	avgqwn1 = 0
	avgqwn2 = 0
	avgqwn3 = 0
	avgqwn4 = 0
	avgqwn1_2 = 0
	avgqwn3_4 = 0

	def change_culc(self, q1, q2, q3, q4):
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


eform1 = Obr_progs()
eform2 = Obr_progs()
reader("input.csv")
