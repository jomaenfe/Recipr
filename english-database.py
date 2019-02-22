import pyexcel as pe

from correspondences import get_correspondences

def process_english_db(fields_correspondences,filename = "bd-inglesa.xlsx"):

    ## Read the sheet (we need to specify the correct sheet of the book)
    sheet = pe.get_sheet(file_name=filename,sheet_name="Proximates")

    # Get field names
    row_names = sheet.row[0]
    n_fields = len(row_names)

    for i in range(n_fields):
        row_names[i] = fields_correspondences[row_names[i]]

    # Save all the changes
    sheet.row[0] = row_names
    sheet.save_as("processed-english-db.xlsx")

    pass


if __name__ == "__main__":
    fields_correspondences = get_correspondences()
    process_english_db(fields_correspondences)
