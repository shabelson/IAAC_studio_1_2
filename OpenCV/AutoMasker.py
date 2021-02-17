import cv2
import numpy as np
import os 
import tkinter as tk


def empty(a):
    pass



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.filePath = "G:\\My Drive\\team2_software_sysData\\team2DataSet_Download\\downloads\\bricks"
        self.files = (img for img in os.listdir(self.filePath))
        self.imgName = self.files.__next__()
        self.path = os.path.join(self.filePath,self.imgName)
        print (self.path)
        
        self.savePath = "G:\\My Drive\\team2_software_sysData\\team2Dataset_train\\"
        self.master = master
        self.pack()
        self.create_widgets()
        
        
    def create_widgets(self):
        self.run = tk.Button(self)
        self.run["text"] = "RESET"
        self.run["command"] = self.runFunc
        self.run.pack(side="top")
       
        self.save = tk.Button(self)
        self.save["text"] = "save"
        self.save["command"] = self.SaveImage
        self.save.pack(side="top")

        self.next = tk.Button(self)
        self.next["text"] = "next file"
        self.next["command"] = self.NextFile
        self.next.pack(side="top")

        self.update = tk.Button(self)
        self.update["text"] = "update"
        self.update["command"] = self.check
        self.update.pack(side="top")
       
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def runFunc(self):
        

        #Making the trackBars
        cv2.namedWindow("TrackBars")
        cv2.resizeWindow("TrackBars",640,480)
        # Control Hue/Saturation/Value in the trackbar
        cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
        cv2.createTrackbar("Hue Max","TrackBars",58,179,empty)
        cv2.createTrackbar("Sat Min","TrackBars",42,255,empty)
        cv2.createTrackbar("Sat Max","TrackBars",162,255,empty)
        cv2.createTrackbar("Val Min","TrackBars",58,255,empty)
        cv2.createTrackbar("Val Max","TrackBars",204,255,empty)
        self.img = cv2.imread(self.path )
        self.check()
        #convert img to HSV

    def check(self):
        
        imgHSV=cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV) 
        h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
        #print(h_min,h_max,s_min,s_max,v_min,v_max)
        lower=np.array([h_min,s_min,v_min])
        upper=np.array([h_max,s_max,v_max])
        self.mask = cv2.inRange(imgHSV,lower,upper)
        imgResult=cv2.bitwise_and(self.img,self.img,mask=self.mask)
 
        
        win_name1  = "Original"
        win_name2 = "Mask"
        cv2.imshow(win_name1,self.img)
        cv2.imshow(win_name2, self.mask)
        
        #cv2.imshow("HSV",imgHSV)
        
        #cv2.imshow("Result", imgResult)
        cv2.waitKey(1)
        self.master.after(50, self.check)

    def SaveImage(self):
        
        imgPath = os.path.join(self.savePath,"img_"+ self.imgName)
        MaskPath = os.path.join(self.savePath,"mask_"+ self.imgName)
        try:
            cv2.imwrite(imgPath, self.img)
            cv2.imwrite(MaskPath, self.mask)
            os.remove(self.path)
            os.remove(self.path)
        except:
            pass
    def NextFile(self):
        self.imgName = self.files.__next__()
        self.path = os.path.join(self.filePath,self.imgName)
        self.img = cv2.imread(self.path )
        self.check()







root = tk.Tk()
app = Application(master=root)
app.mainloop()







