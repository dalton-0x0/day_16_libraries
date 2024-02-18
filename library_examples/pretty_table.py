from prettytable import PrettyTable

# create a table, add rows all at once
table_1 = PrettyTable()

table_1.field_names = ["City Name", "Area", "Population", "Annual Rainfall"]
table_1.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)

# add one row to table_1
table_1.add_row(["Canberra", 1000, 201000, 300.0])

# change alignment
table_1.align['Annual Rainfall'] = "r"
table_1.align['Area'] = "r"
table_1.align['City Name'] = "l"
table_1.align['Population'] = "r"

print(table_1)

# create another table, add rows one after another
table_2 = PrettyTable()

table_2.add_column('Pokemon Name', ["Pikachu", "Squirtle", "Charmander"])
table_2.add_column('Pokemon Type', ["Electric", "Water", "Fire"])

# add multiple rows to table_2
table_2.add_rows([['Floette', 'Fairy'], ['Kakuna', 'Bug'], ['Golduck', 'Water']])

print(table_2)
