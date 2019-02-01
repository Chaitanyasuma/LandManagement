from tkinter import *
import SliceGreen as sg
root=Tk()
photo=PhotoImage(file="Baner gaon.png")
labph=Label(root,image = photo)
labph.pack()
root.mainloop()
window=Tk()
lab=Label(window,text="The number of green Pixels:"+str(sg.num_green))
lab.pack()
lab1=Label(window,text="The green coverage area is: "+ str(sg.green_area)+" sq. metres")
lab1.pack()
lab2=Label(window,text="The carbon emissions is: "+ str(sg.carbonemissions))
lab2.pack()
window.mainloop()

