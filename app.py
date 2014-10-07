__author__ = 'alij'

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys, os, webbrowser, platform
from ui import about_UI, pre_post_main_v02_UI, submit_note_v02_UI, selectedInfo_v01_UI
from lib import db_management

########################################################################
class PrePostMain(QtGui.QMainWindow, pre_post_main_v02_UI.Ui_mainWindow):
    """
    Main window of the Pre/Post Tool
    """
    #----------------------------------------------------------------------
    def __init__(self, parent=None):
        """
        Constructing the Post-Post main window
        """
        super(PrePostMain,self).__init__(parent)
        self.setupUi(self)
        # Setting up the Signals
        self.__setup_signals()
        # Connect to data base
        self.connect_to_db = db_management.DataBaseManagement()
        # Populating the table from the data base
        self.__populate_table()
    #---> End __init__

    #----------------------------------------------------------------------
    def __setup_signals(self):
        """
        Setting up the Signals
        """
        self.actionNew_Note.triggered.connect(self.new_note_action_triggered)
        self.actionUpdate_Note.triggered.connect(self.update_db_action_triggered)
        self.actionWiki.triggered.connect(self.wiki_action_triggered)
        self.actionRemove_Note.triggered.connect(self.remove_note_action_triggered)
        self.actionExport.triggered.connect(self.export_action_triggered)
        self.actionImport.triggered.connect(self.import_action_triggered)
        self.actionAbout.triggered.connect(self.about_action_triggered)
        self.mainTable.cellDoubleClicked.connect(self.note_double_clicked)
    #---> End __setup_signals

    #----------------------------------------------------------------------
    def note_double_clicked(self):
        self.selectedItem = self.mainTable.selectedItems()[0].text()
        info = SelectedInfoWindow(parent=self)
        info.textBrowser.append(self.selectedItem)
        info.show()
        print self.selectedItem
    #---> End note_double_clicked

    #----------------------------------------------------------------------
    def __populate_table(self):
        """Parse the date from the data base and fill in the tables"""
        for k in reversed(range(self.mainTable.rowCount())):
            self.mainTable.removeRow(k)
        self.noteList 	= [self.connect_to_db.read_database()]
        for dataRow in self.noteList:
            for j in dataRow:
                row = self.mainTable.rowCount()
                self.mainTable.setRowCount(row+ 1)
                for i in xrange(1,len(j)):
                    self.mainTable.setItem(row,i-1, QtGui.QTableWidgetItem(str(j[i])))
    #---> End __populate_table

    #----------------------------------------------------------------------
    def about_action_triggered(self):
        self.aboutWindow = AboutMain()
        self.aboutWindow.show()
    #---> End about_action_triggered

    #----------------------------------------------------------------------
    def import_action_triggered(self):
        '''
        '''
        pass
    #---> End import_action_triggered

    #----------------------------------------------------------------------
    def export_action_triggered(self):
        '''
        '''
        pass
    #---> End export_action_triggered

    #----------------------------------------------------------------------
    def new_note_action_triggered(self):

        """
        """

        self.new_notes_submission = SubmitNote(parent=self)
        self.new_notes_submission.cancelButton.clicked.connect(self.new_notes_submission.close)
        self.new_notes_submission.submitNoteButton.clicked.connect(self.add_note_to_db)
        self.new_notes_submission.show()
    #---> End new_note_action_triggered

    #----------------------------------------------------------------------
    def update_db_action_triggered(self):
        '''
        '''
        self.__populate_table()

    #---> End update_db_action_triggered

    #----------------------------------------------------------------------
    def wiki_action_triggered(self):

        '''
        '''
        webbrowser.open("http://alijafargholi.com")
    #---> End wiki_action_triggered

    #----------------------------------------------------------------------
    def remove_note_action_triggered(self):
        '''
        '''
        pass
    #---> End remove_note_action_triggered

    #----------------------------------------------------------------------
    def add_note_to_db(self):

        """
        """
        self.connect_to_db.add_to_database(str(self.new_notes_submission.subjectSpace.text()),
                                           str(self.new_notes_submission.descriptionSpace.toPlainText()),
                                           str(self.new_notes_submission.warningSpace.toPlainText()),
                                           str(self.new_notes_submission.sceneNameSpace.text()),
                                           str(self.new_notes_submission.dateSpace.text()),
                                           str(self.new_notes_submission.timeSpace.text()),
                                           str(self.new_notes_submission.softwareList.currentText()),
                                           str(self.new_notes_submission.userSpace.text()),
                                           str(self.new_notes_submission.tagSpace.text()),
                                           str("Images testing"),
                                           str(self.new_notes_submission.projectSpace.text()))
        # populating teh
        self.__populate_table()
        self.new_notes_submission.close()
    #---> End add_note_to_db
#---> End PrePostMain

########################################################################
class AboutMain(QtGui.QDialog, about_UI.Ui_Form):

    '''
    The About window
    '''
    #----------------------------------------------------------------------
    def __init__(self,parent=None):

        '''
        Constructing the About window
        '''

        super(AboutMain,self).__init__(parent)
        self.setupUi(self)

    #---> End __ini__
#---> End AboutMain

########################################################################
class SubmitNote(QtGui.QDialog, submit_note_v02_UI.Ui_Form):

    """
    Submit Note main window
    """
    #----------------------------------------------------------------------
    def __init__(self, parent=None):

        """
        Constructing the SubmitNote window
        """

        super(SubmitNote, self).__init__(parent)
        self.setupUi(self)
    #---> End __ini__
#---> End SubmitNote

########################################################################
class SelectedInfoWindow(QtGui.QDialog, selectedInfo_v01_UI.Ui_currentInfo):
    """
    """
    #----------------------------------------------------------------------
    def __init__(self, parent=None):
        super(SelectedInfoWindow,self).__init__(parent)
        self.setupUi(self)
    #---> End __ini__
#---> End SelectedInfoWindow

def main():
    """Create an instance of the Main Window"""
    QtCore.QCoreApplication.setApplicationName("Pre-Post")
    QtCore.QCoreApplication.setApplicationVersion("1.0")
    QtCore.QCoreApplication.setOrganizationName("Ali Jafargholi")
    QtCore.QCoreApplication.setOrganizationDomain("alijafargholi.com")

    app = QtGui.QApplication(sys.argv)
    win = PrePostMain()
    win.show()
    app.exec_()

#---> End main
if __name__ == "__main__":
    main()
