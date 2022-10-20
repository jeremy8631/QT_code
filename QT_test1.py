from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit
#导入相关的类 

app = QApplication([])#创建一个对象  作用事提供整个图形界面的管理

window = QMainWindow() #创建一个主窗口对象
window.resize(500, 400) #窗口大小 （宽度，高度）
window.move(300, 310) #控制窗口显示的时候出现在屏幕显示器的位置
window.setWindowTitle('薪资统计') #把薪资统计设置在标题栏上

textEdit = QPlainTextEdit(window) #创建纯文本空间
textEdit.setPlaceholderText("请输入薪资表")#创建提示文本
textEdit.move(10,25)#在窗口处位置  如果有副窗口就显示在副窗口位置
textEdit.resize(300,350) #指定大小

button = QPushButton('统计', window) #设置按键
button.move(380,80) #位置

window.show() #显示界面，想要显示就必须要执行这一段代码

app.exec_() #进入QApplication的事件处理循环  如果不加这句话，界面就会一闪而过 
