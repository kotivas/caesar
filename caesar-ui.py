#by kotivas
#PyQt5

try: # проверка на наличие PyQt5
    from PyQt5 import QtWidgets, uic
except ImportError: 
    print("Requires PyQt5 to run \npip install PyQt5")
    exit()

from sys import argv
import caesar

class Ui(QtWidgets.QMainWindow):
    def __init__(self): # Инициализация окна
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        self.setWindowTitle("Caesar cipher") # изменение заголовка

        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton') # Инициализация кнопки [?], если нажата, то выполняется функция indent_butt
        self.button.clicked.connect(self.indent_butt)
        
        self.spin = self.findChild(QtWidgets.QSpinBox, 'spinBox') # Инициализация спинбокса, если число в нём изменено, то выполняется функция exec
        self.spin.valueChanged.connect(self.exec)

        self.textin = self.findChild(QtWidgets.QTextEdit, 'textEdit_2') # Инициализация поля для входа, если текст в нём изменён, то выполняется функция exec
        self.textin.textChanged.connect(self.exec)

        self.textout = self.findChild(QtWidgets.QTextEdit, 'textEdit') # инициилизация поля вывода

        self.combobox = self.findChild(QtWidgets.QComboBox, 'comboBox') # Инициализация поле для выбора языка, если язык изменён, то выполняется функция exec
        self.combobox.currentIndexChanged.connect(self.exec)

        self.show()

    def indent_butt(self): # если отступ неизвестен, то переменная indent переходит в позицию False, иначе True
        global indent

        if indent==True:
            indent = False

        else:
            indent = True

        self.exec() # вызов функции exec

    def exec(self):
        ind = self.spin.value() # получение отступа
        txt = self.textin.toPlainText().lower() # получения текста для шифрования/дешифрования
        lang = self.combobox.currentText() # получения языка
        self.spin.setReadOnly(not indent) # если отступ неизвестен, блокируется спинбокс для выбора отступа

        if lang=="English": # установка значения переменной lang, понятное для функции caesar.encrypt()
            lang = 0
        elif lang=="Русский":
            lang = 1
              
        self.spin.setMaximum(len(caesar.lang[lang])) # изменение максимального/минимального числа для спинбокса, в зависимости от длины алфавита
        self.spin.setMinimum(len(caesar.lang[lang]) * -1)

        if indent==True: # если отступ известен, функция выполняется 1 раз
            out = caesar.encrypt(caesar.lang[lang], ind, txt) 
        else: # если отступ незивестен, функция выполняется [ДЛИНА АЛФАВИТА ЯЗЫКА] раз
            out = ''
            for i in range(0, len(caesar.lang[lang])):
                out += f"ROT {i * -1}: " + caesar.encrypt(caesar.lang[lang], i * -1, txt) + "\n"

        self.textout.setPlainText(out) # вывод шифрованого/дешифрованого текста


if __name__ == "__main__":
    # простой графический интерфейс для шифрования цезаря

    app = QtWidgets.QApplication(argv)
    window = Ui()
    
    indent = True # по умолчанию отступ известен

    app.exec_()

