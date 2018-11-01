import sys
import time

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from UI_start_page import *
from UI_result_page import *
from UI_routing_page import *

from NextStation_Controller import *


class UI_Manager(QMainWindow):

    def __init__(self, parent = None):
        #init attribute
        self.time = "null"
        
        QMainWindow.__init__(self, None) #init

        #set up main UI
        self.setMinimumSize(1680,900)
        self.setMaximumSize(1680,900)
        self.parent = parent
        self.setWindowTitle("NextStation")
        
        QApplication.setStyle(QStyleFactory.create("Plastique"))
        
        #add background img
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("UIDesign/UIBackground/StartPageUI.png")))
        self.setPalette(palette)
        

        #create stackedwidget + show first page
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        start_page_widget = StartPage(self)
        self.central_widget.addWidget(start_page_widget)


        #add widget
        self.start_page = StartPage(self)
        self.routing_page = RoutingPage(self)
        self.result_page = PathResultPage(self)
            
        #set central widget
        self.central_widget.addWidget(self.start_page)
        self.central_widget.addWidget(self.routing_page)
        self.central_widget.addWidget(self.result_page)

        #create page library
        self.page_list = [self.start_page, self.routing_page, self.result_page]
        self.page_background = [QPixmap("UIDesign/UIBackground/StartPageUI.png"),
                                QPixmap("UIDesign/UIBackground/RoutePageUI.png"),
                                QPixmap("UIDesign/UIBackground/ResultPageUI.png")]


    def user_request(self, request):
        if(request[0] == "astar_time"): # request["astar_time",from,to]
            if(self.time == "null"):
                day = time.strftime("%a") 
                hour, mins = time.strftime("%H:%M").split(':')
                self.time = [day,hour,mins]
                
            result = getShortestPath(request[1],request[2],self.time) # path, cost, train, row, col, exit, place
         
            
            #change page
            self.routing_page.clear()
            self.result_page.updateGUI(result)
            self.changePage(2)

        if(request[0] == "place_details"): # request["place_details", place_name]
            result = getPlaceDetails(request[1])

            return result
            
        
    def changePage(self, page):

        #change page's background
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(self.page_background[page]))
        self.setPalette(palette)

        self.start_page.updateGUI()
        self.centralWidget().setCurrentWidget(self.page_list[page]) 


    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clearLayout(child.layout())
                
    def getColor(self, train):
        if(train == "bts_sukhumvit_line"):
            return "QPushButton{border-image:url("+"UIDesign/StationIcon/su0.png"+") }QPushButton:hover{border-image:url("+"UIDesign/StationIcon/su1.png"+") }"
        elif(train == "bts_silom_line"):
            return "QPushButton{border-image:url("+"UIDesign/StationIcon/si0.png"+") }QPushButton:hover{border-image:url("+"UIDesign/StationIcon/si1.png"+") }"
        elif(train == "mrt_blue_line"):
            return "QPushButton{border-image:url("+"UIDesign/StationIcon/m0.png"+") }QPushButton:hover{border-image:url("+"UIDesign/StationIcon/m1.png"+") }"
        elif(train == "mrt_purple_line"):
            return "QPushButton{border-image:url("+"UIDesign/StationIcon/p0.png"+") }QPushButton:hover{border-image:url("+"UIDesign/StationIcon/p1.png"+") }"
        elif(train == "airlink"):
            return "QPushButton{border-image:url("+"UIDesign/StationIcon/a0.png"+") }QPushButton:hover{border-image:url("+"UIDesign/StationIcon/a1.png"+") }"
        else:
            return "pink"
        


def main():
        app = QApplication(sys.argv)

        w = UI_Manager()
        w.show()
        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())
