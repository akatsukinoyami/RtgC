import re

from pyrogram import filters

class myfilters:

	filters = filters
	
	@staticmethod
	def filter_regex(data):
		def func(flt, app, msg):
			msg_text = app.text(msg)
			if msg_text:
				return re.search(flt.data, msg_text.lower())
			else:
				return None

		return filters.create(func, data=data)