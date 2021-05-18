import sys, os, pytest
sys.path.insert(1, os.getcwd())
from assets import Polynomial, checkType, checkSameType
import numpy as np


def test_checkType():

	# One type
	value = 'carlito'
	types = (int,)

	stringfied_types = ''.join([repr(x)[7:-1] + ' or ' for x in types])[:-3]
	stringfied_value = repr(type(value))[7:-1]

	with pytest.raises(ValueError, match =  f'Value type: {stringfied_value} should belong to: {stringfied_types}'):
		checkType(value, types[0])

	# Two types
	value = 'carlito'
	types = (int, float)

	stringfied_types = ''.join([repr(x)[7:-1] + ' or ' for x in types])[:-3]
	stringfied_value = repr(type(value))[7:-1]

	with pytest.raises(ValueError, match =  f'Value type: {stringfied_value} should belong to: {stringfied_types}'):
		checkType(value, *types)

	# External types
	value = 'carlito'
	types = (np.double, Polynomial)

	stringfied_types = ''.join([repr(x)[7:-1] + ' or ' for x in types])[:-3]
	stringfied_value = str(type(value))[7:-1]

	with pytest.raises(ValueError, match =  f'Value type: {stringfied_value} should belong to: {stringfied_types}'):
		checkType(value, *types)
	

def test_checkSameType():
	value1 = 'carlito'
	value2 = 0

	stringfied_value1 = repr(type(value1))[7:-1]
	stringfied_value2 = repr(type(value2))[7:-1]

	with pytest.raises(TypeError, match = f'Variables of different type {stringfied_value1} and {stringfied_value2}'):
		checkSameType(value1, value2)


