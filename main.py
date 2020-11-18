import tkinter
import time
import matplotlib.pyplot as plt
listNProccess = []
listDurProcess = []
listStartProcess = []
entriesStart = []
entriesDuration = []
maxDurProcess = []
#Creacion de ventana
window = tkinter.Tk()
window.title("PRACTICA 2 - COMPUTACION TOLERANTE A FALLAS")
window.geometry("600x1000")
window.config(bg = "white")



#validar que la entrada solo tenga numeros
def validate_entry(text):
    return text.isdecimal()

labelNumProcess = tkinter.Label(text= "¿Cuántos procesos quieres correr?", bg = "white")
labelNumProcess.grid(row = 0 , column =1)

txtBtnVar = tkinter.StringVar()
txtBtnVar.set(1)
textBtnProcess = tkinter.Entry(window,textvariable = txtBtnVar, bg = "white", validate="key", validatecommand=(window.register(validate_entry), "%S"))
textBtnProcess.grid(row = 0 , column = 2)


#Agregamos a una lista los elementos que se necesitan para graficar
def getData():

    for x in entriesStart:

         listStartProcess.append(x.get())

    for x in entriesDuration:

        listDurProcess.append(x.get())

    for x in range(len(listNProccess)):
        print("Proceso No. " + str(x) + " Inicia al segundo:  " + str(listStartProcess[x]) + " y dura " + str(listDurProcess[x]) + " segundos \n")
        maxDurProcess.append(int(listStartProcess[x]) + int(listDurProcess[x]))
        print(maxDurProcess)
        print(max(maxDurProcess))



def graph():
    getData()
    fig, ax = plt.subplots()
    for x in range(len(listNProccess)):
     ax.broken_barh([(int(listStartProcess[x]),int(listDurProcess[x]))], (x, 1))

    ax.set_ylim(0, len(listNProccess))
    ax.set_xlim(0, max(maxDurProcess))
    ax.set_ylabel('Procesos')
    ax.set_xlabel('Segundos')
    ax.set_yticks(listNProccess)
    ax.set_yticklabels(listNProccess)
    ax.grid(True)
    plt.show()


def WidgetsProcess(np):
    r = 1
 #Se generan los widgets de acuerdo al numero de procesos que se quieren agregar
    for x in range (np):
     lab= tkinter.Label(window, text = "Proceso #" + str(x), bg = "white")
     lab.grid(row = r, column = 0)
     listNProccess.append(x)

     labStart = tkinter.Label(window, text="Inicio", bg = "white")
     labStart.grid(row=r, column= 1)
     startVar = tkinter.StringVar()
     startVar.set(0)
     entriesStart.append(tkinter.Entry(window, textvariable = startVar, validate="key", validatecommand=(window.register(validate_entry), "%S")))
     entriesStart[x].grid( row = r ,column = 2)

     labDur = tkinter.Label(window, text="Duracion ", bg = "white")
     labDur.grid(row=r, column= 3)
     durVar = tkinter.StringVar()
     durVar.set(0)
     entriesDuration.append(tkinter.Entry(window, textvariable=durVar, validate="key", validatecommand=(window.register(validate_entry), "%S")))
     entriesDuration[x].grid(row=r, column= 4)
     r = r +1
    startBtn = tkinter.Button(window, text = "Iniciar", command = graph)
    startBtn.grid(row = r + 1 , column = 2)

insertBtn = tkinter.Button(window, text = "Añadir" , bg = "white", command = lambda : WidgetsProcess(int(textBtnProcess.get())))
insertBtn.grid(row = 0 , column = 3)
window.mainloop()