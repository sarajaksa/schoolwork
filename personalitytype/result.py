import sys
from PyQt4 import QtGui, QtCore
from sklearn.externals import joblib


class PersonalityTypePredictor(QtGui.QWidget):

    def __init__(self):
        super(PersonalityTypePredictor, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(200, 200, 800, 400)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png')) 
        
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)
        
        self.title = QtGui.QLabel('Put the text below.')
        grid.addWidget(self.title, 1, 0)
        
        self.text_input = QtGui.QTextEdit()
        grid.addWidget(self.text_input, 2, 0)
        
        self.button = QtGui.QPushButton("Get your personality type")
        grid.addWidget(self.button, 7, 0)
        
        self.personality = QtGui.QLabel('Your personality type is: ')
        grid.addWidget(self.personality, 8, 0)
        
        self.model = joblib.load('finalmodel.pkl') 
        
        QtCore.QObject.connect(self.button, QtCore.SIGNAL('clicked()'), self.onClicked)      
    
        self.show()
        
    def onClicked(self):
        inputed_text = self.text_input.toPlainText()
        text = []
        text.append(str(inputed_text))
        predicted = self.model.predict(text)
        labelstring = 'Your personality type is: ' + predicted[0]
        self.personality.setText(labelstring)


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = PersonalityTypePredictor()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
