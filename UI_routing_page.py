import sys
#from astar_nextstation import *

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

#from test_name import*
from bt_station import*
from station import*

class RoutingPage(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self,None)
        self.parent = parent
        self.init_routing_page()
        self.click_check = ""
        self.station_name = all_dict()
        self.sender_from_station = self.sender()
        self.sender_to_station = self.sender()
        self.from_station = ""
        self.to_station = ""


    def init_routing_page(self):
        loader = QUiLoader()
        form = loader.load("UIDesign/routing_page.ui")
        self.setCentralWidget(form)


        ####################### set bt ##########################

        # set QPushButton

        self.from_bt = form.findChild(QPushButton, "from_bt")
        self.to_bt = form.findChild(QPushButton, "to_bt")

        self.route_bt = form.findChild(QPushButton, "route_bt")

        self.clear_bt = form.findChild(QPushButton, "clear_bt")
        self.clear_bt.setStyleSheet("QPushButton{border-image:url("+"UIDesign/StationIcon/refresh_button.png"+") }" + "QPushButton:hover{border-image:url("+"UIDesign/StationIcon/refresh_button_2.png"+") }")
        self.clear_bt.setEnabled(False)

        self.background_label = form.findChild(QLabel, "bg_label")
        self.background_label.setStyleSheet("QLabel{border-image:url("+"UIDesign/UIBackground/route_map.png"+")};")

        self.from_bt.setStyleSheet("QPushButton{color: "+"#ffffff"+"; background-color: "+"#0A1215"+"; font-size:32px; border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")
        self.to_bt.setStyleSheet("QPushButton{color: "+"#AFB2B7"+"; background-color: "+"#0A1215"+"; font-size:32px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")
        self.route_bt.setStyleSheet("QPushButton{color: "+"#AFB2B7"+"; background-color: "+"#0A1215"+"; font-size:48px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")



        ####################### connect bt ##########################

        # connect QPushButton
        #self.from_bt.clicked.connect(self.show_click)
        #self.to_bt.clicked.connect(self.show_click)
        self.route_bt.clicked.connect(self.route)

        self.clear_bt.clicked.connect(self.clear)

        ########### set Station Button


        for i in all_name():
            type_st = self.get_station_type(i)
            self.i = form.findChild(QPushButton, i)
            self.i.clicked.connect(self.station_click)
            self.i.setStyleSheet(self.getColor(type_st))


    ####################### fn ##########################


    def get_station_type(self,station):
        if(station in al_name()):
            return "airlink"
        elif(station in bts_g_name()):
            return "bts_silom_line"
        elif (station in bts_lg_name()):
            return "bts_sukhumvit_line"
        elif (station in mrt_p_name()):
            return "mrt_purple_line"
        elif (station in mrt_b_name()):
            return "mrt_blue_line"


    def getColor(self, train):
        if (train == "bts_sukhumvit_line"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/su0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/su1.png" + ") }"
        elif (train == "bts_silom_line"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/si0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/si1.png" + ") }"
        elif (train == "mrt_blue_line"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/m0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/m1.png" + ") }"
        elif (train == "mrt_purple_line"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/p0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/p1.png" + ") }"
        elif (train == "airlink"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/a0.png" + ") }QPushButton:hover{border-image:url(" + "UIDesign/StationIcon/a1.png" + ") }"
        else:
            return "pink"



    def route(self):
        if((self.from_station != "") and (self.to_station != "" )):
            request = ["astar_time",self.from_station,self.to_station]
            self.parent.user_request(request)


    def station_click_color(self,train):
        if (train == "bts_sukhumvit_line"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/su1.png" + ") }"
        elif (train == "bts_silom_line"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/si1.png" + ") }"
        elif (train == "mrt_blue_line"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/m1.png" + ") }"
        elif (train == "mrt_purple_line"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/p1.png" + ") }"
        elif (train == "airlink"):
            return "QPushButton{border-image:url(" + "UIDesign/StationIcon/a1.png" + ") }"
        else:
            return "pink"


    def station_click(self):
        if ((self.click_check == "") | (self.click_check == 0)):
            self.sender_from_station = self.sender()
            self.from_station = self.sender_from_station.objectName()

            type_st = self.get_station_type(self.from_station)
            self.sender().setStyleSheet(self.station_click_color(type_st))

            
            
            from_station_name = self.station_name[self.from_station]

            if(from_station_name == "Queen Sirkit National Covention Center"):
                from_station_name = "QSNCC"
            self.from_bt.setText("From: " + from_station_name)
            self.click_check = "from"
                
            self.from_bt.setStyleSheet("QPushButton{color: "+"#AFB2B7"+"; background-color: "+"#0A1215"+"; font-size:32px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")
            self.to_bt.setStyleSheet("QPushButton{color: "+"#ffffff"+"; background-color: "+"#0A1215"+"; font-size:32px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")
            self.route_bt.setStyleSheet("QPushButton{color: "+"#AFB2B7"+"; background-color: "+"#0A1215"+"; font-size:48px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")

            

        elif (self.click_check == "from"):
            
            
            self.sender_to_station = self.sender()
            self.to_station = self.sender_to_station.objectName()
            if(self.from_station != self.to_station):
                type_st = self.get_station_type(self.to_station)
                self.sender().setStyleSheet(self.station_click_color(type_st))

                to_station_name = self.station_name[self.to_station]
                if(to_station_name == "Queen Sirkit National Covention Center"):
                    to_station_name = "QSNCC"
                self.to_bt.setText("To: " + to_station_name)
                self.click_check = "to"

                self.from_bt.setStyleSheet("QPushButton{color: "+"#AFB2B7"+"; background-color: "+"#0A1215"+"; font-size:32px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")
                self.to_bt.setStyleSheet("QPushButton{color: "+"#AFB2B7"+"; background-color: "+"#0A1215"+"; font-size:32px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")
                self.route_bt.setStyleSheet("QPushButton{color: "+"#ffffff"+"; background-color: "+"#0A1215"+"; font-size:48px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")
                self.clear_bt.setEnabled(True)
            
            
    def clear(self):
        self.from_bt.setText("From")
        self.to_bt.setText("To")
        self.click_check = ""

        

        type_st_from = self.get_station_type(self.from_station)
        type_st_to = self.get_station_type(self.to_station)

        self.to_station = ""
        self.from_station = ""
        
        self.sender_from_station.setStyleSheet(self.getColor(type_st_from))
        self.sender_to_station.setStyleSheet(self.getColor(type_st_to))

        self.from_bt.setStyleSheet("QPushButton{color: "+"#ffffff"+"; background-color: "+"#0A1215"+"; font-size:32px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")
        self.to_bt.setStyleSheet("QPushButton{color: "+"#AFB2B7"+"; background-color: "+"#0A1215"+"; font-size:32px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")
        self.route_bt.setStyleSheet("QPushButton{color: "+"#AFB2B7"+"; background-color: "+"#0A1215"+"; font-size:48px;border-style: outset; border-width: 2px; border-color: "+"#12161C"+"}")

        self.clear_bt.setEnabled(False)
    
