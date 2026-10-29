from PIL import Image, ImageDraw, ImageFont
import numpy as np
D="/usr/share/fonts/opentype/inter/"
F=lambda n,s: ImageFont.truetype(D+n,s)
I="/home/claude/laterretagames-media/inbox/2026-w44/"
ACC=(59,130,246);TXT=(255,255,255);MUT=(148,163,184)
def bg(p,leftdark=0.0):
    im=Image.open(p).convert("RGB"); w,h=im.size; nh=int(w*9/16); y=(h-nh)//2
    im=im.crop((0,y,w,y+nh)).resize((1600,900),Image.LANCZOS)
    a=np.asarray(im).astype(float)
    x=np.linspace(0,1,1600)[None,:,None]
    a*= (1-leftdark*np.clip(1-x/0.6,0,1))
    return Image.fromarray(a.astype(np.uint8))
def wrap(d,t,f,mw):
    o=[];c=""
    for w in t.split():
        x=(c+" "+w).strip()
        if d.textlength(x,font=f)<=mw:c=x
        else:o.append(c);c=w
    o.append(c);return o
def brand(d):
    m=90
    d.text((m,900-m-70),"AppWatch",font=F("Inter-ExtraBold.otf",38),fill=TXT)
    d.text((m,900-m-24),"by La Terreta Games",font=F("Inter-Regular.otf",26),fill=MUT)
    f=F("Inter-SemiBold.otf",30);t="appwatch.dev";d.text((1600-m-d.textlength(t,font=f),900-m-30),t,font=f,fill=ACC)
# Tue
im=bg(I+"tue.png"); d=ImageDraw.Draw(im); m=90
d.rectangle([0,0,1600,10],fill=ACC)
d.text((m,80),"STORE LISTING EXPERIMENTS",font=F("Inter-Bold.otf",30),fill=ACC)
f=F("InterDisplay-ExtraBold.otf",76);y=160
for l in wrap(d,"Changed your store listing. Did it help?",f,1050): d.text((m,y),l,font=f,fill=TXT);y+=94
d.text((m,y+10),"Before and after, from the day it went live.",font=F("Inter-Regular.otf",36),fill=MUT)
brand(d); im.save("w44-tue-x-linkedin-ai.png")
# Thu
im=bg(I+"thu.png",0.75); d=ImageDraw.Draw(im)
d.rectangle([0,0,1600,10],fill=ACC)
d.text((m,80),"STEAM IN APPWATCH",font=F("Inter-Bold.otf",30),fill=ACC)
f=F("InterDisplay-ExtraBold.otf",64);y=150
for l in wrap(d,"\"It feels like it's going well\" is not a metric.",f,720): d.text((m,y),l,font=f,fill=TXT);y+=80
f=F("Inter-SemiBold.otf",34);y+=30
for t in ["Refund rate","Review score trend","Price & discount history","Steam Deck compatibility"]:
    d.ellipse([m,y+10,m+20,y+30],fill=ACC); d.text((m+42,y),t,font=f,fill=TXT); y+=58
brand(d); im.save("w44-thu-x-linkedin-facebook-ai.png")
