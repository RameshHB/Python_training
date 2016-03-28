from xlrd import open_workbook

class Assignment(object):
    def __init__(self, emp_id, emp_name, dob, gender, age, mob, email, qual, dept, pos, sal):
        """
		Initializing the definition
	"""
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.dob = dob
        self.gender = gender
        self.age = age
        self.mob = mob
        self.email = email
        self.qual = qual
        self.dept = dept
        self.pos = pos
        self.sal = sal

    def __str__(self):
        """
		Returning the objects
	"""
        return("Assignment object:\n"
               "  EMPId = {0}\n"
               "  EMPName = {1}\n"
               "  DOB = {2}\n"
               "  GENDER = {3}\n"
               "  AGE = {4} \n"
               "  MOB = {5} \n"
               "  EMAIL = {6}\n"
               "  QUAL = {7} \n"
               "  DEPT = {8} \n"
               "  POS = {9} \n"
               " SAL = {10} "

		.format(self.emp_id, self.emp_name, self.dob,
                       self.gender, self.age, self.mob, self.email,
                       self.qual, self.dept, self.pos, self.sal))

wb = open_workbook('assignment.xlsx') # Opening the file
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
	"""
	Number of rows
	"""        
	values = []
        for col in range(number_of_columns):
	    """
            Number of columns
	    """	
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Assignment(*values)
        items.append(item)

for item in items:
    print item
    print("Accessing one single value (eg.EMPName): {0}".format(item.emp_name))
    print
