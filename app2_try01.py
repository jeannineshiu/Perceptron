#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.setrecursionlimit(10000)
import os
from PyQt5.QtWidgets import QDialog, QApplication,QWidget
from designerUI02 import Ui_Form    #MyFirstUI 是你的.py檔案名字

#for openfile
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#drawing
import random
import matplotlib.pyplot as plt

from pyqtgraph import *
import pyqtgraph as pg
   # data can be a list of values or a numpy array


# In[2]:


class AppWindow(QWidget):
    learning_rate = 0
    iters_num = 0
    
    training =[]
    test =[]
    trtarget =[]
    tstarget =[]
    
    w_train =[]
    w_test =[]
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #1.open file
        self.ui.openbt.clicked.connect(self.openbt_Click)
        #2.input learn,iters
        self.ui.learninginput.editingFinished.connect( self.enterPress1 )
        self.ui.iterationinput.editingFinished.connect( self.enterPress2 )
        
        #3.run
        self.ui.train_bt.clicked.connect(self.trainbt_Click)
        self.ui.test_bt.clicked.connect(self.testbt_Click)
        
        
        self.show()
        
    ###define my functions which i want to do when i touch the objects######
        
    def enterPress1(self):
        self.learning_rate = float(self.ui.learninginput.text())
        print("learning="+str(self.learning_rate))
    def enterPress2(self):
        self.iters_num = int(self.ui.iterationinput.text())
        print("iters="+str(self.iters_num))
        
        
    def trainbt_Click(self):
        
        self.ui.datawidget.canvas.ax.clear()
        
        self.w_train = self.logistic(self.training,self.trtarget,self.learning_rate,self.iters_num)
        
        
        self.vis_data(self.training,self.trtarget)

        l = np.linspace(-5,10)
        a,b = -self.w_train[1]/self.w_train[2], -self.w_train[0]/self.w_train[2]
        self.ui.datawidget.canvas.ax.plot(l, a*l+ b, 'b-')
        #plt.show()
        self.ui.datawidget.canvas.draw()
        
        
    def testbt_Click(self):
        
        self.ui.datawidget.canvas.ax.clear()
        
        self.w_test =self.logistic(self.test,self.tstarget,self.learning_rate,self.iters_num)
        
        self.vis_data(self.test,self.tstarget)

        l = np.linspace(-5,10)
        a,b = -self.w_test[1]/self.w_test[2], -self.w_test[0]/self.w_test[2]
        self.ui.datawidget.canvas.ax.plot(l, a*l+ b, 'b-')
        #plt.show()
        self.ui.datawidget.canvas.draw()
        
    def openbt_Click(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter( QDir.Files  )
        if dlg.exec_():
            filenames= dlg.selectedFiles()
            f = open(filenames[0], 'r') 
            #show filename
            filename = os.path.basename(filenames[0])
            self.ui.filenamelabel.setText(filename)
            
            with f:
                #process_data while reading
                data2d = []
                i = 0
                line = f.readline()
                while line!='':
                    datalist = [float(x) for x in line.split(' ')]
                    #print (datalist) => [-0.912312, 2.056434, 1.0] 
                    #datalist[0]:-0.912312
                    data2d.append([])
                    data2d[i] = datalist
                    print(data2d[i])
                    i = i + 1
                    line = f.readline()

            
            #print(data2d)
            #self.vis_data(data2d)
            
            ##process data
            self.training,self.test,self.trtarget,self.tstarget = self.processData(data2d)
            print(self.training,self.test,self.trtarget,self.tstarget)
            
    # scatter plot them
    def vis_data(self,X_x0,y):
        
        self.ui.datawidget.canvas.ax.clear()
        
        
        self.ui.datawidget.canvas.ax.grid()

        for i in range(y.shape[0]):
            c = 'r'
            if y[i][0] == 0.0:
                c = 'b'
            self.ui.datawidget.canvas.ax.scatter([X_x0[i][1]], [X_x0[i][2]], c=c)
        
    def matplot(self):
        print("***")
        self.ui.mpl.canvas.ax.clear()
        print("***1")
        x=range(0, 10)
        y=range(0, 20, 2)
        self.ui.mpl.canvas.ax.plot(x, y)
        print("***2")
        self.ui.mpl.canvas.draw()
        
    def processData(self,data2d):
        fullData = np.array(data2d)
        
        #
        #把target2改成0以符合sigmoid的設定
        X_c = fullData
        for i in range(fullData.shape[0]):
            if X_c[i][2]==2.0:
                X_c[i][2] = 0.0
        #print(X_c)
        fullData = X_c
        
        
        #x0的column
        a = np.ones([fullData.shape[0],1])
        #X加上x0後完成
        fullData = np.concatenate((a,fullData),axis = 1)
      
        
        
        #洗牌
        np.random.shuffle(fullData)
        #print(fullData)
        #計算前2/3的資料有幾row
        trainRow = int(fullData.shape[0]*(2/3))
        testRow = fullData.shape[0]-trainRow
        
        
        
        #將data2d分成訓練和測試資料
        training, test = fullData[:trainRow,:], fullData[trainRow:,:]
        #成功將data與target分開
        training_target = training[ : , 3:4 ]
        training = training[ : , :3 ]
        test_target = test[ : , 3:4 ]
        test = test[ : , :3 ]
        
        #print(training)
        #print(test)
        #print(training_target)
        #print(test_target)
        
        return training,test,training_target,test_target
    
    #計算機率函數
    def sigmoid(self,z):
        return 1 / (1 + np.exp(-z))
    
    #計算平均梯度_改
    def gradient(self,X_x0,y,w):
        g = np.zeros(len(w))
        for i in range(y.shape[0]):
            x = X_x0[i]
            yy = y[i][0]
            error = self.sigmoid(w.T.dot(x))
            g += (error - yy) * x
        return g / y.shape[0]
    
    #計算現在的權重的錯誤有多少_改
    def cost(self,X_x0,y, w):
        total_cost = 0
        for i in range(y.shape[0]):
            x = X_x0[i]
            yy = y[i][0]
            error = self.sigmoid(w.T.dot(x))
            total_cost += abs(yy - error)
        return total_cost
    
    def logistic(self,X_x0,y,learning,iters): #演算法實作

        w = np.zeros(3) #用0 + 0*x1 + 0*x2當作初始設定 

        limit = iters  #更新十次後停下

        eta = learning #更新幅度

        costs = [] #紀錄每次更新權重後新的cost是多少

        for i in range(limit):
            current_cost = self.cost(X_x0,y, w)
            #print ("current_cost=",current_cost)
            costs.append(current_cost)
            w = w - eta * self.gradient(X_x0,y, w)
            eta *= 0.95 #更新幅度，逐步遞減

        #畫出cost的變化曲線，他應該要是不斷遞減 才是正確
        
        self.ui.costwidget.canvas.ax.clear()

        self.ui.costwidget.canvas.ax.plot(range(limit), costs)
        #self.ui.costwidget.canvas.ax.show()
        
        self.ui.costwidget.canvas.draw()
        
        return w


# In[3]:


## main function
if __name__ == "__main__":
    app = QApplication(sys.argv)  
    MainWindow = AppWindow()
    MainWindow.show()
    sys.exit(app.exec_())    

