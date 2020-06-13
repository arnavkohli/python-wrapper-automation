import os
import json

'''
	- Functionality to add UA for user
	- Indent by spaces or tabs option
'''


class PyFileWriter:

	def __init__(self, file):
		self.file = file

	def write(self, lines):

		with open(self.file, 'w') as f:
			for line in lines:
				f.write(f"{line}\n")
			f.close()

class PyProgrammer:
	modules = [
		'os',
		'json',
		'requests'
	]
	default_indentation = 'space'

	@classmethod
	def get_modules_to_import(cls):
		return cls.modules

	@classmethod
	def its_a_string(cls, value):
		return f"'{value}'"

	@classmethod
	def get_class_variables(cls, extractions):
		base_url = f"{extractions.get('PROTOCOL')}://{extractions.get('HOST')}/"
		if extractions.get('COMMON', None):
			base_url += f"{extractions.get('COMMON')}/"

		headers = extractions.get('HEADERS')

		return {
			"base_url" : cls.its_a_string(base_url),
			"headers" : headers
		}

	@classmethod
	def indent(cls, code, level=1):
		if cls.default_indentation == 'space':
			indentation = '    '
		else:
			indentation = '	'
		return f"{indentation * level}{code}"

	@classmethod
	def to_proper_case(cls, value):
		if value == None or value.strip() == '':
			return ''
		if len(value) > 1:
			return value[0].upper() + value[1:].lower()
		return value[0].upper()

	@classmethod
	def function_name_from_endpoint(cls, ep):
		comps = [comp for comp in ep.split('/') if comp != '']
		if len(comps) > 1:
			return ''.join([comps[0].lower()] + [cls.to_proper_case(comp) for comp in comps[1:]])
		return comps[0].lower()

	@classmethod
	def code_request_method(cls, endpoint, type):
		lines = []
		function_name = cls.function_name_from_endpoint(endpoint)

		# add decorator
		lines.append(cls.indent(f"@classmethod"))

		# add function
		lines.append(cls.indent(f"def {function_name}(cls, **kwargs):"))

		# construct URL
		lines.append(cls.indent(f"url = cls.BASE_URL + {cls.its_a_string(endpoint)}" , 2))

		# call url
		lines.append(cls.indent(f"response = requests.{type.lower()}(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))", 2))

		# return response
		lines.append(cls.indent(f"return response", 2))

		return lines


	@classmethod
	def code_the_wrapper(cls, extractions):
		LINES = []

		# Importing modules
		LINES += [f"import {module}" for module in cls.get_modules_to_import()]

		# Adding space
		LINES += ['\n']

		# Creating wrapper class
		LINES += ['class MyWrapper:']

		# Adding space
		LINES += ['\n']

		# Add class variables
		LINES += [cls.indent(f"{key.upper()} = {value}") for key, value in cls.get_class_variables(extractions).items()]

		# Add request methods
		for ep in EXTRACTIONS['REQUESTS']['GET']:
			# Adding space
			LINES += ['\n']
			LINES += cls.code_request_method(ep, type='GET')

		for ep in EXTRACTIONS['REQUESTS']['POST']:
			# Adding space
			LINES += ['\n']
			LINES += cls.code_request_method(ep, type='POST')

		for ep in EXTRACTIONS['REQUESTS']['DELETE']:
			# Adding space
			LINES += ['\n']
			LINES += cls.code_request_method(ep, type='DELETE')

		for ep in EXTRACTIONS['REQUESTS']['PUT']:
			# Adding space
			LINES += ['\n']
			LINES += cls.code_request_method(ep, type='PUT')



		return LINES




if __name__ == '__main__':
	file_name = 'mera_wrapper.py'
	EXTRACTIONS = json.loads(open('./wrapper-config.json', 'r').read())


	writer = PyFileWriter(os.path.join(os.path.abspath(os.getcwd()), file_name))

	writer.write(PyProgrammer.code_the_wrapper(EXTRACTIONS))



