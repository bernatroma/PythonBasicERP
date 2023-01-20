from tkinter import * 
from tkinter import ttk
from clients import clients
from proveidors import proveidors
from potencials import clients_pot
    
ventana = Tk()
ventana.geometry('1600x1000')
ventana.configure(bg = 'beige')
ventana.title('ElfosSoftware')  
l = Label(text = "Elfos Sofware")
l.pack()
image = PhotoImage(file="images/elfosoftware.png")
small_image = image.subsample(2, 2) 
label = Label(ventana, image=small_image)
label.pack()
label.place(relx=0.5, rely=0.35, anchor=CENTER)

buttonclient = ttk.Button(ventana, text='CLIENTS', command=clients)
buttonclient.place(width=180,height=100,relx=0.13, rely=0.75, anchor=W)

butonproveidors = ttk.Button(ventana, text='PROVEIDORS', command=proveidors)
butonproveidors.place(width=180,height=100,relx=0.32, rely=0.75, anchor=W)

botonpot = ttk.Button(ventana, text='CLIENTS POTENCIALS', command=clients_pot)
botonpot.place(width=180,height=100,relx=0.51, rely=0.75, anchor=W)

botonsortir = ttk.Button(ventana, text='Sortir', command=quit)
botonsortir.place(width=180,height=100,relx=0.7, rely=0.75, anchor=W)



ventana.mainloop()




