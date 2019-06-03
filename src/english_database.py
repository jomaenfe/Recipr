import pyexcel as pe


from src import correspondences as correp

def process_english_db(fields_correspondences,filename = "data/bd-inglesa.xlsx"):

    ## Read the sheet (we need to specify the correct sheet of the book)
    sheet = pe.get_sheet(file_name=filename,sheet_name="Proximates")

    # Get field names
    row_names = sheet.row[0]
    n_fields = len(row_names)

    for i in range(n_fields):
        row_names[i] = fields_correspondences[row_names[i]]

    # Save all the changes
    sheet.row[0] = row_names
    sheet.save_as("data/processed-english-db.xlsx")

    pass


if __name__ == "__main__":
    fields_correspondences = correp.get_correspondences()
    process_english_db(fields_correspondences)
