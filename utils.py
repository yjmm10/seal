import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

class Images:
    def __init__(self):
        pass
    
    def draw_line(self):
        pass
        
    def draw_points(self, x,y, width=1,color =(255,0,0)):
        draw = ImageDraw.Draw(self.image)
        draw.point([x,y],fill=color)
    
    # 绘制旋转文字
    def draw_rotated_char(self,text, font, pos=(150, 150), font_size=(16, 16), angle=20, color=(255, 0, 0), spacing=None, *args, **kwargs):
        """
        https://www.thinbug.com/q/45179820
        Draw text at an angle into an image, takes the same arguments
        as Image.text() except for:

        :param image: Image to write text into
        :param angle: Angle to write text at
        """
        w, h = self.image.size
        # 求出文字占用图片大小
        max_dim = max(font_size[0]*2, font_size[1]*2)
        mask = Image.new('RGBA', (max_dim, max_dim))
        draw = ImageDraw.Draw(mask)
        font_style = ImageFont.truetype(font=font, size=font_size[1], encoding="utf-8")
        xy = ((max_dim-font_size[1])//2,(max_dim-font_size[1])//2)
        # print(xy)
        draw.text(xy,text,(255,0,0),font=font_style,spacing=spacing) #设置位置坐标 文字 颜色 字体
        if max_dim ==font_size[1]*2:
            new_size = (int(max_dim*font_size[0]/font_size[1]),max_dim) 
        else:
            new_size = (int(max_dim*font_size[0]/font_size[1]),max_dim)
        mask = mask.resize(new_size)
        mask = mask.rotate(angle)
        pos = (pos[0]-mask.size[0]//2,pos[1]-mask.size[1]//2)
        self.image.paste(mask,pos,mask=mask)
        
    def draw_ellipse(self):
        pass
    
    def show_image(self,title=" "):
        plt.rcParams['font.family'] = 'SimHei'
        plt.figure()
        plt.suptitle(title,fontsize = 20, color = 'red',backgroundcolor='yellow')
        plt.imshow(self.image)
        ax = plt.gca()
        ax.set_aspect(1)
        plt.show()
        # plt.show(self.image)
        # self.image.show()
    
    # 创建画布
    def create_image(self,path,size:list|tuple,mode:str = "RGB"):
        # size: wh
        self.image = Image.new(mode, (size[0], size[1]), "black")  # 黑色背景
        self.draw = ImageDraw.Draw(self.image)