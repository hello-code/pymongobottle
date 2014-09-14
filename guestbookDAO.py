import string

class GuestbookDAO(object):
    def __init__(self,database):
        self.db=database
        self.mynames=database.mynames

    def find_names(self):
        l=[]
        for each_name in self.mynames.find():
            l.append({'name':each_name['name'],'email':each_name['email']})
        return l

    def insert_name(self,newname,newemail):
        newname={'name':newname,'email':newemail}
        self.mynames.insert(newname)
