import random
import sys
import os
import copy
from datetime import datetime
import shutil

# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入designer工具生成的login模块
from ui2_merge import Ui_Merge

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw,ImageFont,ImageQt 

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene

from imgpro import merge_fore_to_back_image,random_merge_images


class MyMainForm(QMainWindow, Ui_Merge):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        # 初始化印章类
        self.setupUi(self)
        self.show_images.clicked.connect(self.Show_images)
        self.merge_images.clicked.connect(self.Merge_images)
        self.save_image.clicked.connect(self.Save_single_image)
        self.batch_merge_images.clicked.connect(self.Batch_merge_images)
        self.clear_dir.clicked.connect(self.Clear_dir)
    
    
    def Clear_dir(self):
        self.save_dir_ = self.save_dir.text()
        if os.path.exists(self.save_dir_):
            shutil.rmtree(self.save_dir_)
            
    def get_filelists(self,file_dir):
        filelists = os.listdir(file_dir)
        results=[]
        for i in filelists:
            results.append(os.path.join(file_dir,i))
        return results
    
    def Batch_Config_Update(self):
        self.back_dir_ = self.back_dir.text()
        self.fore_dir_ = self.fore_dir.text()
        self.save_dir_ = self.save_dir.text()
        self.file_pre_ = self.file_pre.text()
        self.fore_alphas_ = [float(self.fore_alphas_l.text()),float(self.fore_alphas_r.text())]
        self.fore_factors_ = [float(self.fore_factors_l.text()),float(self.fore_factors_r.text())]
        self.label_on_ = self.label_on.isChecked()
        self.fore_num_ = [self.fore_num_l.value(),self.fore_num_r.value()]
        self.back_use_num_ = self.back_use_num.value()
        
        if not os.path.exists(self.save_dir_):
            os.makedirs(self.save_dir_)
    
    def Batch_merge_images(self):
        self.update_config()
        self.Batch_Config_Update()
        back_filelists = self.get_filelists(self.back_dir_)
        fore_filelists = self.get_filelists(self.fore_dir_)
        # 过滤图片
        image_post = [".png", ".jpg", ".jpeg"]
        back_filelists = [i for i in back_filelists if os.path.splitext(i)[-1].lower() in image_post]
        if self.back_use_num_!=0:
            back_filelists = back_filelists[:self.back_use_num_]
            
        fore_filelists = [i for i in fore_filelists if os.path.splitext(i)[-1].lower() in image_post]
        
        
        
        # 以背景为基础，添加前景
        for ii,back_file in enumerate(back_filelists):
            back_image = Image.open(back_file).resize((1000,1000))
            # 从前景中任选l-r个
            sample_nums = random.choice(range(self.fore_num_[0],self.fore_num_[1]+1))
            if sample_nums > len(fore_filelists):
                sample_nums = len(fore_filelists)
            indexs = random.sample(list(range(len(fore_filelists))), sample_nums)
            fore_images = []
            types = []
            # 选取的前景图片序列,以及对并的标签
            for index in indexs:  
                if "circle" in fore_filelists[index]:
                    types.append("circle")
                elif "rectangle" in fore_filelists[index]:
                    types.append("rectangle")
                elif "oval" in fore_filelists[index]:
                    types.append("oval")
                else:
                    types.append("#")
                fore_images.append(Image.open(fore_filelists[index]))
            final_image,labels,params = random_merge_images(fore_images,back_image,fore_poss=None,fore_alphas = None ,fore_factors = None, fore_full = True, fore_func = lambda x : x, fore_range={"fore_alphas":self.fore_alphas_,"fore_factors":self.fore_factors_})
 
            # 做标注
            size = "_".join([str(i) for i in final_image.size])
            now = datetime.now()
            time1 = now.strftime('%Y%m%d%H%M')
            # alpha = params["fore_alpha"][i]
            # factor = params["fore_factor"][i]
            # pos = "_".join([str(i) for i in params["fore_pos"][i]])
            num = str(len(indexs))
            name = os.path.join(self.save_dir_,self.file_pre_.format(time=time1,num=num,size=size)+f"_{str(ii).zfill(4)}")
            final_image.save(name+".png")
            
            if self.label_on_:
                with open(name+".txt","w") as f:
                    for i in range(len(indexs)):
                        pp = ""
                        for vv in labels[i][:-1]:
                            pp += f"{round(vv[0])},{round(vv[1])},"
                        pp += f"{round(labels[i][-1][0])},{round(labels[i][-1][1])}"
                        f.write(f"{types[i]} {pp}\n")
    
    def Save_single_image(self):
            # 缩放后保存
        # self.save_path_ = self.save_path.text()
        self.merge_image_.save(self.single_save_image_)
            

    def Merge_images(self):
        self.update_config()
        self.fore_image_ = self.fore_image_

        self.merge_image_,labels = merge_fore_to_back_image(self.fore_image_, self.back_image_,fore_pos=self.back_pos_,back_padding=self.back_padding_,fore_alpha=self.fore_alpha_,fore_factor=self.fore_factor_)

        self.view_image(self.merge_image_,"self.merge_view")        
     
    def Show_images(self):
        self.update_config()
        self.show_fore_back_image()
    
    def update_config(self):
        self.back_path_ = self.back_path.text()
        self.fore_path_ = self.fore_path.text()
        self.back_padding_ = self.back_padding.isChecked()
        self.fore_alpha_ = float(self.fore_alpha.value())

        self.back_pos_ = [int(self.back_pos_w.text()),int(self.back_pos_h.text())]
        self.fore_factor_ = float(self.fore_factor.value())
        
        self.fore_image_ = Image.open(self.fore_path_)
        self.back_image_ = Image.open(self.back_path_).convert("RGBA").resize((1000,1000))
        
        self.single_save_image_ = self.single_save_image.text()
        
        
        basedir = os.path.dirname(self.single_save_image_)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        
    def show_fore_back_image(self):
        self.view_image(self.fore_image_,"self.fore_view")
        self.view_image(self.back_image_,"self.back_view")
            
    def view_image(self,image,object): 
        temp_image = image.copy()
        # opencv
        # height = image.shape[0]
        # width = image.shape[1]
        # frame = QImage(image, width, height, QImage.Format_RGB888)
        
        # PIL
        # width, height = temp_image.size
        temp_image = temp_image.resize((250,250),Image.ANTIALIAS)
        temp_image.save("merge_image.png")
        frame = ImageQt.ImageQt(temp_image)
        
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        eval(object).setScene(self.scene)
        
if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())