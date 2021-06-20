import math
from datetime import datetime

#create ratios for specific letter spacings in order to group them etc.   
spacing = {
  "c_right": 0.5,
  "l": 1,
  "n_right": 0.9,
  "a_left": 0.6,
  "v": 0.1,
  "r_right":0.15,
  "k_right":-0.1,
  "o":0.45,
  "t_right": 0.25,
  "t_left": 0.25, 
  "s": 0.45 
}
        
def glyph_a(font, xh, a, d, w, t, s, r, ct, bo):    
    glyph = font.newGlyph("a")
    glyph.unicode = ord("a")

    #for u in glyph.unicode:
    #    print(glyph.unicode[u])
    path = glyph.getPen()
    w=w*.9
    
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
    path.qCurveTo((ct/2, 2/3*xh-t), (ct/2, 1/3*xh)) 
    path.qCurveTo((ct/2,t-bo),(w*r,t-bo))
    path.lineTo((w*(1-r), t-bo))
    path.qCurveTo((w-ct/2, t-bo),(w-ct/2, 1/6*xh+t))
    path.lineTo((w-ct/2, 1/6*xh))
    
    path.qCurveTo((w-ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((-ct/2, -bo),(-ct/2, 1/3*xh))
    path.qCurveTo((-ct/2, 2/3*xh),(w*r, 2/3*xh))
    path.lineTo((w-ct/2-50,2/3*xh))
    path.qCurveTo((w-ct/2, 2/3*xh),(w-ct/2,5/6*xh))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["a_left"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_a_dieresis(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("a_dieresis")
    glyph.unicode = ord("ä")

    path = glyph.getPen()
    w=w*.9
    
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
    path.qCurveTo((ct/2, 2/3*xh-t), (ct/2, 1/3*xh)) 
    path.qCurveTo((ct/2,t-bo),(w*r,t-bo))
    path.lineTo((w*(1-r), t-bo))
    path.qCurveTo((w-ct/2, t-bo),(w-ct/2, 1/6*xh+t))
    path.lineTo((w-ct/2, 1/6*xh))
    
    path.qCurveTo((w-ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((-ct/2, -bo),(-ct/2, 1/3*xh))
    path.qCurveTo((-ct/2, 2/3*xh),(w*r, 2/3*xh))
    path.lineTo((w-ct/2-50,2/3*xh))
    path.qCurveTo((w-ct/2, 2/3*xh),(w-ct/2,5/6*xh))
    path.closePath()

    component_dieresis(path, xh+t*2, w, t, r, ct)
    
    #metrics
    glyph.leftMargin = s*spacing["a_left"]
    glyph.rightMargin = s*spacing["l"]
            
def glyph_b(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("b")
    glyph.unicode = ord("b")

    path = glyph.getPen()
    w=w*.95
    component_o(path, xh, w, t, r, ct, bo)
        
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2,a))
    path.lineTo((ct/2, a))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_c(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("c")
    glyph.unicode = ord("c")
        
    path = glyph.getPen()
    w=w*.94
    
    path.moveTo((w-ct/2, xh*(1-r)))
    path.qCurveTo((w-ct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2,xh*(1-r)))
    path.lineTo((ct/2, xh*r))
    path.qCurveTo((ct/2, t/2), (w*r, t/2))
    path.lineTo((w*(1-r),t/2))
    path.qCurveTo((w-ct/2, t/2), (w-ct/2, xh*r))
    
    path.lineTo((w+ct/2, xh*r))
    path.qCurveTo((w+ct/2, -t/2), (w*(1-r), -t/2))
    path.lineTo((w*r,-t/2))
    path.qCurveTo((-ct/2, -t/2), (-ct/2, xh*r))
    path.lineTo((-ct/2, xh*(1-r)))
    path.qCurveTo((-ct/2, xh+bo), (w*r,xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2,xh*(1-r)))
    path.closePath()    
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["c_right"]
    
def glyph_c_cedilla(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("c_cedilla")
    glyph.unicode = ord("ç")
    
    path = glyph.getPen()
    w=w*.94
    
    path.moveTo((w-ct/2, xh*(1-r)))
    path.qCurveTo((w-ct/2, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2,xh*(1-r)))
    path.lineTo((ct/2, xh*r))
    path.qCurveTo((ct/2, t/2), (w*r, t/2))
    path.lineTo((w*(1-r),t/2))
    path.qCurveTo((w-ct/2, t/2), (w-ct/2, xh*r))
    
    path.lineTo((w+ct/2, xh*r))
    path.qCurveTo((w+ct/2, -t/2), (w*(1-r), -t/2))
    path.lineTo((w*r,-t/2))
    path.qCurveTo((-ct/2, -t/2), (-ct/2, xh*r))
    path.lineTo((-ct/2, xh*(1-r)))
    path.qCurveTo((-ct/2, xh+bo), (w*r,xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2,xh*(1-r)))
    path.closePath()    
    
    component_cedilla(path, -t/2, w, t, r)
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s *spacing["c_right"]

def glyph_d(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("d")
    glyph.unicode = ord("d")

    path = glyph.getPen()
    w=w*.95
    component_o(path, xh, w, t, r, ct, bo)
    
    path.moveTo((w-ct/2, a))
    path.lineTo((w+ct/2, a))
    path.lineTo((w+ct/2, 0))
    path.lineTo((w-ct/2, 0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_e(font, xh, a, d, w, t, s, r, ct, bo):
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
    glyph.leftMargin = s**spacing["o"]
    glyph.rightMargin = s*spacing["c_right"]
    
def glyph_f(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("f")
    glyph.unicode = ord("f")
    
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
    path.closePath()    
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*-spacing["l"]
    
def glyph_g(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("g")
    glyph.unicode = ord("g")
    
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
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_g_breve(font, xh, a, d, w, t, s, r, ct, bo):
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
    
    component_breve(path, xh+t, w, t, r)
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["n_right"]
    

def glyph_h(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("h")
    glyph.unicode = ord("h")
    
    path = glyph.getPen()
    w=w*.85
    
    path.moveTo((0, 0))
    path.lineTo((0, a))
    path.lineTo((ct, a))
    path.lineTo((ct, 0))
    path.closePath()
    
    path.moveTo((0,0))
    path.lineTo((0, 2/3*xh))
    path.qCurveTo((0, xh+bo), (w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w, xh+bo), (w, xh*2/3))
    path.lineTo((w,0))
    path.lineTo((w-ct,0))
    path.lineTo((w-ct, 2/3*xh))
    path.qCurveTo((w-ct, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct, xh-t+bo), (ct, xh*2/3))
    path.lineTo((ct,0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_i_dotless(font, xh, a, d, w, t, s, r, ct, bo):
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
    
def glyph_i(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("i")
    glyph.unicode = ord("i")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh))
    path.lineTo((ct, xh))
    path.lineTo((ct, 0))
    path.closePath()
    
    component_dot(path, ct/2, xh+ct*2, ct, r)
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 
    
def glyph_k(font, xh, a, d, w, t, s, r, ct, bo):
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
    
    path.moveTo
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["v"] 
    
def glyph_l(font, xh, a, d, w, t, s, r, ct, bo):
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
    
def glyph_m(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("m")
    glyph.unicode = ord("m")
    
    m = w*0.8
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh+bo))
    path.lineTo((ct, xh+bo))
    path.lineTo((ct, 0))
    path.closePath()
    
    path.moveTo((0,0))
    path.lineTo((0, 2/3*xh))
    path.qCurveTo((0, xh+bo), (m*r, xh+bo))
    path.lineTo((m*(1-r), xh+bo))
    path.qCurveTo((m+ct/2, xh+bo), (m+ct/2, xh*2/3))
    path.lineTo((m+ct/2,0))
    path.lineTo((m-ct/2,0))
    path.lineTo((m-ct/2, 2/3*xh))
    path.qCurveTo((m-ct/2, xh-t+bo), (m*(1-r), xh-t+bo))
    path.lineTo((m*r, xh-t+bo))
    path.qCurveTo((ct, xh-t+bo), (ct, xh*2/3))
    path.lineTo((ct,0))
    path.closePath()
    
    path.moveTo((m-ct/2,0))
    path.lineTo((m-ct/2, 2/3*xh))
    path.qCurveTo((m-ct/2, xh+bo), (m+m*r, xh+bo))
    path.lineTo((m+m*(1-r), xh+bo))
    path.qCurveTo((m+m, xh+bo), (m+m, xh*2/3))
    path.lineTo((m+m,0))
    path.lineTo((m+m-ct,0))
    path.lineTo((m+m-ct, 2/3*xh))
    path.qCurveTo((m+m-ct, xh-t+bo), (m+m*(1-r), xh-t+bo))
    path.lineTo((m+m*r, xh-t+bo))
    path.qCurveTo((m+ct/2, xh-t+bo), (m+ct/2, xh*2/3))
    path.lineTo((m+ct/2,0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]   

def glyph_n(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("n")
    glyph.unicode = ord("n")
    
    path = glyph.getPen()
    w=w*.85
    
    path.moveTo((0, 0))
    path.lineTo((0, xh+bo))
    path.lineTo((ct, xh+bo))
    path.lineTo((ct, 0))
    path.closePath()
    
    path.moveTo((0,0))
    path.lineTo((0, 2/3*xh))
    path.qCurveTo((0, xh+bo), (w*r, xh+bo))
    path.lineTo((w*(1-r), xh+bo))
    path.qCurveTo((w, xh+bo), (w, xh*2/3))
    path.lineTo((w,0))
    path.lineTo((w-ct,0))
    path.lineTo((w-ct, 2/3*xh))
    path.qCurveTo((w-ct, xh-t+bo), (w*(1-r), xh-t+bo))
    path.lineTo((w*r, xh-t+bo))
    path.qCurveTo((ct, xh-t+bo), (ct, xh*2/3))
    path.lineTo((ct,0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_o(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("o")
    glyph.unicode = ord("o")
    
    path = glyph.getPen()
    w=w*.98
    component_o(path, xh, w, t, r, ct, bo)
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_o_dieresis(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("o_dieresis")
    glyph.unicode = ord("ö")
    
    path = glyph.getPen()
    w=w*.98
    component_o(path, xh, w, t, r, ct, bo)
    
    component_dieresis(path, xh+ct*2, w, t, r, ct)
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_p(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("p")
    glyph.unicode = ord("p")
    
    path = glyph.getPen()
    w=w*.95
    component_o(path, xh, w, t, r, ct, bo)
    
    path.moveTo((-ct/2, -a+xh))
    path.lineTo((-ct/2, xh))
    path.lineTo((ct/2, xh))
    path.lineTo((ct/2, -a+xh))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["o"]

def glyph_q(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("q")
    glyph.unicode = ord("q")
    
    path = glyph.getPen()
    w=w*.95
    component_o(path, xh, w, t, r, ct, bo)
    
    path.moveTo((w-ct/2, -a+xh))
    path.lineTo((w-ct/2,xh))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w+ct/2, -a+xh))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_r(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("r")
    glyph.unicode = ord("r")
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh+bo))
    path.lineTo((ct, xh+bo))
    path.lineTo((ct, 0))
    path.closePath()
    
    path.moveTo((0, xh*(1-r)))
    path.qCurveTo((0, xh+bo), (w/3, xh+bo))
    path.lineTo((w/3, xh-t+bo))
    path.qCurveTo((ct, xh-t+bo), (ct, xh*(1-r)))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["r_right"]
    
def glyph_s(font, xh, a, d, w, t, s, r, ct, bo):    
    glyph = font.newGlyph("s")
    glyph.unicode = ord("s")
    
    path = glyph.getPen()
    w = w*.85
    
    path.moveTo((w,xh*3/4))
    path.qCurveTo((w,xh+t/2),(w*(1-r), xh+t/2))
    path.lineTo((w*r, xh+t/2))
    path.qCurveTo((0,xh+t/2),(0, xh*3/4))
    path.qCurveTo((0,xh*2/4-t/2),(w*r, xh*2/4-t/2))
    path.lineTo((w*(1-r), xh*2/4-t/2))
    path.qCurveTo((w-ct+bo, xh*2/4-t/2), (w-ct+bo, xh*1/4))
    path.qCurveTo((w-ct+bo, t/2), (w*(1-r), t/2))
    path.lineTo((w*r, t/2))
    path.qCurveTo((ct-bo*2,t/2), (ct-bo*2,xh*1/4))
    
    path.lineTo((-bo*2,xh*1/4))
    path.qCurveTo((-bo*2, -t/2), (w*r, -t/2))
    path.lineTo((w*(1-r), -t/2))
    path.qCurveTo((w+bo, -t/2), (w+bo, xh*1/4))
    path.qCurveTo((w+bo, xh*2/4+t/2),(w*(1-r), xh*2/4+t/2))
    path.lineTo((w*r,xh*2/4+t/2))
    path.qCurveTo((ct, xh*2/4+t/2),(ct, xh*3/4))
    path.qCurveTo((ct, xh-t/2),(w*r, xh-t/2))
    path.lineTo((w*(1-r), xh-t/2))
    path.qCurveTo((w-ct, xh-t/2),(w-ct, xh*3/4))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["s"]
    glyph.rightMargin = s*spacing["s"]
    
def glyph_s_cedilla(font, xh, a, d, w, t, s, r, ct, bo):    
    glyph = font.newGlyph("s_cedilla")
    glyph.unicode = ord("ş")
    
    path = glyph.getPen()
    w = w*.85

    path.moveTo((w,xh*3/4))
    path.qCurveTo((w,xh+t/2),(w*(1-r), xh+t/2))
    path.lineTo((w*r, xh+t/2))
    path.qCurveTo((0,xh+t/2),(0, xh*3/4))
    path.qCurveTo((0,xh*2/4-t/2),(w*r, xh*2/4-t/2))
    path.lineTo((w*(1-r), xh*2/4-t/2))
    path.qCurveTo((w-ct+bo, xh*2/4-t/2), (w-ct+bo, xh*1/4))
    path.qCurveTo((w-ct+bo, t/2), (w*(1-r), t/2))
    path.lineTo((w*r, t/2))
    path.qCurveTo((ct-bo*2,t/2), (ct-bo*2,xh*1/4))
    
    path.lineTo((-bo*2,xh*1/4))
    path.qCurveTo((-bo*2, -t/2), (w*r, -t/2))
    path.lineTo((w*(1-r), -t/2))
    path.qCurveTo((w+bo, -t/2), (w+bo, xh*1/4))
    path.qCurveTo((w+bo, xh*2/4+t/2),(w*(1-r), xh*2/4+t/2))
    path.lineTo((w*r,xh*2/4+t/2))
    path.qCurveTo((ct, xh*2/4+t/2),(ct, xh*3/4))
    path.qCurveTo((ct, xh-t/2),(w*r, xh-t/2))
    path.lineTo((w*(1-r), xh-t/2))
    path.qCurveTo((w-ct, xh-t/2),(w-ct, xh*3/4))
    path.closePath()
    
    component_cedilla(path, -t/2, w, t, r)
        
    #metrics
    glyph.leftMargin = s*spacing["s"]
    glyph.rightMargin = s*spacing["s"]

    
def glyph_t(font, xh, a, d, w, t, s, r, ct, bo):    
    glyph = font.newGlyph("t")
    glyph.unicode = ord("t")
    
    path = glyph.getPen()
    
    path.moveTo((0, xh*.2))
    path.lineTo((0, xh*1.2-t/2+t*r/2))
    path.lineTo((ct, xh*1.2-t/2+t*r/2))
    path.lineTo((ct, xh*.2))
    path.qCurveTo((ct, t), (ct+w/4*r,t))
    path.lineTo((ct+w/4*(1-r),t))
    
    path.lineTo((w/4*(1-r)+ct,0))
    path.lineTo((w/4*r+ct, 0))
    path.qCurveTo((0,0), (0, xh*.2))
    path.closePath()
    
    path.moveTo((-w/6*(1-r), xh))
    path.lineTo((ct+w/4*(1-r), xh))
    path.lineTo((ct+w/4*(1-r),xh-t))
    path.lineTo((-w/6*(1-r), xh-t))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["t_left"]
    glyph.rightMargin = s*spacing["t_right"]

    
def glyph_u(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("u")
    glyph.unicode = ord("u")
    
    path = glyph.getPen()
    w=w*.82
    
    path.moveTo((0,xh))
    path.lineTo((0, 1/3*xh))
    path.qCurveTo((0, -bo), (w*r, -bo))
    path.lineTo((w*(1-r), -bo))
    path.qCurveTo((w, -bo), (w, xh*1/3))
    path.lineTo((w-ct, 1/3*xh))
    path.qCurveTo((w-ct, t-bo), (w*(1-r), t-bo))
    path.lineTo((w*r, t-bo))
    path.qCurveTo((ct, t-bo), (ct, xh*1/3))
    path.lineTo((ct,xh))
    path.closePath()
    
    path.moveTo((w-ct, 0))
    path.lineTo((w, 0))
    path.lineTo((w, xh))
    path.lineTo((w-ct, xh))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["n_right"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_u_dieresis(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("u_dieresis")
    glyph.unicode = ord("ü")
    
    path = glyph.getPen()
    w=w*.82
    
    path.moveTo((0,xh))
    path.lineTo((0, 1/3*xh))
    path.qCurveTo((0, -bo), (w*r, -bo))
    path.lineTo((w*(1-r), -bo))
    path.qCurveTo((w, -bo), (w, xh*1/3))
    path.lineTo((w-ct, 1/3*xh))
    path.qCurveTo((w-ct, t-bo), (w*(1-r), t-bo))
    path.lineTo((w*r, t-bo))
    path.qCurveTo((ct, t-bo), (ct, xh*1/3))
    path.lineTo((ct,xh))
    path.closePath()
    
    path.moveTo((w-ct, 0))
    path.lineTo((w, 0))
    path.lineTo((w, xh))
    path.lineTo((w-ct, xh))
    path.closePath()
        
    component_dieresis(path, xh+ct*2, w, t, r, ct)
        
    #metrics
    glyph.leftMargin = s*spacing["n_right"]
    glyph.rightMargin = s *spacing["l"]
    
def glyph_v(font, xh, a, d, w, t, s, r, ct, bo):    
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
    
def glyph_w(font, xh, a, d, w, t, s, r, ct, bo):    
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
    
def glyph_x(font, xh, a, d, w, t, s, r, ct, bo):
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
    
def glyph_y(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("y")
    glyph.unicode = ord("y")
    
    path = glyph.getPen()
    w=w*.82
    
    path.moveTo((0,xh))
    path.lineTo((0, 1/3*xh))
    path.qCurveTo((0, -bo), (w*r, -bo))
    path.lineTo((w*(1-r), -bo))
    path.qCurveTo((w, -bo), (w, xh*1/3))
    path.lineTo((w-ct, 1/3*xh))
    path.qCurveTo((w-ct, t-bo), (w*(1-r), t-bo))
    path.lineTo((w*r, t-bo))
    path.qCurveTo((ct, t-bo), (ct, xh*1/3))
    path.lineTo((ct,xh))
    path.closePath()
    
    path.moveTo((w, xh))
    path.lineTo((w-ct, xh))
    path.lineTo((w-ct, d+xh/3))
    
    path.qCurveTo((w-ct, d+t/2), (w*(1-r), d+t/2))
    path.lineTo((w*r, d+t/2))
    path.qCurveTo((ct, d+t/2), (ct, d+xh/3))
    path.lineTo((0, d+xh/3))
    
    path.qCurveTo((0, d-t/2), (w*r, d-t/2))
    path.lineTo((w*(1-r), d-t/2))
    path.qCurveTo((w, d-t/2), (w, d+xh/3))
    
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["n_right"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_z(font, xh, a, d, w, t, s, r, ct, bo):
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

def glyph_space(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("space")
    glyph.unicode = ord(" ")
    
    glyph.width = w*.8
    
def glyph_hyphen(font, xh, a, d, w, t, s, r, ct, bo):    
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
    
def glyph_underscore(font, xh, a, d, w, t, s, r, ct, bo):    
    glyph = font.newGlyph("underscore")
    glyph.unicode = ord("_")
    
    #print('w:', w, 't:', t, 'r:', r)
    
    path = glyph.getPen()
    
    path.moveTo((0,-t))
    path.lineTo((w,-t))
    path.lineTo((w,0))
    path.lineTo((0,0))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_period(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("period")
    glyph.unicode = ord(".")
    
    path = glyph.getPen()
    
    component_dot(path, 0, t/2, t*1.25, r)
    path.moveTo((0,0))
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 
    
def glyph_comma(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("comma")
    glyph.unicode = ord(",")
    
    path = glyph.getPen()
    dr = t*1.25*(1+r)
    
    ra = math.radians(-20)
    #(x*math.cos(ra)-y*math.sin(ra),x*math.sin(ra)+y*math.cos(ra))
    
    path.moveTo((-dr/2*math.cos(ra)-0*math.sin(ra), -dr/2*math.sin(ra)+0*math.cos(ra)))
    path.qCurveTo((-dr/2*math.cos(ra)-dr/2*math.sin(ra),-dr/2*math.sin(ra)+dr/2*math.cos(ra)), (0*math.cos(ra)-dr/2*math.sin(ra),0*math.sin(ra)+dr/2*math.cos(ra)))
    path.qCurveTo((dr/2*math.cos(ra)-dr/2*math.sin(ra),dr/2*math.sin(ra)+dr/2*math.cos(ra)), (dr/2*math.cos(ra)-0*math.sin(ra),dr/2*math.sin(ra)+0*math.cos(ra)))
    path.lineTo((t/2*math.cos(ra)-d/2*math.sin(ra),t/2*math.sin(ra)+d/2*math.cos(ra)))
    path.lineTo((-t/2*math.cos(ra)-d/2*math.sin(ra),-t/2*math.sin(ra)+d/2*math.cos(ra)))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_quotesingle(font, xh, a, d, w, t, s, r, ct, bo):
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
    
def glyph_quotedbl(font, xh, a, d, w, t, s, r, ct, bo):
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
    
def glyph_exclam(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("exclam")
    glyph.unicode = ord("!")
    
    path = glyph.getPen()
    component_dot(path, 0, t/2, t*1.25, r)
    
    path.moveTo((-t/2, t*3))
    path.lineTo((t/2, t*3))
    path.lineTo((ct/2, ct*4))
    path.lineTo((ct/2, a))
    path.lineTo((-ct/2, a))
    path.lineTo((-ct/2, ct*4))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_colon(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("colon")
    glyph.unicode = ord(":")
    
    path = glyph.getPen()
    
    component_dot(path, 0, t/2, t*1.25, r)
    component_dot(path, 0, xh-t/2, t*1.25, r)
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 
    
def glyph_parenleft(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("parenleft")
    glyph.unicode = ord("(")
    
    path = glyph.getPen()
    
    path.moveTo((w/6,d))
    path.qCurveTo((0,d), (0, a/2))
    path.qCurveTo((0,a), (w/6, a))
    
    path.lineTo((w/6+ct,a))
    path.qCurveTo((ct,a), (ct, a/2))
    path.qCurveTo((ct,d), (w/6+ct, d))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["c_right"]
    
def glyph_parenright(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("parenright")
    glyph.unicode = ord(")")
    
    path = glyph.getPen()
    
    path.moveTo((0,d))
    path.qCurveTo((w/6,d), (w/6, a/2))
    path.qCurveTo((w/6,a), (0, a))
    
    path.lineTo((ct,a))
    path.qCurveTo((w/6+ct,a), (w/6+ct, a/2))
    path.qCurveTo((w/6+ct,d), (ct, d))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["c_right"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_bracketleft(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("bracketleft")
    glyph.unicode = ord("[")
    
    path = glyph.getPen()
    
    path.moveTo((0,d))
    path.lineTo((0,a))
    path.lineTo((w/6,a))
    path.lineTo((w/6,a-t))
    path.lineTo((ct,a-t))
    path.lineTo((ct,d+t))
    path.lineTo((w/6,d+t))
    path.lineTo((w/6,d))
    path.closePath()

    # metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_bracketright(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("bracketright")
    glyph.unicode = ord("]")
    
    path = glyph.getPen()
    
    path.moveTo((0, d))
    path.lineTo((w/6, d))
    path.lineTo((w/6, a))
    path.lineTo((0, a))
    path.lineTo((0, a-t))
    path.lineTo((w/6-ct, a-t))
    path.lineTo((w/6-ct, d+t))
    path.lineTo((0, d+t))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_bullet(font, xh, a, d, w, t, s, r, ct, bo):
    glyph = font.newGlyph("bullet")
    glyph.unicode = ord("•")
    
    path = glyph.getPen()
    
    component_dot(path, 0, xh/2, t*5, r)
    path.moveTo((0,0))
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 

    
def glyph_fi(font, xh, a, d, w, t, s, r, ct, bo):
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
    
def glyph_notdef(font, xh, a, d, w, t, s, r, ct, bo):
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
    path.qCurveTo((-ct/2, xh + t/2),(w*r, xh+bo))
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
    dr = t*(1+r)
    
    path.moveTo((x, y+dr/2))
    path.qCurveTo((x+dr/2, y+dr/2), (x+dr/2, y))
    path.qCurveTo((x+dr/2, y-dr/2), (x, y-dr/2))
    path.qCurveTo((x-dr/2, y-dr/2), (x-dr/2, y))
    path.qCurveTo((x-dr/2, y+dr/2), (x, y+dr/2))
    path.closePath()
    
def component_dieresis(path, h, w, t, r, ct):
    nt = t*.75
    
    component_dot(path, t*2, h+nt/2, ct, r)
    component_dot(path, w-t*2, h+nt/2, ct, r)
    
def component_breve(path, h, w, t, r):
    nt = t*.75
    
    path.moveTo((nt, h+w/6))
    path.qCurveTo((nt, h), (w*r, h))
    path.lineTo((w*(1-r),h))
    path.qCurveTo((w-nt, h), (w-nt,h+w/6))
    
    path.lineTo((w-nt*2, h+w/6))
    path.qCurveTo((w-nt*2, h+nt), (w*(1-r), h+nt))
    path.lineTo((w*r, h+nt))
    path.qCurveTo((nt*2, h+nt), (nt*2, h+w/6))
    path.closePath()
    
def component_cedilla(path, h, w, t, r):
    nt = t*.75
    d = calculateDiagonal(nt, (w/2-nt, 0), (w/2, -nt))
    
    path.moveTo((w/2-nt, h))
    path.lineTo((w/2-nt+d[0], h))
    path.lineTo((w/2+nt+d[0], h-nt*2))
    
    path.lineTo((w/2, h-nt*2))
    path.qCurveTo((w*r+nt, h-nt*2), (w*r+nt, h-nt*2.5))
    path.qCurveTo((w*r+nt, h-nt*3), (w/2, h-nt*3))
    path.lineTo((w/2+nt+d[0], h-nt*3))
    
    path.lineTo((w/2+nt+d[0], h-nt*4))
    path.lineTo((w/2, h-nt*4))
    path.qCurveTo((w*r, h-nt*4),(w*r, h-nt*2.5))
    path.qCurveTo((w*r, h-nt), (w/2, h-nt))

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

def generateSource(masterName, xHeight, ascender, descender, width, thickness, roundness, contrast):   
    master = RFont()#showInterface=False)
    master.info.familyName = familyName
    master.info.styleName = styleName
    master.info.xHeight = xHeight
    master.info.capHeight = capHeight
    master.info.unitsPerEm = capHeight + abs(ascender)
    master.info.descender = descender
    master.info.ascender = ascender
    spacing = thickness/50 + 100
    contrast_thickness = thickness*(1+contrast)
    bottom_offset = thickness*.25

    glyph_notdef(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_space(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_a(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_a_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_b(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_c(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_c_cedilla(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_d(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_e(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_f(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_g(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_g_breve(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_h(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_i_dotless(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_i(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_k(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_l(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_m(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_n(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_o(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_o_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_p(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_q(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_r(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_s(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_s_cedilla(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_t(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_u(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_u_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_v(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_w(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_x(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_y(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_z(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_period(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_comma(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_quotesingle(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_quotedbl(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_colon(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_hyphen(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_underscore(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_parenleft(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_parenright(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_bracketleft(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_bracketright(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_exclam(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)
    glyph_bullet(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset)

    source = doc.newSourceDescriptor()
    source.font = master.naked()
    source.location = dict(Width=width, Thickness=thickness, Roundness=roundness, Contrast=contrast)
    if width == 600 and thickness == 40 and roundness == .3 and contrast == .2:
        source.copyLib=True
        print('This is the base master', source.location, source.copyLib)
    doc.addSource(source)

minW = 100
maxW = 900

minT = 1
maxT = 50

minR = 0.05
maxR = 0.45

minC = 0
maxC = 1

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
axisR.default = 0.3
axisR.maximum = maxR
doc.addAxis(axisR)

axisC = doc.newAxisDescriptor()
axisC.name = "Contrast"
axisC.tag = "CNTR"
axisC.minimum = minC
axisC.default = .2
axisC.maximum = maxC
doc.addAxis(axisC)

familyName = "Shah"
styleName = "Regular"
xHeight = 300
capHeight = 400

#change roundness from 0.1-0.5 to 1-100
def testing():
    a = 0
    d = 1
    r = 7
    w = 3
    t = 4
    c = 3
    generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*100, (t+1)*5, (r+1)/20, c*.2)

def export():  
    for w in range(9):
        for t in range(10):
            for r in range(10):
                for c in range(6):
                    a = 0
                    d = 1
                    generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*100, (t+1)*5, (r+1)/20, c*.2)

    print('Compiling TTF...')
    varFont = ufo2ft.compileVariableTTF(doc)
    print('Saving...')
    font_name = f"export/{familyName}GX-{datetime.now()}.ttf"
    varFont.save(font_name)
    print(f"Done exporting {font_name}")
    
testing()
