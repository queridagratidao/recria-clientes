from PIL import Image, ImageEnhance, ImageFilter
import numpy as np, cv2, pillow_heif
pillow_heif.register_heif_opener()
A='/mnt/user-data/attachments/5356abd7-a95d-530a-916e-477012a99e54/'
def fitim(im,out,top=0.0,bright=1.03,box=None):
    im=im.convert('RGB')
    if box: im=im.crop(box)
    w,h=im.size
    tw,th=(w,int(w*1.25)) if h/w>=1.25 else (int(h*0.8),h)
    x=(w-tw)//2; y=int((h-th)*top)
    im=im.crop((x,y,x+tw,y+th)).resize((1080,1350),Image.LANCZOS)
    im=ImageEnhance.Brightness(im).enhance(bright); im.save('src/'+out,quality=92); return im
# Bel avatar: top part (avoid text)
av=Image.open('/tmp/claude-chrome-screenshots-2oyHFd/screenshot-1793803696477-0.png').convert('RGB')
av.crop((14,0,86,72)).resize((300,300),Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2,60)).save('src/av_bel.jpg',quality=93)
fitim(Image.open('src/p_corpo.jpg'),'n6_d03capa.jpg')
fitim(Image.open('src/p_perfil.jpg'),'n6_d03cta.jpg')
# sunglasses: inpaint DKNY logo
im=Image.open(A+'23d18c68-image.png').convert('RGB'); a=np.array(im)
g=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY); m=np.zeros_like(g)
roi=g[1150:1330,250:560]; m[1150:1330,250:560]=(roi>120).astype(np.uint8)*255
m=cv2.dilate(m,np.ones((9,9),np.uint8))
a=cv2.inpaint(a,m,9,cv2.INPAINT_TELEA); Image.fromarray(a).save('src/n6_sun.jpg',quality=92)
fitim(Image.fromarray(a),'n6_sun.jpg',bright=1.0)
fitim(Image.open(A+'de19a0fc-image.jpg'),'n6_snow.jpg',top=0.5)
fitim(Image.open(A+'0137de42-image.png'),'n6_corr.jpg')
fitim(Image.open(A+'71649135-image.png'),'n6_vald.jpg',box=(0,250,1080,1350),top=0)
fitim(Image.open(A+'9eb037b3-image.jpg'),'n6_pool.jpg',top=0.4,bright=1.05)
print('ok')
