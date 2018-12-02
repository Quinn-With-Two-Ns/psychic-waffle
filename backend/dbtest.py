import db

dbconn = db.DbHandler('test.db')

#dbconn.add_user('Simong')
dbconn.add_restriction('test restriction', 'allergy')

