import sys
from astar_nextstation import *
from UI_draw_train_path import DrawTrainPath
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class PathResultPage(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self,None)
        self.parent = parent
        self.init_path_result_page()

    def init_path_result_page(self):
        loader = QUiLoader()
        form = loader.load("UIDesign/result_page.ui")
        self.setCentralWidget(form)

        #train path widget
        self.train_path_label = form.findChild(QLabel,"train_path_label")
        self.train_path_label.setStyleSheet("QLabel { background-color :#F3F3F3;}")
        
        #self.path_grid_layout = form.findChild(QGridLayout,"path_grid_layout")
        self.path_vertical_layout = form.findChild(QVBoxLayout,"path_vertical_layout")
        
        #exit widget
        self.exit_label = form.findChild(QLabel, "exit_label")
        self.exit_label.setStyleSheet("QLabel { background-color :#F3F3F3;}")
       
        self.traveling_time_label = form.findChild(QLabel, "traveling_time_label")
        self.arrival_time_label = form.findChild(QLabel, "arrival_time_label")
        
        self.exit_scroll_area = form.findChild(QScrollArea, "exit_scroll_area")
        self.exit_scroll_area.setStyleSheet("QScrollArea { background-color :#F3F3F3;}")

        self.back_button = form.findChild(QPushButton, "backBtn")
        self.back_button.setText("Try Again")
        self.back_button.setStyleSheet("QPushButton{color:white;background-color:#EB6553; font-size:24px}")
        self.connect(self.back_button, SIGNAL("clicked()"), lambda page = 0: self.parent.changePage(page))

        #place widget
        self.place_scroll_area = form.findChild(QScrollArea, "place_scroll_area")
        self.place_scroll_area.setStyleSheet("QScrollArea { background-color:white; height:0px; width:0px}")

        self.line_input_one = form.findChild(QLineEdit,"lineEditOne")
        self.line_input_two = form.findChild(QLineEdit, "lineEditTwo")

        
        
        self.blur_bg_label = form.findChild(QLabel,"blur_bg_label")
        self.blur_bg_label.setVisible(False)

        pixmap_blur_pic = QPixmap("UIDesign/UIBackground/BlurResultPageUI.png")
        self.blur_bg_label.setPixmap(pixmap_blur_pic)
        


                
    def printTwo(self):
        self.parent.changePage(1)

    def updateGUI(self, result):
        self.parent.clearLayout(self.path_vertical_layout)
        
        ## train_path widget ##
        self.path_vertical_layout.addWidget(DrawTrainPath(result))


        ## exit widget ##
                
        # traveling
        mins_secs = result[1].split(".")
        
        traveling_time = " " + mins_secs[0] + " mins" 
        self.traveling_time_label.setText(traveling_time)
        self.traveling_time_label.setStyleSheet("QLabel{color: #4B4C51;font-size: 72px}")
        
        # arrival
        sum_mins = (int(self.parent.time[2]) + int(mins_secs[0]))

        if(sum_mins >= 60):
             arrival_hour = int(self.parent.time[1]) + sum_mins/60
             arrival_minute = sum_mins - ((sum_mins/60) * 60)
             if(arrival_minute < 10):
                 arrival_minute = "0" + str(arrival_minute)
        else:
            arrival_hour = self.parent.time[1]
            if(sum_mins >= 10):
                arrival_minute = sum_mins
            else:
                arrival_minute = "0" + str(sum_mins)

        if(arrival_hour == 24):
            arrival_hour = "00"
        arrival_time = "   arrival time " + str(arrival_hour) + ":" + str(arrival_minute)

        self.arrival_time_label.setText(arrival_time)
        self.arrival_time_label.setStyleSheet("QLabel{color: #4B4C51;}")


        # show exit
        exit_list = result[5]

        exit_widget = QWidget()
        main_exit_layout = QVBoxLayout()

        for i in range(len(exit_list)):
            HLayout = QHBoxLayout()
            exit_no = QLabel("  " + str(i))
            exit_no.setStyleSheet("QLabel{font-size:48px;font:bold;color: #8F8E8B}")

            VLayout = QVBoxLayout()
            transportation_list = exit_list[i].split(",")
            
            for n in transportation_list:
                exit_way = QLabel(n)
                exit_way.setStyleSheet("QLabel{color: #8F8E8B; font-size:15px}")
                VLayout.addWidget(exit_way)
                
            

            
            HLayout.addWidget(exit_no)
            HLayout.addLayout(VLayout)

            tempWidget = QFrame()
            tempWidget.setLayout(HLayout)
            tempWidget.setStyleSheet("QFrame{background-color:#ffffff}")
            main_exit_layout.addWidget(tempWidget)
            #main_exit_layout.addLayout(HLayout)

        exit_widget.setLayout(main_exit_layout)
        self.exit_scroll_area.setWidget(exit_widget)
            

        ## place widget ##
        place_list = result[6]

        widget = QWidget()
        widget.setStyleSheet("background-color: #F3F3F3")
        main_place_layout = QHBoxLayout()
        
        for n in place_list:
            place_button = QPushButton()
            self.connect(place_button, SIGNAL("clicked()"), lambda place_name = n: self.showDialogBox(place_name))
            place_details = self.parent.user_request(["place_details", n])
            place_button.setStyleSheet("QPushButton{border-image:url(\"" + place_details[1] + ".png\"); width:312px; height:180px;} QPushButton:hover{border-image:url(\"" + place_details[1] + "_2.png\"); width:312px; height:180px;}")

            layout = QVBoxLayout()
            layout.addWidget(place_button)
            main_place_layout.addLayout(layout)

            #layout = QVBoxLayout()
            #layout.addWidget(place_button)
            #frame = QFrame()
            #frame.setLayout(layout)
            #frame.resize(310,180)
            #main_place_layout.addWidget(frame)
            main_place_layout.addLayout(layout)
            
        widget.setLayout(main_place_layout)
        self.place_scroll_area.setWidget(widget)
            

    def showDialogBox(self, place_name):
        ## show error in form of dialog box ##
        self.blur_bg_label.setVisible(True)
        
        result = self.parent.user_request(["place_details", place_name])

        self.dialogBox = QDialog(self)
        self.dialogBox.setMinimumSize(730, 730)
        
        layout = QVBoxLayout()

        loader = QUiLoader()
        dialogForm = loader.load("UIDesign/place_detail_dialog_box.ui")
        layout.addWidget(dialogForm)


        self.place_name_label = dialogForm.findChild(QLabel, "place_name_label")
        self.place_name_label.setText(result[0])
        
        self.place_pic_label = dialogForm.findChild(QLabel, "place_picture_label")
        self.place_pic_label.setStyleSheet("QLabel{border-image:url(\"" + result[1] + "\"); width:312px; height:180px;}")

        self.place_detail_label = dialogForm.findChild(QLabel, "place_detail_label")
        self.place_detail_label.setText(result[2])

        self.place_address_label = dialogForm.findChild(QLabel, "place_address_label")
        self.place_address_label.setText(result[3])
        
        self.close_button = dialogForm.findChild(QPushButton, "close_button")
        self.close_button.clicked.connect(self.closeKub)

        self.dialogBox.setLayout(layout)
        self.dialogBox.show()

    def closeKub(self):
        self.blur_bg_label.setVisible(False)
        self.dialogBox.close()

     
'''
def main():
    app = QApplication(sys.argv)

    w = PathResultPage()
    w.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
'''

