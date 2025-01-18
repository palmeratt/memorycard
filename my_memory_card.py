from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton,  QPushButton, QLabel
from random import shuffle

class Question(): #создаем рандомайзейр
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup() #делаем группу
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_4 = QHBoxLayout()

layout_ans1 = QHBoxLayout() #создаем лейауты
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_4.addWidget(RadioGroupBox)
layout_5 = QHBoxLayout()
layout_5.addLayout(layout_4)


RadioGroup.setExclusive(False)
rbtn_1.setChecked(False)
rbtn_2.setChecked(False)
rbtn_3.setChecked(False)
rbtn_4.setChecked(False)
RadioGroup.setExclusive(True)

question_list = [] #пишем какие вопросы будут в тесте
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Французкий', 'Африканский'))
question_list.append(Question('Дата крещения Руси', '988', '1161', '812', '889'))
question_list.append(Question('В каком году вышел раст', '2013', '2019', '2017', '2012'))


bth_OK = QPushButton('Ответить')
lb_Question = QLabel('Вопрос сложный мазафака')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Вариант 1')
rbtn_1 = QRadioButton('Вариант 2')
rbtn_1 = QRadioButton('Вариант 3')
rbtn_1 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup() #делем еще 1 группу
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout() #еще лэйауты
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) #панель с вариантами ответов

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('тру ор нот') #надпись правльно или нет
Lb_Correct = QLabel('ответ тут') #ответ будет написан тут

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Lb_Correct, alignment=Qt.AlignHCenter, stretch=2) #растянули ответ

layout_line1 = QHBoxLayout() #вопрос
layout_line2 = QHBoxLayout() #варианты ответов
layout_line3 = QHBoxLayout() # кнопка ответить

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() #прячем панель с ответом

layout_line3.addStretch(1)
layout_line3.addWidget(bth_OK, stretch=2) #большая кнопка
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) #пробелы

def show_result():
    ''' покаать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    bth_OK.setText('Следующий вопрос')

def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    bth_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    Lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if bth_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.cur_question = -1

bth_OK.clicked.connect(click_OK)

next_question()
window.resize(400, 300)
window.show()
app.exec_()

