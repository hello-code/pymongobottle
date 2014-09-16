import string
from bson.objectid import ObjectId # delete use id

class GuestbookDAO(object):
    def __init__(self,database):
        self.db=database
        self.mynames=database.mynames

    def find_names(self):
        l=[]
        for each_name in self.mynames.find():
            l.append({'id':each_name['_id'],'name':each_name['name'],'email':each_name['email']})
        return l

    def count_names(self):
        return self.mynames.count() # return a number

    def insert_name(self,newname,newemail):
        newname={'name':newname,'email':newemail}
        self.mynames.insert(newname)

    def delete_names(self,id):
        id={'_id':ObjectId(id)}
        self.mynames.remove(id)
