from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu

def reporting(counter, percent_answers, type_id, type_of_profile , type_of_discipline, avgqwn):

	template = DocxTemplate('template.docx')
	full_name = type_id + " " + type_of_profile + " " + type_of_discipline
	current_q1percent = avgqwn[0] / 4 * 100
	current_q2percent = avgqwn[1] / 4 * 100
	current_q3percent = avgqwn[2] / 4 * 100
	current_q4percent = avgqwn[3] / 4 * 100
	current_q5percent = avgqwn[4] / 4 * 100
	current_q6percent = avgqwn[5] / 4 * 100
	current_q7percent = avgqwn[6] / 4 * 100
	current_q8percent = avgqwn[7] / 4 * 100
	current_q9percent = avgqwn[8] / 4 * 100
	current_avg_1_6 = avgqwn[0] + avgqwn[1] + avgqwn[2]+ avgqwn[3]+ avgqwn[4]+ avgqwn[5]
	current_avg_1_6percent = (avgqwn[0] + avgqwn[1] + avgqwn[2]+ avgqwn[3]+ avgqwn[4]+ avgqwn[5]) / 24 * 100
	current_avg_7_8 = avgqwn[6] + avgqwn[7]
	current_avg_7_8percent = (avgqwn[6] + avgqwn[7]) / 8 * 100

	context = {
	    'counter_current_obj': counter,
	    'current_percent': percent_answers,
	    'current_direction': full_name,
	    'current_q1avg': avgqwn[0],
	    'current_q1percent': current_q1percent, # 5 это максимум балов за ответ если меньше то другое значение
		'current_q2avg': avgqwn[1],
		'current_q2percent': current_q1percent,
		'current_q3avg': avgqwn[2],
		'current_q3percent': current_q1percent,
		'current_q4avg': avgqwn[3],
		'current_q4percent': current_q1percent,
		'current_q5avg': avgqwn[4],
		'current_q5percent': current_q1percent,
		'current_q6avg': avgqwn[5],
		'current_q6percent': current_q1percent,
		'current_q7avg': avgqwn[6],
		'current_q7percent': current_q1percent,
		'current_q8avg': avgqwn[7],
		'current_q8percent': current_q8percent,
		'current_q9avg': avgqwn[8],
		'current_q9percent': current_q9percent,
	    'current_avg_1_6': current_avg_1_6,
	    'current_avg_1_6percent': current_avg_1_6percent,
		'current_avg_7_8': current_avg_7_8,
		'current_avg_7_8percent': current_avg_7_8percent

		# 15 максимальная сумма балов по этим вопросам если другое занчение то другое
	    	#дальше по порядку все остальные вопросы, 
	    	#после последнего значение не ставится "," 
	    }

	template.render(context)
	template.save("Automated_report " + full_name + ".docx")