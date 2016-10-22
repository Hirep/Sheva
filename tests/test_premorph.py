import unittest


import sys
from os import path
from os import listdir
from os.path import isfile, join

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )


text_path = path.dirname( path.abspath(__file__) )+"/test_texts"
allfiles = [f for f in listdir(text_path) if isfile(join(text_path, f))]
# print(allfiles)

from components import premorph


class TestRegularExpressions(unittest.TestCase):

	def test_reg_sentence(self):
		pass

	def test_eng_sentence(self):
		pass

	def test_num_sentence(self):
		pass

	def test_abbr_sentence(self):
		pass


class TestGenerateResponsse(unittest.TestCase):
	# Generate response foe large text 
	# from folder @test_texts
	# to folder @generated_text_response
	
	def test_reg_sentence(self):
		pass

	def test_eng_sentence(self):
		pass

	def test_num_sentence(self):
		pass

	def test_abbr_sentence(self):
		pass

if __name__ == '__main__':
    unittest.main()
