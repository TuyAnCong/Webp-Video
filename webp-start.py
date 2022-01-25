
from tkinter import *
top=Tk()
cv = Canvas(top, height = 300, width = 300)
coord = 10, 10, 250, 250
cv.create_rectangle(coord,  outline = "red", fill='blue')
cv.create_line(1,275,260,275,fill = 'orange', width=5)
cv.create_oval(200,200,50,50, fill='yellow')
cv.create_text(125,225,text='Welcome to Webp to Video',font=("Arial",20),fill='white')
cv.pack()
top.title('Hello Python')
top.mainloop()
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print('Selected File: ' + filename)
