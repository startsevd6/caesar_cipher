def cipher_direction():
	while True:
		print('Выберите направление (шифрование или дешифрование):')
		s = input().lower()
		if s[0] == 'ш' or s[0] == 'д':
			return s[0]
		else:
			print('Вы должны ввести "шифрование" или "дешифрование"')


def language():
	while True:
		print('Выберите язык (русский или английский):')
		s = input().lower()
		if s[0] == 'р' or s[0] == 'а':
			return s[0]
		else:
			print('Вы должны ввести "русский" или "английский"')


def shear_step(lang_ru_en):
	while True:
		print('Выберите шаг сдвига:')
		n = input()
		if n.isdigit():
			n = int(n)
			if lang_ru_en == 'р':
				if 0 < n < 32:
					return n
				else:
					if n <= 0:
						print('Шаг сдвига не может быть меньше 0')
					elif n >= 32:
						print('Шаг сдвига не может быть больше 32 в русском языке')
			if lang_ru_en == 'а':
				if 0 < n < 26:
					return n
				else:
					if n <= 0:
						print('Шаг сдвига не может быть меньше 0')
					elif n >= 26:
						print('Шаг сдвига не может быть больше 26 в английском')
		else:
			print('Вы должны ввести число')


def string_query():
	while True:
		print('Введите строку которую будем шифровать:')
		s = input()
		if s != '':
			return s
		else:
			print('Вы должны ввести строку для шифровки')


def encryption(dir_c, langs, ss):
	s = string_query()
	initial_shear_step = ss
	minsn, maxsn = 0, 0
	for i in range(len(s)):
		sn = ord(s[i])
		ss = initial_shear_step

		if langs == 'а':
			if 65 <= sn <= 90:
				minsn, maxsn = 65, 90
			elif 97 <= sn <= 122:
				minsn, maxsn = 97, 122
			else:
				continue
		elif langs == 'р':
			if 1040 <= sn <= 1071:
				minsn, maxsn = 1040, 1071
			elif 1072 <= sn <= 1103:
				minsn, maxsn = 1072, 1103
			else:
				continue
		step_lang = maxsn - minsn + 1

		if dir_c == 'ш':
			if sn + ss > maxsn:
				ss -= step_lang
			sn += ss
		elif dir_c == 'д':
			if sn - ss < minsn:
				ss -= step_lang
			sn -= ss
		if i == 0:
			s = chr(sn) + s[i + 1:]
		elif 0 < i < len(s) - 1:
			s = s[:i] + chr(sn) + s[i + 1:]
		elif i == len(s) - 1:
			s = s[:i] + chr(sn)

	print('Зашифрованная строка: ' + s, end='\n\n')


while True:
	cipher_dir = cipher_direction()
	lang = language()
	shear_s = shear_step(lang)
	if cipher_dir == 'ш' or cipher_dir == 'д':
		encryption(cipher_dir, lang, shear_s)
	else:
		print('Направление шифрования не выбрано')
