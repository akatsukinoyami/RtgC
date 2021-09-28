from pyrogram import Client, idle, ContinuePropagation

from classes.js_dict			import js_dict

from classes.filters 			import myfilters
from classes.config_messages	import config_messages
from classes.text_methods		import text_methods
from classes.switch				import switch_decorator

class app(Client, myfilters, config_messages, switch_decorator, text_methods):
	id = js_dict(
		katsu	= 600432868,
		admins	= {600432868,},
		config	= -1001328058005,
		media	= -1001157282357
	)

	switch_value = True
	ContinuePropagation = ContinuePropagation
	
	def start(self):
		super().start()

		self.bot = self.get_me()

		self.db_file = f'DB/{self.bot.username}'
		
		self.send_awaking_message()
	
	def close(self):
		super().close()

	def run(self, func=False):
		self.start()

		if func: self.db = func(self.db_file) 

		idle()

		self.close()

		if self.db is not None: self.db.close()