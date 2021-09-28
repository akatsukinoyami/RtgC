import time, requests, traceback

not_none = lambda x: x is not None

class config_messages:
	def find_location(self):
		url = 'http://ipinfo.io/json'
		with requests.get(url) as response:
			try:
				response.raise_for_status()
				json = response.json()
				return f'''\
					Location: {json["city"]} ({json["country"]})\n\
					IP:       {json["ip"]}```'''
			except:
				return ''

	def prepare_awaking_msg(self):
		return f'''
			**Turned on bot:** ```
			
			Bot:      {self.bot.first_name}
			Username: @{self.bot.username}
			User ID:  {self.bot.id}
			
			Time:     {time.strftime("%H:%M:%S %d/%m/%Y", time.localtime())}
			{self.find_location()}'''

	def send_awaking_msg(self):
		txt = self.prepare_awaking_msg()	
		self.send_message(self.id.config, txt)

	def prepare_info_msg(self, msg):
		user= msg.from_user

		txt = f'**Bot:** __@{self.username}__'
		txt+= f'\n**Chat:** __{msg.chat.title}__'
		txt+= f'\n**Chat ID:** __{msg.chat.id}__** / **__{msg.message_id}__'
		txt+= f'\n**User:** __{user.first_name} __'
		txt+= f' __{user.last_name}__'	 if not_none(user.last_name) else ''
		txt+= f' __(@{user.username})__' if not_none(user.username)  else '' 
		txt+= f'\n**User ID:** __{user.id}__'

		if   not_none(msg.text): txt+= f'\n**Text:** {msg.text.html}'
		elif not_none(msg.media) and msg.media:
			msg_types = {
				"Audio"		: msg.audio,
				"Document"	: msg.document,
				"Photo"		: msg.photo,
				"Sticker"	: msg.sticker,
				"Animation"	: msg.animation,
				"Video"		: msg.video,
				"Voice"		: msg.voice,
				"Video note": msg.video_note,
				}
			for name, msg_type in msg_types:
				if not_none(msg_type):
					txt+= f'\n**{name}**:_{msg_type.file_id}__'

			if   not_none(msg.caption): txt+= f'\n**Caption**:__{msg.caption}__'

		return txt
	
	def prepare_error_msg(self, msg, error):
		return f'''**Error occured in message:**
				{self.prepare_info_msg(msg)}
				**Error:** ```{str(error)}```
				**Traceback:** ```{str(traceback.format_exc())}```'''

	def send_error_msg(self, msg, error):
		txt = self.prepare_error_msg(msg, error)

		self.send_message(self.id.config, txt)
		self.forward_messages(self.id.config, msg.chat.id, (msg.message_id,))