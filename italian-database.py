import pyexcel as pe

from correspondences import get_correspondences

def process_english_db(fields_correspondences,filename = "bd-italiana.xlsx"):

    ## Read the sheet (we need to specify the correct sheet of the book)
    sheet = pe.get_sheet(file_name=filename)

    # Get field names
    row_names = sheet.row[1]
    n_fields = len(row_names)

    for i in range(n_fields):
        row_names[i] = fields_correspondences[row_names[i]]

    # Save all the changes
    sheet.row[1] = row_names
    sheet.save_as("processed-italian-db.xlsx")

    pass


if __name__ == "__main__":
    fields_correspondences = get_correspondences()
    process_english_db(fields_correspondences)
