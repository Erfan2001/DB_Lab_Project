from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Datamodel(QAbstractTableModel):
    def __init__(self,data):
        super(Datamodel,self).__init__()
        self.data=data
        self.header=["Id","FirstName","LastName","Nation","Club","Post","Overall"]
    
    def headerData(self, section, orientation, role) :
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.header[section])
            return(section+1)
        
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.data[index.row()][index.column()]
        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

    def rowCount(self, index) :
        return len(self.data)

    def columnCount(self, index) :
        return len(self.data[0])
