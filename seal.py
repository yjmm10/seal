import cv2
import numpy as np

import math
class SEAL:
    def __init__(self):
        pass
    
    # 椭圆角度对应的坐标,
    def cal_ellipse_xy(self,a,b,degree):
        # a: 长轴 
        # b: 短轴
        # ref: https://blog.csdn.net/u014789533/article/details/114692234
        rad = math.radians(degree)
        ecc_angle = self.cal_eccentric_angle(a, b, rad)
        x = a * math.cos(ecc_angle)
        y = b * math.sin(ecc_angle)
        return [x,y]
    
    # 离心角度求解，可得到唯一解
    @staticmethod
    def cal_eccentric_angle(a,b,rad):
        return math.atan2(a*math.sin(rad),b*math.cos(rad))
    # 欧氏距离
    @staticmethod
    def get_l2_dist(point1:list,point2:list):
        return math.sqrt((point1[1]-point2[1])**2 +(point1[0]-point2[0])**2)
    
    # 微分思想获取椭圆上的坐标点
    def cal_draw_points(self,a,b,start_degree,cross_degree, split_nums=1000):
        # a: 长轴
        # b: 短轴
        # start_degree: 开始角度，与x轴正方向相同
        # cross_degree: 角度跨度
        result = []
        for i in range(split_nums):
            degree = start_degree + (i*cross_degree) / split_nums
            point = self.cal_ellipse_xy(a,b,degree)
            result.append(point)
        return result
    
    # 获取列表中所有相邻点之间的长度
    def cal_points_length(self,xy:list):
        # xy : 坐标点列表 [[x,y],...]
        assert isinstance(xy,(list,tuple)), print("输出的xy非数组，检查类型",xy)
        total_length = 0 
        part_length_list = []
        for i in range(0,len(xy)-1):
            l = self.get_l2_dist(xy[i],xy[i+1])
            part_length_list.append(l)
            total_length += l
        return total_length,part_length_list
    
    # 根据起始角度、角度跨度，获取文字位置
    def cal_text_pos(self,a,b,start_degree,cross_degree, split_nums, text_nums):
        # a: 长轴
        # b: 短轴
        # start_degree: 开始角度，与x轴正方向相同
        # cross_degree: 角度跨度
        # split_nums: 划分数量
        # text_nums: 文本长度
        xys = self.cal_draw_points(a,b,start_degree,cross_degree,split_nums)
        length, part_length_list = self.cal_points_length(xys)
        # 每个字的弧长
        text_cross_per = length / (text_nums-1)   
        # 第一个字
        result = [xys[0]]
        cross_length_cnt = 0
        for i in range(len(part_length_list)):  # 
            cross_length_cnt += part_length_list[i]
            if cross_length_cnt >= text_cross_per:
                pre_dis = abs(cross_length_cnt - text_cross_per - part_length_list[i-1])
                cur_dis = abs(cross_length_cnt - text_cross_per) 
                # 取距离小的值
                if pre_dis <= cur_dis:
                    result.append(xys[i])
                else:
                    result.append(xys[i+1])
                cross_length_cnt = 0
        if len(result) < text_nums:
            result.append(xys[-1])
        
        return result
    
    # 计算椭圆切线角度
    @staticmethod
    def cal_tangent_degree(a,b,x,y):
        if y==0:
            return 90
        k = -b*b*x/(a*a*y)
        result = math.degrees(math.atan(k))
        return result
    
    # 计算椭圆的坐标以及角度信息
    def cal_ellipse_text_info_basic(self,a,b,start_degree,cross_degree, split_nums,texts,top=True):
        # a: 长轴
        # b: 短轴
        # start_degree: 开始角度，与x轴正方向相同
        # cross_degree: 角度跨度
        # split_nums: 划分数量
        # text_nums: 文本长度
        result = [] # item: char, x,y degree
        text_len = len(texts)
        text_pos = self.cal_text_pos(a,b,start_degree,cross_degree, split_nums,text_len)
        for i in range(text_len):
            degree = self.cal_tangent_degree(a,b,text_pos[i][0],text_pos[i][1])
            if top and text_pos[i][1]<=0:
                degree -= 180
            if not top and text_pos[i][1]>=0:
                degree -= 180
            # y轴需要做个翻转
            result.append([texts[text_len-1-i], text_pos[i][0],text_pos[i][1],degree])
        return result, start_degree, cross_degree
    
    # 已知直线，求线上点到线上某一点距离为dis的点
    def cal_point_at_line_with_dis(self,k,b,fix_points:list,dis):
        # k,b 直线斜率
        # fix_points: 线上固定点
        # dis: 到固定点的距离
        # return  [外点，内点]
        c = (k*(b-fix_points[1])-fix_points[0])/(k**2+1)
        d = ((b-fix_points[1])**2+fix_points[0]**2-dis**2)/(k**2+1)
        
        e = (c**2-d)**0.5
        x1 = e-c
        y1 = k*x1 + b
        x2 = -e-c
        y2 = k*x2 + b
        result = [[x1,y1],[x2,y2]]
        # y大的为外点
        result.sort(key=lambda x: x[1],reverse=True)
        return result           
    
    # 计算某一个点绕着固定点旋转的坐标
    def cal_rotate_at_fix_point(self,degree,valuex,valuey,pointx,pointy,clock=False):
        # degree : 旋转角度值
        # valuex, valuey : 旋转的点
        # pointx, pointy : 固定点
        # clock          : 顺时针方向
        rad = math.radians(degree)
        if clock:
            rad = -rad

        valuex = np.array(valuex)
        valuey = np.array(valuey)
        nRotatex = (valuex-pointx)*math.cos(rad) - (valuey-pointy)*math.sin(rad) + pointx
        nRotatey = (valuex-pointx)*math.sin(rad) + (valuey-pointy)*math.cos(rad) + pointy
        return nRotatex, nRotatey
    
    #####################################################
    # 通过对称位置，计算椭圆的坐标以及角度信息
    def cal_ellipse_text_info_with_cross(self,a,b,cross_degree, split_nums,texts,top=True):
        # a: 长轴
        # b: 短轴
        # start_degree: 开始角度，与x轴正方向相同
        # cross_degree: 角度跨度
        # split_nums: 划分数量
        # text_nums: 文本长度
        start_degree = cross_degree/2
        # print("起始角度：",start_degree)
        if not top:
            start_degree -= 180
            texts = texts[::-1]
        # 从最后一个文字开始算起点
        start_degree = 90 - start_degree
        return self.cal_ellipse_text_info_basic(a,b,start_degree,cross_degree, split_nums,texts,top=top) 
       
    # 通过对称以及字体计算椭圆坐标以及角度信息，简洁版（推荐）,求标签版
    def cal_ellipse_text_label_info_sim(self,a,b,font_size,space,split_nums,texts,label_nums,top=True):
        # a: 长轴
        # b: 短轴
        # start_degree: 开始角度，与x轴正方向相同
        # cross_degree: 角度跨度
        # split_nums: 划分数量
        # texts: 文本
        # label_nums:  标注点数量
        # top : 上半区还是小半区
        error = 1.2 # 精度，用于调整
        text_len = len(texts)
        cross_length = (font_size[0]*text_len+text_len*space)*error
        # 一半
        half_cross_length = cross_length / 2
        # 模拟从90~-90的点位置
        xys = self.cal_draw_points(a,b,270,180,split_nums)
        _, part_length_list = self.cal_points_length(xys)
        sums = 0
        cross_degree = 0
        for i in part_length_list:
            sums += i
            cross_degree += 180/split_nums
            if sums >= half_cross_length:
                break
        # 完整区域
        cross_degree *= 2
        _,start_degree,cross_degree = self.cal_ellipse_text_info_with_cross(a,b, cross_degree, split_nums,texts,top=top)
        texts = " "*label_nums
        return self.cal_ellipse_text_info_basic(a,b,start_degree,cross_degree,split_nums,texts,top=top)
    
    # 通过对称以及字体计算椭圆坐标以及角度信息，简洁版（推荐）
    def cal_ellipse_text_info_sim(self,a,b,font_size,space,split_nums,texts,top=True):
        # a: 长轴
        # b: 短轴
        # font_size:  wh 文字宽高
        # space: 字间距
        # split_nums: 划分数量
        # texts: 文本
        # top : 上半区还是小半区
        error = 1.1 # 精度，用于调整
        text_len = len(texts)
        cross_length = (font_size[0]*text_len+(text_len-1)*space)*error
        # 一半
        half_cross_length = cross_length // 2
        # 模拟从90~-90的点位置
        xys = self.cal_draw_points(a,b,270,180,split_nums)
        _, part_length_list = self.cal_points_length(xys)
        sums = 0
        cross_degree = 0
        for i in part_length_list:
            sums += i
            cross_degree += 180/split_nums
            if sums >= half_cross_length:
                break
        # 完整区域
        cross_degree *= 2
        return self.cal_ellipse_text_info_with_cross(a,b, cross_degree, split_nums,texts,top=top)
        
    # 计算旋转后文本框四个点
    def cal_text_border_pos(self,center_xy,wh,degree,clock=False):
        # center_xy: 文本框中心
        # wh: 文本框宽高
        # degree: 旋转角度
        # 返回值, r：右边 l:左边 t:顶部 b:底部 m:中间
        #               mt
        #       lt .____.____. rt
        #/      ml !____!____! mr
        #/      lb !____!____! rb
        #               mb
        degree = 180 - degree # 用于调试
        x,y = center_xy
        w,h = [i//2 for i in wh]
        lt,rt,rb,lb = [x-w,y+h],[x+w,y+h],[x+w,y-h],[x-w,y-h]
        ml,mt,mr,mb = [x-w,y],[x,y+h],[x+w,y],[x,y-h]
        new_lt = self.cal_rotate_at_fix_point(degree,*lt,x,y,clock=clock)
        new_rt = self.cal_rotate_at_fix_point(degree,*rt,x,y,clock=clock)
        new_rb = self.cal_rotate_at_fix_point(degree,*rb,x,y,clock=clock)
        new_lb = self.cal_rotate_at_fix_point(degree,*lb,x,y,clock=clock)
        
        new_ml = self.cal_rotate_at_fix_point(degree,*ml,x,y,clock=clock)
        new_mt = self.cal_rotate_at_fix_point(degree,*mt,x,y,clock=clock)
        new_mr = self.cal_rotate_at_fix_point(degree,*mr,x,y,clock=clock)
        new_mb = self.cal_rotate_at_fix_point(degree,*mb,x,y,clock=clock)
        return new_lt,new_rt,new_rb,new_lb, new_ml,new_mt,new_mr, new_mb
    
    # 计算文本与标签，合成版，
    def cal_text_and_label_pos(self,ellipse_ab,txt_wh,space,texts, label_nums=28, split_nums=1000,top=True):
        # ellipse_ab : 椭圆长短轴
        # txt_wh : 文字宽高
        # space : 文字间距
        # texts : 文本
        # label_nums :标签数量，上下包含
        infos,_,_ = self.cal_ellipse_text_info_sim(*ellipse_ab, txt_wh, space, split_nums,texts, top=top)
        label_infos,_,_ = self.cal_ellipse_text_label_info_sim(*ellipse_ab, txt_wh, space, split_nums,texts, label_nums//2, top=top)
        label_top,label_buttom = [],[]
        for char,x,y,degree in label_infos:
            lt,rt,rb,lb,ml,mt,mr,mb = self.cal_text_border_pos([x,y],txt_wh[::-1],degree,clock=True)
            label_top.append(mt)
            label_buttom.append(mb)
        if top:
            label_info = label_buttom[::-1] + label_top
        else:
            label_info = label_buttom + label_top[::-1]
        return infos, label_info
    
    def cal_text_and_label_pos(self,ellipse_ab,txt_wh,space,texts, label_nums=28, split_nums=1000,top=True):
        # ellipse_ab : 椭圆长短轴
        # txt_wh : 文字宽高
        # space : 文字间距
        # texts : 文本
        # label_nums :标签数量，上下包含
        infos,_,_ = self.cal_ellipse_text_info_sim(*ellipse_ab, txt_wh, space, split_nums,texts, top=top)
        label_infos,_,_ = self.cal_ellipse_text_label_info_sim(*ellipse_ab, txt_wh, space, split_nums,texts, label_nums//2, top=top)
        label_top,label_buttom = [],[]
        for char,x,y,degree in label_infos:
            lt,rt,rb,lb,ml,mt,mr,mb = self.cal_text_border_pos([x,y],txt_wh[::-1],degree,clock=True)
            label_top.append(mt)
            label_buttom.append(mb)
        if top:
            label_info = label_buttom[::-1] + label_top
        else:
            label_info = label_buttom + label_top[::-1]
        return infos, label_info
    
    
    def cal_every_text_and_label_pos(self,ellipse_ab,txt_wh,space,texts,split_nums=1000,top=True):
        # ellipse_ab : 椭圆长短轴
        # txt_wh : 文字宽高
        # space : 文字间距
        # texts : 文本
        infos,_,_ = self.cal_ellipse_text_info_sim(*ellipse_ab, txt_wh, space, split_nums,texts, top=top)
        every_label = []
        if top:
            for char,x,y,degree in infos[::-1]:
                lt,rt,rb,lb,ml,mt,mr,mb = self.cal_text_border_pos([x,y],txt_wh[::-1],degree,clock=True)
                every_label.append([rb,lb,lt,rt,char])
        else:
            for char,x,y,degree in infos:
                lt,rt,rb,lb,ml,mt,mr,mb = self.cal_text_border_pos([x,y],txt_wh[::-1],degree,clock=True)
                every_label.append([rb,lb,lt,rt,char])
        return infos, every_label
        
    # 计算矩形文本，指定标注数量
    def cal_rec_text_pos_label(self,txt_wh,space,texts,label_nums=4):
        """计算矩形文本的文字中心坐标以及指定标注数目的标签坐标

        Args:
            # rec_wh (list | tuple): 矩形文本行的宽高
            txt_wh (_type_): 文字的宽高
            space (_type_): 文字间距
            texts (_type_): 文字
            label_nums (int, optional): 文本行标注数目，包含上下. Defaults to 4.

        Returns:
            _type_: 文本中心以及文本行标注
        """
        error = 1.1 # 精度，用于调整
        label_error = 1.1 # 精度，用于调整
        text_len = len(texts)
        # 文本的长度
        text_cross_length = (txt_wh[0]*text_len+(text_len-1)*space)*error
        per_text_length = text_cross_length/(text_len-1)
        start_pos = text_cross_length//2
        text_pos = [[-start_pos+per_text_length*i, 0] for i in range(text_len)]
        infos = []
        for i in range(text_len):
            infos.append([texts[i],*(text_pos[i]),0])
        
        
        # 标注的长度
        label_cross_length = (txt_wh[0]*text_len+text_len*space)*label_error
        # 一半标签
        per_label_length = label_cross_length/(label_nums//2-1)
        start_pos = label_cross_length // 2
        label_pos = [[-start_pos+per_label_length*i, txt_wh[1]//2] for i in range(label_nums//2)]
        label_pos += [[start_pos-per_label_length*i, -txt_wh[1]//2] for i in range(label_nums//2)]
        return infos, label_pos

            