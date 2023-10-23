import psycopg2 as ps

connection = ps.connect(dbname='testdb', host='127.0.0.1', port='5432', user='postgres', password='postgres')

cursor = connection.cursor()

# persons = [('Michael', 46), ('Jim', 28), ('Pam', 27)]
# cursor.executemany("INSERT INTO person (name, age) VALUES (%s, %s)", persons)
# connection.commit()

cursor.execute('SELECT * FROM person ORDER BY age DESC')
print('FETCHALL')
for person in cursor.fetchall():
    print(f'id:{person[0]}\t name:{person[1]}\t age:{person[2]}')

# print('FETCHMANY(2)')
# for person in cursor.fetchmany(2):
#     print(f'id:{person[0]}\t name:{person[1]}\t age:{person[2]}')
#
# print('FETCHMANY(1)')
# for person in cursor.fetchmany(1):
#     print(f'id:{person[0]}\t name:{person[1]}\t age:{person[2]}')
#
# print('FETCHONE')
# p_id, name, age = cursor.fetchone()
# print(f'name:{name}\t age:{age}')

cursor.close()
connection.close()
