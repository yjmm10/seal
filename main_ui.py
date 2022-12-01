import sys
import os
from datetime import datetime
import shutil

# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入designer工具生成的login模块
from ui import Ui_Dialog

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw,ImageFont,ImageQt 
from seal import SEAL
from utils import Images

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsScene

from faker  import Faker
import random


class MyMainForm(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        # 初始化印章类
        self.images_ = Images()
        self.seal_ = SEAL()
        self.setupUi(self)
        
        self.label_nums_ = 28
        self.resize_factor_ = 2
        
        self.image_draw.clicked.connect(self.show_image)
        self.update_config.clicked.connect(self.Update_config)
        self.single_save.clicked.connect(self.Single_save)
        self.batch_save.clicked.connect(self.Get_batch_images)
        self.clear_dir.clicked.connect(self.Clear_dir)
    
    def Clear_dir(self):
        self.save_dir_ = self.save_dir.text()
        if os.path.exists(self.save_dir_):
            shutil.rmtree(self.save_dir_)
    
    def Single_save(self):
        # 缩放后保存
        save_path = self.save_path.text()
        temp_image = self.images_.image
        width, height = temp_image.size
        temp_image = temp_image.resize((width//self.resize_factor_, height//self.resize_factor_),Image.Resampling.LANCZOS)
        temp_image.save(save_path)
   
      
    def view_image(self,image): 
        temp_image = image.copy()
        # opencv
        # height = image.shape[0]
        # width = image.shape[1]
        # frame = QImage(image, width, height, QImage.Format_RGB888)
        
        # PIL
        width, height = temp_image.size
        temp_image = temp_image.resize((width//self.resize_factor_, height//self.resize_factor_),Image.ANTIALIAS)
        frame = ImageQt.ImageQt(temp_image)
        
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.image_win.setScene(self.scene)
        
    def Update_batch_config(self):
        self.batch_nums_ = int(self.batch_nums.text())
        self.save_dir_ = self.save_dir.text()
        self.file_pre_ = self.file_pre.text()
        
        
        self.top_random_ = self.top_random.isChecked()
        self.top_filepath_ = self.top_filepath.text()
        self.bottom_random_ = self.bottom_random.isChecked()
        self.bottom_filepath_ = self.bottom_filepath.text()
        self.inter_random_ = self.inter_random.isChecked()
        self.inter_filepath_ = self.inter_filepath.text()
        self.line_label_on_ = self.line_label_on.isChecked()
           
        self.label_nums_ = int(self.label_nums.value())
        
        
    def Get_batch_images(self):
        # 展示最终的样子
        self.show_image()
        self.Update_batch_config()
        fakeinfo = Faker("zh-CN")
        
        if self.top_random_:
            top_content = []
            # 随机
            for i in range(self.batch_nums_):
                top_content.append(fakeinfo.company())
        else:
            with open(self.top_filepath_,"r",encoding='utf-8') as f:
                top_content = f.readlines()[:self.batch_nums_]
        if self.bottom_random_:
            bottom_content = []
            # 随机
            for i in range(self.batch_nums_):
                bottom_content.append(fakeinfo.ssn())
        else:
            with open(self.bottom_filepath_,"r",encoding='utf-8') as f:
                bottom_content = f.readlines()[:self.batch_nums_]        
        
        if self.inter_random_:
            content = ["人事专用章","财务专用章","报关专用章","图书专用章","品检部","公章","合同章","合同专用章","发票专用章","财务章","法人章"]
            # 随机
            inter_content = []
            for i in range(self.batch_nums_):
                inter_content.append(random.choice(content))
        else:
            with open(self.inter_filepath_,"r",encoding='utf-8') as f:
                inter_content = f.readlines()[:self.batch_nums_]  
        
        for i in range(self.batch_nums_):
            labels_content = {}
            self.images_.create_image("draw_test.png",self.img_size_)

            image = self.images_.image

            draw = ImageDraw.Draw(image)
            if self.out_on_:
                if self.out_shape_ == "rectangle":
                    pass
                    draw.rectangle(self.out_xyxy_,outline=self.color_,width=self.out_width_)
                else:
                    draw.ellipse(self.out_xyxy_,outline=self.color_,width=self.out_width_)
            if self.border_on_:    
                if self.border_shape_ == "rectangle":
                    draw.rectangle(self.border_xyxy_,outline=self.color_,width=self.border_width_)
                else:
                    draw.ellipse(self.border_xyxy_,outline=self.color_,width=self.border_width_)
            if self.in_on_:
                if self.in_shape_ == "rectangle":
                    draw.rectangle(self.in_xyxy_,outline=self.color_,width=self.in_width_)
                else:
                    draw.ellipse(self.in_xyxy_,outline=self.color_,width=self.in_width_)
                    
            if self.top_text_on_:
                if self.top_text_shape_ =="rectangle":
                    infos,labels = self.seal_.cal_rec_text_pos_label(self.top_font_wh_,self.top_text_space_,top_content[i],label_nums=self.label_nums_)
                    for char,x,y,degree in infos: 
                        self.images_.draw_rotated_char(char, self.top_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)), font_size=self.top_font_wh, angle=degree, color=self.color_, spacing=self.top_text_space_)   
                else:
                    infos,labels = self.seal_.cal_text_and_label_pos(self.top_text_wh_,self.top_font_wh_,self.top_text_space_,top_content[i], label_nums=self.label_nums_, top=self.top_istop_)
                    for char,x,y,degree in infos:
                        self.images_.draw_rotated_char(char, self.top_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)), font_size=self.top_font_wh_, angle=degree, color=self.color_, spacing=self.top_text_space_)
                labels_content[top_content[i]] = []
                for l in labels:
                    labels_content[top_content[i]].append([l[0]+self.center[0],self.center[1]-l[1]])
                
                
            if self.bottom_text_on_:
                if self.bottom_text_shape_ =="rectangle":
                    infos,labels = self.seal_.cal_rec_text_pos_label(self.bottom_font_wh_,self.bottom_text_space_,bottom_content[i],label_nums=self.label_nums_)
                    for char,x,y,degree in infos:
                        self.images_.draw_rotated_char(char, self.bottom_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)), font_size=self.bottom_font_wh_, angle=degree, color=self.color_, spacing=self.bottom_text_space_)   
                else:
                    infos,labels = self.seal_.cal_text_and_label_pos(self.bottom_text_wh_,self.bottom_font_wh_,self.bottom_text_space_,bottom_content[i], label_nums=self.label_nums_, top=self.bottom_istop_)
                    for char,x,y,degree in infos:
                        self.images_.draw_rotated_char(char,self.bottom_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)), font_size=self.bottom_font_wh_, angle=degree, color=self.color_, spacing=self.bottom_text_space_)
                labels_content[bottom_content[i]] = []
                for l in labels:
                    labels_content[bottom_content[i]].append([l[0]+self.center[0],self.center[1]-l[1]])
                        
            if self.inter_text_on_:
                if self.inter_text_shape_ =="rectangle":
                    infos,labels = self.seal_.cal_rec_text_pos_label(self.inter_font_wh_,self.inter_text_space_,inter_content[i],label_nums=self.label_nums_)
                    for char,x,y,degree in infos:
                        self.images_.draw_rotated_char(char, self.inter_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)+self.inter_shift_y_), font_size=self.inter_font_wh_, angle=degree, color=self.color_, spacing=self.inter_text_space_)   
                else:
                    infos,labels = self.seal_.cal_text_and_label_pos(self.inter_text_wh_,self.inter_font_wh,self.inter_text_space_,inter_content[i], label_nums=self.label_nums_, top=self.inter_istop_)
                    for char,x,y,degree in infos:
                        self.images_.draw_rotated_char(char, self.inter_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)+self.inter_shift_y_), font_size=self.inter_font_wh_, angle=degree, color=self.color_, spacing=self.inter_text_space_)
                labels_content[inter_content[i]] = []
                for l in labels:
                    labels_content[inter_content[i]].append([l[0]+self.center[0],self.center[1]-l[1]])
            
            if not os.path.exists(self.save_dir_):
                os.makedirs(self.save_dir_)
            now = datetime.now()
            time1 = now.strftime('%Y%m%d%H%M')
            color = "_".join([str(i) for i in self.color_])
            size = "_".join([str(i//self.resize_factor_) for i in self.img_size_])
            png_name = os.path.join(self.save_dir_,self.file_pre_.format(time=time1,num=self.batch_nums_,shape=self.out_shape_,color=color,size=size)+f"_{str(i).zfill(4)}")
            temp_image = image
            width, height = temp_image.size
            temp_image = temp_image.resize((width//self.resize_factor_, height//self.resize_factor_),Image.Resampling.LANCZOS)
            temp_image.save(png_name+".png")
            
            if self.line_label_on_:
                with open(png_name+".txt",'w') as f:
                    for k,v in labels_content.items():
                        pp = ""
                        for vv in v[:-1]:
                            pp += f"{round(vv[0]/self.resize_factor_)},{round(vv[1]/self.resize_factor_)},"
                        pp += f"{round(v[-1][0]/self.resize_factor_)},{round(v[-1][1]/self.resize_factor_)}"
                        f.write(f"{k} {pp}\n")            



    # 配置更新
    def Update_config(self):
        self.resize_factor_ = int(self.resize_factor.value())
        self.img_size_ = [self.resize_factor_*int(self.image_w.text()),self.resize_factor_*int(self.image_h.text())]
        self.center = [i//2 for i in self.img_size_] 
        
        # out 参数
        self.out_on_ = self.out_on.isChecked()
        self.out_shape_ = self.out_shape.currentText()
        self.out_size_ = [self.resize_factor_*int(self.out_size_w.text()),self.resize_factor_*int(self.out_size_h.text())]
        self.color_ = tuple([int(self.img_r.text()),int(self.img_g.text()),int(self.img_b.text())])
        self.out_width_ = self.resize_factor_*int(self.out_width.value())
        # self.sp.valueChanged.connect(self.Valuechange)
        self.out_xyxy_ = [self.center[i]-self.out_size_[i] for i in range(len(self.center))]+[self.center[i]+self.out_size_[i] for i in range(len(self.center))]
        
        self.border_on_ = self.border_on.isChecked()
        self.border_shape_ = self.border_shape.currentText()
        self.border_size_ = [self.resize_factor_*int(self.border_size_w.text()),self.resize_factor_*int(self.border_size_h.text())]
        self.border_xyxy_ = [self.center[i]-self.border_size_[i] for i in range(len(self.center))]+[self.center[i]+self.border_size_[i] for i in range(len(self.center))]
        self.border_width_ = self.resize_factor_*int(self.border_width.value())

        # 内边界大小 xyxy
        self.in_on_ = self.in_on.isChecked()
        self.in_shape_ = self.in_shape.currentText()
        self.in_size_ = [self.resize_factor_*int(self.in_size_w.text()),self.resize_factor_*int(self.in_size_h.text())]
        self.in_xyxy_ = [self.center[i]-self.in_size_[i] for i in range(len(self.center))]+[self.center[i]+self.in_size_[i] for i in range(len(self.center))]
        self.in_width_ = self.resize_factor_*int(self.in_width.value())
        
        self.top_text_on_ = self.top_text_on.isChecked()
        self.top_text_shape_ = self.top_text_shape.currentText()
        self.top_text_content_ = self.top_text_content.text()
        # 整行文本占据的长度
        self.top_text_wh_ = [self.resize_factor_*int(self.top_text_size_w.text()),self.resize_factor_*int(self.top_text_size_h.text())]
        # 单个字体宽高
        self.top_font_wh_ = [self.resize_factor_*int(self.top_text_font_w.text()),self.resize_factor_*int(self.top_text_font_h.text())]
        self.top_text_font_ = self.top_text_font.text()
        self.top_text_space_ = int(self.top_text_space.value())
        self.top_istop_ = True
        
        # 底部文字
        self.bottom_text_on_ = self.bottom_text_on.isChecked()
        self.bottom_text_shape_ = self.bottom_text_shape.currentText()
        self.bottom_text_content_ = self.bottom_text_content.text()
        # 整行文本占据的长度
        self.bottom_text_wh_ = [self.resize_factor_*int(self.bottom_text_size_w.text()),self.resize_factor_*int(self.bottom_text_size_h.text())]
        # 单个字体宽高
        self.bottom_font_wh_ = [self.resize_factor_*int(self.bottom_text_font_w.text()),self.resize_factor_*int(self.bottom_text_font_h.text())]
        self.bottom_text_font_ = self.bottom_text_font.text()
        self.bottom_text_space_ = int(self.bottom_text_space.value())
        self.bottom_istop_ = False
        
        # 中间文本
        self.inter_text_on_ = self.inter_text_on.isChecked()
        self.inter_text_shape_ = self.inter_text_shape.currentText()
        self.inter_text_content_ = self.inter_text_content.text()
        # 整行文本占据的长度
        self.inter_text_wh_ = [self.resize_factor_*int(self.inter_text_size_w.text()),self.resize_factor_*int(self.inter_text_size_h.text())]
        # 单个字体宽高
        self.inter_font_wh_ = [self.resize_factor_*int(self.inter_text_font_w.text()),self.resize_factor_*int(self.inter_text_font_h.text())]
        self.inter_text_font_ = self.inter_text_font.text()
        self.inter_text_space_ = int(self.inter_text_space.value())
        self.inter_shift_y_ = self.resize_factor_*self.inter_shift_y.value()
        self.inter_istop_ = True
    
    # 单张显示图片
    def show_image(self):
        self.Update_config()
        # 
        self.images_.create_image("draw_test.png",self.img_size_)

        image = self.images_.image

        draw = ImageDraw.Draw(image)
        if self.out_on_:
            if self.out_shape_ == "rectangle":
                pass
                draw.rectangle(self.out_xyxy_,outline=self.color_,width=self.out_width_)
            else:
                draw.ellipse(self.out_xyxy_,outline=self.color_,width=self.out_width_)
        if self.border_on_:    
            if self.border_shape_ == "rectangle":
                draw.rectangle(self.border_xyxy_,outline=self.color_,width=self.border_width_)
            else:
                draw.ellipse(self.border_xyxy_,outline=self.color_,width=self.border_width_)
            
        if self.in_on_:
            if self.in_shape_ == "rectangle":
                draw.rectangle(self.in_xyxy_,outline=self.color_,width=self.in_width_)
            else:
                draw.ellipse(self.in_xyxy_,outline=self.color_,width=self.in_width_)
        if self.top_text_on_:
            if self.top_text_shape_ =="rectangle":
                infos,_ = self.seal_.cal_rec_text_pos_label(self.top_font_wh_,self.top_text_space_,self.top_text_content_,label_nums=self.label_nums_)
                for char,x,y,degree in infos:
                    self.images_.draw_rotated_char(char, self.top_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)), font_size=self.top_font_wh, angle=degree, color=self.color_, spacing=self.top_text_space_)   
            else:
                infos,_ = self.seal_.cal_text_and_label_pos(self.top_text_wh_,self.top_font_wh_,self.top_text_space_,self.top_text_content_, label_nums=self.label_nums_, top=self.top_istop_)
                for char,x,y,degree in infos:
                    self.images_.draw_rotated_char(char, self.top_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)), font_size=self.top_font_wh_, angle=degree, color=self.color_, spacing=self.top_text_space_)
            
        if self.bottom_text_on_:
            if self.bottom_text_shape_ =="rectangle":
                infos,_ = self.seal_.cal_rec_text_pos_label(self.bottom_font_wh_,self.bottom_text_space_,self.bottom_text_content_,label_nums=self.label_nums_)
                for char,x,y,degree in infos:
                    self.images_.draw_rotated_char(char, self.bottom_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)), font_size=self.bottom_font_wh_, angle=degree, color=self.color_, spacing=self.bottom_text_space_)   
            else:
                infos,_ = self.seal_.cal_text_and_label_pos(self.bottom_text_wh_,self.bottom_font_wh_,self.bottom_text_space_,self.bottom_text_content_, label_nums=self.label_nums_, top=self.bottom_istop_)
                for char,x,y,degree in infos:
                    self.images_.draw_rotated_char(char,self.bottom_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)), font_size=self.bottom_font_wh_, angle=degree, color=self.color_, spacing=self.bottom_text_space_)
                    
        if self.inter_text_on_:
            if self.inter_text_shape_ =="rectangle":
                infos,_ = self.seal_.cal_rec_text_pos_label(self.inter_font_wh_,self.inter_text_space_,self.inter_text_content_,label_nums=self.label_nums_)
                for char,x,y,degree in infos:
                    self.images_.draw_rotated_char(char, self.inter_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)+self.inter_shift_y_), font_size=self.inter_font_wh_, angle=degree, color=self.color_, spacing=self.inter_text_space_)   
            else:
                infos,_ = self.seal_.cal_text_and_label_pos(self.inter_text_wh_,self.inter_font_wh,self.inter_text_space_,self.inter_text_content_, label_nums=self.label_nums_, top=self.inter_istop_)
                for char,x,y,degree in infos:
                    self.images_.draw_rotated_char(char, self.inter_text_font_, pos=((int(x)+self.center[0]), self.center[1]-int(y)+self.inter_shift_y_), font_size=self.inter_font_wh_, angle=degree, color=self.color_, spacing=self.inter_text_space_)            
    
        self.view_image(self.images_.image)


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

