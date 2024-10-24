import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                            font=("Arial", 24,"italic","bold","underline"))],
                           [sg.Text("NPM     :  2310010154")],
                           [sg.Text("Nama    :  NURIANITA")],
                           [sg.Text("Kelas    :  5B NonRegular Banjarmasin")],
                           [sg.Text("Matkul  :  Pemprograman Visual 3")]
                           ],
                           size=(500,200), 
                           font=("Times", 16))
window()
window.close()