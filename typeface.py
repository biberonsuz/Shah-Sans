import math
from datetime import datetime

#create ratios for specific letter spacings in order to group them etc.   
spacing = {
  "c_right": 0.6,
  "l": 1,
  "n_right": 0.7,
  "a_left": 0.6,
  "v": 0.1,
  "r_right":0.45,
  "k_right":-0.1,
  "o":0.45,
  "t_right": 0.35,
  "t_left": 0.40, 
  "s": 0.45 
}

width = {
  "a": .9,"c": .94,"f":.5,
  "b": .95,"d": .95,"p": .95,"q": .95,
  "s": .9,"t": .8,"z": .8,
  "u": .82, "n": .9
}
 
def glyph_C(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("C")
    glyph.unicode = ord("C")

    path = glyph.getPen()
    
    path.moveTo((0,a))
    path.lineTo((w*(1-r), a))
    path.qCurveTo((w, a), (w,a/2))
    path.qCurveTo((w, 0), (w*(1-r), 0))
    path.lineTo((0,0))
    path.closePath()
    
    path.moveTo((ct,a-t))
    path.lineTo((ct,t))
    path.lineTo((w*(1-r)-ct, t))
    path.qCurveTo((w-ct, t), (w-ct, a/2))
    path.qCurveTo((w-ct, a-t), (w*(1-r)-ct, a-t))
    path.closePath()
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["o"]   

def glyph_D(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("D")
    glyph.unicode = ord("D")

    path = glyph.getPen()
    
    path.moveTo((0,a))
    path.lineTo((w*(1-r), a))
    path.qCurveTo((w, a), (w,a/2))
    path.qCurveTo((w, 0), (w*(1-r), 0))
    path.lineTo((0,0))
    path.closePath()
    
    path.moveTo((ct,a-t))
    path.lineTo((ct,t))
    path.lineTo((w*(1-r)-ct, t))
    path.qCurveTo((w-ct, t), (w-ct, a/2))
    path.qCurveTo((w-ct, a-t), (w*(1-r)-ct, a-t))
    path.closePath()
    
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["o"]  
    
def glyph_O(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("O")
    glyph.unicode = ord("O")

    path = glyph.getPen()
    
    component_o(path, a, w, t, r, ct, bo)
    
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["o"]  

def glyph_a(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("a")
    glyph.unicode = ord("a")

    path = glyph.getPen()
    w=w*width["a"]
    
    path.moveTo((-ct/2,xh*2/3))
    path.qCurveTo((-ct/2, xh+bo), (w*r, xh+bo))
    path.lineTo((w*(1-r),xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2, xh*2/3))
    path.lineTo((w+ct/2,0))
    
    path.lineTo((w-ct/2, 0))
    path.lineTo((w-ct/2, xh*2/3))
    path.qCurveTo((w-ct/2, xh-t+bo),(w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*2/3))
    path.closePath()
    
    path.moveTo((w-ct/2, 5/6*xh-t))
    path.qCurveTo((w-ct/2, 2/3*xh-t),(w-ct/2-50, 2/3*xh-t))
    path.lineTo((w*r, 2/3*xh-t))
    path.qCurveTo((rct/2, 2/3*xh-t), (rct/2, 1/3*xh)) 
    path.qCurveTo((rct/2,t-bo),(w*r,t-bo))
    path.lineTo((w*(1-r), t-bo))
    path.qCurveTo((w-ct/2, t-bo),(w-ct/2, 1/6*xh+t))
    path.lineTo((w-ct/2, 1/6*xh))
    
    path.qCurveTo((w-ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((-rct/2, -bo),(-rct/2, 1/3*xh))
    path.qCurveTo((-rct/2, 2/3*xh),(w*r, 2/3*xh))
    path.lineTo((w-ct/2-50,2/3*xh))
    path.qCurveTo((w-ct/2, 2/3*xh),(w-ct/2,5/6*xh))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["a_left"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_a_dieresis(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("a_dieresis")
    glyph.unicode = ord("ä")

    path = glyph.getPen()
    w=w*width["a"]
    
    path.moveTo((-ct/2,xh*2/3))
    path.qCurveTo((-ct/2, xh+bo), (w*r, xh+bo))
    path.lineTo((w*(1-r),xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2, xh*2/3))
    path.lineTo((w+ct/2,0))
    
    path.lineTo((w-ct/2, 0))
    path.lineTo((w-ct/2, xh*2/3))
    path.qCurveTo((w-ct/2, xh-t+bo),(w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*2/3))
    path.closePath()
    
    path.moveTo((w-ct/2, 5/6*xh-t))
    path.qCurveTo((w-ct/2, 2/3*xh-t),(w-ct/2-50, 2/3*xh-t))
    path.lineTo((w*r, 2/3*xh-t))
    path.qCurveTo((rct/2, 2/3*xh-t), (rct/2, 1/3*xh)) 
    path.qCurveTo((rct/2,t-bo),(w*r,t-bo))
    path.lineTo((w*(1-r), t-bo))
    path.qCurveTo((w-ct/2, t-bo),(w-ct/2, 1/6*xh+t))
    path.lineTo((w-ct/2, 1/6*xh))
    
    path.qCurveTo((w-ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((-rct/2, -bo),(-rct/2, 1/3*xh))
    path.qCurveTo((-rct/2, 2/3*xh),(w*r, 2/3*xh))
    path.lineTo((w-ct/2-50,2/3*xh))
    path.qCurveTo((w-ct/2, 2/3*xh),(w-ct/2,5/6*xh))
    path.closePath()


    component_dieresis(path, xh, w, t, r, ct)
    
    #metrics
    glyph.leftMargin = s*spacing["a_left"]
    glyph.rightMargin = s*spacing["n_right"]
            
def glyph_b(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("b")
    glyph.unicode = ord("b")

    path = glyph.getPen()
    w=w*width["b"]
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2,a))
    path.lineTo((ct/2, a))
    path.lineTo((ct/2, xh-t+bo))
    path.lineTo((t/2,xh*(1-r)))
    path.lineTo((ct/2, t-bo))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    path.moveTo((w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2, xh*(1-r)))
    path.lineTo((w+ct/2, xh*r))
    path.qCurveTo((w+ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((t/2, -bo), (t/2, r*xh))
    path.lineTo((t/2, xh*(1-r)))
    path.qCurveTo((t/2, xh+bo),(w*r, xh+bo))
    path.closePath()
    
    path.moveTo((w*r-bo, xh-t+bo))
    path.qCurveTo((ct/2-bo, xh-t+bo), (ct/2-bo, xh*(1-r)))
    path.lineTo((ct/2-bo, xh*r))
    path.qCurveTo((ct/2-bo, t-bo), (w*r-bo, t-bo))
    path.lineTo((w*(1-r)-bo, t-bo))
    path.qCurveTo((w-ct/2-bo, t-bo), (w-ct/2-bo, xh*r))
    path.lineTo((w-ct/2-bo, xh*(1-r)))
    path.qCurveTo((w-ct/2-bo, xh-t+bo), (w*(1-r)-bo, xh-t+bo))
    path.lineTo((w*r-bo, xh-t+bo))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_c(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("c")
    glyph.unicode = ord("c")
        
    path = glyph.getPen()
    w=w*width["c"]
    
    path.moveTo((w-ct/2, xh*(1-r)))
    path.qCurveTo((w-rct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((rct/2, xh-t+bo), (rct/2,xh*(1-r)))
    path.lineTo((rct/2, xh*r))
    path.qCurveTo((rct/2, t-bo), (w*r, t-bo))
    path.lineTo((w*(1-r),t-bo))
    path.qCurveTo((w-rct/2, t-bo), (w-rct/2, xh*r))
    
    path.lineTo((w+rct/2, xh*r))
    path.qCurveTo((w+rct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r,-bo))
    path.qCurveTo((-rct/2, -bo), (-rct/2, xh*r))
    path.lineTo((-rct/2, xh*(1-r)))
    path.qCurveTo((-rct/2, xh+bo), (w*r,xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+rct/2, xh+bo), (w+rct/2,xh*(1-r)))
    path.closePath()    
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["c_right"]
    
def glyph_c_cedilla(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("c_cedilla")
    glyph.unicode = ord("ç")
    
    path = glyph.getPen()
    w=w*width["c"]
    
    path.moveTo((w-ct/2, xh*(1-r)))
    path.qCurveTo((w-rct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((rct/2, xh-t+bo), (rct/2,xh*(1-r)))
    path.lineTo((rct/2, xh*r))
    path.qCurveTo((rct/2, t-bo), (w*r, t-bo))
    path.lineTo((w*(1-r),t-bo))
    path.qCurveTo((w-rct/2, t-bo), (w-rct/2, xh*r))
    
    path.lineTo((w+rct/2, xh*r))
    path.qCurveTo((w+rct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r,-bo))
    path.qCurveTo((-rct/2, -bo), (-rct/2, xh*r))
    path.lineTo((-rct/2, xh*(1-r)))
    path.qCurveTo((-rct/2, xh+bo), (w*r,xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+rct/2, xh+bo), (w+rct/2,xh*(1-r)))
    path.closePath()
    
    component_cedilla(path, -bo, w, t, r, ct)
    
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s *spacing["c_right"]

def glyph_d(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("d")
    glyph.unicode = ord("d")

    path = glyph.getPen()
    w=w*width["d"]
    
    path.moveTo((w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w-t/2, xh+bo), (w-t/2, xh*(1-r)))
    path.lineTo((w-t/2, xh*r))
    path.qCurveTo((w-t/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((-ct*.6, -bo), (-ct*.6, r*xh))
    path.lineTo((-ct*.6, xh*(1-r)))
    path.qCurveTo((-ct*.6, xh+bo),(w*r, xh+bo))
    path.closePath()
    
    path.moveTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*(1-r)))
    path.lineTo((ct/2, xh*r))
    path.qCurveTo((ct/2, t-bo), (w*r, t-bo))
    path.lineTo((w*(1-r), t-bo))
    path.qCurveTo((w-ct/2+bo, t-bo), (w-ct/2+bo, xh*r))
    path.lineTo((w-ct/2+bo, xh*(1-r)))
    path.qCurveTo((w-ct/2+bo, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.closePath()
    
    path.moveTo((w-ct/2, a))
    path.lineTo((w+ct/2, a))
    path.lineTo((w+ct/2, 0))
    path.lineTo((w-ct/2, 0))
    path.lineTo((w-ct/2, t-bo))
    path.lineTo((w-t/2, xh*r))
    path.lineTo((w-ct/2, xh-t+bo))
    path.closePath()
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_e(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("e")
    glyph.unicode = ord("e")
    
    path = glyph.getPen()
    
    path.moveTo((w-ct/2, xh*(1-r)))
    path.qCurveTo((w-ct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2,xh*(1-r)))
    path.lineTo((ct/2, xh*r))
    path.qCurveTo((ct/2, t-bo), (w*r, t-bo))
    path.lineTo((w*(1-r),t-bo))
    path.qCurveTo((w-ct/2, t-bo), (w-ct/2, xh*r))
    
    path.lineTo((w+ct/2, xh*r))
    path.qCurveTo((w+ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r,-bo))
    path.qCurveTo((-ct/2, -bo), (-ct/2, xh*r))
    path.lineTo((-ct/2, xh*(1-r)))
    path.qCurveTo((-ct/2, xh+bo), (w*r,xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2,xh*(1-r)))
    
    path.lineTo((w+ct/2,xh/2+1))
    path.lineTo((ct/2,xh/2+1))
    path.lineTo((ct/2,xh/2+t+1))
    path.lineTo((w-ct/2,xh/2+t+1))
    
    path.closePath()    
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["c_right"]
    
def glyph_f(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("f")
    glyph.unicode = ord("f")
    
    path = glyph.getPen()
    w=w*width["f"]
    top = a - xh
    
    path.moveTo((w-ct/2, xh+top*(1-r)))
    path.qCurveTo((w-ct/2, a-t+bo), (w*(1-r), a-t+bo))
    path.lineTo((w*r, a-t+bo))
    path.qCurveTo((ct/2, a-t+bo), (ct/2,xh+top*(1-r)))
    
    path.lineTo((ct/2, xh))
    path.lineTo((w*(1-r), xh))
    path.lineTo((w*(1-r), xh-t))
    path.lineTo((ct/2, xh-t))
    path.lineTo((ct/2, 0))
    path.lineTo((-ct/2, 0))
    path.lineTo((-ct/2, xh))
    
    path.lineTo((-ct/2, xh+top*(1-r)))
    path.qCurveTo((-ct/2, a+bo), (w*r,a+bo))
    path.lineTo((w*(1-r), a+bo))
    path.qCurveTo((w+ct/2, a+bo), (w+ct/2,xh+top*(1-r)))
    path.closePath()    
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*-spacing["l"]
    
def glyph_g(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("g")
    glyph.unicode = ord("g")
    
    path = glyph.getPen()
    w=w*.9
    
    path.moveTo((w*r-t/2, xh+bo))
    path.lineTo((w*(1-r)-t/2, xh+bo))
    path.qCurveTo((w-t/2, xh+bo), (w-t/2, xh*(1-r)))
    path.lineTo((w-t/2, xh*r))
    path.qCurveTo((w-t/2, -bo), (w*(1-r)-t/2, -bo))
    path.lineTo((w*r-t/2, -bo))
    path.qCurveTo((-ct/2, -bo), (-ct/2, r*xh))
    path.lineTo((-ct/2, xh*(1-r)))
    path.qCurveTo((-ct/2, xh+bo),(w*r-t/2, xh+bo))
    path.closePath()
    
    path.moveTo((w*r+bo, xh-t+bo))
    path.qCurveTo((ct/2+bo, xh-t+bo), (ct/2+bo, xh*(1-r)))
    path.lineTo((ct/2+bo, xh*r))
    path.qCurveTo((ct/2+bo, t-bo), (w*r+bo, t-bo))
    path.lineTo((w*(1-r)+bo, t-bo))
    path.qCurveTo((w-ct/2+bo, t-bo), (w-ct/2+bo, xh*r))
    path.lineTo((w-ct/2+bo, xh*(1-r)))
    path.qCurveTo((w-ct/2+bo, xh-t+bo), (w*(1-r)+bo, xh-t+bo))
    path.lineTo((w*r+bo, xh-t+bo))
    path.closePath()
    
    path.moveTo((w-ct/2, 0))
    path.lineTo((w-ct/2, t-bo))
    path.lineTo((w-t/2, xh*r))
    path.lineTo((w-ct/2, xh-t+bo))
    path.lineTo((w-ct/2, xh))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w+ct/2, 0))
    
    path.lineTo((w+ct/2, d+(xh*1/3)))
    path.qCurveTo((w+ct/2, d-bo), (w*(1-r), d-bo))
    path.lineTo((w*r, d-bo))
    path.qCurveTo((-ct/2, d-bo), (-ct/2, d+(xh*1/3)))
    
    path.lineTo((ct/2, d+(xh*1/3)))
    path.qCurveTo((ct/2, d+t-bo),(w*r, d+t-bo))
    path.lineTo((w*(1-r), d+t-bo))
    path.qCurveTo((w-ct/2, d+t-bo), (w-ct/2, d+(xh*1/3)))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_g_breve(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("g_breve")
    glyph.unicode = ord("ğ")
    
    path = glyph.getPen()
    w=w*.9
    component_o(path, xh, w, t, r, ct, bo)
    
    path.moveTo((w-ct/2, 0))
    path.lineTo((w-ct/2, xh))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w+ct/2, 0))
    
    path.lineTo((w+ct/2, d+(xh*1/3)))
    path.qCurveTo((w+ct/2, d-t/2), (w*(1-r), d-t/2))
    path.lineTo((w*r, d-t/2))
    path.qCurveTo((-ct/2, d-t/2), (-ct/2, d+(xh*1/3)))
    
    path.lineTo((ct/2, d+(xh*1/3)))
    path.qCurveTo((ct/2, d+t/2),(w*r, d+t/2))
    path.lineTo((w*(1-r), d+t/2))
    path.qCurveTo((w-ct/2, d+t/2), (w-ct/2, d+(xh*1/3)))
    path.closePath()
    
    component_breve(path, xh+t, w, t*.75, r)
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["n_right"]
    

def glyph_h(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("h")
    glyph.unicode = ord("h")
    
    path = glyph.getPen()
    w=w*.85
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, a))
    path.lineTo((ct/2, a))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    path.moveTo((ct/2-t/2, 2/3*xh))
    path.qCurveTo((ct/2-t/2, xh+bo), (w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2, xh*2/3))
    path.lineTo((w+ct/2,0))
    path.lineTo((w-ct/2,0))
    path.lineTo((w-ct/2, 2/3*xh))
    path.qCurveTo((w-ct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*2/3))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_i_dotless(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("idotless")
    glyph.unicode = ord("ı")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh))
    path.lineTo((ct, xh))
    path.lineTo((ct, 0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_i(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("i")
    glyph.unicode = ord("i")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh))
    path.lineTo((ct, xh))
    path.lineTo((ct, 0))
    path.closePath()
    
    component_dot(path, ct/2, xh+t*2, rct, r)
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 
    
def glyph_j(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("j")
    glyph.unicode = ord("j")
    
    path = glyph.getPen()
    
    path.moveTo((0, d*.2))
    path.lineTo((0, xh))
    path.lineTo((-ct, xh))
    path.lineTo((-ct, d*.2))
    path.qCurveTo((-ct, d+t), (-ct-w/4*r,d+t))
    path.lineTo((-ct-w/4*(1-r),d+t))
    
    path.lineTo((-ct-w/4*(1-r),d))
    path.lineTo((-w/4*r-ct, d))
    path.qCurveTo((0,d), (0, d*.2))
    path.closePath()
    
    component_dot(path, -ct/2, xh+t*2, ct, r)
        
    #metrics
    glyph.leftMargin = s*spacing["t_right"]
    glyph.rightMargin = s*spacing["n_right"]

    
def glyph_k(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("k")
    glyph.unicode = ord("k")
    
    path = glyph.getPen()
    w=w*.75
    
    path.moveTo((0, 0))
    path.lineTo((0, a))
    path.lineTo((ct, a))
    path.lineTo((ct, 0))
    path.closePath()
    
    dt = calculateDiagonal(ct, (0, xh*.6),(w*.6, xh))
    db = calculateDiagonal(ct, (0, xh*.6),(w*.9,0))
    
    path.moveTo((ct,xh*.6+dt[1]/2))
    path.lineTo((ct+w*.6-dt[0]/2, xh))
    path.lineTo((ct+w*.6+dt[0]/2, xh))
    path.lineTo((ct+dt[0]/2,xh*.6))
    
    path.lineTo((ct+w*.9+db[0]/2, 0))
    path.lineTo((ct+w*.9-db[0]/2, 0))
    path.lineTo((ct+0,xh*.6-db[1]/2))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["v"] 
    
def glyph_l(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("l")
    glyph.unicode = ord("l")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, a))
    path.lineTo((ct, a))
    path.lineTo((ct, 0))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_m(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("m")
    glyph.unicode = ord("m")
    
    m = w*0.8
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, xh))
    path.lineTo((ct/2, xh))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    path.moveTo((ct/2-t/2, 2/3*xh))
    path.qCurveTo((ct/2-t/2, xh+bo), (m*r, xh+bo))
    path.lineTo((m*(1-r), xh+bo))
    path.qCurveTo((m+ct/2, xh+bo), (m+ct/2, xh*2/3))
    path.lineTo((m+ct/2,0))
    path.lineTo((m-ct/2,0))
    path.lineTo((m-ct/2, 2/3*xh))
    path.qCurveTo((m-ct/2, xh-t+bo), (m*(1-r), xh-t+bo))
    path.lineTo((m*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*2/3))
    path.closePath()
    
    path.moveTo((m+ct/2-t/2, 2/3*xh))
    path.qCurveTo((m+ct/2-t/2, xh+bo), (m+m*r, xh+bo))
    path.lineTo((m+m*(1-r), xh+bo))
    path.qCurveTo((m+m+ct/2, xh+bo), (m+m+ct/2, xh*2/3))
    path.lineTo((m+m+ct/2,0))
    path.lineTo((m+m-ct/2,0))
    path.lineTo((m+m-ct/2, 2/3*xh))
    path.qCurveTo((m+m-ct/2, xh-t+bo), (m+m*(1-r), xh-t+bo))
    path.lineTo((m+m*r, xh-t+bo))
    path.qCurveTo((m+ct/2, xh-t+bo), (m+ct/2, xh*2/3))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]   

def glyph_n(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("n")
    glyph.unicode = ord("n")
    
    path = glyph.getPen()
    w=w*width["n"]
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, xh))
    path.lineTo((ct/2, xh))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    path.moveTo((ct/2-t/2, 2/3*xh))
    path.qCurveTo((ct/2-t/2, xh+bo), (w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2, xh*2/3))
    path.lineTo((w+ct/2,0))
    path.lineTo((w-ct/2,0))
    path.lineTo((w-ct/2, 2/3*xh))
    path.qCurveTo((w-ct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*2/3))
    path.closePath()            
            
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]
    
    
def glyph_o(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("o")
    glyph.unicode = ord("o")
    
    path = glyph.getPen()
    w=w*.98
    component_o(path, xh, w, t, r, ct, bo)
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_o_dieresis(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("o_dieresis")
    glyph.unicode = ord("ö")
    
    path = glyph.getPen()
    w=w*.98
    component_o(path, xh, w, t, r, ct, bo)
    component_dieresis(path, xh, w, t, r, ct)  
      
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_p(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("p")
    glyph.unicode = ord("p")
    
    path = glyph.getPen()
    w=w*.95
    
    path.moveTo((w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+ct*.6, xh+bo), (w+ct*.6, xh*(1-r)))
    path.lineTo((w+ct*.6, xh*r))
    path.qCurveTo((w+ct*.6, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((-ct/2, -bo), (-ct/2, r*xh))
    path.lineTo((-ct/2, xh*(1-r)))
    path.qCurveTo((-ct/2, xh+bo),(w*r, xh+bo))
    path.closePath()
    
    path.moveTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*(1-r)))
    path.lineTo((ct/2, xh*r))
    path.qCurveTo((ct/2, t-bo), (w*r, t-bo))
    path.lineTo((w*(1-r), t-bo))
    path.qCurveTo((w-ct/2, t-bo), (w-ct/2, xh*r))
    path.lineTo((w-ct/2, xh*(1-r)))
    path.qCurveTo((w-ct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.closePath()
    
    path.moveTo((-ct/2, -a+xh))
    path.lineTo((-ct/2, xh))
    path.lineTo((ct/2, xh))
    path.lineTo((ct/2, -a+xh))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["o"]

def glyph_q(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("q")
    glyph.unicode = ord("q")
    
    path = glyph.getPen()
    w=w*.95
    
    path.moveTo((w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2, xh*(1-r)))
    path.lineTo((w+ct/2, xh*r))
    path.qCurveTo((w+ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((-ct*.6, -bo), (-ct*.6, r*xh))
    path.lineTo((-ct*.6, xh*(1-r)))
    path.qCurveTo((-ct*.6, xh+bo),(w*r, xh+bo))
    path.closePath()
    
    path.moveTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*(1-r)))
    path.lineTo((ct/2, xh*r))
    path.qCurveTo((ct/2, t-bo), (w*r, t-bo))
    path.lineTo((w*(1-r), t-bo))
    path.qCurveTo((w-ct/2, t-bo), (w-ct/2, xh*r))
    path.lineTo((w-ct/2, xh*(1-r)))
    path.qCurveTo((w-ct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.closePath()
    
    path.moveTo((w-ct/2, -a+xh))
    path.lineTo((w-ct/2,xh))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w+ct/2, -a+xh))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_r(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("r")
    glyph.unicode = ord("r")
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, xh))
    path.lineTo((ct/2, xh))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    path.moveTo((ct/2-t/2, 2/3*xh))
    path.qCurveTo((ct/2-t/2, xh+bo), (w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.lineTo((w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*2/3))
    path.closePath()      
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["r_right"]
    
def glyph_s(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("s")
    glyph.unicode = ord("s")
    
    path = glyph.getPen()
    w = w*width["s"]
    
    path.moveTo((w+ct/2,xh*3/4+bo/2-t/4))
    path.qCurveTo((w+ct/2,xh+bo),(w*(1-r), xh+bo))
    path.lineTo((w*r, xh+bo))
    path.qCurveTo((-ct/2,xh+bo),(-ct/2, xh*3/4+bo/2-t/4))
    path.qCurveTo((-ct/2,xh*2/4-t/2),(w*r, xh*2/4-t/2))
    path.lineTo((w*(1-r), xh*2/4-t/2))
    path.qCurveTo((w-ct/2+bo, xh*2/4-t/2), (w-ct/2+bo, xh*1/4+t/4-bo/2))
    path.qCurveTo((w-ct/2+bo, t-bo), (w*(1-r), t-bo))
    path.lineTo((w*r, t-bo))
    path.qCurveTo((ct/2-bo*2,t-bo), (ct/2-bo*2,xh*1/4+t/4-bo/2))
    
    path.lineTo((-ct/2-bo*2,xh*1/4+t/4-bo/2))
    path.qCurveTo((-ct/2-bo*2, -bo), (w*r, -bo))
    path.lineTo((w*(1-r), -bo))
    path.qCurveTo((w+ct/2+bo, -bo), (w+ct/2+bo, xh*1/4+t/4-bo/2))
    path.qCurveTo((w+ct/2+bo, xh*2/4+t/2),(w*(1-r), xh*2/4+t/2))
    path.lineTo((w*r,xh*2/4+t/2))
    path.qCurveTo((ct/2, xh*2/4+t/2),(ct/2, xh*3/4+bo/2-t/4))
    path.qCurveTo((ct/2, xh+bo-t),(w*r, xh+bo-t))
    path.lineTo((w*(1-r), xh+bo-t))
    path.qCurveTo((w-ct/2, xh+bo-t),(w-ct/2, xh*3/4+bo/2-t/4))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["s"]
    glyph.rightMargin = s*spacing["s"]
    
def glyph_s_cedilla(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("s_cedilla")
    glyph.unicode = ord("ş")
    
    path = glyph.getPen()
    w = w*width["s"]
    
    path.moveTo((w+ct/2,xh*3/4+bo/2-t/4))
    path.qCurveTo((w+ct/2,xh+bo),(w*(1-r), xh+bo))
    path.lineTo((w*r, xh+bo))
    path.qCurveTo((-ct/2,xh+bo),(-ct/2, xh*3/4+bo/2-t/4))
    path.qCurveTo((-ct/2,xh*2/4-t/2),(w*r, xh*2/4-t/2))
    path.lineTo((w*(1-r), xh*2/4-t/2))
    path.qCurveTo((w-ct/2+bo, xh*2/4-t/2), (w-ct/2+bo, xh*1/4+t/4-bo/2))
    path.qCurveTo((w-ct/2+bo, t-bo), (w*(1-r), t-bo))
    path.lineTo((w*r, t-bo))
    path.qCurveTo((ct/2-bo*2,t-bo), (ct/2-bo*2,xh*1/4+t/4-bo/2))
    
    path.lineTo((-ct/2-bo*2,xh*1/4+t/4-bo/2))
    path.qCurveTo((-ct/2-bo*2, -bo), (w*r, -bo))
    path.lineTo((w*(1-r), -bo))
    path.qCurveTo((w+ct/2+bo, -bo), (w+ct/2+bo, xh*1/4+t/4-bo/2))
    path.qCurveTo((w+ct/2+bo, xh*2/4+t/2),(w*(1-r), xh*2/4+t/2))
    path.lineTo((w*r,xh*2/4+t/2))
    path.qCurveTo((ct/2, xh*2/4+t/2),(ct/2, xh*3/4+bo/2-t/4))
    path.qCurveTo((ct/2, xh+bo-t),(w*r, xh+bo-t))
    path.lineTo((w*(1-r), xh+bo-t))
    path.qCurveTo((w-ct/2, xh+bo-t),(w-ct/2, xh*3/4+bo/2-t/4))
    path.closePath()
    
    component_cedilla(path, -bo, w, t, r, ct)
        
    #metrics
    glyph.leftMargin = s*spacing["s"]
    glyph.rightMargin = s*spacing["s"]

    
def glyph_t(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("t")
    glyph.unicode = ord("t")
    
    path = glyph.getPen()
    
    path.moveTo((0, xh*.2))
    path.lineTo((0, xh*1.2-t/2+t*r/2))
    path.lineTo((ct, xh*1.2-t/2+t*r/2))
    path.lineTo((ct, xh*.2))
    path.qCurveTo((ct, t-bo), (ct+w/4*r,t-bo))
    path.lineTo((ct+w/4*(1-r),t-bo))
    
    path.lineTo((w/4*(1-r)+ct,-bo))
    path.lineTo((w/4*r+ct, -bo))
    path.qCurveTo((0,-bo), (0, xh*.2))
    path.closePath()
    
    path.moveTo((-w/6*(1-r), xh))
    path.lineTo((ct+w/4*(1-r), xh))
    path.lineTo((ct+w/4*(1-r),xh-t))
    path.lineTo((-w/6*(1-r), xh-t))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["t_left"]
    glyph.rightMargin = s*spacing["t_right"]

    
def glyph_u(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("u")
    glyph.unicode = ord("u")
    
    path = glyph.getPen()
    w=w*width["u"]
    
    path.moveTo((-ct/2,xh))
    path.lineTo((-ct/2, 1/3*xh))
    path.qCurveTo((-ct/2, -bo), (w*r, -bo))
    path.lineTo((w*(1-r), -bo))
    path.qCurveTo((w-ct/2+t/2, -bo), (w-ct/2+t/2, xh*1/3))
    path.lineTo((w-ct/2, 1/3*xh))
    path.qCurveTo((w-ct/2, t-bo), (w*(1-r), t-bo))
    path.lineTo((w*r, t-bo))
    path.qCurveTo((ct/2, t-bo), (ct/2, xh*1/3))
    path.lineTo((ct/2,xh))
    path.closePath()
    
    path.moveTo((w-ct/2, 0))
    path.lineTo((w+ct/2, 0))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w-ct/2, xh))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["n_right"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_u_dieresis(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("u_dieresis")
    glyph.unicode = ord("ü")
    
    path = glyph.getPen()
    w=w*.82
    
    path.moveTo((-ct/2,xh))
    path.lineTo((-ct/2, 1/3*xh))
    path.qCurveTo((-ct/2, -bo), (w*r, -bo))
    path.lineTo((w*(1-r), -bo))
    path.qCurveTo((w-ct/2+t/2, -bo), (w-ct/2+t/2, xh*1/3))
    path.lineTo((w-ct/2, 1/3*xh))
    path.qCurveTo((w-ct/2, t-bo), (w*(1-r), t-bo))
    path.lineTo((w*r, t-bo))
    path.qCurveTo((ct/2, t-bo), (ct/2, xh*1/3))
    path.lineTo((ct/2,xh))
    path.closePath()
    
    path.moveTo((w-ct/2, 0))
    path.lineTo((w+ct/2, 0))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w-ct/2, xh))
    path.closePath()
        
    component_dieresis(path, xh, w, t, r, ct)
        
    #metrics
    glyph.leftMargin = s*spacing["n_right"]
    glyph.rightMargin = s *spacing["l"]
    
def glyph_v(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("v")
    glyph.unicode = ord("v")
    
    path = glyph.getPen()
    w=w*.92
    d = calculateDiagonal(t, (w/2, 0),(w, xh))
    d1 = calculateDiagonal(t, (w/2, 0),(w, xh))
    
    path.moveTo((0,xh))
    path.lineTo((w/2-d[0]/2-d1[0]/2, 0))
    path.lineTo((w/2+d[0]/2+d1[0]/2, 0))
    path.lineTo((w,xh))
    path.lineTo((w-d[0]-d1[0]/2,xh))
    path.lineTo((w/2, d1[1]/2))
    path.lineTo((d[0]+d1[0]/2,xh))
    
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["v"]
    glyph.rightMargin = s*spacing["v"]
    
def glyph_w(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("w")
    glyph.unicode = ord("w")
    
    path = glyph.getPen()
    w=w*.92
    d = calculateDiagonal(t, (0, 0),(w*.3, xh))
    d1 = calculateDiagonal(t, (0, 0),(w*.3, xh))
    
    path.moveTo((0,xh))
    path.lineTo((w*.4-d[0]/2-d1[0]/2, 0))
    path.lineTo((w*.4+d[0]/2+d1[0]/2, 0))
    path.lineTo((w*.8,xh-d1[1]/2))
    path.lineTo((w*1.2-d[0]/2-d1[0]/2, 0))
    path.lineTo((w*1.2+d[0]/2+d1[0]/2, 0))
    path.lineTo((w*1.6,xh))
    
    path.lineTo((w*1.6-d[0]-d1[0]/2, xh))
    path.lineTo((w*1.2, d1[1]/2))
    path.lineTo((w*.8+d[0]/2+d1[0]/2, xh))
    path.lineTo((w*.8-d[0]/2-d1[0]/2, xh))
    path.lineTo((w*.4, d1[1]/2))
    path.lineTo((d[0]+d1[0]/2, xh))
    
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["v"]
    glyph.rightMargin = s*spacing["v"]
    
def glyph_x(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("x")
    glyph.unicode = ord("x")
    
    path = glyph.getPen()
    w=w*.8
    d = calculateDiagonal(ct, (0,0), (w,xh))
    
    path.moveTo((-d[0]/2,0))
    path.lineTo((w-d[0]/2,xh))
    path.lineTo((w+d[0]/2,xh))
    path.lineTo((d[0]/2,0))
    path.closePath()
    
    path.moveTo((w-d[0]/2,0))
    path.lineTo((-d[0]/2,xh))
    path.lineTo((d[0]/2,xh))
    path.lineTo((w+d[0]/2,0))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["v"]
    glyph.rightMargin = s*spacing["v"]
    
def glyph_y(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("y")
    glyph.unicode = ord("y")
    
    path = glyph.getPen()
    w=w*.82
    
    path.moveTo((-ct/2,xh))
    path.lineTo((-ct/2, 1/3*xh))
    path.qCurveTo((-ct/2, -bo), (w*r, -bo))
    path.lineTo((w*(1-r), -bo))
    path.qCurveTo((w-ct/2+t/2, -bo), (w-ct/2+t/2, xh*1/3))
    path.lineTo((w-ct/2, 1/3*xh))
    path.qCurveTo((w-ct/2, t-bo), (w*(1-r), t-bo))
    path.lineTo((w*r, t-bo))
    path.qCurveTo((ct/2, t-bo), (ct/2, xh*1/3))
    path.lineTo((ct/2,xh))
    path.closePath()
    
    path.moveTo((w+ct/2, xh))
    path.lineTo((w-ct/2, xh))
    path.lineTo((w-ct/2, d+xh/3))
    
    path.qCurveTo((w-ct/2, d+t-bo), (w*(1-r), d+t-bo))
    path.lineTo((w*r, d+t-bo))
    path.qCurveTo((ct/2, d+t-bo), (ct/2, d+xh/3))
    path.lineTo((-ct/2, d+xh/3))
    
    path.qCurveTo((-ct/2, d-bo), (w*r, d-bo))
    path.lineTo((w*(1-r), d-bo))
    path.qCurveTo((w+ct/2, d-bo), (w+ct/2, d+xh/3))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["n_right"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_z(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("z")
    glyph.unicode = ord("z")
    
    path = glyph.getPen()
    w=w*.8
    d = calculateDiagonal(ct, (0,t/2), (w,xh-t/2))
    
    path.moveTo((0,xh))
    path.lineTo((w,xh))
    path.lineTo((w,xh-t))
    path.lineTo((d[0], t))
    path.lineTo((w,t))
    path.lineTo((w,0))
    path.lineTo((0,0))
    path.lineTo((0,t))
    path.lineTo((w-(d[0]),xh-t))
    path.lineTo((0,xh-t))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["t_left"]
    glyph.rightMargin = s*spacing["t_left"]

def glyph_space(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("space")
    glyph.unicode = ord(" ")
    
    glyph.width = w*.8
    
def glyph_hyphen(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("hyphen")
    glyph.unicode = ord("-")
        
    path = glyph.getPen()
    
    path.moveTo((0,xh/2-t/2))
    path.lineTo((w,xh/2-t/2))
    path.lineTo((w,xh/2+t/2))
    path.lineTo((0,xh/2+t/2))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_underscore(font, xh, a, d, w, t, s, r, ct, bo, rct):    
    glyph = font.newGlyph("underscore")
    glyph.unicode = ord("_")
    
    path = glyph.getPen()
    
    path.moveTo((0,-t))
    path.lineTo((w,-t))
    path.lineTo((w,0))
    path.lineTo((0,0))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_period(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("period")
    glyph.unicode = ord(".")
    
    path = glyph.getPen()
    
    component_dot(path, 0, ct/2, ct*1.25, r)
    path.moveTo((0,0))
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 
    
def glyph_comma(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("comma")
    glyph.unicode = ord(",")
    
    path = glyph.getPen()
    dr = ct*(1+r)
    
    ra = math.radians(-20)
    #(x*math.cos(ra)-y*math.sin(ra),x*math.sin(ra)+y*math.cos(ra))
    
    path.moveTo((-dr/2*math.cos(ra)-0*math.sin(ra), -dr/2*math.sin(ra)+0*math.cos(ra)))
    path.qCurveTo((-dr/2*math.cos(ra)-dr/2*math.sin(ra),-dr/2*math.sin(ra)+dr/2*math.cos(ra)), (0*math.cos(ra)-dr/2*math.sin(ra),0*math.sin(ra)+dr/2*math.cos(ra)))
    path.qCurveTo((dr/2*math.cos(ra)-dr/2*math.sin(ra),dr/2*math.sin(ra)+dr/2*math.cos(ra)), (dr/2*math.cos(ra)-0*math.sin(ra),dr/2*math.sin(ra)+0*math.cos(ra)))
    path.lineTo((t/2*math.cos(ra)+dr*math.sin(ra),t/2*math.sin(ra)-dr*math.cos(ra)))
    path.lineTo((-t/2*math.cos(ra)+dr*math.sin(ra),-t/2*math.sin(ra)-dr*math.cos(ra)))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_quotesingle(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("quotesingle")
    glyph.unicode = ord("'")
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2, a))
    path.lineTo((ct/2, a))
    path.lineTo((t/2, a*.75))
    path.lineTo((-t/2, a*.75))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_quotedbl(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("quotedbl")
    glyph.unicode = 34
    
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2, a))
    path.lineTo((ct/2, a))
    path.lineTo((t/2, a*.75))
    path.lineTo((-t/2, a*.75))
    path.closePath()
    
    path.moveTo((ct*2-ct/2, a))
    path.lineTo((ct*2+ct/2, a))
    path.lineTo((ct*2+t/2, a*.75))
    path.lineTo((ct*2-t/2, a*.75))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_exclam(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("exclam")
    glyph.unicode = ord("!")
    
    path = glyph.getPen()
    component_dot(path, 0, ct/2, ct*1.25, r)
    
    path.moveTo((-t/2, ct*2))
    path.lineTo((t/2, ct*2))
    path.lineTo((ct/2, ct*4))
    path.lineTo((ct/2, a))
    path.lineTo((-ct/2, a))
    path.lineTo((-ct/2, ct*4))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_colon(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("colon")
    glyph.unicode = ord(":")
    
    path = glyph.getPen()
    
    component_dot(path, 0, ct/2, ct*1.25, r)
    component_dot(path, 0, xh-ct/2, ct*1.25, r)
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 
    
def glyph_parenleft(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("parenleft")
    glyph.unicode = ord("(")
    
    path = glyph.getPen()
    h = a+d
    
    path.moveTo((w/6,d))
    path.qCurveTo((0,d), (0, h/2))
    path.qCurveTo((0,a), (w/6, a))
    
    path.lineTo((w/6+ct,a))
    path.qCurveTo((ct,a), (ct, h/2))
    path.qCurveTo((ct,d), (w/6+ct, d))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["c_right"]
    
def glyph_parenright(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("parenright")
    glyph.unicode = ord(")")
    
    path = glyph.getPen()
    h = a+d
    
    path.moveTo((0,d))
    path.qCurveTo((w/6,d), (w/6, h/2))
    path.qCurveTo((w/6,a), (0, a))
    
    path.lineTo((ct,a))
    path.qCurveTo((w/6+ct,a), (w/6+ct, h/2))
    path.qCurveTo((w/6+ct,d), (ct, d))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["c_right"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_bracketleft(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("bracketleft")
    glyph.unicode = ord("[")
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2,d))
    path.lineTo((-ct/2,a))
    path.lineTo((w/6,a))
    path.lineTo((w/6,a-t))
    path.lineTo((ct/2,a-t))
    path.lineTo((ct/2,d+t))
    path.lineTo((w/6,d+t))
    path.lineTo((w/6,d))
    path.closePath()

    # metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_bracketright(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("bracketright")
    glyph.unicode = ord("]")
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2, d))
    path.lineTo((w/6, d))
    path.lineTo((w/6, a))
    path.lineTo((-ct/2, a))
    path.lineTo((-ct/2, a-t))
    path.lineTo((w/6-ct, a-t))
    path.lineTo((w/6-ct, d+t))
    path.lineTo((-ct/2, d+t))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_bullet(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("bullet")
    glyph.unicode = ord("•")
    
    path = glyph.getPen()
    
    component_dot(path, 0, xh/2, t*5, r)
    path.moveTo((0,0))
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 
    
def glyph_grave(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("grave")
    glyph.unicode = ord("`")
    
    path = glyph.getPen()
    
    path.moveTo((ct/2, a))
    path.lineTo((-ct/2, a))
    path.lineTo((t, a*.9))
    path.lineTo((t*2, a*.9))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_fi(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph("fi")
    glyph.unicode = ord("ﬁ")
    
    path = glyph.getPen()
    w=w*.5
    top = a - xh
    
    path.moveTo((w-ct/2, xh+top*(1-r)))
    path.qCurveTo((w-ct/2, a-t+bo), (w*(1-r), a-t+bo))
    path.lineTo((w*r, a-t+bo))
    path.qCurveTo((ct/2, a-t+bo), (ct/2,xh+top*(1-r)))
    
    path.lineTo((ct/2, xh))
    path.lineTo((w*(1-r), xh))
    path.lineTo((w*(1-r), xh-t))
    path.lineTo((ct/2, xh-t))
    path.lineTo((ct/2, 0))
    path.lineTo((-ct/2, 0))
    path.lineTo((-ct/2, xh))
    
    path.lineTo((-ct/2, xh+top*(1-r)))
    path.qCurveTo((-ct/2, a+bo), (w*r,a+bo))
    path.lineTo((w*(1-r), a+bo))
    path.qCurveTo((w+ct/2, a+bo), (w+ct/2,xh+top*(1-r)))
    path.lineTo((w+ct/2, xh+ct*2))
    path.qCurveTo((w+ct/2, xh+ct*(1+r)), (w, xh+ct*(1+r)))
    path.qCurveTo((w-ct/2, xh+ct*(1+r)), (w-ct/2, xh+ct*2))
    path.closePath()    
    
    path.moveTo((w-ct/2, 0))
    path.lineTo((w-ct/2, xh))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w+ct/2, 0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_notdef(font, xh, a, d, w, t, s, r, ct, bo, rct):
    glyph = font.newGlyph(".notdef")
    d = calculateDiagonal(ct, (t,t), (w-t,a-t))
    
    
    path = glyph.getPen()
    
    path.moveTo((0,0))
    path.lineTo((0,a))
    path.lineTo((w,a))
    path.lineTo((w,0))
    path.closePath()
    
    path.moveTo((ct,t))
    path.lineTo((w-ct,t))
    path.lineTo((w-ct,a-t))
    path.lineTo((ct,a-t))
    path.closePath()
    
    path.moveTo((ct-d[0]/2,t))
    path.lineTo((w-ct-d[0]/2,a-t))
    path.lineTo((w-ct+d[0]/2,a-t))
    path.lineTo((ct+d[0]/2,t))
    path.closePath()
    
    path.moveTo((w-ct-d[0]/2,t))
    path.lineTo((ct-d[0]/2,a-t))
    path.lineTo((ct+d[0]/2,a-t))
    path.lineTo((w-ct+d[0]/2,t))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
    
def component_o(path, xh, w, t, r, ct, bo):
    path.moveTo((w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2, xh*(1-r)))
    path.lineTo((w+ct/2, xh*r))
    path.qCurveTo((w+ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((-ct/2, -bo), (-ct/2, r*xh))
    path.lineTo((-ct/2, xh*(1-r)))
    path.qCurveTo((-ct/2, xh+bo),(w*r, xh+bo))
    path.closePath()
    
    path.moveTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*(1-r)))
    path.lineTo((ct/2, xh*r))
    path.qCurveTo((ct/2, t-bo), (w*r, t-bo))
    path.lineTo((w*(1-r), t-bo))
    path.qCurveTo((w-ct/2, t-bo), (w-ct/2, xh*r))
    path.lineTo((w-ct/2, xh*(1-r)))
    path.qCurveTo((w-ct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.closePath()
    
def component_dot(path, x, y, t, r):
    #Dot ratio
    dr = t
    
    path.moveTo((x, y+dr/2))
    path.qCurveTo((x+dr/2, y+dr/2), (x+dr/2, y))
    path.qCurveTo((x+dr/2, y-dr/2), (x, y-dr/2))
    path.qCurveTo((x-dr/2, y-dr/2), (x-dr/2, y))
    path.qCurveTo((x-dr/2, y+dr/2), (x, y+dr/2))
    path.closePath()
    
def component_dieresis(path, h, w, t, r, ct):
    component_dot(path, t*1.25, h+t*2, ct, r)
    component_dot(path, w-t*1.25, h+t*2, ct, r)
    
def component_breve(path, h, w, t, r):    
    path.moveTo((t, h+w/6))
    path.qCurveTo((t, h), (w*r, h))
    path.lineTo((w*(1-r),h))
    path.qCurveTo((w-t, h), (w-t,h+w/6))
    
    path.lineTo((w-t*2, h+w/6))
    path.qCurveTo((w-t*2, h+t), (w*(1-r), h+t))
    path.lineTo((w*r, h+t))
    path.qCurveTo((t*2, h+t), (t*2, h+w/6))
    path.closePath()
    
def component_cedilla(path, h, w, t, r, ct):
    nt = t/2
    nct = ct/2
    d = calculateDiagonal(nt, (w/2-nt, 0), (w/2, -nt))
    
    path.moveTo((w/2-nt, h))
    path.lineTo((w/2-nt+d[0], h))
    path.lineTo((w/2+nt+d[0], h-nt*2))
    
    path.lineTo((w/2, h-nt*2))
    path.qCurveTo((w*r, h-nt*2), (w*r, h-nt*2.5))
    path.qCurveTo((w*r, h-nt*3), (w/2, h-nt*3))
    path.lineTo((w/2+nt+d[0], h-nt*3))
    
    path.lineTo((w/2+nt+d[0], h-nt*4))
    path.lineTo((w/2, h-nt*4))
    path.qCurveTo((w*r-nct, h-nt*4),(w*r-nct, h-nt*2.5))
    path.qCurveTo((w*r-nct, h-nt), (w/2, h-nt))

    path.closePath()
    
def component_left_top(path, x, h, w, t, r, ct, bo):
    path.moveTo((x, h))
    path.lineTo((x, h+t/2))
    path.qCurveTo((x+ct, h+t/2), (x+ct, h))
    path.closePath()
    
def component_right_top(path, x, h, w, t, r, ct, bo):
    path.moveTo((x, h))
    path.qCurveTo((x, h+t/2), (x+ct, h+t/2))
    path.lineTo((x+ct, h))
    path.closePath()
    
def component_left_bottom(path, x, h, w, t, r, ct, bo):
    path.moveTo((x, h+t/2))
    path.lineTo((x+ct, h+t/2))
    path.qCurveTo((x+ct, h), (x, h))
    path.closePath()
    
def component_right_bottom(path, x, h, w, t, r, ct, bo):
    path.moveTo((x, h+t/2))
    path.lineTo((x+ct, h+t/2))
    path.lineTo((x+ct, h))
    path.qCurveTo((x, h), (x, h+t/2))
    path.closePath()
    
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

def generateSource(masterName, xHeight, ascender, descender, width, thickness, roundness, contrast, interface):   
    master = RFont(showInterface=interface)
    master.info.familyName = familyName
    master.info.styleName = styleName
    master.info.xHeight = xHeight
    master.info.capHeight = capHeight
    master.info.unitsPerEm = capHeight + abs(ascender)
    master.info.descender = descender
    master.info.ascender = ascender
    spacing = thickness/50 + 80
    contrast_thickness = thickness*(1+contrast)
    bottom_offset = thickness*.1
    round_contrast_thickness = contrast_thickness * 1.1

    glyph_notdef(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_space(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    #glyph_D(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    #glyph_O(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_a(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_a_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_b(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_c(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_c_cedilla(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_d(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_e(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_f(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_g(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_g_breve(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_h(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_i_dotless(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_i(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_j(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_k(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_l(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_m(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_n(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_o(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_o_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_p(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_q(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_r(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_s(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_s_cedilla(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_t(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_u(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_u_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_v(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_w(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_x(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_y(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_z(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_period(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_comma(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_quotesingle(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_quotedbl(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_colon(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_hyphen(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_underscore(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_parenleft(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_parenright(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_bracketleft(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_bracketright(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_exclam(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_bullet(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)
    glyph_grave(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness)

    source = doc.newSourceDescriptor()
    source.font = master.naked()
    source.location = dict(Width=width, Thickness=thickness, Roundness=roundness, Contrast=contrast)
    print(source.location)
    if width == 600 and thickness == 40 and roundness == .3 and contrast == .2:
        source.copyLib=True
        print('This is the base master', source.location, source.copyLib)
    doc.addSource(source)

minW = 100
maxW = 900
masterW = 9

minT = 5
maxT = 50
masterT = 10

minR = 0.05
maxR = 0.5
masterR = 10

minC = 0
maxC = 1
masterC = 5

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
axisR.tag = "RNDN"
axisR.minimum = minR
axisR.default = .3
axisR.maximum = maxR
doc.addAxis(axisR)

axisC = doc.newAxisDescriptor()
axisC.name = "Contrast"
axisC.tag = "CNTR"
axisC.minimum = minC
axisC.default = .2
axisC.maximum = maxC
doc.addAxis(axisC)

familyName = "Shah Sans"
styleName = "Regular"
xHeight = 300
capHeight = 400

#change roundness from 0.1-0.5 to 1-100
def testing(w, t, r, c):
    a = .5
    d = .5
    generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, int((w+1)*(maxW/masterW)), int((t+1)*(maxT/masterT)), int((r+1)*(maxR/masterR)), int(c*(maxC/masterC)), True)

def export():  
    for w in range(masterW):
        for t in range(masterT):
            for r in range(masterR):
                for c in range(masterC):
                    a = .5
                    d = .5
                    generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*(maxW/masterW), (t+1)*(maxT/masterT), round((r+1)*(maxR/masterR),2), round(c*(maxC/masterC),1), False)
                    
    print('Compiling TTF...')
    varFont = ufo2ft.compileVariableTTF(doc)
    print('Saving...')
    font_name = f"export/{familyName}GX-{datetime.now()}.ttf"
    varFont.save(font_name)
    print(f"Done exporting {font_name}")
    
#testing(0,0,0,0)
export()
