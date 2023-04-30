#Front end (placement of all buttons, background etc. Designed with the help of figma),  designed by Atmanand, 
#Back end designed(binding all buttons, designing program and logic)  by Akarsh , akarshs.malvekar@gmail.com 
import sqlite3
import textwrap
from pathlib import Path
from random import randint
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

font = 'Quicksand'

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/aken/Assets/Technical quize/Quiz round 3/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#setting window parameters 
window = Tk()
window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")


# extracting the data from database and putting it in dictionary 
conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('SELECT category, question, answer FROM Table1')

rows = c.fetchall()

data = {'CategoryAndHint': [], 'question': [], 'answer': []}

# Loop over the rows and append the values to the corresponding list in the dictionary
for row in rows:
    data['CategoryAndHint'].append(row[0])
    data['question'].append(row[1])
    data['answer'].append(row[2])



#String variable 
Q_N =0 # Question number
Q = StringVar()
A = StringVar()
C_H = StringVar()
R_T = StringVar()
Current_Q = StringVar()
#These flags are meant to restrict the flow in only one direction, eg:- the answer will be only revealed when the question is displayed 
#Category, Question and Answer flag
c_flag, q_flag, a_flag = 0, 0, 0
displayed_questions = [] #to keep tack of displayed questions 


# To pick up questions randomly without repeating 
def pick_question_number():
    global displayed_questions
    flag = True
    while flag:
        N = randint(0, 27)
        if N not in displayed_questions:
            displayed_questions.append(N)
            flag = False
        elif len(displayed_questions)==20:
            exit()
    return N

#prevents overflowing of strings outside the box 
def str_fltr(St, wid):

    b = textwrap.wrap(St, placeholder='\n', width=wid)
    str = ''
    for i in range(len(b)):
        str = str + b[i] + '\n'

    return str



def next_category():
    global Q_N, C_H, c_flag, Current_Q, displayed_questions
    print('question number', Q_N)
    
    # next category will be displayed only if the question and answer is displayed 
    if c_flag==a_flag:
        Current_Q.set('Q'+str(len(displayed_questions)+1))
        Q_N = pick_question_number()
        cat_hin = data['CategoryAndHint'][Q_N]
        
        #The length was selected using trial and error method
        if len(cat_hin) > 65:
            cat_hin = str_fltr(cat_hin, 65)
            
        print(cat_hin)
        C_H.set(cat_hin)

        entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
        entry_1 = canvas.create_image(
            959.5,
            269.5,
            image=entry_image_1
        )
        entry_1 = Label(
            bd=0, textvariable=C_H,
            bg="#4BC073", font=(font, 30),
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=342.0,
            y=219.0,
            width=1235.0,
            height=99.0
        )
        c_flag += 1

        #the following functions removes the previous question and answer from the boxes
        reveal_question(True)
        reveal_answer(True)


def reveal_question(destroy=False):

    global Q_N, Q, q_flag
    question = data['question'][Q_N]

    # The length was selected using trial and error method 
    if len(question) > 78:
        question = str_fltr(question, 78)

    #To reset the question box
    if destroy==True:
        Q.set('')

    elif (c_flag > q_flag) and destroy==False:
        print('in reveal question c', c_flag, 'q', q_flag, destroy)
        Q.set(question)
        entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            956.0,
            497.0,
            image=entry_image_2
        )
        entry_2 = Label(
            bd=0,
            bg="#47509C", textvariable=Q,font=(font, 28),
            fg="white",
            highlightthickness=0
        )
        entry_2.place(
            x=149.0,
            y=364.0,
            width=1614.0,
            height=264.0
        )
        q_flag += 1


def reveal_answer(destroy=False):
    global Q_N, A, a_flag
    font_size = 28
    answer = data['answer'][Q_N]

    # The string length was selected using trial and error method
    if len(answer)>40:
        answer = str_fltr(answer, 50)
        print('more than 20')
        font_size = 17
    print(answer)
    
    
    #to reset the answer box
    if destroy==True:
        A.set('')

    elif a_flag < q_flag and destroy==False:
        A.set(answer)
        print('in reveal question a', a_flag, 'q', q_flag, destroy)
        entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
        entry_3 = canvas.create_image(
            957.0,
            727.5,
            image=entry_image_3
        )
        entry_3 = Label(
            bd=0, textvariable=A,font=(font, font_size),
            bg="#A0EA66",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=606.0,
            y=697.0,
            width=702.0,
            height=79.0
        )
        a_flag += 1


def random_team():
    t = StringVar()
    team = 'Team:' + str(randint(1, 5))
    t.set(team)
    entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        1085.5,
        1001.5,
        image=entry_image_4
    )
    entry_4 = Label(
        bd=0, textvariable=t, font=("DejaVu Serif", 30),   
        bg="#66D7F0",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=936.0,
        y=950.0,
        width=299.0,
        height=59.0
    )



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    960.0,
    540.0,
    image=image_image_1
)

canvas.create_text(
    785.0,
    93.0,
    anchor="nw",
    text="GAMBLING",
    fill="#000000",
    font=("Inter", 64 * -1)
)

canvas.create_text(
    868.0,
    54.0,
    anchor="nw",
    text="Third Round",
    fill="#000000",
    font=("Inter", 32 * -1)
)





# Next catagory button 
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1_ = Button(
    image=button_image_1,
    borderwidth=5, bd=5,
    highlightthickness=0,
    command=next_category,
    text='button1',
    relief="flat"
).place(
    x=238.0,
    y=792.0,
    width=301.0,
    height=82.0
)

#Reveal Question button 
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0, bd=5,
    highlightthickness=5, 
    command=reveal_question,
    relief="flat"
)
button_2.place(
    x=809.0,
    y=792.0,
    width=301.0,
    height=82.0
)

#Reveal Answer button 
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=5, bd=5,
    highlightthickness=0,
    command=reveal_answer,
    relief="flat"
)
button_3.place(
    x=1380.0,
    y=792.0,
    width=301.0,
    height=82.0
)

#Select Team 
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=5, bd=5,
    highlightthickness=0,
    command=random_team,
    relief="flat"
)
button_4.place(
    x=623.0,
    y=950.0,
    width=232.0,
    height=62.0
)


question_window = Label(
    bd=0, textvariable=Current_Q,
    bg="#C500FF", font=(font, 30),
    fg="#000716",
    highlightthickness=0
)
question_window.place(
    x=238.0,
    y=70,
    width=100.0,
    height=100.0
)

window.mainloop()
