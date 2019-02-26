import unittest
import pyexcel as pe

from correspondences import get_correspondences
from english_database import process_english_db
from german_database import process_german_db
from italian_database import process_italian_db
from greek_database import process_greek_db


class correspondencesTestCase(unittest.TestCase):

    def setUp(self):

        # we open the sheets
        # we get the hash table with correspondences
        self.fields_correspondences = get_correspondences()
        pass


    def tearDown(self):
        pass


    def test_english_db(self):


        process_english_db(self.fields_correspondences)
        english_db_to_test = pe.get_sheet(file_name="processed-english-db.xlsx")
        new_row_names = english_db_to_test.row[0]


        # Check first and last name fields
        self.assertEqual(new_row_names[0], "food-code", "The content of the fields doesn't match")
        self.assertEqual(new_row_names[-1], "cholesterol-mg", "The content of the fields doesn't match")
        pass

    def test_german_db(self):

        process_german_db(self.fields_correspondences)
        german_db_to_test = pe.get_sheet(file_name="processed-german-db.xlsx")
        new_row_names = german_db_to_test.row[2]

        # Check first and last name fields
        self.assertEqual(new_row_names[0], "food-name-ger", "The content of the fields doesn't match")
        self.assertEqual(new_row_names[-1], "hexadecatetraenoic-acid-mg", "The content of the fields doesn't match")
        pass

    def test_greek_db(self):

        # old_row_names = greek_example_sheet.row[1]

        process_greek_db(self.fields_correspondences)
        greek_db_to_test = pe.get_sheet(file_name="processed-greek-db.xlsx")
        new_row_names = greek_db_to_test.row[0]

        # Check first and last name fields
        self.assertEqual(new_row_names[0], "food-name", "The content of the fields doesn't match")
        self.assertEqual(new_row_names[-1], "copper-mg", "The content of the fields doesn't match")


        pass

    def test_italian_db(self):

        process_italian_db(self.fields_correspondences)
        italian_db_to_test = pe.get_sheet(file_name="processed-italian-db.xlsx")
        new_row_names = italian_db_to_test.row[1]

        # Check first and last name fields
        self.assertEqual(new_row_names[0], "food-code", "The content of the fields doesn't match")
        self.assertEqual(new_row_names[-1], "lactose-g", "The content of the fields doesn't match")
        pass




# Testear que las columnas no estén vacías



# Testear que solo sea una palabra
