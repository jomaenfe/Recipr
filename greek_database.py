import pyexcel as pe

from correspondences import get_correspondences

# ------------------------------------------------------------------------------
def process_greek_db(fields_correspondences,filename = "hhf-greece.gr.xlsx"):

    ## Read the sheet
    sheet = pe.get_sheet(file_name=filename)

    # In the case of the greek database, we take into consideration all the fields
    # We discriminate row 0 (spanish name fields) and column 0 (spanish name of foods)
    del sheet.column[0]
    del sheet.row[0]

    # We are going to adapt name fields in order to unify with the other databases

    # Get field names
    row_names = sheet.row[0]
    # # Then we modify them
    row_names[0]="Food name" # we modify it because it is ' '

    n_fields = len(row_names)

    for i in range(n_fields):
        row_names[i] = fields_correspondences[row_names[i]]

    # Save all the changes
    sheet.row[0] = row_names
    sheet.save_as("processed-greek-db.xlsx")

    pass


# ------------------------------------------------------------------------------

if __name__ == "__main__":
    fields_correspondences = get_correspondences()
    process_greek_db(fields_correspondences)
