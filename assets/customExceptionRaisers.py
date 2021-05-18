import inspect

from attr import s
def checkType(value, *types):
	if any(map(lambda x: isinstance(value, x), types)):
		return

	stringfied_types = ''.join([repr(x)[7:-1] + ' or ' for x in types])[:-3]
	stringfied_value = str(type(value))[7:-1]

	raise ValueError(f'Value type: {stringfied_value} should belong to: {stringfied_types}')

def checkSameType(value1, value2):
	if type(value1) != type(value2):
		stringfied_value1 = str(type(value1))[7:-1]
		stringfied_value2 = str(type(value2))[7:-1]
		raise TypeError(f'Variables of different type {stringfied_value1} and {stringfied_value2}')
