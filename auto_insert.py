import csv

# function to automate insert_into
def insert_into(csv_file, table_name, final_file, sep=','):
    with open(csv_file, 'r') as fichier_csv :
        reader = csv.reader(fichier_csv, delimiter = sep)
        table_csv = list(reader)
        fields = table_csv[0]
        del table_csv[0]
        insert = "INSERT INTO " + table_name + " ("
        for field in fields:
            insert += field + ', '
        insert = insert[:-2]
        insert += ') VALUES \n'
        for row in table_csv:
            insert += '('
            for i in range(len(fields)):
                is_int = True
                try:
                    int(row[i])
                except ValueError:
                    try:
                        float(row[i])
                    except ValueError:
                        is_int = False
                    # is_int = False

                if not is_int: # if field[i] is not an id
                    new = row[i]
                    insert += "'"
                    if "'" in row[i]:
                        new = row[i].replace("'", "''")
                    insert += new + "'" + ', '
                else:
                    insert += row[i] + ', '
            insert = insert[:-2]
            insert += '),\n'
        insert = insert[:-2]
        insert += ';\n'
        with open(final_file, "a+") as output:
            output.write(insert)

# call the function
final_file = 'init.sql'
insert_into('tables-small/table_actors.csv', 'actors', final_file)
insert_into('tables-small/table_countries.csv', 'countries', final_file)
insert_into('tables-small/table_directors.csv', 'directors', final_file)
insert_into('tables-small/table_movies.csv', 'movies', final_file)
insert_into('tables-small/table_play.csv', 'play', final_file)
insert_into('tables-small/table_manage.csv', 'manage', final_file)
insert_into('tables-small/table_come_from.csv', 'come_from', final_file)
