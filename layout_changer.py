from convert import Convert
from pyperclip import paste, copy
from keyboard import add_hotkey, press_and_release, wait
from sys import exit

class Changer:

	def __init__(self, hotkey):

		add_hotkey(hotkey, Changer.change_symbols)

	@staticmethod
	def change_symbols():
		
		press_and_release('ctrl+c')

		clipboard = Convert.convert_symbols(paste())

		if clipboard is None:
			return

		copy(clipboard)
		press_and_release('ctrl+v')

	@staticmethod
	def start():

		wait()

if __name__ == '__main__':

	try:
		HOTKEY = 'ctrl+b'
		Changer(HOTKEY).start()
	except (KeyboardInterrupt, SystemExit):
		exit()
