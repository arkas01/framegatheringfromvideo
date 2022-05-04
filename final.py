from tkinter import *
from tkinter import filedialog
import cv2
#taking the  input of the directory to where the file is to be saved from the user
path = filedialog.askdirectory(initialdir="C:\examples",title="MY frieeend, At first you choose where to save your file")

#the ultimate function to slice the frames
def Slicetheframes():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Open file okay?",
                                          filetypes= (("Video files","*.mp4"),
                                          ("all files","*.*")))
    def framebreaker(path1,video):
        vidcap = cv2.VideoCapture(video)
        success,image = vidcap.read()
        count = 0
        while success:
            z=cv2.imwrite(path1+'/frame%d.jpg' % count, image)
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
    framebreaker(path,filepath)
    """ file = open(filepath,'r')
    print(file.read())
    file.close() """


window = Tk()
window.geometry('500x300') 

#using the buttons to browse through directories and upload the file.
button = Button(text="Choose the file that you want to upload to slice it into frames ;)",command=Slicetheframes)
button.pack()



window.mainloop()