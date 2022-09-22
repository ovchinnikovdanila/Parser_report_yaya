from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu

def reporting(counter, percent_answers, type_id, type_of_profile , type_of_discipline, avgqwn):

	template = DocxTemplate('template.docx')
	full_name = type_id + " " + type_of_profile + " " + type_of_discipline
	context = {
	    'counter_current_obj': counter,
	    'current_percent': percent_answers,
	    'current_direction': type_of_discipline,
	    'current_q1avg': avgqwn[0],
	    'current_q1percent': avgqwn[0] / 5 * 100, # 5 это максимум балов за ответ если меньше то другое значение
	    

	    'current_avg_1_3': (avgqwn[0] + avgqwn[1] + avgqwn[2]) / 3
	    'current_avg_1_3percent' (avgqwn[0] + avgqwn[1] + avgqwn[2]) / 3 / 15 * 100 # 15 максимальная сумма балов по этим вопросам если другое занчение то другое
	    	#дальше по порядку все остальные вопросы, 
	    	#после последнего значение не ставится "," 
	    }

	template.render(context)
	template.save("Automated_report " + full_name + ".docx")