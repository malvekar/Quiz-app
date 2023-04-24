#Front end (placement of all buttons, background etc. Designed with the help of figma),  designed by Atmanand, 
#Back end designed(binding all buttons, designing program and logic)  by Akarsh , akarshs.malvekar@gmail.com 

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

#questions
data = {
    "CategoryAndHint": [
        "Sci-Fi - Has characters called Marty McFly & Emmett “Doc” Brown",
        "Tech - South Indian King",
        "Miscellaneous - Management",
        "Current Affairs - Original Name of an Island",
        "Fintech - No Brainer",
        "Logical Reasoning and Aptitude - Number Series",
        "Audio engineering - Audio codec",
        "CGI - Movies",
        "Chemical - Nobel Prize",
        "Space - The Solar System",
        "Software - Worm",
        "Automobile - Baby Steps",
        "Biomedical - Imaging",
        "Pure Science - Biology",
        "Sci-Fi - Agent J and Agent K to action",
        "Tech - OpenPOWER",
        "Miscellaneous - History in Tech",
        "Current Affairs - When Technology is accused of Racism",
        "Fintech - Indian Village",
        "Logical Reasoning and Aptitude - Solving a Crime",
        "Audio engineering - R.I.P Freddie Mercury",
        "CGI - Animation",
        "Chemical - Principles of Chemistry",
        "Space - Satellites of Earth",
        "Software - Mind your language!",
        "Automobile - Brand",
        "Biomedical - 'They did SURGERY on a GRAPE!'",
        "Pure Science - Microbiology"
    ],
    "question": [
        "What kind of car is the time machine made from in Back To The Future?",
        "This Indian King first time used the iron casted rockets in 1792 against the war with the British. Considered as the pioneer of rocket artillery, Identify the King.",
        "Today, the 10th of November is celebrated as World Science Day for Peace and Development. This year’s theme for its celebration is a management principle for meeting human development goals while also preserving nature and its resources. What is the theme??",
        "On 4th Sept 2015 an island in the state of Odisha was named after the late Indian President Dr APJ Abdul Kalam. What was the original name of the island?",
        "In 1972 Abraham Bettinger coined a term in his book 'FINTECH: A series of 40 time shared Models Used at Manufacturers Hanover Trust Company'.What was the term?  ",
        "Look at this series: 12, 11, 13, 12, 14, 13, … What number should come next?",
        "What does mp3 stand for?",
        "'CGI Is the Future', which movie was MOST important to the widespread use of CGI technology?",
        "This German chemist who received the Nobel Prize is credited for a method which is used to synthesize ammonia from nitrogen gas and hydrogen gas. He weaponized chlorine during world war 1. Name the invention for which he got the Nobel prize.",
        "Which planet is covered by clouds of sulphuric acid?",
        "In 2022 people had been emailed with the words 'I Love You'.What is the name of the worm?",
        "ABC of manual cars? ",
        "What is the 'M' in MRI?",
        "The camera shutter controls the amount of light entering the camera for image capture. What part of the human eye parallels this operation? ",
        "What did they have to do in the first Men in Black movie? ",
        "Full Form of FOSS ",
        "The first text message was sent on 3 Dec 1992 after the development of SMS. Which country did this happen in?",
        "Which technology company has dropped facial recognition software amid racial profiling concerns? ",
        "From April 2015 to March 2017 police from 12 Indian states made a lot of journeys to this village. Nicknamed as the phishing capital of India, what is the name of the village?",
        "A senior police officer asks his junior officers to visit a murder location and note everything they see there. Officers return with the information: Body lying, television on, a cup of tea on the table, newspaper opened with page numbers 7 and 8. Are officers lying? If yes Why? If no Why?",
        "Which astronomer's name is part of the song 'Bohemian Rhapsody' ? ",
        "The suit used to record human movements for creating animated movies is called ?",
        "In the TV series, Breaking Bad, the fictional character of Walter White uses the alias ‘Heisenberg’, derived from the name of German Chemist, Werner Heisenberg. What is the principle formulated by Werner Heisenber regarding the position and velocity of an object? ",
        "Orbits around Earth and provides a living area for astronauts to conduct tests and exploration.",
        "___ contains text as well as information about the text.",
        "Audi, Lamborghini, Bently and Porsche are owned by the same group of business. Which brand is it? ",
        "They did a surgery on a grape. Name the minimally invasive surgical system responsible for the above 2018 meme.",
        "Name of the virus which caused the COVID-19 pandemic."
    ],
    "answer": [
        "Delorean",
        "Tipu sultan",
        "Sustainable Development",
        "Wheeler island",
        "Fintech",
        "15",
        "MPEG Audio Layer-3",
        "Jurassic Park",
        "Haber process",
        "Venus",
        "The love bug",
        "Accelerator , Brake and Clutch",
        "Magnetic",
        "Iris",
        "Catch a bug",
        "Free and Open Source Software",
        "United Kingdom",
        "IBM",
        "Jamtara",
        "Yes, even page number on left, odd number on right",
        "Galileo Galilei",
        "MoCap Suit",
        "Heisenberg’s Uncertainty Principle",
        "space station",
        "Markup language",
        "Volkswagen",
        "da Vinci Surgical System",
        "SARS-CoV-2"
    ]
}




#String variable 
Q_N =0
Q = StringVar()
A = StringVar()
C_H = StringVar()
R_T = StringVar()
Current_Q = StringVar()
#These flags are meant to restrict the flow in only one direction, eg:- the answer will be only revealed when the question is displayed 
#hint, question and answer flag
c_flag, q_flag, a_flag = 0, 0, 0
displayed_questions = [] #to keep tack of displayed questions 



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
    

    if c_flag==a_flag:
        Current_Q.set('Q'+str(len(displayed_questions)+1))
        Q_N = pick_question_number()
        cat_hin = data['CategoryAndHint'][Q_N]
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
        reveal_question(True)
        reveal_answer(True)


def reveal_question(destroy=False):

    global Q_N, Q, q_flag
    question = data['question'][Q_N]

    if len(question) > 78:
        question = str_fltr(question, 78)


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
    if len(answer)>40:
        answer = str_fltr(answer, 50)
        print('more than 20')
        font_size = 17
    print(answer)
    
    
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
