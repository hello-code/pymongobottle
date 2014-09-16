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
    mynames_count=guestbook.count_names()
    return bottle.template('index',dict(mynames=mynames_list,count=mynames_count))

@bottle.route('/newguest',method='POST')
def insert_newguest():
    name=bottle.request.forms.get("name")
    email=bottle.request.forms.get("email")
    guestbook.insert_name(name,email)
    bottle.redirect('/')

@bottle.route('/delete/:id',method='POST')
def delete_guest(id):
    guestbook.delete_names(id)
    #bottle.redirect('/')        # since ansyn so not working

bottle.debug(True)
bottle.run(host='localhost',port=8080)
