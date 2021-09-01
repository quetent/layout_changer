from convert import Convert
from pyperclip import paste
from keyboard import add_hotkey, wait
from sys import exit

class Changer:

	def __init__(self, hotkey):

		add_hotkey(hotkey, Changer.change_symbols)

	@staticmethod
	def change_symbols():
		
		Convert.convert_symbols(paste())

	@staticmethod
	def start():

		wait()

if __name__ == '__main__':

	try:
		HOTKEY = 'ctrl+shift'
		Changer(HOTKEY).start()
	except (KeyboardInterrupt, SystemExit):
		exit()
