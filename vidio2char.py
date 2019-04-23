import sys
import os
import time
import threading
import cv2
import pyprind
import imageio as igo 
import numpy as np 


class V2Char():
    charVideo = []
    timeInterval = 0.033

    def __init__(self, path):
        if path.endswith('txt'):
            #self.load(path)
            pass
        else:
            self.genCharVideo(path)

    def genCharVideo(self, filepath):
        self.charVideo = []
        # 用opencv读取视频
        cap = cv2.VideoCapture(filepath)
        self.timeInterval = round(1 / cap.get(5), 3)
        nf = int(cap.get(7))
        print('Generate char video, please wait...')
        string = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        #A=[]
        #vvw = cv2.VideoWriter('mymovie.avi',cv2.VideoWriter_fourcc('X','V','I','D'),24,(640,480))
        #fourcc = cv2.cv.FOURCC(*'XVID')
        #out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('X','V','I','D'), 20, (640, 480))
        fps = cap.get(cv2.CAP_PROP_FPS)
        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        videoWriter = cv2.VideoWriter('trans.mp4', cv2.VideoWriter_fourcc(*'MP4V'), fps, size)  
        #wid = int(cap.get(3))
        #hei = int(cap.get(4))
        framenum = int(cap.get(7))
        #video = np.zeros((1,hei,wid,3),dtype='float16')
        #cnt = 0
        for i in pyprind.prog_bar(range(nf)):
            img_frame=cap.read()[1]
            #img = img_frame.astype('float16')/255
            img = img_frame
            #video[cnt]=b
            #cnt+=1
            #img=video
            
            u,v,_=img.shape
            #u,v=hei,wid
            #img=cap.read()[1]
            c=img*0+255
            # 转换颜色空间，第二个参数是转换类型，cv2.COLOR_BGR2GRAY表示从BGR↔Gray
            rawFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            #----------------------------------
            #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            gray=rawFrame
            for i in range(0,u,6):
                for j in range(0,v,6):
                    pix=gray[i,j]
                    b,g,r=img[i,j]
                    zifu=string[int(((len(string)-1)*pix)/256)]
                    cv2.putText(c,zifu,(j,i),cv2.FONT_HERSHEY_COMPLEX,0.3,(int(b),int(g),int(r)),1)
            videoWriter.write(c)
                    
            #A.append(c)
            #----------------------------------
            #frame = self.convert(rawFrame, os.get_terminal_size(), fill=True)
            #self.charVideo.append(frame)
            #igo.mimsave('cc.gif',A,'GIF',duration=0.1)
        videoWriter.release()
        cap.release()



if __name__ == '__main__':
    #v2char = V2Char()
    #v2char.genCharVideo('vedio.mp4')
    v2char = V2Char('vedio.mp4')
