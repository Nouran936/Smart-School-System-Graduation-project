from PySide6.QtWidgets import QApplication
from SchoolFinal1.frontPage import MySideBar
import sys
app = QApplication(sys.argv)
window = MySideBar()
window.show()
app.exec()
