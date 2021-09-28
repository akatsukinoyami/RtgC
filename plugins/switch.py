from classes.client import app

command = app.filters.command
user	= app.filters.user
katsu	= app.id.admins

def switch(app, msg, to_state, txt2):
	if app.switch == to_state:
		txt1 = 'уже'
	else:
		app.switch = True
		txt1 = ''
		
	msg.reply(f'Бот {txt1} {txt2}.')

@app.on_message(command([f'on@{app.bot.username}']) & user(katsu))
def switch_on(app, msg):
	switch(app, msg, True, 'включен')

@app.on_message(command([f'off@{app.bot.username}']) & user(katsu))
def switch_off(app, msg):
	switch(app, msg, False, 'выключен')
	
