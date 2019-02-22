import pyexcel as pe

fields_correspondences = {}

# values = ["food-name", "energy-kcal", "total-lipids-fats", "protein" ,"cholesterol",
# "carbohydrates", "starch"  , "sugars", "glucose", "galactose", "fructose", "maltose",
# "lactose", "retinol-equivalent", "retinol"   , "beta-carotene-equivalent", "vitamin-B1",
# "thiamin", "vitamin-B2", "riboflavin", "vitamin-C", "niacin", "vitamin-D", "vitamin-E",
#  "alpha-tocopherol", "vitamin-B12", "dietary-fibre-fiber", "water", "iron"  , "calcium",
#   "sodium", "potassium", "phosphorus"  , "zinc"  , "magnesium", "manganese", "copper"  ,
#    "saturated-fatty-acids","monounsaturated-fatty-acids","polyunsaturated-fatty-acids"]


def process_greek_db(filename = "hhf-greece.gr.xlsx"):

    ## Read the sheet
    sheet = pe.get_sheet(file_name=filename)

    correspondences_values = ["food-name","energy-kcal", "protein-g", "total-lipids-fats-g",
    "saturated-fatty-acids-g", "monounsaturated-fatty-acids-g", "polyunsaturated-fatty-acids-g",
    "carbohydrates-g", "dietary-fibre-fiber-g", "water-g", "sodium-mg",  "potassium-mg", "calcium-mg",
     "magnesium-mg", "phosphorus-mg", "iron-mg", "zinc-mg","copper-mg"]
    # create dictionary

    # In the case of the greek database, we take into consideration all the fields
    # We discriminate row 0 (spanish name fields) and column 0 (spanish name of foods)
    del sheet.column[0]
    del sheet.row[0]

    # We are going to adapt name fields in order to unify with the other databases

    # Get field names
    row_names = sheet.row[0]
    # # Then we modify them
    row_names[0]="Food name" # we modify it because it is ' '


    for i,name in enumerate(row_names):
        fields_correspondences[name] = correspondences_values[i]


    pass


def process_english_db(filename = "bd-inglesa.xlsx"):

    ## Read the sheet
    sheet = pe.get_sheet(file_name=filename, sheet_name="Proximates")
    row_names = sheet.row[0]




    # Firstly, we need a list with all the name fields we are going to use in order to
    # add the database information to "correspondences_values"

    correspondences_values = ["food-code","food-name","description","group","previous",
    "main-data-references","footnote","water-g","total-nitrogen-g","protein-g",
    "fat-g","carbohydrate-g","energy-kcal","energy-kj","starch-g","oligosaccharide-g",
    "total-sugars-g","glucose-g","galactose-g","fructose-g","sucrose-g","maltose-g",
    "lactose-g","alcohol-g","nsp-g","aoac-fibre-g","satd-FA-per-100g-FA-g",
    "satd-FA-per-100g-fd-g","n-6-poly-per-100g-FA-g","n-6-poly-per-100g-food-g",
    "n-3-poly-per-100g-FA-g","n-3-poly-per-100g-food-g", "cis-mono-FA-per-100g-FA-g",
    "cis-mono-FA-per-100g-food-g","mono-FA-per-100g-FA-g","mono-FA-per-100g-food-g",
    "cis-poly-FA-per-100g-FA-g","cis-poly-FA-per-100g-food-g", "poly-FA-100g-FA-g",
    "poly-FA-per-100g-food-g","sat-FA-excl-br-per-100g-FA-g","sat-FA-excl-br-per-100g-food-g",
    "branched-chain-FA-per-100g-FA-g", "branched-chain-FA-per-100g-food-g",
    "trans-FAs-per-100g-FA-g", "trans-FAs-per-100g-food-g","cholesterol-mg"]

    for i,name in enumerate(row_names):
        # check if we already have the key value in the dict (we cant update
        # the actual value to any other different)
        # if name not in fields_correspondences.keys():
            # if the key exists, but the content its the same, we dont have to
            # worry about it. The problem is when we have same key different value
        fields_correspondences[name] = correspondences_values[i]
    pass



def process_italian_db(filename="bd-italiana.xlsx"):

    ## Read the sheet
    sheet = pe.get_sheet(file_name=filename)
    row_names = sheet.row[1]

    # Firstly, we need a list with all the name fields we are going to use in order to
    # add the database information to "correspondences_values"

    correspondences_values = ["food-code","food-name-ita", "food-name-eng","scientific-name","food-category",
    "edible-part","energy-kj","energy-fibre-kj","energy-kcal","energy-fibre-kcal", "total-protein-g",
    "animal-protein-g","vegetable-proteing-g","total-fat-g",
    "animal-fat-g","vegetable-fat-g","cholesterol-g","available-carbohydrates-g", "starch-g",
    "soluble--carbohydrates-g", "dietary-total-fibre-g", "alcohol-g","water-g","iron-mg","calcium-mg","sodium-mg","potassium-,mg",
    "phosphorus-mg",
    "zinc-mg", "magnesium-mg","cupper-mg","selenium-ug", "chloride-mg","iodine-ug","manganese-mg","suphur-mg",
    "vitamin-b1-thiamin-mg", "vitamin-b2-riboflavin-mg", "vitamin-c","niacin-mg","vitamin-b6","total-folate-ug",
    "pantotenic-acid-mg", "biotin-ug", "vitamin-b12-ug","retinol-equivalent-ug", "retinol-ug", "b-carotene-eq-ug",
    "vitamin-e-mg", "vitamin-d-ug", "vitamin-k-ug", "saturated-fatty-acids-g","butyric-caproic-caprylic-capric-acid-g",
    "lauric-acid-g", "myristic-acid-g", "palmitic-acid-g", "stearic-acid-g","arachidic-acid-g", "behenic-acid",
    "monounsaturated-fatty-acids-g", "myristoleic-acid-g", "palmitoleic-acid-g", "oleic-acid-g","eicosenic-acid-g",
    "erucic-acid-g","polyunsaturated-fatty-acids-g", "linoleic-acid-g", "linolenic-acid-g", "arachidonic-acid-g",
    "eicosapentaenoic-acid-g", "decosahexaenoic-acid-g", "other-polyunsaturated-fatty-acids-g", "tryptophan-mg",
    "threonine-mg", "isoleucine-mg","leucine-mg", "lysine-mg", "methionine-mg", "cystine-mg","phenilalanine-mg",
    "tyrosine-mg","valine-mg","arginine-mg","histidine-mg","alanine-mg","aspartic-acid-mg","glutamic-acid-mg",
    "glycine-mg", "proline-mg","serine-mg","glucose-g","fructose-g","galactose-g","saccarose-g","maltose-g","lactose-g"]

    for i,name in enumerate(row_names):
        fields_correspondences[name] = correspondences_values[i]

    pass

def get_correspondences():
    process_greek_db()
    process_english_db()
    process_italian_db()
    # call the other databases to complete correspondences.....
    return fields_correspondences



d = get_correspondences()
# for i in d.keys():
#     print(i+","+d[i])
