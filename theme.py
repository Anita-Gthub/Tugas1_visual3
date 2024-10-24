import PySimpleGUI as sg
sg.theme("DarkGreen4")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM       :  2310010154")],
                           [sg.Text("Nama      :  NURIANITA")],
                           [sg.Text("Kelas      :  5B Non Regular Banjarmasin")],
                           [sg.Text("Matkul     :  Pemprograman Visual 3")]],
                           size=(400,200))
window()
window.close()