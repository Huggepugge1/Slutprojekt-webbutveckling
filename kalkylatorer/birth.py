import PySimpleGUI as sg
import datetime

layout = [
    [
        sg.Text("EDD (yyyy mm dd)"),
        sg.In(enable_events=True, key="EDD"),
    ],
    [
        sg.Text("fd (yyyy mm dd)"),
        sg.In(enable_events=True, key="fd"),
    ],
    [
        sg.Text("pregnancy (weeks days)"),
        sg.In(enable_events=True, key="pregnancy"),
    ],
    [
        sg.Button("calculate")
    ],
    [
        sg.Output(key="out")
    ]
]

window = sg.Window("Test", layout)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "calculate":
        normal = 279
        EDD = [int(i) for i in values["EDD"].split()]
        fd = [int(i) for i in values["fd"].split()]
        pregnancy = [int(i) for i in values["pregnancy"].split()]
        window.FindElement('out').Update('')
        if EDD and fd:
            delta = datetime.date(fd[0], fd[1], fd[2]) - datetime.date(EDD[0], EDD[1], EDD[2])
            print(f'{(normal + delta.days) // 7} + {(normal + delta.days) % 7}')
        elif EDD:
            offset = ((pregnancy[0] * 7) + pregnancy[1]) - normal
            EDD = datetime.date(EDD[0], EDD[1], EDD[2])
            print(f'Born at: {EDD + datetime.timedelta(offset)}')

        elif fd:
            offset = normal - ((pregnancy[0] * 7) + pregnancy[1])
            fd = datetime.date(fd[0], fd[1], fd[2])
            print(f'Calculated at: {fd + datetime.timedelta(offset)}')

        else:
            print("Non acceptable input")

    if event == sg.WIN_CLOSED:
        break

window.close()
