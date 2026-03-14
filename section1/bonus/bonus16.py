import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")
label2 = sg.Text("Select files to compress:")
input2 = sg.Input()
cb2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window('App',
                    layout=[[label1,input1,choose_button1],
                    [label2,input2,cb2],
                    [compress_button]])
window.read()
window.close()