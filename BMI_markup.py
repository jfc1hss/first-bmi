#exit fn breaks the loop at 0, or returns an error for other numbers.
from sys import exit

#list defined because "or" fn confuses python
#variables can have the same name as the script. Here: "bmi" (original script is called bmi).
bmi = ["what is bmi?", "what is bmi", "bmi", "bmi?"]

male=["male","m"]

female=["female", "f"]

#Functions cannot have the same name as the script
def bmi_q():
	print "Very good! Let's start with your age."
	age= float(raw_input("How old are you %s?	>	" %name))
	height= float(raw_input("How tall are you, in m?	>	"))
	
	#not needed here, just a note. global allows variables to be used out of fn
	global weight
	weight=float(raw_input("What do you weight in kg?	>	"))
	Gender=raw_input("Finally, are you male or female? (No offense.)	>	")
	
	result = bmi_c(weight,height)
	
	analysis(result)
	
def analysis(result):
	if result < 18.5:
		print result, "You are far too skinny, please eat more."
		print "A healthy BMI is between 18.5 and 25."
		#exit at each option, or will go back to consent.
		exit(0)
	
	elif result > 25:
		print result, "You are far too fat, please eat less."
		print "A healthy BMI is between 18.5 and 25."
		exit(0)
	
	else:
		print result, "Congratulations! You're well fit. "
		print "A healthy BMI is between 18.5 and 25."
		exit(0)
	
def bmi_c(weight,height):
	return weight / (height**2)

def consent_q():	
	#defining True starts infinite loop. Need cap letter
	unsure = True
	
	while True:
		print "Would you like to calculate your BMI?" 
		consent = raw_input("> Answer: \"Yes\", \"No\", or \"What is BMI?\"	>	")
		
		#".lower" takes the input of "consent" and converts it to all lower case.
		if consent.lower() == "no":
			print ("What did you open a script called \"BMI\" for then??? This is all I can do!")
	
		elif consent.lower() in bmi:
			print """Wise man at CDC say: 
				\"Body Mass Index (BMI) is a person's weight in kilograms 
				divided by the square of height in meters. 
				
				A high BMI can be an indicator of high body fatness. 
				
				BMI can be used to screen for weight categories that may 
				lead to health problems but it is not diagnostic of the 
				body fatness or health of an individual.\" """
	
		elif consent.lower() == "yes":
			#False now to end loop
			unsure = False
			bmi_q()
						
		else:
			print "Sorry, me no hablo ingles so good. Try again."
 
			
print "Thank you for running the BMI script." 
print "Before we begin, please tell me your name:"
name=raw_input(">	")
print "Hello %s, nice to meet you." % (name)
consent_q()