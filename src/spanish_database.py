# -*- coding: utf-8 -*-
import pyexcel as pe


from src import correspondences as correp

# ------------------------------------------------------------------------------
def process_spanish_db(fields_correspondences,filename = "data/espanola.xlsx"):

    ## Read the sheet (we need to specify the correct sheet of the book)
    sheet = pe.get_sheet(file_name=filename)

    # Get field names
    row_names = sheet.row[0]
    # print(row_names)
    n_fields = len(row_names)

    for i in range(n_fields):
        row_names[i] = fields_correspondences[row_names[i]]

    # Save all the changes
    sheet.row[0] = row_names
    sheet.save_as("data/processed-spanish-db.xlsx")

    pass


# ------------------------------------------------------------------------------

if __name__ == "__main__":
    fields_correspondences = get_correspondences()
    process_greek_db(fields_correspondences)
