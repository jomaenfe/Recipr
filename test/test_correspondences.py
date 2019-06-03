# -*- coding: utf-8 -*-
import unittest
import pyexcel as pe


from src import correspondences as correp
from src import english_database as en_db
from src import italian_database as it_db
from src import german_database as ger_db
from src import spanish_database as es_db
from src import english_database as en_db
#from src import greek_database as gk_db


class correspondencesTestCase(unittest.TestCase):

    def setUp(self):

        # we open the sheets
        # we get the hash table with correspondences
        self.fields_correspondences = correp.get_correspondences()
        pass


    def tearDown(self):
        pass


    def test_english_db(self):


        en_db.process_english_db(self.fields_correspondences)
        english_db_to_test = pe.get_sheet(file_name="data/processed-english-db.xlsx")
        new_row_names = english_db_to_test.row[0]


        # Check first and last name fields
        self.assertEqual(new_row_names[0], "food-code", "The content of the fields doesn't match")
        self.assertEqual(new_row_names[-1], "cholesterol-mg", "The content of the fields doesn't match")
        pass

    def test_german_db(self):

        ger_db.process_german_db(self.fields_correspondences)
        german_db_to_test = pe.get_sheet(file_name="data/processed-german-db.xlsx")
        new_row_names = german_db_to_test.row[2]

        # Check first and last name fields
        self.assertEqual(new_row_names[0], "food-name-ger", "The content of the fields doesn't match")
        self.assertEqual(new_row_names[-1], "hexadecatetraenoic-acid-mg", "The content of the fields doesn't match")
        pass

    # def test_greek_db(self):
    #
    #     # old_row_names = greek_example_sheet.row[1]
    #
    #     process_greek_db(self.fields_correspondences)
    #     greek_db_to_test = pe.get_sheet(file_name="data/processed-greek-db.xlsx")
    #     new_row_names = greek_db_to_test.row[0]
    #
    #     # Check first and last name fields
    #     self.assertEqual(new_row_names[0], "food-name", "The content of the fields doesn't match")
    #     self.assertEqual(new_row_names[-1], "copper-mg", "The content of the fields doesn't match")
    #
    #
    #     pass

    def test_italian_db(self):

        it_db.process_italian_db(self.fields_correspondences)
        italian_db_to_test = pe.get_sheet(file_name="data/processed-italian-db.xlsx")
        new_row_names = italian_db_to_test.row[1]

        # Check first and last name fields
        self.assertEqual(new_row_names[0], "food-code", "The content of the fields doesn't match")
        self.assertEqual(new_row_names[-1], "lactose-g", "The content of the fields doesn't match")
        pass


    def test_spanish_db(self):

        es_db.process_spanish_db(self.fields_correspondences)
        spanish_db_to_test = pe.get_sheet(file_name="data/processed-spanish-db.xlsx")
        new_row_names = spanish_db_to_test.row[0]

        # Check first and last name fields
        self.assertEqual(new_row_names[0], "id_alimento", "The content of the fields doesn't match")
        self.assertEqual(new_row_names[-1], "fecha_creado", "The content of the fields doesn't match")
        pass
