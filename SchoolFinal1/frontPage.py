import os

import cv2
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, \
    QTableWidget, \
    QTableWidgetItem, QRadioButton, QCheckBox, QLabel, QHeaderView, QSizePolicy, QScrollArea, QStyledItemDelegate, \
    QMessageBox
# from PyQt6  QApplication,  QMenu, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, \
#     QTableWidgetItem, QRadioButton
from ui_June1 import Ui_MainWindow
from ViolenceRealTime import *
from ViolenceRealTime import DetectYacta
from PySide6.QtCore import Qt, QSize
from Display_Video import Display_Video
from StudentDialogJune1 import Ui_StudentsDialog


class ActionsWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set initial size of the main window
        layout = QHBoxLayout()
        self.update_button = QPushButton("")
        self.delete_button = QPushButton("")
        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        # Apply styling
        self.update_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #01e3b0;"
            "   border: none;"
            "   border-radius: 5px"
            "   color: #0e0d6a;"
            "   padding: 8px 12px;"
            "   text-align: center;"
            "   text-decoration: none;"
            "   display: inline-block;"
            "   font-size: 12px;"
            "   margin: 2px 2px;"
            "   cursor: pointer;"
            "}"
            # "QPushButton:hover {background-color: #45a049;}"
            # "QPushButton:pressed {background-color: #3e8e41;}"
        )

        self.delete_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #fe4f51;"
            "   border: none;"
            "   border-radius: 5px"
            "   color: #0e0d6a;"
            "   padding: 8px 12px;"
            "   text-align: center;"
            "   text-decoration: none;"
            "   display: inline-block;"
            "   font-size: 12px;"
            "   margin: 2px 2px;"
            "   cursor: pointer;"
            "}"
            # "QPushButton:hover {background-color: #45a049;}"
            # "QPushButton:pressed {background-color: #3e8e41;}"
        )

        # Adjust button sizes
        # self.update_button.setFixedSize(30, 30)
        # self.delete_button.setFixedSize(30, 30)

        # Set icon for update button and adjust size
        update_icon = QIcon("SchoolFinal1/Icons/pen.png")  # Path to update icon image
        update_icon_actual_size = update_icon.actualSize(QSize(20, 20))  # Adjust size as needed
        self.update_button.setIcon(update_icon)
        self.update_button.setIconSize(update_icon_actual_size)

        # Set icon for delete button and adjust size
        delete_icon = QIcon("SchoolFinal1/Icons/trash.png")  # Path to delete icon image
        delete_icon_actual_size = delete_icon.actualSize(QSize(20, 20))  # Adjust size as needed
        self.delete_button.setIcon(delete_icon)
        self.delete_button.setIconSize(delete_icon_actual_size)

        # Set fixed size for buttons
        self.update_button.setFixedSize(30, 30)
        self.delete_button.setFixedSize(30, 30)

        # # Create a scroll area
        # scroll_area = QScrollArea()
        # scroll_area.setWidgetResizable(True)
        #
        # # Create a widget to hold the stacked widget
        # stacked_widget_container = QWidget()
        # scroll_area.setWidget(stacked_widget_container)
        #
        # # Create a layout for the stacked widget container
        # stacked_layout = QVBoxLayout(stacked_widget_container)
        #
        # # Add the stacked widget to the container widget
        # stacked_widget_container.setLayout(stacked_layout)
        #
        # # Add the scroll area to the central widget
        # self.setCentralWidget(scroll_area)


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Smart School Management System")

        self.icon_text_widget.setHidden(True)

        # connect buttons to switch different pages
        self.home_1.clicked.connect(self.switch_to_home)
        self.home_2.clicked.connect(self.switch_to_home)

        self.students_1.clicked.connect(self.switch_to_students)
        self.students_2.clicked.connect(self.switch_to_students)

        self.classMonitoring_1.clicked.connect(self.switch_to_classMonitoring)
        self.classMonitoring_2.clicked.connect(self.switch_to_classMonitoring)

        self.attendance_monitoring_1.clicked.connect(self.switch_to_attendanceMonitoring)
        self.attendance_monitoring_2.clicked.connect(self.switch_to_attendanceMonitoring)

        self.attendance_1.clicked.connect(self.switch_to_attendance)
        self.dateEdit.dateChanged.connect(self.filterTableByDateAttendance)
        self.attendance_2.clicked.connect(self.switch_to_attendance)

        self.reports_1.clicked.connect(self.switch_to_reports)
        self.reports_2.clicked.connect(self.switch_to_reports)

        # self.reports_2.clicked.connect(self.change_text)

        # # connect buttons to respective context menus
        # self.students_1.clicked.connect(self.students_context_menu)

        # open student dialog
        self.addStudent_button.clicked.connect(self.open_addStudent_dialog)


        # display_video button
        self.addStudent_button_2.clicked.connect(self.display_video)


        # # Connect loadData function to show students page
        # self.stackedWidget.currentChanged.connect(self.on_page_changed)

        # set the default page to home
        self.switch_to_home()



    def display_video(self):
        if self.selected_video_path:
            Display_Video(self.selected_video_path)
        else:
            print("Please select a video to display.")

    def loadData(self):
        import SQLServerDoWork
        students =SQLServerDoWork.diplayAllStudents()

        # Clear existing data
        self.studentInfo_table.clearContents()

        # Set the number of rows in the table to match the number of students
        self.studentInfo_table.setRowCount(len(students))

        # Populate the table with student information
        for row, student in enumerate(students):
            self.studentInfo_table.setItem(row, 0, QTableWidgetItem(str(student[1])))
            self.studentInfo_table.setItem(row, 1, QTableWidgetItem(str(student[0])))
            self.studentInfo_table.setItem(row, 2, QTableWidgetItem(str(student[2])))
            self.studentInfo_table.setItem(row, 3, QTableWidgetItem(str(student[3])))
            self.studentInfo_table.setItem(row, 4, QTableWidgetItem(str(student[4])))
            self.studentInfo_table.setItem(row, 5, QTableWidgetItem(str(student[5])))
            self.studentInfo_table.setItem(row, 6, QTableWidgetItem(str(student[6])))
            self.studentInfo_table.setItem(row, 7, QTableWidgetItem(str(student[7])))
            self.studentInfo_table.setItem(row, 8, QTableWidgetItem(str(student[8])))

            # Add buttons for update and delete
            #update_button = QPushButton("Update")
            #delete_button = QPushButton("Delete")

            # # Set the buttons in the last column of each row
            # self.studentInfo_table.setCellWidget(row, 9, update_button)
            # self.studentInfo_table.setCellWidget(row, 10, delete_button)
            # Add update and delete buttons
            actions_widget = ActionsWidget()
            self.studentInfo_table.setCellWidget(row, 9, actions_widget)

    def loadDataViolence(self):
        import SQLServerDoWork
        violence_videos =SQLServerDoWork.Diplay_Violence_Incidences()

        # Clear existing data
        self.violence_reoprts_table.clearContents()

        # Set the number of rows in the table to match the number of students
        self.violence_reoprts_table.setRowCount(len(violence_videos))
        self.violence_reoprts_table.setColumnCount(3)

        self.selected_video_path = None

        # Populate the table with student information
        for row, video in enumerate(violence_videos):
            self.violence_reoprts_table.setItem(row, 0, QTableWidgetItem(str(video[1])))
            self.violence_reoprts_table.setItem(row, 1, QTableWidgetItem(str(video[1])))

            # Create radio button for each row
            radio_button = QRadioButton()
            self.violence_reoprts_table.setCellWidget(row, 2, radio_button)
            radio_button = QRadioButton()
            radio_button.clicked.connect(lambda _, path=video[2]: self.set_selected_video(path))
            self.violence_reoprts_table.setCellWidget(row, 2, radio_button)

            # # Set the buttons in the last column of each row
            # self.studentInfo_table.setCellWidget(row, 9, update_button)
            # self.studentInfo_table.setCellWidget(row, 10, delete_button)
            # Add update and delete buttons

    def set_selected_video(self, video_path):
        self.selected_video_path = video_path

    # methods to switch different pages
    def switch_to_home(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_students(self):
        self.stackedWidget.setCurrentIndex(1)
        # Load data when switching to students page
        self.loadData()

    def switch_to_classMonitoring(self):
        DetectYacta()
        self.stackedWidget.setCurrentIndex(2)

    def loadDataAttendanceDeafult(self):
        import SQLServerDoWork
        attendance_Deafult_Date =SQLServerDoWork.showStudeentStatusWithoutDate()

        # Clear existing data
        self.studentInfo_table_2.clearContents()

        # Set the number of rows in the table to match the number of students
        self.studentInfo_table_2.setRowCount(len(attendance_Deafult_Date))
        self.studentInfo_table_2.setColumnCount(5)

        #self.selected_video_path = None

        # Populate the table with student information
        for row, video in enumerate(attendance_Deafult_Date):
            #s.id,s.name, sa.date,s.StClass
            self.studentInfo_table_2.setItem(row, 0, QTableWidgetItem(str(video[0])))
            self.studentInfo_table_2.setItem(row, 1, QTableWidgetItem(str(video[1])))
            self.studentInfo_table_2.setItem(row, 2, QTableWidgetItem(str(video[2])))
            self.studentInfo_table_2.setItem(row, 3, QTableWidgetItem(str(video[3])))
            Attendstatus="Attend"
            if video[2] != "None":
                Attendstatus = "Attend"
            else:
                Attendstatus = "Absent"
            self.studentInfo_table_2.setItem(row, 4, QTableWidgetItem(Attendstatus))



            #self.studentInfo_table_2.setItem(row, 4, QTableWidgetItem(str("hi")))

    def filterTableByDateAttendance(self, selected_date):
        selected_date_str = selected_date.toString("MM/dd/yyyy")  # Convert QDate to string format
        import SQLServerDoWork
        attendance_Deafult_Date = SQLServerDoWork.showStudeentStatus(selected_date_str)

        # Clear existing data
        self.studentInfo_table_2.clearContents()

        # Set the number of rows in the table to match the number of students
        self.studentInfo_table_2.setRowCount(len(attendance_Deafult_Date))
        self.studentInfo_table_2.setColumnCount(5)

        # self.selected_video_path = None

        # Populate the table with student information
        for row, video in enumerate(attendance_Deafult_Date):
            # s.id,s.name, sa.date,s.StClass
            self.studentInfo_table_2.setItem(row, 0, QTableWidgetItem(str(video[0])))
            self.studentInfo_table_2.setItem(row, 1, QTableWidgetItem(str(video[1])))
            self.studentInfo_table_2.setItem(row, 2, QTableWidgetItem(str(video[2])))
            self.studentInfo_table_2.setItem(row, 3, QTableWidgetItem(str(video[3])))
            Attendstatus = "Attend"
            if str(video[2]) != "None":
                Attendstatus = "Attend"
            else:
                Attendstatus = "Absent"
            self.studentInfo_table_2.setItem(row, 4, QTableWidgetItem(Attendstatus))

    def switch_to_attendanceMonitoring(self):
        self.stackedWidget.setCurrentIndex(3)
        import RealTime
        RealTime.FaceYacta()

    def switch_to_attendance(self):
        self.loadDataAttendanceDeafult()
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_reports(self):
        self.stackedWidget.setCurrentIndex(5)
        self.loadDataViolence()

        # Open dialog for inserting new students

    def open_addStudent_dialog(self):
        #from StudentDialog import Ui_StudentsDialog
        # instantiate and show the dialog
        addStudent_dialog = Ui_StudentsDialog(self)

        # Connect the clicked signal of the "Save" button to the uiAddStu method
        addStudent_dialog.saveStudent_Button.clicked.connect(lambda: self.uiAddStu(addStudent_dialog))

        addStudent_dialog.TakePhotobtn.clicked.connect(lambda: self.OnClickAddFromCamera(addStudent_dialog))

        addStudent_dialog.uploadPhotobtn.clicked.connect(lambda: self.UploadFromPC(addStudent_dialog))

        result = addStudent_dialog.exec()  # This will block until the dialog is closed


    def uiAddStu(self, addStudent_dialog):
        name = addStudent_dialog.name_lineEdit.text()
        gender = addStudent_dialog.gender_comboBox.currentText()
        class_ = addStudent_dialog.class_comboBox.currentText()
        dob = addStudent_dialog.dob_dateEdit.date().toString(Qt.ISODate)
        address = addStudent_dialog.address_lineEdit.text()
        phone = addStudent_dialog.phone_lineEdit.text()
        email = addStudent_dialog.email_lineEdit.text()
        id = addStudent_dialog.name_lineEdit_2.text()
        Age = addStudent_dialog.name_lineEdit_3.text()

        # Perform validation
        if not name or not gender or not class_ or not dob or not address or not phone or not email:
            # Display message indicating invalid input
            QMessageBox.warning(self, "Invalid Input", "Please fill in all fields.")
            return

        # Proceed with saving the student data
        import SQLServerDoWork
        SQLServerDoWork.AddStudent(id, name, gender, class_, dob, Age, address, phone, email)
        self.loadData()



    def OnClickAddFromCamera(self,TakePhoto):
        import Add_photo_from_camrea
        id = TakePhoto.name_lineEdit_2.text()
        name = TakePhoto.name_lineEdit.text()
        if not name or not id :
            # Display message indicating invalid input
            QMessageBox.warning(self, "Invalid Input", "Please fill in all fields.")
            return
        FolderName= f'CameraPhotos/{name}'
        #print(FolderName)
        self.create_folder(FolderName)
        Add_photo_from_camrea.open_camera(id,0,name)

    def UploadFromPC(self, TakePhoto):
        import Add_photo_static
        id = TakePhoto.name_lineEdit_2.text()
        name = TakePhoto.name_lineEdit.text()
        if not name or not id:
            # Display message indicating invalid input
            QMessageBox.warning(self, "Invalid Input", "Please fill in all fields.")
            return
        FolderName = f'CameraPhotos/{name}'
        # print(FolderName)
        self.create_folder(FolderName)
        for i in range(1,6):
            Add_photo_static.select_and_save_image(FolderName,i,id)

    def create_folder(self,path):
        try:
            # Create the directory, including any necessary intermediate directories
            os.makedirs(path, exist_ok=True)
            print(f"Folder '{path}' created successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

