import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
"""
窗口的setWindowIcon方法用于设置窗口的图标，只在Windows中可用
QApplication中的setWindowIcon方法用于设置主窗口的图标和应用程序图标，但调用了窗口的setWindowIcon方法
QApplication中的setWindowIcon方法就只能设置应用程序图标
"""

class IconForm(QMainWindow):
    def __init__(self, parent = None):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 250)
        # 设置主窗口标题
        self.setWindowTitle("设置窗口图标")
        # 设置窗口图标
        self.setWindowIcon(QIcon('./logo.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon('./logo.ico'))
    main = IconForm()
    main.show()

    sys.exit(app.exec_())