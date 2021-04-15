import math
from datetime import datetime

def createBase_o(path, xh, w, t, r):
    path.moveTo((w*r, xh+t/2))
    path.lineTo((w*(1-r), xh+t/2))
    path.qCurveTo((w+t/2, xh+t/2), (w+t/2, xh*(1-r)))
    path.lineTo((w+t/2, xh*r))
    path.qCurveTo((w+t/2, -t/2), (w*(1-r), -t/2))
    path.lineTo((w*r, -t/2))
    path.qCurveTo((-t/2, -t/2), (-t/2, r*xh))
    path.lineTo((-t/2, xh*(1-r)))
    path.qCurveTo((-t/2, xh + t/2),(w*r, xh+t/2))
    path.closePath()
    
    path.moveTo((w*r, xh-t/2))
    path.qCurveTo((t/2, xh-t/2), (t/2, xh*(1-r)))
    path.lineTo((t/2, xh*r))
    path.qCurveTo((t/2, t/2), (w*r, t/2))
    path.lineTo((w*(1-r), t/2))
    path.qCurveTo((w-t/2, t/2), (w-t/2, xh*r))
    path.lineTo((w-t/2, xh*(1-r)))
    path.qCurveTo((w-t/2, xh-t/2), (w*(1-r), xh-t/2))
    path.lineTo((w*r, xh-t/2))
    path.closePath()
    
def createDot(path, x, y, t, r):
    #Dot ratio
    dr = t*(1+r)
    
    path.moveTo((x, y+dr/2))
    path.qCurveTo((x+dr/2, y+dr/2), (x+dr/2, y))
    path.qCurveTo((x+dr/2, y-dr/2), (x, y-dr/2))
    path.qCurveTo((x-dr/2, y-dr/2), (x-dr/2, y))
    path.qCurveTo((x-dr/2, y+dr/2), (x, y+dr/2))
    path.closePath()
        
def glyph_a(font, xh, a, d, w, t, s, r):    
    glyph = font.newGlyph("a")
    glyph.unicode = ord("a")
    
    #print('w:', w, 't:', t, 'r:', r)
    
    path = glyph.getPen()
    
    path.moveTo((0,xh*2/3))
    path.qCurveTo((0, xh+t/2), (w*r, xh+t/2))
    path.lineTo((w*(1-r),xh+t/2))
    path.qCurveTo((w, xh+t/2), (w, xh*2/3))
    path.lineTo((w,0))
    
    path.lineTo((w-t, 0))
    path.lineTo((w-t, xh*2/3))
    path.qCurveTo((w-t, xh-t/2),(w*(1-r), xh-t/2))
    path.lineTo((w*r, xh-t/2))
    path.qCurveTo((t, xh-t/2), (t, xh*2/3))
    path.closePath()
    
    path.moveTo((w-t, 5/6*xh-t))
    path.qCurveTo((w-t, 2/3*xh-t),(w-t-50, 2/3*xh-t))
    path.lineTo((w*r, 2/3*xh-t))
    path.qCurveTo((t, 2/3*xh-t), (t, 1/3*xh)) 
    path.qCurveTo((t,t),(w*r,t))
    path.lineTo((w*(1-r), t))
    path.qCurveTo((w-t, t),(w-t, 1/6*xh+t))
    path.lineTo((w-t, 1/6*xh))
    path.qCurveTo((w-t, 0), (w*(1-r), 0))
    path.lineTo((w*r, 0))
    path.qCurveTo((0, 0),(0, 1/3*xh))
    path.qCurveTo((0, 2/3*xh),(w*r, 2/3*xh))
    path.lineTo((w-t-50,2/3*xh))
    path.qCurveTo((w-t, 2/3*xh),(w-t,5/6*xh))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_ä(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("ä")
    glyph.unicode = ord("ä")
    
    path = glyph.getPen()
    
    path.moveTo((0,xh*2/3))
    path.qCurveTo((0, xh+t/2), (w*r, xh+t/2))
    path.lineTo((w*(1-r),xh+t/2))
    path.qCurveTo((w, xh+t/2), (w, xh*2/3))
    path.lineTo((w,0))
    
    path.lineTo((w-t, 0))
    path.lineTo((w-t, xh*2/3))
    path.qCurveTo((w-t, xh-t/2),(w*(1-r), xh-t/2))
    path.lineTo((w*r, xh-t/2))
    path.qCurveTo((t, xh-t/2), (t, xh*2/3))
    path.closePath()
    
    path.moveTo((w-t, 5/6*xh-t))
    path.qCurveTo((w-t, 2/3*xh-t),(w-t-50, 2/3*xh-t))
    path.lineTo((w*r, 2/3*xh-t))
    path.qCurveTo((t, 2/3*xh-t), (t, 1/3*xh)) 
    path.qCurveTo((t,t),(w*r,t))
    path.lineTo((w*(1-r), t))
    path.qCurveTo((w-t, t),(w-t, 1/6*xh+t))
    path.lineTo((w-t, 1/6*xh))
    path.qCurveTo((w-t, 0), (w*(1-r), 0))
    path.lineTo((w*r, 0))
    path.qCurveTo((0, 0),(0, 1/3*xh))
    path.qCurveTo((0, 2/3*xh),(w*r, 2/3*xh))
    path.lineTo((w-t-50,2/3*xh))
    path.qCurveTo((w-t, 2/3*xh),(w-t,5/6*xh))
    path.closePath()

    createDot(path, t*2, xh+t*2, t, r)
    createDot(path, w-t*2, xh+t*2, t, r)
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
            
def glyph_b(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("b")
    glyph.unicode = ord("b")
    
    path = glyph.getPen()
    createBase_o(path, xh, w, t, r)
    
    path.moveTo((-t/2, 0))
    path.lineTo((-t/2,a))
    path.lineTo((t/2, a))
    path.lineTo((t/2, 0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_c(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("c")
    glyph.unicode = ord("c")
    
    path = glyph.getPen()
    
    path.moveTo((w-t/2, xh*(1-r)))
    path.qCurveTo((w-t/2, xh-t/2), (w*(1-r), xh-t/2))
    path.lineTo((w*r, xh-t/2))
    path.qCurveTo((t/2, xh-t/2), (t/2,xh*(1-r)))
    path.lineTo((t/2, xh*r))
    path.qCurveTo((t/2, t/2), (w*r, t/2))
    path.lineTo((w*(1-r),t/2))
    path.qCurveTo((w-t/2, t/2), (w-t/2, xh*r))
    
    path.lineTo((w+t/2, xh*r))
    path.qCurveTo((w+t/2, -t/2), (w*(1-r), -t/2))
    path.lineTo((w*r,-t/2))
    path.qCurveTo((-t/2, -t/2), (-t/2, xh*r))
    path.lineTo((-t/2, xh*(1-r)))
    path.qCurveTo((-t/2, xh+t/2), (w*r,xh+t/2))
    path.lineTo((w*(1-r), xh+t/2))
    path.qCurveTo((w+t/2, xh+t/2), (w+t/2,xh*(1-r)))
    path.closePath()    
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s

def glyph_d(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("d")
    glyph.unicode = ord("d")
    
    path = glyph.getPen()
    createBase_o(path, xh, w, t, r)
    
    path.moveTo((w-t/2, a))
    path.lineTo((w+t/2, a))
    path.lineTo((w+t/2, -t/2))
    path.qCurveTo((w-t/2, -t/2), (w-t/2, t/2-t*r/2))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_e(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("e")
    glyph.unicode = ord("e")
    
    path = glyph.getPen()
    
    path.moveTo((w-t/2, xh*(1-r)))
    path.qCurveTo((w-t/2, xh-t/2), (w*(1-r), xh-t/2))
    path.lineTo((w*r, xh-t/2))
    path.qCurveTo((t/2, xh-t/2), (t/2,xh*(1-r)))
    path.lineTo((t/2, xh*r))
    path.qCurveTo((t/2, t/2), (w*r, t/2))
    path.lineTo((w*(1-r),t/2))
    path.qCurveTo((w-t/2, t/2), (w-t/2, xh*r))
    
    path.lineTo((w+t/2, xh*r))
    path.qCurveTo((w+t/2, -t/2), (w*(1-r), -t/2))
    path.lineTo((w*r,-t/2))
    path.qCurveTo((-t/2, -t/2), (-t/2, xh*r))
    path.lineTo((-t/2, xh*(1-r)))
    path.qCurveTo((-t/2, xh+t/2), (w*r,xh+t/2))
    path.lineTo((w*(1-r), xh+t/2))
    path.qCurveTo((w+t/2, xh+t/2), (w+t/2,xh*(1-r)))
    
    path.lineTo((w+t/2,xh/2+1))
    path.lineTo((t/2,xh/2+1))
    path.lineTo((t/2,xh/2+t+1))
    path.lineTo((w-t/2,xh/2+t+1))
    path.closePath()    
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_f(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("f")
    glyph.unicode = ord("f")
    
    path = glyph.getPen()
    
    top = a - xh
    
    path.moveTo((w-t/2, xh+top*(1-r)))
    path.qCurveTo((w-t/2, a-t/2), (w*(1-r), a-t/2))
    path.lineTo((w*r, a-t/2))
    path.qCurveTo((t/2, a-t/2), (t/2,xh+top*(1-r)))
    
    path.lineTo((t/2, xh))
    path.lineTo((w*(1-r), xh))
    path.lineTo((w*(1-r), xh-t))
    path.lineTo((t/2, xh-t))
    path.lineTo((t/2, 0))
    path.lineTo((-t/2, 0))
    path.lineTo((-t/2, xh))
    
    path.lineTo((-t/2, xh+top*(1-r)))
    path.qCurveTo((-t/2, a+t/2), (w*r,a+t/2))
    path.lineTo((w*(1-r), a+t/2))
    path.qCurveTo((w+t/2, a+t/2), (w+t/2,xh+top*(1-r)))
    
    
    
    path.closePath()    
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_g(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("g")
    glyph.unicode = ord("g")
    
    path = glyph.getPen()
    
    createBase_o(path, xh, w, t, r)
    
    path.moveTo((w-t/2, 0))
    path.lineTo((w-t/2, xh))
    path.lineTo((w+t/2, xh))
    path.lineTo((w+t/2, 0))
    
    path.lineTo((w+t/2, d+(xh*1/3)))
    path.qCurveTo((w+t/2, d-t/2), (w*(1-r), d-t/2))
    path.lineTo((w*r, d-t/2))
    path.qCurveTo((0, d-t/2), (0, d+(xh*1/3)))
    
    path.lineTo((t, d+(xh*1/3)))
    path.qCurveTo((t, d+t/2),(w*r, d+t/2))
    path.lineTo((w*(1-r), d+t/2))
    path.qCurveTo((w-t/2, d+t/2), (w-t/2, d+(xh*1/3)))
    
    
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s 

def glyph_h(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("h")
    glyph.unicode = ord("h")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, a))
    path.lineTo((t, a))
    path.lineTo((t, 0))
    path.closePath()
    
    path.moveTo((0,0))
    path.lineTo((0, 2/3*xh))
    path.qCurveTo((0, xh+t/2), (w*r, xh+t/2))
    path.lineTo((w*(1-r), xh+t/2))
    path.qCurveTo((w, xh+t/2), (w, xh*2/3))
    path.lineTo((w,0))
    path.lineTo((w-t,0))
    path.lineTo((w-t, 2/3*xh))
    path.qCurveTo((w-t, xh-t/2), (w*(1-r), xh-t/2))
    path.lineTo((w*r, xh-t/2))
    path.qCurveTo((t, xh-t/2), (t, xh*2/3))
    path.lineTo((t,0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s  
    
def glyph_ı(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("idotless")
    glyph.unicode = ord("ı")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh))
    path.lineTo((t, xh))
    path.lineTo((t, 0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s  
    
def glyph_i(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("i")
    glyph.unicode = ord("i")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh))
    path.lineTo((t, xh))
    path.lineTo((t, 0))
    path.closePath()
    
    createDot(path, t/2, xh+t*2, t, r)
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s 
    
def glyph_l(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("l")
    glyph.unicode = ord("l")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, a+t/2))
    path.qCurveTo((t, a+t/2), (t, a-t/2+t*r/2))
    path.lineTo((t, a))
    path.lineTo((t, 0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s  
    
def glyph_m(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("m")
    glyph.unicode = ord("m")
    
    m = w*0.8
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh+t/2))
    path.qCurveTo((t, xh+t/2), (t, xh-t/2+t*r/2))
    path.lineTo((t, 0))
    path.closePath()
    
    path.moveTo((0,0))
    path.lineTo((0, 2/3*xh))
    path.qCurveTo((0, xh+t/2), (m*r, xh+t/2))
    path.lineTo((m*(1-r), xh+t/2))
    path.qCurveTo((m+t/2, xh+t/2), (m+t/2, xh*2/3))
    path.lineTo((m+t/2,0))
    path.lineTo((m-t/2,0))
    path.lineTo((m-t/2, 2/3*xh))
    path.qCurveTo((m-t/2, xh-t/2), (m*(1-r), xh-t/2))
    path.lineTo((m*r, xh-t/2))
    path.qCurveTo((t, xh-t/2), (t, xh*2/3))
    path.lineTo((t,0))
    path.closePath()
    
    path.moveTo((m-t/2,0))
    path.lineTo((m-t/2, 2/3*xh))
    path.qCurveTo((m-t/2, xh+t/2), (m+m*r, xh+t/2))
    path.lineTo((m+m*(1-r), xh+t/2))
    path.qCurveTo((m+m, xh+t/2), (m+m, xh*2/3))
    path.lineTo((m+m,0))
    path.lineTo((m+m-t,0))
    path.lineTo((m+m-t, 2/3*xh))
    path.qCurveTo((m+m-t, xh-t/2), (m+m*(1-r), xh-t/2))
    path.lineTo((m+m*r, xh-t/2))
    path.qCurveTo((m+t/2, xh-t/2), (m+t/2, xh*2/3))
    path.lineTo((m+t/2,0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s    

def glyph_n(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("n")
    glyph.unicode = ord("n")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh+t/2))
    path.qCurveTo((t, xh+t/2), (t, xh-t/2+t*r/2))
    path.lineTo((t, 0))
    path.closePath()
    
    path.moveTo((0,0))
    path.lineTo((0, 2/3*xh))
    path.qCurveTo((0, xh+t/2), (w*r, xh+t/2))
    path.lineTo((w*(1-r), xh+t/2))
    path.qCurveTo((w, xh+t/2), (w, xh*2/3))
    path.lineTo((w,0))
    path.lineTo((w-t,0))
    path.lineTo((w-t, 2/3*xh))
    path.qCurveTo((w-t, xh-t/2), (w*(1-r), xh-t/2))
    path.lineTo((w*r, xh-t/2))
    path.qCurveTo((t, xh-t/2), (t, xh*2/3))
    path.lineTo((t,0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s   
    
def glyph_o(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("o")
    glyph.unicode = ord("o")
    
    path = glyph.getPen()
    createBase_o(path, xh, w, t, r)
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s 
    
def glyph_ö(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("ö")
    glyph.unicode = ord("ö")
    
    path = glyph.getPen()
    createBase_o(path, xh, w, t, r)
    createDot(path, t*2, xh+t*2, t, r)
    createDot(path, w-t*2, xh+t*2, t, r)
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s 
    
def glyph_p(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("p")
    glyph.unicode = ord("p")
    
    path = glyph.getPen()
    createBase_o(path, xh, w, t, r)
    
    path.moveTo((-t/2, -a+xh))
    path.lineTo((-t/2, xh+t/2))
    path.qCurveTo((t/2, xh+t/2), (t/2, xh-t/2+t*r/2))
    path.lineTo((t/2, -a+xh))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s

def glyph_q(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("q")
    glyph.unicode = ord("q")
    
    path = glyph.getPen()
    createBase_o(path, xh, w, t, r)
    
    path.moveTo((w-t/2, -a+xh))
    path.lineTo((w-t/2,xh))
    path.lineTo((w+t/2, xh))
    path.lineTo((w+t/2, -a+xh))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_r(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("r")
    glyph.unicode = ord("r")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh+t/2))
    path.qCurveTo((t, xh+t/2), (t, xh-t/2+t*r/2))
    path.lineTo((t, 0))
    path.closePath()
    
    path.moveTo((0, xh*(1-r)))
    path.qCurveTo((0, xh+t/2), (w*r, xh+t/2))
    path.lineTo((w*(1-r),xh+t/2))
    path.lineTo((w*(1-r),xh-t/2))
    path.lineTo((w*r, xh-t/2))
    path.qCurveTo((t, xh-t/2), (t, xh*(1-r)))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s   
    
def glyph_u(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("u")
    glyph.unicode = ord("u")
    
    path = glyph.getPen()
    
    path.moveTo((0,xh))
    path.lineTo((0, 1/3*xh))
    path.qCurveTo((0, -t/2), (w*r, -t/2))
    path.lineTo((w*(1-r), -t/2))
    path.qCurveTo((w, -t/2), (w, xh*1/3))
    path.lineTo((w-t, 1/3*xh))
    path.qCurveTo((w-t, t/2), (w*(1-r), t/2))
    path.lineTo((w*r, t/2))
    path.qCurveTo((t, t/2), (t, xh*1/3))
    path.lineTo((t,xh))
    path.closePath()
    
    path.moveTo((w-t, +t/2-t*r/2))
    path.qCurveTo((w-t, -t/2), (w, -t/2))
    path.lineTo((w, xh))
    path.lineTo((w-t, xh))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_ü(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("ü")
    glyph.unicode = ord("ü")
    
    path = glyph.getPen()
    
    path.moveTo((0,xh))
    path.lineTo((0, 1/3*xh))
    path.qCurveTo((0, -t/2), (w*r, -t/2))
    path.lineTo((w*(1-r), -t/2))
    path.qCurveTo((w, -t/2), (w, xh*1/3))
    path.lineTo((w-t, 1/3*xh))
    path.qCurveTo((w-t, t/2), (w*(1-r), t/2))
    path.lineTo((w*r, t/2))
    path.qCurveTo((t, t/2), (t, xh*1/3))
    path.lineTo((t,xh))
    path.closePath()
    
    path.moveTo((w-t, +t/2-t*r/2))
    path.qCurveTo((w-t, -t/2), (w, -t/2))
    path.lineTo((w, xh))
    path.lineTo((w-t, xh))
    path.closePath()
    
    createDot(path, t*2, xh+t*2, t, r)
    createDot(path, w-t*2, xh+t*2, t, r)
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s 
    
def glyph_y(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("y")
    glyph.unicode = ord("y")
    
    path = glyph.getPen()
    
    path.moveTo((0,xh))
    path.lineTo((0, 1/3*xh))
    path.qCurveTo((0, -t/2), (w*r, -t/2))
    path.lineTo((w*(1-r), -t/2))
    path.qCurveTo((w, -t/2), (w, xh*1/3))
    path.lineTo((w,0))
    
    path.lineTo((w-t,0))
    path.lineTo((w-t, 1/3*xh))
    path.qCurveTo((w-t, t/2), (w*(1-r), t/2))
    path.lineTo((w*r, t/2))
    path.qCurveTo((t, t/2), (t, xh*1/3))
    path.lineTo((t,xh))
    path.closePath()
    
    path.moveTo((w-t, 0))
    path.lineTo((w-t, xh))
    path.lineTo((w, xh))
    path.lineTo((w, 0))
    
    path.lineTo((w, d+(xh*1/3)))
    path.qCurveTo((w, d-t/2), (w*(1-r), d-t/2))
    path.lineTo((w*r, d-t/2))
    path.qCurveTo((0, d-t/2), (0, d+(xh*1/3)))
    
    path.lineTo((t, d+(xh*1/3)))
    path.qCurveTo((t, d+t/2),(w*r, d+t/2))
    path.lineTo((w*(1-r), d+t/2))
    path.qCurveTo((w-t, d+t/2), (w-t, d+(xh*1/3)))
    
    
    path.closePath()
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s 

def glyph_space(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph("space")
    glyph.unicode = ord(" ")
    
    # metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_notdef(font, xh, a, d, w, t, s, r):
    glyph = font.newGlyph(".notdef")
    d = calculateDiagonal(t, (t,t), (w-t,a-t))
    
    path = glyph.getPen()
    
    path.moveTo((0,0))
    path.lineTo((0,a))
    path.lineTo((w,a))
    path.lineTo((w,0))
    path.closePath()
    
    path.moveTo((t,t))
    path.lineTo((w-t,t))
    path.lineTo((w-t,a-t))
    path.lineTo((t,a-t))
    path.closePath()
    
    path.moveTo((t-d[0]/2,t))
    path.lineTo((w-t-d[0]/2,a-t))
    path.lineTo((w-t+d[0]/2,a-t))
    path.lineTo((t+d[0]/2,t))
    path.closePath()
    
    path.moveTo((w-t-d[0]/2,t))
    path.lineTo((t-d[0]/2,a-t))
    path.lineTo((t+d[0]/2,a-t))
    path.lineTo((w-t+d[0]/2,t))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def calculateDiagonal(t, p1, p2):
    angle = math.atan2((p2[1] - p1[1]), (p2[0] - p1[0]))
    # substract 90°
    anglex = angle - math.radians(90)

    x, y = p1
    # pythagoras
    ax = t
    bx = t * math.tan(anglex)
    cx = math.sqrt(ax**2 + bx**2)
    
    angley = angle
    
    ay = t
    by = t * math.tan(angley)
    cy = math.sqrt(ay**2 + by**2)
    
    return cx, cy, bx, by
    
from fontTools.designspaceLib import DesignSpaceDocument
import ufo2ft

def generateSource(masterName, xHeight, ascender, descender, width, thickness, roundness):   
    master = RFont()#showInterface=False)
    master.info.familyName = familyName
    master.info.styleName = styleName
    master.info.xHeight = xHeight
    master.info.capHeight = capHeight
    master.info.unitsPerEm = capHeight + abs(ascender)
    master.info.descender = descender
    master.info.ascender = ascender
    spacing = 50

    glyph_notdef(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_space(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_a(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_ä(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_b(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_c(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_d(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_e(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_f(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_g(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_h(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_ı(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_i(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_l(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_m(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_n(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_o(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_ö(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_p(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_q(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_r(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_u(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_ü(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_y(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    
    source = doc.newSourceDescriptor()
    source.font = master.naked()## maybe this??
    source.location = dict(Width=width, Thickness=thickness, Roundness=roundness)
    if width == 600 and thickness == 40 and roundness == .3:
        source.copyLib=True
        print('This is the base master', source.location, source.copyLib)
    doc.addSource(source)

minW = 100
maxW = 900

minT = 1
maxT = 50

minR = 0
maxR = 0.5

doc = DesignSpaceDocument()

axisW = doc.newAxisDescriptor()
axisW.name = "Width"
axisW.tag = "wdth"
axisW.minimum = minW
axisW.default = 600
axisW.maximum = maxW
doc.addAxis(axisW)

axisT = doc.newAxisDescriptor()
axisT.name = "Thickness"
axisT.tag = "thck"
axisT.minimum = minT
axisT.default = 40
axisT.maximum = maxT
doc.addAxis(axisT)

axisR = doc.newAxisDescriptor()
axisR.name = "Roundness"
axisR.tag = "rndn"
axisR.minimum = minR
axisR.default = 0.3
axisR.maximum = maxR
doc.addAxis(axisR)


familyName = "Shah"
styleName = "Regular"
xHeight = 300
capHeight = 400

def testing():
    a = 1
    d = 0
    r = 3
    w = 3
    t = 1
    if t == 0:
        generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*100, 1, r/10)
    else:
        generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*100, (t+1)*5, r/10)


def export():  
    for w in range(9):
        for t in range(10):
            for r in range(6):
                a = 0
                d = 1
                if t == 0:
                    generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*100, 1, r/10)
                else:
                    generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*100, (t+1)*5, r/10)


    varFont = ufo2ft.compileVariableTTF(doc)
    varFont.save(f"export/{familyName} variable {datetime.now()}.ttf")

    print(f"Done exporting {familyName} variable {datetime.now()}.ttf")
    
export()