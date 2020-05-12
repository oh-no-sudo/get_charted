class Get_Charted():
	"""Comment this code you idiot"""
	def __init__(self, html=""):
		from bs4 import BeautifulSoup

		self.html_raw = html # File address of inputted html file 

		try:
			with open(self.html_raw, "r", encoding="utf-8") as f_obj:
				self.raw_stream = f_obj # Raw html before soupifying
				self.html_soup = BeautifulSoup(f_obj, "lxml") #Soupified 
		except FileNotFoundError:
			print("Failed to import from html. Did you specify a valid file?")
			print("Continuing anyway...\n")
			


	def prettify(self, inp=""):
		out_var = str(self.html_soup.prettify())

		if inp == "":
			with open(f"{self.html_raw[:-5]}.prettify.html", "w", encoding="utf-8") as f_obj:
				f_obj.write(out_var)

		else:
			with open(inp, "w", encoding="utf-8") as f_obj:
				f_obj.write(out_var)


	def get_dates(self, end_date=[2020, 1, 1], begin_date=[2020, 5, 12]):
		import datetime 

		# One day delta (for adding and subtracting days)
		try:
			self.one_day_delta = datetime.timedelta(1)

			self.begin_date = datetime.date(begin_date[0], begin_date[1], begin_date[2])
			self.end_date = datetime.date(end_date[0], end_date[1], end_date[2])

			self.days_diff = abs(self.begin_date - self.end_date).days

			self.days_diff_list = []
			


			# Append all the days between start day and end day to a list. 
			var1 = self.begin_date
			control_string = "{dt:%A}, {dt.day} {dt:%B} {dt.year}"

			for nums in range(self.days_diff+1):
				self.days_diff_list.append(control_string.format(dt=var1))
				var1 = var1 - self.one_day_delta

		except IndexError:
			print("Datetime failed. Did you supply dates properly?")
		




	def pull_self(self):
		print(abs(self.begin_date - self.end_date).days)
		print(self.days_diff_list)

test = Get_Charted()
test.get_dates()

test.pull_self()