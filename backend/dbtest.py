import db
import api

mode = 2

if mode == 0:
    dbconn = db.DbHandler('test.db')

    #dbconn.add_user('Simong')
    dbconn.add_restriction('test restriction', 'allergy')

elif mode == 1:
    cmd = r'/usr/bin/tesseract'
    nutrition = api.read_label(cmd, 'juice.jpg')
    print(nutrition)

elif mode == 2:
    dbconn = db.DbHandler('test.db')

    #dbconn.add_user('Simong')
    dbconn.add_consumption(1, 'juice.jpg')
