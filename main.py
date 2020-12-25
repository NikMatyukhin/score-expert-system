import sys
import wrapper

from PySide2 import QtWidgets


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)

    window = wrapper.ExpertSystemWrapper()
    window.show()

    sys.exit(application.exec_())
