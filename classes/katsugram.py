from pyrogram import Client, idle, ContinuePropagation
import os

from classes.filters 			import myfilters
from classes.text_methods		import text_methods
from classes.important_ids 		import important_ids
from classes.config_messages	import config_messages
from classes.switch				import switch_decorator

class app(Client, myfilters, config_messages, switch_decorator, text_methods, important_ids):
	
	switch_value = True
	ContinuePropagation = ContinuePropagation
	
	def start(self, func=False):
		print(os.system('ls /app'), flush=True)

		super().start()

		self.bot = self.get_me()

		self.db_file = f'DB/{self.bot.username}'

		if func: self.db = func(self.db_file) 
		
		self.send_awaking_msg()
	
	def close(self):
		super().close()

		if self.db is not None: self.db.close()

	def run(self, func=False):
		self.start(func)
		idle()
		self.close()
