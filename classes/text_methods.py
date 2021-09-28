from time import sleep

not_none = lambda x: x is not None

class text_methods:

	def bot_can(self, msg, action):
		bot = self.get_chat_member(str(msg.chat.id), self.bot.id)
		if action == 'd':	return True if bot.can_delete_messages  else False
		if action == 'r':	return True if bot.can_restrict_members else False

	def roleplay_send(self, msg, txt):
		if not_none(msg.reply_to_message):	
			msg.reply(txt, reply_to_message_id=msg.reply_to_message.message_id)
		else:					 			
			msg.reply(txt, quote=False)
		self.msg_del(msg)
	
	def is_admin(self, msg):
		if msg.from_user.id == self.id.katsu: return True
		user	= self.get_chat_member(msg.from_user.id)
		return True if user.status in {'creator', 'administrator'} else False

	@staticmethod
	def msg_del(msg1, msg2=False):
		try:
			msg1.delete()
			if msg2:
				sleep(6)
				msg2.delete()
		except:
			pass

	@staticmethod
	def username_finder(user):
		if   not_none(user.username ):		return f"@{user.username}" 
		elif not_none(user.last_name):		return f"{user.first_name} {user.last.name}"
		else:						  		return user.first_name

	@staticmethod
	def text(msg):
		if 	 not_none(msg.text	 ):			return msg.text
		elif not_none(msg.caption): 		return msg.caption
		else:								return False

	@staticmethod
	def iter_choose(iterable, searching):
		if searching in iterable:
			return searching
		return False