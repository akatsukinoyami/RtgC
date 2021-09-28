class switch_decorator:

	@staticmethod
	def switch(func):
		def wrapper(app, msg):
			if app.switch:					
				func(app, msg)
		return wrapper
		