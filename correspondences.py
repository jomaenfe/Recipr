import pyexcel as pe

fields_correspondences = {}

# values = ["food-name", "energy-kcal", "total-lipids-fats", "protein" ,"cholesterol",
# "carbohydrates", "starch"  , "sugars", "glucose", "galactose", "fructose", "maltose",
# "lactose", "retinol-equivalent", "retinol"   , "beta-carotene-equivalent", "vitamin-B1",
# "thiamin", "vitamin-B2", "riboflavin", "vitamin-C", "niacin", "vitamin-D", "vitamin-E",
#  "alpha-tocopherol", "vitamin-B12", "dietary-fibre-fiber", "water", "iron"  , "calcium",
#   "sodium", "potassium", "phosphorus"  , "zinc"  , "magnesium", "manganese", "copper"  ,
#    "saturated-fatty-acids","monounsaturated-fatty-acids","polyunsaturated-fatty-acids"]


def correspondences_greek_db(filename = "data/hhf-greece.gr.xlsx"):

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


def correspondences_english_db(filename = "data/bd-inglesa.xlsx"):

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



def correspondences_italian_db(filename="data/bd-italiana.xlsx"):

    ## Read the sheet
    sheet = pe.get_sheet(file_name=filename)
    row_names = sheet.row[1]

    # Firstly, we need a list with all the name fields we are going to use in order to
    # add the database information to "correspondences_values"

    correspondences_values = ["food-code","food-name-ita", "food-name-eng","scientific-name","food-category",
    "edible-part","energy-kj","energy-fibre-kj","energy-kcal","energy-fibre-kcal", "total-protein-g",
    "animal-protein-g","vegetable-proteing-g","total-fat-g",
    "animal-fat-g","vegetable-fat-g","cholesterol-mg","available-carbohydrates-g", "starch-g",
    "soluble-carbohydrates-g", "dietary-total-fibre-g", "alcohol-g","water-g","iron-mg","calcium-mg","sodium-mg","potassium-,mg",
    "phosphorus-mg",
    "zinc-mg", "magnesium-mg","cupper-mg","selenium-ug", "chloride-mg","iodine-ug","manganese-mg","suphur-mg",
    "vitamin-b1-thiamin-mg", "vitamin-b2-riboflavin-mg", "vitamin-c","niacin-mg","vitamin-b6-mg","total-folate-ug",
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




def correspondences_german_db(filename = "data/bd-alemana.xlsx"):

    ## Read the sheet
    sheet = pe.get_sheet(file_name=filename)
    row_names = sheet.row[2]

    # Firstly, we need a list with all the name fields we are going to use in order to
    # add the database information to "correspondences_values"

    # Vitamine - Vitamins: values per 100g -> has  always"werge pro 100g"
    # Kalorien - Calories: values per 100g -> has  always"werge pro 100g"
    # Mineralstoffe - Minerals: values per 100g -> has  always"werge pro 100g"
    # Spurenelemente - Trace elements: -> has  always"werge pro 100g"
    # Kohlenhydrate - Carbohydrates: -> has  always"werge pro 100g"
    # Ballaststoffe - Dietary Fibres: -> has  always"werge pro 100g"
    # Aminosäuren - Amino acids: values per 100g-> has  always"werge pro 100g"
    # Fettsäuren - Fatty acids: values per 100g-> has  always"werge pro 100g"


    correspondences_values = ["food-name-ger", "food-name", "food-name-esp", "nutritional-values",
    "energy-kcal", "energy-kj", "fat-mg","carbohydrates-mg","protein-mg","salt-mg","dietary-fibre-mg",
    "minerals-mg","bread-units-BE","vitamins-per-100g", "vitamin-a-retinol-mg", "vitamin-a-beta-carotin-ug",
    "vitamin-e-alpha-tocopherol-equivalent-ug","vitamin-e-alpha-tocopherol-ug", "vitamin-b1-thiamin-ug",
    "vitamin-b2-riboflavin-ug","vitamin-b3-niacin.nicotinic-acid-ug", "vitamin-b3-equivalent-ug",
    "vitamin-b5-pantothenic-acid-ug","vitamin-b6-pyidoxine-ug","vitamin-b7-biotin-ug","vitamin-b9-total-folic-acid-ug",
    "vitamin-c-ascorbic-acid-ug","calories-per-100g", "energy-kcal", "energy-kj", "energy-including-fibre-kcal",
    "energy-including-fibre-kj","minerals-per-100g", "sodium-mg", "potassium-mg","calcium-mg",
    "magnesium-mg","phosphorus-mg","sulphur-mg","chloride-mg","trace-elements-per-100g", "iron-ug", "zink-ug",
    "copper-ug","manganese-ug","fluoride-ug","iodine-ug","carbohydrates-per-100g","glucose-mg",
    "fructose-mg", "monosaccharides-mg","sucrose-mg", "disaccharides-mg","sugar-mg","dietary-fibres-per-100g",
    "poly-pentoses-mg","poly-hexoses-mg","poly-uronic-mg","acid-cellulose-mg","lignin-mg",
    "water-soluble-dietary-fibres-mg", "water-insoluble-dietary-fibres-mg","amino-acids-per-100g",
    "isoleucine-mg","leucine-mg","lysine-mg", "methionine-mg","cysteine-mg", "phenylalanine-mg","tyrosine-mg",
    "threonine-mg","tryptophan-mg","valine-mg","arginine-mg","histidine-mg","essential-amino-acids-mg",
    "alanine-mg","aspartic-acid-mg","glutamic-acid-mg","glycine-mg","proline-mg","serine-mg",
    "nonessential-amino-acids-mg", "uric-acid-mg","purine-mg","fatty-acids-per-100g","dodecanoic-acid-lauric-acid-mg",
    "tetradecanoic-acid-myristic-acid-mg","hexadecanoic-acid-palmitic-acid-mg","octadecanoic-acid-stearic-acid-mg",
    "saturated-fatty-acids-mg","hexadecenoic-acid-palmitoleic-acid-mg","octadecenoic-acid-oleic-acid-mg",
    "monounsaturated-fatty-acids-mg","octadecadienoic-acid-linoleic-acid-mg","octadecatrienoic-acid-linolenic-acid-mg",
    "polyunsaturated-fatty-acids-mg","long-chain-fatty-acids-mg","omega-3-fatty-acids-mg",
    "omega-6-fatty-acids-mg","glycering-lipoids-mg","starch-mg","polysaccharides-mg","cobalamin-ug",
    "mannitol-mg","sorbitol-mg","sugar-alcohols-mg","galactose-mg","maltose-mg","oligosaccharides-absorbable-mg",
    "oligosaccharides-non-absorbable-mg", "heptadecanoic-acid-mg","eicosanoic-acid-araquinic-acid-mg",
    "vitamin-a-retinol-mg","vitamin-d-calciferols-mg","hexanoic-acid-caproic-acid-mg","decanoic-acid-capric-acid-mg",
    "pentadecanoic-acid-mg","decosanoic-acid-behenic-acid-mg","tetracosanoic-acid-lignoceric-acid-mg",
    "tetradecenoic-acid-mg","eicosene-acid-mg","decosene-acid-erucaic-acid-mg","octradecatetraenoic-acid-stearidonic-acid-mg",
    "eicosadienoic-acid-mg", "eicosatrienoic-acid-mg", "eicosatetraenoic-acid-arachidonic-acid-mg",
    "eicosapentaenoic-aic-mg","docosatetraenoic-acid-mg","docosapentaenoic-acid-mg","docosahexaenoic-acid-mg",
    "short-chain-fatty-acids-mg","medium-chain-fatty-acids-mg","cholesterol-mg",
    "lactose-mg","butanoic-acid-butyric-acid-mg","octanoic-acid-caprylic-acid-mg","pentadecenoic-acid-mg",
    "heptadecenoic-acid-mg","glycogen-mg","Tetracosenoic-acid-nervonic-acid-mg","nonadecatrienoic-acid-mg",
    "xylitol-mg", "hexadecadienoic-acid-mg", "Docosadienoic-acid-mg","docosatrienoic-acid-mg","hexadecatetraenoic-acid-mg"]

    for i,name in enumerate(row_names):
        fields_correspondences[name] = correspondences_values[i]

    pass

    # for i in fields_correspondences.keys():
    #     print(i)


def get_correspondences(greek_db = "data/hhf-greece.gr.xlsx", english_db = "data/bd-inglesa.xlsx",
italian_db = "data/bd-italiana.xlsx" ,german_db = "data/bd-alemana.xlsx"):

    correspondences_greek_db(greek_db)
    correspondences_english_db(english_db)
    correspondences_italian_db(italian_db)
    correspondences_german_db(german_db)
    # call the other databases to complete correspondences.....
    return fields_correspondences



d = get_correspondences()
# for i in d.keys():
#     print(i+","+d[i])



all_values = open("values.md",'w')
all_values.write("# List of name fields\n")
for key in sorted(d.keys()):
    # print( d[key])
    all_values.write("- "+d[key]+"\n")

all_values.close()
