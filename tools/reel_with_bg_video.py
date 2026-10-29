import numpy as np, wave, subprocess, math
from PIL import Image, ImageDraw, ImageFont
D="/usr/share/fonts/opentype/inter/"
F=lambda n,s: ImageFont.truetype(D+n,s)
W,H,FPS=1080,1920,30; SC=5.5; N=4; T=SC*N
BG=(11,18,32); ACC=(59,130,246); TXT=(255,255,255); MUT=(148,163,184); CARD=(22,33,54)
ease=lambda x: 1-(1-min(max(x,0),1))**3
scenes=[("A PUBLIC ROADMAP",["We keep our","roadmap","public."]),
        ("SHIPPED SO FAR",None),
        ("NOT PROMISED YET",["Plus a long list","of ideas we are","not promising."]),
        ("YOUR TURN",["What should","be next?"])]
fh=F("InterDisplay-ExtraBold.otf",120); fl=F("Inter-Bold.otf",40)
fbig=F("InterDisplay-ExtraBold.otf",420); fmid=F("InterDisplay-ExtraBold.otf",96)
import subprocess as sp
R="/home/claude/laterretagames-media/inbox/2026-w44/sat-bg.mp4"
raw=sp.run(["ffmpeg","-loglevel","error","-i",R,"-vf","scale=1080:1920","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
BGF=np.frombuffer(raw,dtype=np.uint8).reshape(-1,H,W,3); NB=len(BGF)
grad=np.linspace(0.45,0.8,H)[:,None,None]  # darker toward bottom
yy=np.linspace(0,1,H)[:,None,None]; dark=0.5+0.3*np.abs(yy-0.45)*2
def bgframe(t):
    k=int(t*24)%(2*NB-2); k=k if k<NB else 2*NB-2-k
    return Image.fromarray((BGF[k]*dark).clip(0,255).astype(np.uint8)).convert("RGBA")
def layer(): return Image.new("RGBA",(W,H),(0,0,0,0))
def txt(ov,xy,s,font,fill,a):
    if a<=0: return
    d=ImageDraw.Draw(ov); d.text(xy,s,font=font,fill=fill+(int(255*min(a,1)),))
def frame(t):
    i=min(int(t//SC),N-1); lt=t-i*SC; m=90
    im=bgframe(t); d=ImageDraw.Draw(im); d.rectangle([0,0,W,10],fill=ACC)
    ov=layer(); lab,lines=scenes[i]
    a=ease(lt/0.4); txt(ov,(m-60*(1-a),300),lab,fl,ACC,a)
    if i==1:
        n=int(round(63*ease(lt/1.8))); s=str(n)
        a=ease((lt-0.1)/0.4); txt(ov,(m,400+30*(1-a)),s,fbig,TXT,a)
        a=ease((lt-0.9)/0.5); txt(ov,(m,860+40*(1-a)),"features shipped.",fmid,TXT,a)
        a=ease((lt-1.8)/0.5); txt(ov,(m,1010+30*(1-a)),"and counting.",F("Inter-SemiBold.otf",56),MUT,a)
    else:
        for k,l in enumerate(lines):
            a=ease((lt-0.25-0.2*k)/0.45); txt(ov,(m,380+k*140+45*(1-a)),l,fh,TXT,a)
        if i==3:
            a=ease((lt-1.0)/0.5); sc=1+0.03*math.sin(lt*5)
            bw,bh=int((W-2*m)*sc),int(120*sc); x0=(W-bw)//2; y0=800
            b=ImageDraw.Draw(ov); b.rounded_rectangle([x0,y0,x0+bw,y0+bh],radius=24,fill=ACC+(int(255*a),))
            f=F("Inter-Bold.otf",54); s="appwatch.dev/roadmap"
            b.text((W/2-b.textlength(s,font=f)/2,y0+bh/2-34),s,font=f,fill=TXT+(int(255*a),))
    # brand + progress
    txt(ov,(m,H-420),"AppWatch",F("Inter-ExtraBold.otf",56),TXT,1)
    txt(ov,(m,H-350),"by La Terreta Games",F("Inter-Regular.otf",36),MUT,1)
    p=ImageDraw.Draw(ov); p.rounded_rectangle([m,H-150,W-m,H-138],radius=6,fill=CARD+(255,))
    p.rounded_rectangle([m,H-150,m+int((W-2*m)*t/T),H-138],radius=6,fill=ACC+(255,))
    f=min(ease(lt/0.3),ease((SC-lt)/0.3))
    if f<1:
        a=ov.getchannel("A").point(lambda v:int(v*f)); ov.putalpha(a)
    im=Image.alpha_composite(im,ov)
    return im.convert("RGB")
# audio
sr=44100; n=int(sr*T); tt=np.arange(n)/sr
pad=sum(np.sin(2*np.pi*f*tt) for f in (110,164.81,220.0,277.18))/4*0.11
pad*= (0.75+0.25*np.sin(2*np.pi*0.25*tt))
# gentle pulse beat (soft kick) every 0.5s
beat=np.zeros(n)
for k in np.arange(0.0,T,0.5):
    s=int(k*sr); L=int(0.18*sr); x=np.arange(L)/sr
    beat[s:s+L]+=np.sin(2*np.pi*(90*np.exp(-x*18)+40)*x)*np.exp(-x*22)*0.16
rng=np.random.default_rng(7); wh=np.zeros(n)
for k in [0,SC,2*SC,3*SC]:
    L=int(0.7*sr); noise=rng.standard_normal(L); x=np.linspace(0,1,L)
    # crude lowpass sweep via cumulative smoothing
    k1=np.convolve(noise,np.ones(40)/40,mode="same")
    env=np.sin(np.pi*x)**2; s=int(k*sr)
    wh[s:s+L]+=k1*env*0.9
ticks=np.zeros(n)
for k in [0.5,SC+0.3,SC+1.0,2*SC+0.5,3*SC+0.5,3*SC+1.2]:
    s=int(k*sr); L=int(0.06*sr); x=np.arange(L)/sr; ticks[s:s+L]+=np.sin(2*np.pi*1400*x)*np.exp(-x*70)*0.18
mix=pad+beat+wh*0.35+ticks
fade=np.minimum(1,np.minimum(tt/0.5,(T-tt)/0.8)); mix*=fade
mix=mix/max(1,np.abs(mix).max()/0.8)
with wave.open("a.wav","wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((mix*32767).astype(np.int16).tobytes())
p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-i","a.wav","-c:v","libx264","-pix_fmt","yuv420p","-crf","23","-c:a","aac","-b:a","128k","-shortest","-movflags","+faststart","w44-sat-reel-ai.mp4"],stdin=subprocess.PIPE)
for fi in range(int(T*FPS)): p.stdin.write(frame(fi/FPS).tobytes())
p.stdin.close(); p.wait()
for t in (1.0,7.2,10.0,21.0): frame(t).save(f"v2chk{int(t*10)}.png")
