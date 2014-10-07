import sys, os
import sqlite3

if not os.path.exists(r"D:\GOOGLEDRIVE\Google Drive\Code\pre_post"):
    app_path	= r"/Users/alij/GoogleDrive/Code/pre_post"
else:
    app_path = r"D:\GOOGLEDRIVE\Google Drive\Code\pre_post"

app_dir = "APP_DATA"
db_name = "db_note.db"

#If the data base directory not found make one
if not os.path.exists(os.path.join(app_path, app_dir)):
    print "The Data Base Directory was not found\nCreating the in the following location\n--> {0} <--".format(
        os.path.join(app_path, app_dir))
    os.mkdir(os.path.join(app_path, app_dir))

########################################################################
class DataBaseManagement(object):
    """This object creates and handle the Project Note data"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""

        super(DataBaseManagement, self).__init__()
        #Data base path
        self.dbPath = os.path.join(app_path, app_dir, db_name)
    #---> End __init__

    #----------------------------------------------------------------------
    def __connect__(self):
        """Create the connection to data base"""
        self.dbConnect = sqlite3.connect(self.dbPath)
        self.db = self.dbConnect.cursor()
        #Initial data base
        self.db.execute('''CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMERY KEY,
        subject TEXT, description TEXT, waning TEXT, scenname TEXT, date TEXT, time TEXT, software TEXT, user TEXT, tag TEXT, image TEXT, project TEXT)''')

        self.lastID = self.db.execute('SELECT max(id) FROM note').fetchone()[0]
        if not self.lastID:
            self.lastID = 0
    #---> End __connect__

    #----------------------------------------------------------------------
    def add_to_database(self, subject, description, wanrings, scename, date, times, software, user, tag, image, project):
        """Insert a roz of data into the data base"""
        try:
            self.__connect__()    #Connect to data base
            values = (self.lastID + 1, subject, description, wanrings, scename, date, times, software, user, tag, image, project,)
            self.db.execute('INSERT INTO note VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', values)
            self.dbConnect.commit()    #Save it
        except Exception, e:
            print "Error while adding into the data base:\n", e
        finally:
            if self.dbConnect:
                self.dbConnect.close()    #Close the data base

    #end add_to_database
    #----------------------------------------------------------------------
    def read_database(self):
        """Pars and read the data base"""
        self.__connect__()    #Connect to data base
        retunData = []
        for row in self.db.execute('SELECT * FROM note'):
            retunData.append(row)
        self.dbConnect.close()        #Close the data base
        return retunData
        #end read_database

#end DataBaseManagement