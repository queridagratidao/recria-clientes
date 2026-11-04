from PIL import Image, ImageEnhance, ImageFilter
A='/mnt/user-data/attachments/5356abd7-a95d-530a-916e-477012a99e54/'
def fit(f,out,top=0.0,bright=1.03,col=1.0,smooth=False):
    im=Image.open(A+f).convert('RGB'); w,h=im.size
    tw,th=(w,int(w*1.25)) if h/w>=1.25 else (int(h*0.8),h)
    x=(w-tw)//2; y=int((h-th)*top)
    im=im.crop((x,y,x+tw,y+th)).resize((1080,1350),Image.LANCZOS)
    if smooth:
        b=im.filter(ImageFilter.GaussianBlur(2.2)); e=im.filter(ImageFilter.FIND_EDGES).convert('L').filter(ImageFilter.GaussianBlur(3)).point(lambda v:255 if v>18 else v*14)
        im=Image.composite(im,Image.blend(im,b,.55),e)
    im=ImageEnhance.Brightness(im).enhance(bright); im=ImageEnhance.Color(im).enhance(col)
    im.save('src/'+out,quality=92)
fit('629be70c-image.png','n5_nb11.jpg',bright=1.04)
fit('5a73c92d-image.png','n5_nb25.jpg',top=0.0,bright=1.0,smooth=True)
fit('9eb037b3-image.jpg','n5_d10.jpg',top=0.6,bright=1.05,col=.92)
fit('bbf465a5-image.png','n5_d24.jpg',bright=1.06)
for a,b in [('7c5a1a2e','k')]: pass
import glob
S='/tmp/claude-chrome-screenshots-8voOxb/'
for n,f in [('manfroi','screenshot-1793801748999-10.png'),('fridel','screenshot-1793801749000-11.png'),('kati','screenshot-1793801748999-9.png')]:
    Image.open(S+f).convert('RGB').resize((300,300),Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2,60)).save(f'src/av_{n}.jpg',quality=93)
print('ok')
