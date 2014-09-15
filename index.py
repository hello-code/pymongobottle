import bottle
import pymongo
import guestbookDAO

connection_string="mongodb://localhost"
connection=pymongo.MongoClient(connection_string)
database=connection.names
guestbook=guestbookDAO.GuestbookDAO(database)

@bottle.route('/')
def guestbook_index():
    mynames_list=guestbook.find_names()
    return bottle.template('index',dict(mynames=mynames_list))

@bottle.route('/newguest',method='POST')
def insert_newguest():
    name=bottle.request.forms.get("name")
    email=bottle.request.forms.get("email")
    guestbook.insert_name(name,email)
    bottle.redirect('/')


bottle.debug(True)
bottle.run(host='localhost',port=8080)
