import pytest
from dstk import matrix_ops

def test_oneHotEncode(data):
	data = ['hello', 'goodbye', 'hello', 'later']
	matrix = np.matrix([True, False, True, False], [False, True, False, False], [False, False, False, True])
	assert one_hot_encode(data) == matrix
	
