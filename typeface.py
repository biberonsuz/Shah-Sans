import math
from datetime import datetime
import logging
import os
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#create ratios for specific letter spacings in order to group them etc.   
spacing = {
    "l": 1,
    "n_right": .88,
    "a_left": .55,
    "a_right": .7,
    "s_right": .6,
    "a_left": .6,
    "o":.52,
    "e_left": .49,
    "e_right":.45,
    "c_right": .43,
    "z": .4,
    "f_right":.36,
    "f_left":.28,
    "r_right":.1,
    "t_left": .40,
    "t_right": .45,
    "v": .1,
    "j_left":-.14,
    "k_right":-.1,
    "A":-.1,
    "O":.8,
    "T": .2,
    "E_right": .5,
    "V": .14,
}

width = {
    "m": 1.66,
    "w": 1.44,
    "d": 1.11, "p": 1.11, "q": 1.11, "b": 1.11, "g": 1.11,
    "o": 1.11,
    "e": 1.11, "n": 1.11, "h": 1.11,
    "u": 1.11, "y": 1.11,
    "a": 1.11, 
    "c": 1,
    "s": 1, 
    "x": 1,
    "k": 1,
    "z": 1, "v": 1,
    "r": .66,
    "t": .55,  "f": .55,
    "A": 1.33, "K": 1.33, "V": 1.33, "X": 1.33,
    "O": 1.55,
    "D": 1.44,
    "L": 1.11,
    "T": 1.4,
    "E": 1.33,
    "F": 1.22,
    "U": 1.44, "H": 1.44, "N": 1.44,
    "Z": 1.22,
    "W": 1.88
}

def kerning_groups(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    font.kerning["A", "T"] = s*-1.5
    font.kerning["L", "T"] = s*-1.4

def glyph_A(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("A")
    glyph.unicode = ord("A")
    
    w=w*width["A"]
    
    d = calculate_diagonal(ct,(0,0),(w/2,a))
    midh = xh/2
        
    path = glyph.getPen()
    
    path.moveTo((-d[0]/2, 0))
    path.lineTo((w/2-d[0]/2, a))
    path.lineTo((w/2+d[0]/2, a))
    path.lineTo((w+d[0]/2, 0))
    path.lineTo((w-d[0]/2, 0))
    path.lineTo((w/2, a-d[1]/2))
    path.lineTo((d[0]/2, 0))
    path.closePath()
    
    path.moveTo((d[0]*midh/d[1],midh+t/2))
    path.lineTo((w-d[0]*midh/d[1],midh+t/2))
    path.lineTo((w-d[0]*midh/d[1],midh-t/2))
    path.lineTo((d[0]*midh/d[1],midh-t/2))
    path.closePath()
    
    glyph.leftMargin = s*spacing["A"]
    glyph.rightMargin = s*spacing["A"] 
 
def glyph_C(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("C")
    glyph.unicode = ord("C")

    path = glyph.getPen()
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["o"]   

def glyph_D(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("D")
    glyph.unicode = ord("D")

    w=w*width["D"]
    path = glyph.getPen()
    
    wc = 0.552284749831*(2-r)*(w+ct)/2
    ac = 0.552284749831*a/2
    
    path.moveTo((0,a))
    path.lineTo((w/2, a))
    path.curveTo((w/2+wc, a), (w+ct/2, a/2+ac), (w+ct/2, a/2))
    path.curveTo((w+ct/2, a/2-ac),(w/2+wc, 0), (w/2, 0))
    path.lineTo((0,0))
    path.closePath()
        
    wc = 0.552284749831*(2-r)*(w-ct)/2
    ac = 0.552284749831*a/2-t/2
    
    path.moveTo((ct, a-t))
    path.lineTo((ct, t))
    path.lineTo((w/2, t))
    path.curveTo((w/2+wc, t), (w-ct/2, a/2-ac), (w-ct/2, a/2))
    path.curveTo((w-ct/2, a/2+ac), (w/2+wc, a-t), (w/2, a-t))
    path.closePath()
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["o"]  
    
def glyph_E(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("E")
    glyph.unicode = ord("E")
    
    w=w*width["E"]
    midh = a*.55
    midw = w*.7
        
    path = glyph.getPen()
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, a))
    path.lineTo((w, a))
    
    path.lineTo((w, a-t))
    path.lineTo((ct/2, a-t))
    path.lineTo((ct/2, midh+t/2))
    path.lineTo((midw, midh+t/2))
    path.lineTo((midw, midh-t/2))
    path.lineTo((ct/2, midh-t/2))
    
    path.lineTo((ct/2, t))
    path.lineTo((w, t))
    path.lineTo((w, 0))
    path.closePath()
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["E_right"] 
    
def glyph_F(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("F")
    glyph.unicode = ord("F")

    w=w*width["F"]
    
    midh = a*.55    
    midw = w*.7
    
    path = glyph.getPen()
        
    path.moveTo((-ct/2, a))
    path.lineTo((w, a))
    
    path.lineTo((w, a-t))
    path.lineTo((ct/2, a-t))
    path.lineTo((ct/2, midh+t/2))
    path.lineTo((midw, midh+t/2))
    path.lineTo((midw, midh-t/2))
    path.lineTo((ct/2, midh-t/2))
    
    path.lineTo((ct/2, 0))
    path.lineTo((-ct/2, 0))
    path.closePath()

    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["E_right"]  

    
def glyph_H(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("H")
    glyph.unicode = ord("H")

    w=w*width["H"]
    
    midh = a/2
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2,a))
    path.lineTo((ct/2, a))
    path.lineTo((ct/2, midh+t/2))
    path.lineTo((w-ct/2, midh+t/2))
    path.lineTo((w-ct/2, a))
    path.lineTo((w+ct/2, a))
    path.lineTo((w+ct/2, 0))
    path.lineTo((w-ct/2, 0))
    path.lineTo((w-ct/2, midh-t/2))
    path.lineTo((ct/2, midh-t/2))
    path.lineTo((ct/2, 0))
    path.lineTo((-ct/2, 0))
    path.closePath()
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]  
    
def glyph_I(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("I")
    glyph.unicode = ord("I")
    
    w=ct 
    path = glyph.getPen()
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, a))
    path.lineTo((ct/2, a))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 
    
def glyph_K(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("K")
    glyph.unicode = ord("K")
    
    w=w*width["K"]
    
    midh = a/2
    d = calculate_diagonal(t,(ct,midh),(w,a))
        
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, a))
    path.lineTo((ct, a))
    path.lineTo((ct, 0))
    path.closePath()
    
    path.moveTo((ct, midh))
    path.lineTo((w, a))
    path.lineTo((w+d[0], a))
    path.lineTo((ct+d[0], midh))
    path.lineTo((w+d[0], 0))
    path.lineTo((w, 0))
    path.closePath()
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["A"] 
    
def glyph_L(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("L")
    glyph.unicode = ord("L")
    
    w=w*width["L"]
        
    path = glyph.getPen()
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, a))
    path.lineTo((ct/2, a))
    path.lineTo((ct/2, t))
    path.lineTo((w, t))
    path.lineTo((w, 0))
    path.closePath()
    
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["T"] 
    
def glyph_N(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("N")
    glyph.unicode = ord("N")
    
    w=w*width["N"]
    
    d = calculate_diagonal(t,(0,0),(w,a))
        
    path = glyph.getPen()
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, a))
    path.lineTo((d[0]/2, a))
    
    path.lineTo((w+d[0]/4, d[1]/4))
    path.lineTo((w-ct/2, 0))
    path.lineTo((w-ct/2, a))
    path.lineTo((w+ct/2, a))
    path.lineTo((w+ct/2, 0))
    path.lineTo((w-d[0]/2, 0))
    
    path.lineTo((-d[0]/4, a-d[1]/4))
    path.lineTo((ct/2, a))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 

def glyph_O(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("O")
    glyph.unicode = ord("O") 
     
    w=w*width["O"]
    
    path = glyph.getPen()
    
    wc = 0.552284749831*(2-r)*(w+ct)/2
    ac = 0.552284749831*a/2+bo
    
    path.moveTo((w/2, a+bo))
    path.curveTo((w/2+wc, a+bo), (w+ct/2, a/2+ac), (w+ct/2, a/2))
    path.curveTo((w+ct/2, a/2-ac),(w/2+wc, -bo), (w/2, -bo))
    path.curveTo((w/2-wc, -bo), (-ct/2, a/2-ac), (-ct/2, a/2))
    path.curveTo((-ct/2, a/2+ac), (w/2-wc, a+bo), (w/2, a+bo))
    path.closePath()
    
    wc = 0.552284749831*(2-r)*(w-ct)/2
    ac = 0.552284749831*a/2+bo-t/2
    
    path.moveTo((w/2, a+bo-t))
    path.curveTo((w/2-wc, a+bo-t), (ct/2, a/2+ac), (ct/2, a/2))
    path.curveTo((ct/2, a/2-ac), (w/2-wc, -bo+t), (w/2, -bo+t))
    path.curveTo((w/2+wc, -bo+t), (w-ct/2, a/2-ac), (w-ct/2, a/2))
    path.curveTo((w-ct/2, a/2+ac), (w/2+wc, a+bo-t), (w/2, a+bo-t))
    path.closePath()
        
    glyph.appendAnchor("top", (w/2, a+bo))
    glyph.appendAnchor("bottom", (w/2, -bo))
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_O_dieresis(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("O_dieresis")
    
    construction = GlyphConstructionBuilder("Odieresis = O + dieresis@top", font)
    construction.draw(glyph.getPen())
    
    glyph.unicode = ord("Ö")
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_T(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("T")
    glyph.unicode = ord("T")
    
    w=w*width["T"]
    
    path = glyph.getPen()
    path.moveTo((0,a))
    path.lineTo((w,a))
    path.lineTo((w, a-t))
    path.lineTo((w/2+ct/2, a-t))
    path.lineTo((w/2+ct/2, 0))
    path.lineTo((w/2-ct/2, 0))
    path.lineTo((w/2-ct/2, a-t))
    path.lineTo((0,a-t))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["T"]
    glyph.rightMargin = s*spacing["T"]
    
def glyph_U(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("U")
    glyph.unicode = ord("U")
    
    w=w*width["U"]
    
    path = glyph.getPen()
    
    ch = 0.4*xh
    wc = 0.6*(2-r)*(w/2-ct/2)
    xhc = 0.6*(2-r)*(ch+bo-t)
    
    path.moveTo((-ct/2,a))
    path.lineTo((ct/2,a))
    path.lineTo((ct/2,ch))
    path.curveTo((ct/2, ch-xhc),(w/2-wc, t-bo), (w/2, t-bo))
    path.curveTo((w/2+wc, t-bo),(w-ct/2, ch-xhc),(w-ct/2, ch))
    path.lineTo((w-ct/2, a))
    
    wc = 0.6*(2-r)*(w/2+ct/2)
    xhc = 0.6*(2-r)*(ch+bo)
    
    path.lineTo((w+ct/2, a))
    path.lineTo((w+ct/2,ch))
    path.curveTo((w+ct/2, ch-xhc), (w/2+wc, -bo), (w/2, -bo))
    path.curveTo((w/2-wc, -bo), (-ct/2, ch-xhc), (-ct/2, ch))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["T"]
    glyph.rightMargin = s*spacing["T"]
    
def glyph_V(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("V")
    glyph.unicode = ord("V")
    
    w=w*width["V"]
    
    path = glyph.getPen()
    
    d = calculate_diagonal(t, (0, 0),(w/2, a))
        
    path.moveTo((-d[0]/2,a))
    path.lineTo((w/2-d[0]/2,0))
    path.lineTo((w/2+d[0]/2,0))
    path.lineTo((w+d[0]/2,a))
    path.lineTo((w-d[0]/2,a))
    path.lineTo((w/2-d[0]/2,0))  
    path.lineTo((w/2+d[0]/2,0))  
    path.lineTo((d[0]/2,a))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["V"]
    glyph.rightMargin = s*spacing["V"]
    
def glyph_W(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("W")
    glyph.unicode = ord("W")
    
    w=w*width["W"]
    
    path = glyph.getPen()
    d = calculate_diagonal(ct, (0, 0),(w/4, a))
        
    path.moveTo((-d[0]/2,a))
    path.lineTo((w*.24-d[0]/2, 0))
    path.lineTo((w*.24+d[0]/2, 0))
    path.lineTo((w*.5+d[0]/2, a))
    path.lineTo((w*.5-d[0]/2, a))
    path.lineTo((w*.76-d[0]/2, 0))
    path.lineTo((w*.76+d[0]/2, 0))
    path.lineTo((w+d[0]/2, a))
    path.lineTo((w-d[0]/2, a))
    path.lineTo((w*.76-d[0]/2, 0))
    path.lineTo((w*.76+d[0]/2, 0))
    path.lineTo((w*.5+d[0]/2, a))
    path.lineTo((w*.5-d[0]/2, a))
    path.lineTo((w*.24-d[0]/2, 0))
    path.lineTo((w*.24+d[0]/2, 0))
    path.lineTo((d[0]/2, a))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["v"]
    glyph.rightMargin = s*spacing["v"]

    
def glyph_X(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("X")
    glyph.unicode = ord("X")
    
    w=w*width["X"]
    
    path = glyph.getPen()
   
    d = calculate_diagonal(t, (0,0), (w,a))
    
    path.moveTo((-d[0]/2,0))
    path.lineTo((w-d[0]/2,a))
    path.lineTo((w+d[0]/2,a))
    path.lineTo((d[0]/2,0))
    path.closePath()
    
    path.moveTo((w-d[0]/2,0))
    path.lineTo((-d[0]/2,a))
    path.lineTo((d[0]/2,a))
    path.lineTo((w+d[0]/2,0))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s*spacing["V"]
    glyph.rightMargin = s*spacing["V"]
    
def glyph_Z(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("Z")
    glyph.unicode = ord("Z")
    
    w=w*width["Z"]
    
    path = glyph.getPen()
    
    d = calculate_diagonal(ct, (0,t), (w,a-t))
    
    path.moveTo((-d[0]/2,a))
    path.lineTo((w+d[0]/2,a))
    path.lineTo((w+d[0]/2,a-t))
    path.lineTo((d[0]/2, t))
    path.lineTo((w+d[0]/2,t))
    path.lineTo((w+d[0]/2,0))
    path.lineTo((-d[0]/2,0))
    path.lineTo((-d[0]/2,t))
    path.lineTo((w-d[0]/2,a-t))
    path.lineTo((-d[0]/2,a-t))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["z"]
    glyph.rightMargin = s*spacing["z"]
    
def glyph_a(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("a")
    glyph.unicode = ord("a")

    w=w*width["a"]
    
    midh = 1.5/3*xh
    
    path = glyph.getPen()
    
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
    
    path.moveTo((w-ct/2, midh-t/2))
    path.qCurveTo((w-ct/2, midh-t/2),(w-ct/2-50, midh-t/2))
    path.lineTo((w*r, midh-t/2))
    path.qCurveTo((rct/2, midh-t/2), (rct/2, (midh-bo+t/2)/2)) 
    path.qCurveTo((rct/2,t-bo),(w*r,t-bo))
    path.lineTo((w*(1-r), t-bo))
    path.qCurveTo((w-ct/2, t-bo),(w-ct/2, 1/6*xh+t))
    path.lineTo((w-ct/2, 1/6*xh))
    
    path.qCurveTo((w-ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w*r, -bo))
    path.qCurveTo((-rct/2, -bo),(-rct/2, (midh-bo+t/2)/2))
    path.qCurveTo((-rct/2, midh+t/2),(w*r, midh+t/2))
    path.lineTo((w-ct/2-50,midh+t/2))
    path.lineTo((w-ct/2, midh+t/2))
    path.closePath()
    
    glyph.appendAnchor("top", (w/2, xh+bo))
        
    #metrics
    glyph.leftMargin = s*spacing["a_left"]
    glyph.rightMargin = s*spacing["a_right"]
    
def glyph_a_dieresis(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("a_dieresis")
    
    construction = GlyphConstructionBuilder("adieresis = a + dieresis@top", font)
    construction.draw(glyph.getPen())
    
    glyph.unicode = ord("ä")
    
    #metrics
    glyph.leftMargin = s*spacing["a_left"]
    glyph.rightMargin = s*spacing["a_right"]
                
def glyph_b(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("b")
    glyph.unicode = ord("b")

    w=w*width["b"]
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2, a))
    path.lineTo((ct/2,a))
    path.lineTo((ct/2,0))
    path.lineTo((-ct/2, 0))
    path.closePath()
    
    hc = w/2
    #curve thickness intersecting the stem
    it = ct*0.5
    
    wc = 0.552284749831*(2-r)*(w/2+ct/2-it)
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path.moveTo((ct/2-it, xh/2))
    path.curveTo((ct/2-it, xh/2+xhc), (hc-wc, xh+bo), (hc, xh+bo))
    
    wc = 0.552284749831*(2-r)*(w/2+rct/2)
    
    path.curveTo((hc+wc, xh+bo), (w+rct/2, xh/2+xhc), (w+rct/2, xh/2))
    path.curveTo((w+rct/2, xh/2-xhc), (hc+wc, -bo), (hc, -bo))
    
    wc = 0.552284749831*(2-r)*(w/2+ct/2-it)
    
    path.curveTo((hc-wc, -bo), (ct/2-it, xh/2-xhc), (ct/2-it, xh/2))
    path.closePath()
    
    wc = 0.552284749831*(2-r)*(w/2-rct/2)
    xhc = 0.552284749831*xh/2+bo-t/2
        
    path.moveTo((ct/2, xh/2))
    path.curveTo((ct/2, xh/2-xhc), (hc-wc, -bo+t), (hc, -bo+t))
    path.curveTo((hc+wc, -bo+t), (w-rct/2, xh/2-xhc), (w-rct/2, xh/2))
    path.curveTo((w-rct/2, xh/2+xhc), (hc+wc, xh-t+bo), (hc, xh-t+bo))
    path.curveTo((hc-wc, xh-t+bo), (ct/2, xh/2+xhc), (ct/2, xh/2))
    path.closePath()     
        
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["e_left"]
    
def glyph_c(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("c")
    glyph.unicode = ord("c")
    
    w=w*width["c"]  
       
    path = glyph.getPen()
    
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
    
    glyph.appendAnchor("top", (w/2, xh+bo))
    glyph.appendAnchor("bottom", (w/2, -bo))
    
    #metrics
    glyph.leftMargin = s*spacing["e_left"]
    glyph.rightMargin = s*spacing["c_right"]
    
def glyph_c_cedilla(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("c_cedilla")
    
    construction = GlyphConstructionBuilder("ccedilla = c + cedilla@bottom", font)
    construction.draw(glyph.getPen())
    
    glyph.unicode = ord("ç")
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["c_right"]

def glyph_d(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("d")
    glyph.unicode = ord("d")

    w=w*width["d"]
    
    path = glyph.getPen()
    
    path.moveTo((w-ct/2, a))
    path.lineTo((w+ct/2,a))
    path.lineTo((w+ct/2,0))
    path.lineTo((w-ct/2, 0))
    path.closePath()
    
    hc = w/2
    #curve thickness intersecting the stem
    it = ct*0.5
    
    wc = 0.552284749831*(2-r)*(w/2+rct/2)
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path.moveTo((-rct/2, xh/2))
    path.curveTo((-rct/2, xh/2+xhc), (hc-wc, xh+bo), (hc, xh+bo))
    
    wc = 0.552284749831*(2-r)*(w/2+ct/2-it)
    
    path.curveTo((hc+wc, xh+bo), (w-ct/2+it, xh/2+xhc), (w-ct/2+it, xh/2))
    path.curveTo((w-ct/2+it, xh/2-xhc), (hc+wc, -bo), (hc, -bo))
    
    wc = 0.552284749831*(2-r)*(w/2+ct/2-it)
    
    path.curveTo((hc-wc, -bo), (-rct/2, xh/2-xhc), (-rct/2, xh/2))
    path.closePath()
    
    wc = 0.552284749831*(2-r)*(w/2-rct/2)
    xhc = 0.552284749831*xh/2+bo-t/2
        
    path.moveTo((rct/2, xh/2))
    path.curveTo((rct/2, xh/2-xhc), (hc-wc, -bo+t), (hc, -bo+t))
    path.curveTo((hc+wc, -bo+t), (w-ct/2, xh/2-xhc), (w-ct/2, xh/2))
    path.curveTo((w-ct/2, xh/2+xhc), (hc+wc, xh-t+bo), (hc, xh-t+bo))
    path.curveTo((hc-wc, xh-t+bo), (rct/2, xh/2+xhc), (rct/2, xh/2))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["e_left"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_e(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("e")
    glyph.unicode = ord("e")
    
    w=w*width["o"]
    wc = 0.552284749831*(2-r)*(w+ct)/2
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path = glyph.getPen()
    
    path.moveTo((w/2, xh+bo))
    path.curveTo((w/2+wc, xh+bo), (w+ct/2, xh/2-t/2+xhc), (w+ct/2, xh/2-t/2))
    path.lineTo((ct/2, xh/2-t/2))
    
    wc = 0.552284749831*(2-r)*(w-ct)/2
    xhc = 0.552284749831*xh/2+bo-t
    
    path.curveTo((ct/2, xh/2-t/2-xhc), (w/2-wc, -bo+t), (w/2, -bo+t))
    ter = calculate_terminals(5.75, w/2-ct/2, xh/2+bo-t)
    path.curveTo((w/2+ter[0], xh/2+ter[1]))
    path.lineTo((w/2+ter[0]+ct, xh/2+ter[1]))
    
    wc = 0.552284749831*(2-r)*(w+ct)/2
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    #path.lineTo((w+ct/2, xh*r))
    #path.qCurveTo((w+ct/2, -bo), (w*(1-r), -bo))
    path.lineTo((w/2, -bo))
    path.curveTo((w/2-wc, -bo), (-ct/2, xh/2-xhc), (-ct/2, xh/2))
    path.lineTo((-ct/2, xh/2))
    
    path.curveTo((-ct/2, xh/2+xhc), (w/2-wc, xh+bo), (w/2, xh+bo))
    path.closePath()
    
    wc = 0.552284749831*(2-r)*(w-ct)/2
    xhc = 0.552284749831*xh/2+bo-t
    
    path.moveTo((w/2, xh+bo-t))
    path.curveTo((w/2-wc, xh+bo-t), (ct/2, xh/2+t/2+xhc), (ct/2, xh/2+t/2))
    path.lineTo((w-ct/2, xh/2+t/2))
    path.curveTo((w-ct/2, xh/2+t/2+xhc), (w/2+wc, xh+bo-t), (w/2, xh+bo-t))
    path.closePath() 
        
    #metrics
    glyph.leftMargin = s*spacing["e_left"]
    glyph.rightMargin = s*spacing["e_right"]
    
def glyph_f(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("f")
    glyph.unicode = ord("f")
    
    w=w*width["f"]
    top = a - xh
    
    path = glyph.getPen()
    
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
    
def glyph_g(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("g")
    glyph.unicode = ord("g")
    
    w=w*width["g"]
    
    path = glyph.getPen()

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
    glyph.leftMargin = s*spacing["e_left"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_g_breve(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("g_breve")
    
    construction = GlyphConstructionBuilder("gbreve = g + breve@top", font)
    construction.draw(glyph.getPen())
    
    glyph.unicode = ord("ğ")
    
    #metrics
    glyph.leftMargin = s*spacing["e_left"]
    glyph.rightMargin = s*spacing["l"]

def glyph_h(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("h")
    glyph.unicode = ord("h")
    
    w=w*width["h"]
    #horizontal curve center
    hc = w/2+ct*.25
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, a))
    path.lineTo((ct/2, a))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    wc = 0.552284749831*(2-r)*(w/2-ct/2+(bo*2))
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path.moveTo((ct/2-bo*2, xh/2))
    path.curveTo((ct/2-bo*2, xh/2+xhc), (hc-wc, xh+bo), (hc, xh+bo))
    
    wc = 0.552284749831*(2-r)*(w+ct)/2
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path.curveTo((hc+wc, xh+bo), (w+ct/2, xh/2+xhc), (w+ct/2, xh/2))
    path.lineTo((w+ct/2,0))
    
    wc = 0.552284749831*(2-r)*(w-ct)/2
    xhc = 0.552284749831*xh/2+bo-t/2
    
    path.lineTo((w-ct/2,0))
    path.lineTo((w-ct/2, xh/2))
    path.curveTo((w-ct/2, xh/2+xhc), (hc+wc, xh-t+bo), (hc, xh-t+bo))
    path.curveTo((hc-wc, xh-t+bo), (ct/2, xh/2+xhc), (ct/2, xh/2))
    path.closePath()     

    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_i_dotless(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("idotless")
    glyph.unicode = ord("ı")
    
    w=ct
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, xh))
    path.lineTo((ct, xh))
    path.lineTo((ct, 0))
    path.closePath()
    
    glyph.appendAnchor("top", (ct/2, xh))
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_i(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("i")
    
    construction = GlyphConstructionBuilder("i = idotless + dot@top", font)
    construction.draw(glyph.getPen())
    
    glyph.unicode = ord("i")
        
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_j_dotless(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("jdotless")
    glyph.unicode = ord("ȷ")
    
    #w=ct
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
    
    glyph.appendAnchor("top", (-ct/2, xh))

    #metrics
    glyph.leftMargin = s*spacing["j_left"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_j(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("j")
    
    construction = GlyphConstructionBuilder("j = jdotless + dot@top", font)
    construction.draw(glyph.getPen())
    
    glyph.unicode = ord("j")
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]

    
def glyph_k(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("k")
    glyph.unicode = ord("k")
    
    d = calculate_diagonal(t,(0,xh/4),(w,xh))
    da = calculate_diagonal(t,(0,0),(w,xh/1.5))
    
    do = calculate_intersection([(0,xh/4),(w,xh)], [(0,xh/1.5),(w,0)])
        
    w=w*width["k"]
    
    path = glyph.getPen()
    path.moveTo((-ct/2,0))
    path.lineTo((-ct/2,a))
    path.lineTo((ct/2,a))
    path.lineTo((ct/2,0))
    path.closePath()
        
    path.moveTo((w-d[0],xh))
    path.lineTo((w, xh))
    path.lineTo((ct/2, xh/4))
    path.lineTo((ct/2, xh/4+d[1]*1.23))
    path.closePath()      
    
    path.moveTo((do[0]-da[0]/2,do[1]))
    path.lineTo((do[0]+da[0]*.15,do[1]+da[1]*.50))
    path.lineTo((w+da[0]/2,0))
    path.lineTo((w-da[0]/2,0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["k_right"] 
    
def glyph_l(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("l")
    glyph.unicode = ord("l")
    
    w=ct
    
    path = glyph.getPen()
    
    path.moveTo((0, 0))
    path.lineTo((0, a))
    path.lineTo((ct, a))
    path.lineTo((ct, 0))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_m(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("m")
    glyph.unicode = ord("m")
    
    w=w*width["m"]
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2, 0))
    path.lineTo((-ct/2, xh))
    path.lineTo((ct/2, xh))
    path.lineTo((ct/2, 0))
    path.closePath()
    
    path.moveTo((ct/2-t/2, 2/3*xh))
    path.qCurveTo((ct/2-t/2, xh+bo), (w/2*r, xh+bo))
    path.lineTo((w/2*(1-r), xh+bo))
    path.qCurveTo((w/2+ct/2, xh+bo), (w/2+ct/2, xh*2/3))
    path.lineTo((w/2+ct/2,0))
    path.lineTo((w/2-ct/2,0))
    path.lineTo((w/2-ct/2, 2/3*xh))
    path.qCurveTo((w/2-ct/2, xh-t+bo), (w/2*(1-r), xh-t+bo))
    path.lineTo((w/2*r, xh-t+bo))
    path.qCurveTo((ct/2, xh-t+bo), (ct/2, xh*2/3))
    path.closePath()
    
    path.moveTo((w/2+ct/2-t/2, 2/3*xh))
    path.qCurveTo((w/2+ct/2-t/2, xh+bo), (w/2+w/2*r, xh+bo))
    path.lineTo((w/2+w/2*(1-r), xh+bo))
    path.qCurveTo((w+ct/2, xh+bo), (w+ct/2, xh*2/3))
    path.lineTo((w+ct/2,0))
    path.lineTo((w-ct/2,0))
    path.lineTo((w-ct/2, 2/3*xh))
    path.qCurveTo((w-ct/2, xh-t+bo), (w/2+w/2*(1-r), xh-t+bo))
    path.lineTo((w/2+w/2*r, xh-t+bo))
    path.qCurveTo((w/2+ct/2, xh-t+bo), (w/2+ct/2, xh*2/3))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]   

def glyph_n(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("n")
    glyph.unicode = ord("n")
    
    w=w*width["n"]
    #horizontal curve center
    hc = w/2+ct*.25
    
    path = glyph.getPen()
    
    stem(path, -ct/2, 0, ct, xh)
    
    wc = 0.552284749831*(2-r)*(w/2-ct/2+(bo*2))
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path.moveTo((ct/2-bo*2, xh/2))
    path.curveTo((ct/2-bo*2, xh/2+xhc), (hc-wc, xh+bo), (hc, xh+bo))
    
    wc = 0.552284749831*(2-r)*(w+ct)/2
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path.curveTo((hc+wc, xh+bo), (w+ct/2, xh/2+xhc), (w+ct/2, xh/2))
    path.lineTo((w+ct/2,0))
    
    wc = 0.552284749831*(2-r)*(w-ct)/2
    xhc = 0.552284749831*xh/2+bo-t/2
    
    path.lineTo((w-ct/2,0))
    path.lineTo((w-ct/2, xh/2))
    path.curveTo((w-ct/2, xh/2+xhc), (hc+wc, xh-t+bo), (hc, xh-t+bo))
    path.curveTo((hc-wc, xh-t+bo), (ct/2, xh/2+xhc), (ct/2, xh/2))
    path.closePath()     
    
            
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["n_right"]
    
def glyph_o(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("o")
    glyph.unicode = ord("o")
    
    w=w*width["o"]
    wc = 0.552284749831*(2-r)*(w+ct)/2
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path = glyph.getPen()
    
    path.moveTo((w/2, xh+bo))
    path.curveTo((w/2+wc, xh+bo), (w+ct/2, xh/2+xhc), (w+ct/2, xh/2))
    path.curveTo((w+ct/2, xh/2-xhc),(w/2+wc, -bo), (w/2, -bo))
    path.curveTo((w/2-wc, -bo), (-ct/2, xh/2-xhc), (-ct/2, xh/2))
    path.curveTo((-ct/2, xh/2+xhc), (w/2-wc, xh+bo), (w/2, xh+bo))
    path.closePath()
    
    wc = 0.552284749831*(2-r)*(w-ct)/2
    xhc = 0.552284749831*(2-r)*xh/2+bo-t/2
    
    path.moveTo((w/2, xh+bo-t))
    path.curveTo((w/2-wc, xh+bo-t), (ct/2, xh/2+xhc), (ct/2, xh/2))
    path.curveTo((ct/2, xh/2-xhc), (w/2-wc, -bo+t), (w/2, -bo+t))
    path.curveTo((w/2+wc, -bo+t), (w-ct/2, xh/2-xhc), (w-ct/2, xh/2))
    path.curveTo((w-ct/2, xh/2+xhc), (w/2+wc, xh+bo-t), (w/2, xh+bo-t))
    path.closePath()
    
    glyph.appendAnchor("top", (w/2, xh+bo))
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_o_dieresis(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("o_dieresis")
    
    construction = GlyphConstructionBuilder("odieresis = o + dieresis@top", font)
    construction.draw(glyph.getPen())
    
    glyph.unicode = ord("ö")
    
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["o"]
    
def glyph_p(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("p")
    glyph.unicode = ord("p")
    
    w=w*width["p"]
    
    w=w*width["b"]
    
    path = glyph.getPen()
    stem(path, -ct/2, d, ct, a)
    
    hc = w/2
    #curve thickness intersecting the stem
    it = ct*0.5
    
    wc = 0.552284749831*(2-r)*(w/2+ct/2-it)
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path.moveTo((ct/2-it, xh/2))
    path.curveTo((ct/2-it, xh/2+xhc), (hc-wc, xh+bo), (hc, xh+bo))
    
    wc = 0.552284749831*(2-r)*(w/2+rct/2)
    
    path.curveTo((hc+wc, xh+bo), (w+rct/2, xh/2+xhc), (w+rct/2, xh/2))
    path.curveTo((w+rct/2, xh/2-xhc), (hc+wc, -bo), (hc, -bo))
    
    wc = 0.552284749831*(2-r)*(w/2+ct/2-it)
    
    path.curveTo((hc-wc, -bo), (ct/2-it, xh/2-xhc), (ct/2-it, xh/2))
    path.closePath()
    
    wc = 0.552284749831*(2-r)*(w/2-rct/2)
    xhc = 0.552284749831*xh/2+bo-t/2
        
    path.moveTo((ct/2, xh/2))
    path.curveTo((ct/2, xh/2-xhc), (hc-wc, -bo+t), (hc, -bo+t))
    path.curveTo((hc+wc, -bo+t), (w-rct/2, xh/2-xhc), (w-rct/2, xh/2))
    path.curveTo((w-rct/2, xh/2+xhc), (hc+wc, xh-t+bo), (hc, xh-t+bo))
    path.curveTo((hc-wc, xh-t+bo), (ct/2, xh/2+xhc), (ct/2, xh/2))
    path.closePath()    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["e_left"]

def glyph_q(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("q")
    glyph.unicode = ord("q")
    
    w=w*width["q"]

    path = glyph.getPen()
    stem(path, w-ct/2, d, ct, a)
    
    path.moveTo((w-ct/2, xh))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w+ct/2, d))
    path.lineTo((w-ct/2, d))
    path.closePath()
    
    hc = w/2
    #curve thickness intersecting the stem
    it = ct*0.5
    
    wc = 0.552284749831*(2-r)*(w/2+rct/2)
    xhc = 0.552284749831*(2-r)*xh/2+bo
    
    path.moveTo((-rct/2, xh/2))
    path.curveTo((-rct/2, xh/2+xhc), (hc-wc, xh+bo), (hc, xh+bo))
    
    wc = 0.552284749831*(2-r)*(w/2+ct/2-it)
    
    path.curveTo((hc+wc, xh+bo), (w-ct/2+it, xh/2+xhc), (w-ct/2+it, xh/2))
    path.curveTo((w-ct/2+it, xh/2-xhc), (hc+wc, -bo), (hc, -bo))
    
    wc = 0.552284749831*(2-r)*(w/2+ct/2-it)
    
    path.curveTo((hc-wc, -bo), (-rct/2, xh/2-xhc), (-rct/2, xh/2))
    path.closePath()
    
    wc = 0.552284749831*(2-r)*(w/2-rct/2)
    xhc = 0.552284749831*xh/2+bo-t/2
        
    path.moveTo((rct/2, xh/2))
    path.curveTo((rct/2, xh/2-xhc), (hc-wc, -bo+t), (hc, -bo+t))
    path.curveTo((hc+wc, -bo+t), (w-ct/2, xh/2-xhc), (w-ct/2, xh/2))
    path.curveTo((w-ct/2, xh/2+xhc), (hc+wc, xh-t+bo), (hc, xh-t+bo))
    path.curveTo((hc-wc, xh-t+bo), (rct/2, xh/2+xhc), (rct/2, xh/2))
    path.closePath()     
      
    #metrics
    glyph.leftMargin = s*spacing["o"]
    glyph.rightMargin = s*spacing["e_left"]
    
def glyph_r(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("r")
    glyph.unicode = ord("r")
    
    w=w*width["r"]
    hc = w
    #curve thickness intersecting the stem
    it = ct*0.5

    path = glyph.getPen()
    stem(path, -ct/2, 0, ct, xh)
    
    wc = 0.552284749831*(2-r)*(hc+ct/2-it)
    xhc = 0.552284749831*(2-r)*xh/2+bo
    path.moveTo((ct/2-it, xh/2))
    path.curveTo((ct/2-it, xh/2+xhc), (hc-wc, xh+bo), (hc, xh+bo))  
    
    xhc = 0.552284749831*(2-r)*xh/2+bo-t
    path.lineTo((hc, xh+bo-t))  
    path.curveTo((hc-wc, xh+bo-t), (ct/2, xh/2+xhc), (ct/2, xh/2))
    path.closePath()
      
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["r_right"]
    
def glyph_s(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("s")
    glyph.unicode = ord("s")
    
    w = w*width["s"]
    
    path = glyph.getPen()

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
    
    glyph.appendAnchor("top", (w/2, xh+bo))
    glyph.appendAnchor("bottom", (w/2, -bo))
        
    #metrics
    glyph.leftMargin = s*spacing["z"]
    glyph.rightMargin = s*spacing["s_right"]
    
def glyph_s_cedilla(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("s_cedilla")
    
    construction = GlyphConstructionBuilder("scedilla = s + cedilla@bottom", font)
    construction.draw(glyph.getPen())
    
    glyph.unicode = ord("ş")
    
    #metrics
    glyph.leftMargin = s*spacing["z"]
    glyph.rightMargin = s*spacing["s_right"]

    
def glyph_t(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("t")
    glyph.unicode = ord("t")
    
    w=w*width["t"]

    path = glyph.getPen()
    
    path.moveTo((0, xh*.2))
    path.lineTo((0, a*.9-t/2+t*r/2))
    path.lineTo((ct, a*.9-t/2+t*r/2))
    path.lineTo((ct, xh*.2))
    path.qCurveTo((ct, t-bo), (ct+w/4*r,t-bo))
    path.lineTo((ct+w/2*(1-r),t-bo))
    
    path.lineTo((w/2*(1-r)+ct,-bo))
    path.lineTo((w/4*r+ct, -bo))
    path.qCurveTo((0,-bo), (0, xh*.2))
    path.closePath()
    
    path.moveTo((-w/3*(1-r), xh))
    path.lineTo((ct+w/2*(1-r), xh))
    path.lineTo((ct+w/2*(1-r),xh-t))
    path.lineTo((-w/3*(1-r), xh-t))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["t_left"]
    glyph.rightMargin = s*spacing["t_right"]

    
def glyph_u(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("u")
    glyph.unicode = ord("u")
    
    w=w*width["u"]
    
    path = glyph.getPen()
    hc = w*0.45
    vc = xh*0.4
    #curve thickness intersecting the stem
    it = ct*0.5
    
    wc = 0.552284749831*(2-r)*(w/2-ct/2)
    xhc = 0.552284749831*xh/2+bo-t/2
    
    path.moveTo((-ct/2, xh))
    path.lineTo((ct/2, xh))
    path.lineTo((ct/2, vc))
    path.curveTo((ct/2, vc-xhc), (hc-wc, -bo+t), (hc, -bo+t))
    wc = 0.552284749831*(2-r)*(w/2-ct/2)
    path.curveTo((hc+wc, -bo+t), (w-ct/2, vc-xhc), (w-ct/2, vc))
    path.lineTo((w-ct/2+it, vc))

    wc = 0.552284749831*(2-r)*(w/2+ct/2)
    xhc = 0.552284749831*vc+bo
    path.curveTo((w-ct/2+it, vc-xhc), (hc+wc, -bo), (hc, -bo))
    wc = 0.552284749831*(2-r)*(w/2+ct/2)
    path.curveTo((hc-wc, -bo), (-ct/2, vc-xhc), (-ct/2, vc))
    path.closePath()
    
    path.moveTo((w-ct/2, xh))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w+ct/2, 0))
    path.lineTo((w-ct/2, 0))
    path.closePath()
    
    glyph.appendAnchor("top", (w/2, xh))
    
    #metrics
    glyph.leftMargin = s*spacing["n_right"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_u_dieresis(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("u_dieresis")
    
    construction = GlyphConstructionBuilder("udieresis = u + dieresis@top", font)
    construction.draw(glyph.getPen())
    
    glyph.unicode = ord("ü")
    
    #metrics
    glyph.leftMargin = s*spacing["n_right"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_v(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("v")
    glyph.unicode = ord("v")
    
    w=w*width["v"]
    
    path = glyph.getPen()
    
    d = calculate_diagonal(t, (0, 0),(w/2, xh))
        
    path.moveTo((-d[0]/2,xh))
    path.lineTo((w/2-d[0]/2,0))
    path.lineTo((w/2+d[0]/2,0))
    path.lineTo((w+d[0]/2,xh))
    path.lineTo((w-d[0]/2,xh))
    path.lineTo((w/2-d[0]/2,0))  
    path.lineTo((w/2+d[0]/2,0))  
    path.lineTo((d[0]/2,xh))
    
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["v"]
    glyph.rightMargin = s*spacing["v"]
    
def glyph_w(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
    glyph = font.newGlyph("w")
    glyph.unicode = ord("w")
    
    w=w*width["w"]
    
    path = glyph.getPen()
    d = calculate_diagonal(ct, (0, 0),(w/4, xh))
        
    path.moveTo((-d[0]/2,xh))
    path.lineTo((w*.24-d[0]/2, 0))
    path.lineTo((w*.24+d[0]/2, 0))
    path.lineTo((w*.5+d[0]/2, xh))
    path.lineTo((w*.5-d[0]/2, xh))
    path.lineTo((w*.76-d[0]/2, 0))
    path.lineTo((w*.76+d[0]/2, 0))
    path.lineTo((w+d[0]/2, xh))
    path.lineTo((w-d[0]/2, xh))
    path.lineTo((w*.76-d[0]/2, 0))
    path.lineTo((w*.76+d[0]/2, 0))
    path.lineTo((w*.5+d[0]/2, xh))
    path.lineTo((w*.5-d[0]/2, xh))
    path.lineTo((w*.24-d[0]/2, 0))
    path.lineTo((w*.24+d[0]/2, 0))
    path.lineTo((d[0]/2, xh))
    path.closePath()
        
    #metrics
    glyph.leftMargin = s*spacing["v"]
    glyph.rightMargin = s*spacing["v"]
    
def glyph_x(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("x")
    glyph.unicode = ord("x")
    
    w=w*width["x"]
    
    path = glyph.getPen()
   
    d = calculate_diagonal(t, (0,0), (w,xh))
    
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
    
def glyph_y(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("y")
    glyph.unicode = ord("y")
    
    w=w*width["y"]
    
    path = glyph.getPen()
    
    d1 = calculate_diagonal(t, (0, 0),(w/2, xh))
    th = d*0.6
        
    path.moveTo((-d1[0]/2,xh))
    path.lineTo((d1[0]/2,xh))
    path.lineTo((w/2+d1[0]/2,0))
    path.lineTo((w/2-d1[0]/2,0))
    path.closePath()
    
    angle = math.atan2((xh - 0), (w/2 - 0))
    tw = th/math.tan(angle)
    twc = d/math.tan(angle)
    
    path.moveTo((w-d1[0]/2,xh))
    path.lineTo((w+d1[0]/2,xh))
    path.lineTo((w/2+tw+d1[0]/2,th))
    path.curveTo((w/2+twc+d1[0]/2, d), (w/2+tw-d1[0]/2, d), (ct/2, d))
    path.lineTo((t/2,d))
    path.lineTo((t/2, d+t))
    path.lineTo((ct/2, d+t))
    wc = (d+t)/math.tan(angle)
    path.curveTo((w/2+twc-d1[0]/2, d+t), (w/2+wc-d1[0]/2, d+t), (w/2+tw-d1[0]/2, th))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["n_right"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_z(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("z")
    glyph.unicode = ord("z")
    
    w=w*width["z"]
    
    path = glyph.getPen()
    
    d = calculate_diagonal(ct, (0,t), (w,xh-t))
    
    path.moveTo((-d[0]/2,xh))
    path.lineTo((w+d[0]/2,xh))
    path.lineTo((w+d[0]/2,xh-t))
    path.lineTo((d[0]/2, t))
    path.lineTo((w+d[0]/2,t))
    path.lineTo((w+d[0]/2,0))
    path.lineTo((-d[0]/2,0))
    path.lineTo((-d[0]/2,t))
    path.lineTo((w-d[0]/2,xh-t))
    path.lineTo((-d[0]/2,xh-t))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["z"]
    glyph.rightMargin = s*spacing["z"]

def glyph_space(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("space")
    glyph.unicode = ord(" ")
    
    glyph.width = w*.8
    
def glyph_hyphen(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
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
    
def glyph_underscore(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):    
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
    
def glyph_period(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("period")
    glyph.unicode = ord(".")
    
    path = glyph.getPen()
    
    glyph.appendComponent("dot", offset=(0, 0))
    
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"] 
    
def glyph_comma(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("comma")
    glyph.unicode = ord(",")
    
    glyph.appendComponent("dot", offset=(ct/2, 0))
    
    path = glyph.getPen()
    path.moveTo((ct/2,0))
    path.qCurveTo((ct/2, -rct/2), (0,-rct/2))
    path.lineTo((0, -rct))
    path.qCurveTo((ct, -rct), (ct, 0))
    path.closePath()
            
    #metrics
    glyph.leftMargin = s*spacing["l"]
    glyph.rightMargin = s*spacing["l"]
    
def glyph_quotesingle(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
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
    
def glyph_quotedbl(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
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
    
def glyph_exclam(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("exclam")
    glyph.unicode = ord("!")
    
    path = glyph.getPen()
    #component_dot(path, 0, ct/2, ct*1.25, r)
    
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
    
def glyph_colon(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("colon")
    glyph.unicode = ord(":")
    
    #path = glyph.getPen()
    
    #component_dot(path, 0, ct/2, ct*1.25, r)
    #component_dot(path, 0, xh-ct/2, ct*1.25, r)
    
def glyph_parenleft(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
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
    
def glyph_parenright(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
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
    
def glyph_bracketleft(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
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
    
def glyph_bracketright(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
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
    
def glyph_bullet(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("bullet")
    glyph.unicode = ord("•")
    
    #component_dot(path, 0, xh/2, t*5, r)

    
def glyph_grave(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
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
    
def glyph_fi(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
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
    path.qCurveTo((w+ct/2, xh+ct*(2-r)), (w, xh+ct*(2-r)))
    path.qCurveTo((w-ct/2, xh+ct*(2-r)), (w-ct/2, xh+ct*2))
    path.closePath()    
    
    path.moveTo((w-ct/2, 0))
    path.lineTo((w-ct/2, xh))
    path.lineTo((w+ct/2, xh))
    path.lineTo((w+ct/2, 0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = s*spacing["f_left"]
    glyph.rightMargin = s*spacing["f_right"]
    
def glyph_notdef(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph(".notdef")
    
    path = glyph.getPen()
    
    path.moveTo((-ct/2,0))
    path.lineTo((-ct/2,a))
    path.lineTo((w+ct/2,a))
    path.lineTo((w+ct/2,0))
    path.closePath()
    
    path.moveTo((ct/2,t))
    path.lineTo((w-ct/2,t))
    path.lineTo((w-ct/2,a-t))
    path.lineTo((ct/2,a-t))
    path.closePath()
    
    # metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_dot_round(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("dot")
    glyph.unicode = ord("˙")
    
    path = glyph.getPen()
    
    o = bo/xh*ct
    c = 0.552284749831*rct/2#(4/3)*math.tantan(mat.pi/(2*4))
    
    path.moveTo((0, rct))
    path.curveTo((c,rct),(rct/2, rct/2+c),(rct/2,rct/2))
    path.curveTo((rct/2, rct/2-c),(c,0),(0,0))
    path.curveTo((-c,0),(-rct/2,rct/2-c),(-rct/2,rct/2))
    path.curveTo((-rct/2, rct/2+c),(-c, rct),(0,rct))
    path.closePath()
    
    glyph.convertToQuadratic()
    glyph.appendAnchor("top", (0,t))
    glyph.appendAnchor("bottom", (0,0))
    glyph.appendAnchor("center", (0,t/2))
    glyph.appendAnchor("right", (rct/2, rct/2))
    glyph.appendAnchor("_top", (0,-xh/6))
    
def glyph_dot_square(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("dot")
    glyph.unicode = ord("˙")
    
    path = glyph.getPen()
    path.moveTo((-ct/2, rct))
    path.lineTo((ct/2, rct))
    path.lineTo((ct/2, 0))
    path.lineTo((-ct/2, 0))
    path.closePath()
    
    glyph.appendAnchor("top", (0,rct))
    glyph.appendAnchor("bottom", (0,0))
    glyph.appendAnchor("center", (0,rct/2))
    glyph.appendAnchor("right", (ct/2, rct/2))
    glyph.appendAnchor("_top", (0,-xh/6))
    
def glyph_dot_diamond(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("dot")
    glyph.unicode = ord("˙")
    
    path = glyph.getPen()
    path.moveTo((0, rct))
    path.lineTo((rct/2,rct/2))
    path.lineTo((0, 0))
    path.lineTo((-rct/2, rct/2))
    path.closePath()
    
    glyph.appendAnchor("top", (0,rct))
    glyph.appendAnchor("bottom", (0,0))
    glyph.appendAnchor("center", (0,rct/2))
    glyph.appendAnchor("right", (ct/2, rct/2))
    glyph.appendAnchor("_top", (0,-xh/6))
    
def glyph_dot_star(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("dot")
    glyph.unicode = ord("˙")
    
    rct = rct*1.5
    
    path = glyph.getPen()
    path.moveTo((0, rct))
    path.qCurveTo((0, rct/2),(rct/2,rct/2))
    path.qCurveTo((0, rct/2),(0, 0))
    path.qCurveTo((0, rct/2),(-rct/2, rct/2))
    path.qCurveTo((0, rct/2),(0, rct))
    path.closePath()
    
    glyph.appendAnchor("top", (0,rct))
    glyph.appendAnchor("bottom", (0,0))
    glyph.appendAnchor("center", (0,rct/2))
    glyph.appendAnchor("right", (ct/2, rct/2))
    glyph.appendAnchor("_top", (0,-xh/6+t))
    
def glyph_dieresis(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("dieresis")
    glyph.unicode = ord("¨")
    
    s = w/3
    
    glyph.appendComponent("dot", offset=(-s, 0))
    glyph.appendComponent("dot", offset=(s, 0))
    
    glyph.appendAnchor("_top", (0, -xh/6))

def glyph_breve(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):  
    glyph = font.newGlyph("breve")
    glyph.unicode = ord("˘")  
    
    h = xh/6
    
    path = glyph.getPen()
    
    path.moveTo((t, h+w/6))
    path.qCurveTo((t, h), (w*r, h))
    path.lineTo((w*(1-r),h))
    path.qCurveTo((w-t, h), (w-t,h+w/6))
    
    path.lineTo((w-t*2, h+w/6))
    path.qCurveTo((w-t*2, h+t), (w*(1-r), h+t))
    path.lineTo((w*r, h+t))
    path.qCurveTo((t*2, h+t), (t*2, h+w/6))
    path.closePath()
    
    glyph.appendAnchor("_top", (0,0), color=(1, 0, 0, 1))
    
def glyph_cedilla(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("cedilla")
    glyph.unicode = ord("¸") 
    
    nt = t/2
    nct = ct/2
    d = calculate_diagonal(nt, (w/2-nt, 0), (w/2, -nt))
    h = xh/6
    
    path = glyph.getPen()
    
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
    
    glyph.appendAnchor("_bottom", (w/2, h), color=(1, 0, 0, 1))
    
#Components
    
def stem(path, x, y, w, h):
    path.moveTo((x,y+h))
    path.lineTo((x+w,y+h))
    path.lineTo((x+w,y))
    path.lineTo((x,y))
    path.closePath()
    
def component_serif_bottom_left(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("serif_bottom_left")
    
    path = glyph.getPen()
    path.moveTo((0, 0))
    path.lineTo((-t, 0))
    path.qCurveTo((0, 0), (0, t))
    path.closePath()
    
def component_serif_bottom_right(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("serif_bottom_right")
    
    path = glyph.getPen()
    path.moveTo((0, 0))
    path.lineTo((t, 0))
    path.qCurveTo((0, 0), (0, t))
    path.closePath()

def component_serif_top_left(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("serif_top_left")
    
    path = glyph.getPen()
    path.moveTo((0, 0))
    path.lineTo((-t, 0))
    path.qCurveTo((0, 0), (0, -t))
    path.closePath()
    
def component_serif_top_right(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("serif_top_right")
    
    path = glyph.getPen()
    path.moveTo((0, 0))
    path.lineTo((t, 0))
    path.qCurveTo((0, 0), (0, -t))
    path.closePath()
    
def component_serif_top_cap(font, xh, a, d, w, t, s, r, ct, bo, rct, srfs):
    glyph = font.newGlyph("serif_top_cap")
    
    path = glyph.getPen()
    path.moveTo((ct, t/2))
    path.lineTo((ct, -t/2))
    path.lineTo((0, -t/2))
    path.qCurveTo((0, 0), (-t, 0))
    path.closePath()
    
    
#calculation functions
    
def calculate_diagonal(t, p1, p2):
    angle1 = math.atan2((p2[1] - p1[1]), (p2[0] - p1[0]))
    # substract 90°
    angle2 = angle1 - math.radians(90)

    x, y = p1
    # pythagoras
    ax = t
    bx = t * math.tan(angle2)
    cx = math.sqrt(ax**2 + bx**2)
            
    ay = t
    by = t * math.tan(angle1)
    cy = math.sqrt(ay**2 + by**2)
        
    return cx, cy, bx, by
    
def calculate_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y
    
def calculate_terminals(angle, w, h):
    x = w*math.cos(angle)
    y = h*math.sin(angle)
    return x, y
    
from fontTools.designspaceLib import DesignSpaceDocument
import ufo2ft
from glyphConstruction import GlyphConstructionBuilder

def generateSource(masterName, xHeight, ascender, descender, width, thickness, roundness, contrast, dot_style, serifs, interface):   
    master = RFont(showInterface=interface)
    master.info.familyName = familyName
    master.info.styleName = styleName
    master.info.xHeight = xHeight
    master.info.capHeight = capHeight
    master.info.unitsPerEm = capHeight + abs(ascender)
    master.info.descender = descender
    master.info.ascender = ascender
    master.info.versionMajor = 2
    master.info.versionMinor = 290
    
    spacing = thickness/50 + 80
    contrast_thickness = thickness*(1+contrast)
    bottom_offset = thickness*0.2*roundness
    round_contrast_thickness = contrast_thickness * 1.15
    
    if dot_style == "round":
        glyph_dot_round(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    elif dot_style == "square":
        glyph_dot_square(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    elif dot_style == "diamond":
        glyph_dot_diamond(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    elif dot_style == "star":
        glyph_dot_star(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)

    glyph_notdef(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
        
    #white spaces
    glyph_space(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    
    #diacritics
    glyph_grave(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_cedilla(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    
    #capitals
    #glyph_D(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_A(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_C(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_D(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_E(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs) 
    glyph_F(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs) 
    glyph_H(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs) 
    glyph_I(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_K(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_L(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_N(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_O(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_O_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_T(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_U(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_V(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_W(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_X(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_Z(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)

    #lower-case
    glyph_a(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_a_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_b(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_c(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_c_cedilla(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_d(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_e(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_f(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_g(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_g_breve(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_h(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_i_dotless(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_i(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_j_dotless(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_j(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_k(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_l(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_m(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_n(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_o(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_o_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_p(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_q(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_r(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_s(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_s_cedilla(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_t(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_u(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_u_dieresis(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_v(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_w(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_x(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_y(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_z(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    
    #punctuation
    glyph_period(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_comma(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_quotesingle(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_quotedbl(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_colon(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_hyphen(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_underscore(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_parenleft(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_parenright(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_bracketleft(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_bracketright(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_exclam(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    glyph_bullet(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    
    #serif components
    component_serif_bottom_left(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    component_serif_bottom_right(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    component_serif_top_left(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    component_serif_top_right(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)    
    component_serif_top_cap(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)

    #kerning
    kerning_groups(master, xHeight, ascender, descender, width, thickness, spacing, roundness, contrast_thickness, bottom_offset, round_contrast_thickness, serifs)
    
    source = doc.newSourceDescriptor()
    source.font = master.naked()
    source.location = dict(Width=width, Thickness=thickness, Roundness=roundness, Contrast=contrast)
    print(source.location)
    if width == defW and thickness == defT and roundness == defR and contrast == defC:
        source.copyLib=True
        print('This is the base master', source.location, source.copyLib)
    doc.addSource(source)

minW = 100
defW = 600
maxW = 900
masterW = 9

minT = 10
defT = 40
maxT = 50
masterT = 5

minR = 0.1
defR = 1
maxR = 1
masterR = 10

minC = 0
defC = .3
maxC = 1
masterC = 3

doc = DesignSpaceDocument()

axisW = doc.newAxisDescriptor()
axisW.name = "Width"
axisW.tag = "wdth"
axisW.minimum = minW
axisW.default = defW
axisW.maximum = maxW
doc.addAxis(axisW)

axisT = doc.newAxisDescriptor()
axisT.name = "Thickness"
axisT.tag = "thck"
axisT.minimum = minT
axisT.default = defT
axisT.maximum = maxT
doc.addAxis(axisT)

axisR = doc.newAxisDescriptor()
axisR.name = "Roundness"
axisR.tag = "RNDN"
axisR.minimum = minR
axisR.default = defR
axisR.maximum = maxR
doc.addAxis(axisR)

axisC = doc.newAxisDescriptor()
axisC.name = "Contrast"
axisC.tag = "CNTR"
axisC.minimum = minC
axisC.default = defC
axisC.maximum = maxC
doc.addAxis(axisC)

familyName = "Shah Sans"
styleName = "Regular"
xHeight = 300
capHeight = 400

#change roundness from 0.1-0.5 to 1-100
def testing(w, t, r, c, ds, serifs):
    a = .5
    d = .5
    generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*(maxW/masterW), (t+1)*(maxT/masterT), round((r+1)*(maxR/masterR),2), round(c*(maxC/masterC),1), ds, serifs, True)

def export(file_formats, dot_style, serifs):  
    for w in range(masterW):
       for t in range(masterT):
           for r in range(masterR):
               for c in range(masterC+1):
                   a = .5
                   d = .5
                   generateSource(f"masterW{(w+1)*100}T{(t+1)*5}R{0.5+r/10}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*(maxW/masterW), (t+1)*(maxT/masterT), round((r+1)*(maxR/masterR),2), round(c*(maxC/masterC),1), dot_style, serifs, False)
                   
    cur_path = os.getcwd()
    if not os.path.exists(cur_path + '/export'):
        os.mkdir(cur_path + '/export')
    formats = file_formats.split() 
    time = datetime.now()
    if 'ttf' in formats:               
        print('Compiling TTF...')
        varFont = ufo2ft.compileVariableTTF(doc) 
        print('Saving TTF...')
        font_name = f"export/{familyName}GX-{time}.ttf"
        varFont.save(font_name)
        print(f"Done exporting {font_name}")
    if 'otf' in formats:               
        print('Compiling OTF...')
        varFont = ufo2ft.compileVariableCFF2(doc) 
        print('Saving OTF...')
        font_name = f"export/{familyName}GX-{time}.otf"
        varFont.save(font_name)
        print(f"Done exporting {font_name}")

testing(2,3,7,1, "round", False)
#export("ttf", "square", False)
