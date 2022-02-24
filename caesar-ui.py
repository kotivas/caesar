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
        self.combobox.addItems(languages) # добавления языков
        self.combobox.currentIndexChanged.connect(self.exec)

        self.show()

    def indent_butt(self): # если отступ неизвестен, то переменная indent переходит в позицию False, иначе True
        global indent_is_known

        if indent_is_known==True:
            indent_is_known = False

        else:
            indent_is_known = True

        self.exec() # вызов функции exec

    def exec(self):
        indent = self.spin.value() # получение отступа
        text = self.textin.toPlainText().lower() # получения текста для шифрования/дешифрования
        language = self.combobox.currentText() # получения языка
        self.spin.setReadOnly(not indent_is_known) # если отступ неизвестен, блокируется спинбокс для выбора отступа

        language = (language[0] + language[1]).lower()# установка значения переменной lang, понятное для функции caesar.encrypt()
              
        self.spin.setMaximum(len(caesar.alphabets[caesar.languages.index(language)])) # изменение максимального/минимального числа для спинбокса, в зависимости от длины алфавита
        self.spin.setMinimum(len(caesar.alphabets[caesar.languages.index(language)]) * -1)
        
        if indent_is_known==True: # если отступ известен, функция выполняется 1 раз
            out = caesar.encrypt(language, indent, text) 
        else: # если отступ незивестен, функция выполняется [ДЛИНА АЛФАВИТА ЯЗЫКА] раз
            out = ''
            for i in range(0, len(caesar.alphabets[caesar.languages.index(language)])):
                out += f"ROT {i * -1}: " + caesar.encrypt(language, i * -1, text) + "\n"

        self.textout.setPlainText(out) # вывод шифрованого/дешифрованого текста


if __name__ == "__main__":
    # простой графический интерфейс для шифрования цезаря
    
    indent_is_known = True # по умолчанию отступ известен
    languages = ['English','Russian'] # языки


    app = QtWidgets.QApplication(argv)
    window = Ui()

    app.exec_()

