# 图像处理
# 合并图片，合并多张图片

import PIL.Image as Image
import matplotlib.pyplot as plt
import numpy as np
import random

def xywh2xyxyxyxy(x,y,w,h):
    return [[x,y],[x+w,y],[x+w,y+h],[x,y+h]]

def merge_image(fore_image, back_image, fore_pos=(0,0),fore_alpha=1.0,fore_factor=1.0,back_padding=False,fore_func=lambda x:x):
    """将两个图片进行合并，支持自定义透明度 alpha, 缩放factor, 背景图缩放开关 padding, 前景图回调函数 func

    Args:
        fore_image (PIL.Image): 前景图
        back_image (PIL.Image): 背景图
        fore_pos (tuple, list): 左上角位置. Defaults to (0,0).
        fore_alpha (float, optional): 前景透明度. Defaults to 1.0.
        fore_factor (float, optional): 前景缩放因子. Defaults to 1.0.
        back_padding (bool, optional): 背景自适应缩放. Defaults to False.
        fore_func (Functional, optional): 前景处理回调函数. Defaults to lambdax:x.

    Returns:
        PIL.Image: 合并后的图片
    """
    assert fore_alpha <= 1.0, "Alpha must be less or equel than 1.0"
    final_image = back_image.copy() 
    fore_image_temp = fore_image.copy()   
    
    # 设置缩放因子 透明度
    fore_w, fore_h  = fore_image_temp.size
    fore_new_w = int(fore_w / fore_factor)
    fore_new_h = int(fore_h / fore_factor)
    fore_image_temp = fore_image_temp.resize((fore_new_w, fore_new_h), Image.Resampling.LANCZOS)
    fore_w, fore_h  = fore_image_temp.size
    for i in range(fore_new_w):
        for k in range(fore_new_h):
            color = fore_image_temp.getpixel((i, k))
            color = color[:-1] + (int((color[-1]*fore_alpha)%255), )
            fore_image_temp.putpixel((i, k), color)

    fore_image_temp = fore_func(fore_image_temp)

    # 背景图不够大将会被resize
    if back_padding:
        back_limit_w = fore_new_w + fore_pos[0]
        back_limit_h = fore_new_h + fore_pos[1]
    else:
        back_limit_w = fore_new_w
        back_limit_h = fore_new_h
    
    # 设置背景图片大小
    back_w, back_h = final_image.size
    # 设置背景图大小
    if back_w < back_limit_w:
        back_new_w = back_limit_w
        print(f"背景图宽度过小, {back_w} < {back_limit_w}")
    if back_h < back_limit_h:
        back_new_h = back_limit_h
        print(f"背景图高度过小, {back_h} < {back_limit_h}")
    back_new_w = back_w
    back_new_h = back_h
    final_image = final_image.resize((back_new_w,back_new_h),Image.Resampling.LANCZOS)
    
    final_image.paste(fore_image_temp, fore_pos, mask=fore_image_temp)
    fore_final_w, fore_final_h  = fore_image_temp.size
    back_final_w, back_final_h =final_image.size
    label_x = fore_pos[0] if fore_pos[0]>0 else 0
    label_y = fore_pos[1] if fore_pos[1]>0 else 0
    label_w = fore_pos[0]+fore_final_w-label_x if fore_pos[0]+fore_final_w < back_final_w else back_final_w-label_x
    label_h = fore_pos[1]+fore_final_h-label_y if fore_pos[1]+fore_final_h < back_final_h else back_final_h-label_y
    
    return final_image, xywh2xyxyxyxy(label_x,label_y,label_w,label_h)

def random_merge_images(fore_images,back_image,fore_poss=None,fore_alphas = None ,fore_factors = None, fore_full = True, fore_func = lambda x : x):
    
    final_image = back_image.copy()
    back_w, back_h = final_image.size
    
    image_nums = len(fore_images)
    if fore_alphas == None:
        fore_alphas = [random.randint(1,100)/100 for i in range(image_nums)]
    elif isinstance(fore_alphas, (float,int)):
        fore_alphas = [fore_alphas]*image_nums
    elif isinstance(fore_alphas, (tuple,list)):
        pass
    else:
        print(f"fore_alphas error {fore_alphas}")
        
    if fore_factors == None:
        fore_factors = [random.randint(1,20)/10 for i in range(image_nums)]
    elif isinstance(fore_factors, (float,int)):
        fore_factors = [fore_factors]*image_nums
    elif isinstance(fore_factors, (tuple,list)):
        pass
    else:
        print(f"fore_factors error {fore_factors}")
    
    # print(fore_alphas,fore_factors)
    if isinstance(fore_poss, (float,int)) or fore_poss == None:
        fore_poss = []
        for i in range(image_nums): 
            # 避免前景超出背景范围
            if fore_full:
                fw,fh = fore_images[i].size
                max_h = back_h - fh
                max_w = back_w - fw
                if max_h <0 or max_w <0:
                    print("背景图太小了，前景图太大")
                    max_h = back_h
                    max_w = back_w
                    fore_poss.append(None)
                    continue
            else:
                max_h = back_h
                max_w = back_w
            x = random.randint(0,max_w-1)
            y = random.randint(0,max_h-1)
            fore_poss.append([x,y])
    else:
        pass
    labels = []
    for i in range(image_nums): 
        fore_image = fore_images[i]
        fore_alpha = fore_alphas[i]
        fore_factor = fore_factors[i] 
        fore_pos = fore_poss[i]
        if fore_pos == None:
            continue
        # print(fore_image.size,fore_alpha,fore_factor,fore_pos)
        final_image,label = merge_image(fore_image, final_image, fore_pos=fore_pos, fore_alpha=fore_alpha, fore_factor=fore_factor, back_padding=False, fore_func=fore_func)
        print("label",label)
        labels.append(label)
    return final_image,labels


if __name__ == '__main__':
    fore_image = Image.open("fore/hh.png").convert("RGBA")
    back_image = Image.open("back/bg01.png").convert("RGBA").resize((1000,1000))
    # print(back_image.size)
    # final_image,label = merge_image(fore_image, back_image,fore_pos=(100,100),back_padding=0,fore_alpha=0.5)
    # label = np.array(label)
    # plt.figure()
    # plt.subplot(1,3,1)
    # plt.imshow(fore_image)
    # plt.subplot(1,3,2)
    # plt.imshow(back_image)
    # plt.subplot(1,3,3)
    # plt.imshow(final_image)
    # plt.scatter(label[:,0],label[:,1],marker='.',linewidths=1)
    # plt.show()
    
    
    final_image,labels = random_merge_images([fore_image]*5,back_image,fore_poss=None, fore_alphas=0.5)
    ##plt 同时显示多幅图像
    label = np.array(labels)
    # print([:,0])
    
    plt.figure()
    plt.subplot(1,3,1)
    plt.imshow(fore_image)
    plt.subplot(1,3,2)
    plt.imshow(back_image)
    plt.subplot(1,3,3)
    plt.imshow(final_image)
    plt.scatter(label[:,:,0],label[:,:,1],marker='.',linewidths=1)
    plt.show()
    print("结束")
    while True:
        pass
