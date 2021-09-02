class Convert:

	ru_symbols = list('Ёёйцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХ/ЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"№;:?')
	en_symbols = list('~`qwertyuiop[]asdfghjkl;\'zxcvbnm,./QWERTYUIOP{|}ASDFGHJKL:"ZXCVBNM<>@#$%^&')

	@staticmethod
	def detect_layout(symbols):

		string_length = len(symbols)
		ru_percentage = en_percentage = 0

		for symbol in symbols:
			
			if symbol in Convert.ru_symbols:
				ru_percentage += 1 / string_length * 100
			elif symbol in Convert.en_symbols:
				en_percentage += 1 / string_length * 100

		return None if ru_percentage == en_percentage else ('ru' if ru_percentage > en_percentage else 'en')

	@staticmethod
	def convert_symbols(symbols):
		
		layout = Convert.detect_layout(symbols)

		if layout is None:
			return

		clipboard = ''

		for symbol in symbols:
			
			try:
				if layout == 'ru':
					clipboard += Convert.en_symbols[Convert.ru_symbols.index(symbol)]
				elif layout == 'en':
					clipboard += Convert.ru_symbols[Convert.en_symbols.index(symbol)]
			except ValueError:
				clipboard += symbol

		return clipboard
