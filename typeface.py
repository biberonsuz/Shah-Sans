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
    
    path.moveTo((w-t,5/6*xh))
    path.qCurveTo((w-t, 2/3*xh), (w-t-50,2/3*xh))
    path.lineTo((w*r, 2/3*xh))
    path.qCurveTo((0, 2/3*xh), (0, 1/3*xh))
    path.qCurveTo((0, 0), (w*r, 0))
    path.lineTo((w*(1-r), 0))
    path.qCurveTo((w-t, 0), (w-t, 1/6*xh))
    
    path.lineTo((w-t, 1/6*xh+t))
    path.qCurveTo((w-t, t), (w*(1-r), t))
    path.lineTo((w*r,t))
    path.qCurveTo((t,t),(t, 1/3*xh))
    path.qCurveTo((t, 2/3*xh-t), (w*r, 2/3*xh-t))
    path.lineTo((w-t-50, 2/3*xh-t))
    path.qCurveTo((w-t, xh*(1-r)-t), (w-t, 5/6*xh-t))
    path.closePath()
        
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
    glyph = font.newGlyph("ı")
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
    
    createDot(path, t/2, a, t, r)
    
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
    createDot(path, t*2, a, t, r)
    createDot(path, w-t*2, a, t, r)
    
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
    
    createDot(path, t*2, a, t, r)
    createDot(path, w-t*2, a, t, r)
    
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
    
from fontParts.world import RFont
from fontTools.designspaceLib import DesignSpaceDocument
import ufo2ft

def generateSource(masterName, xHeight, ascender, descender, width, thickness, roundness):   
    master = RFont()
    master.info.familyName = familyName
    master.info.styleName = styleName
    master.info.xHeight = xHeight
    master.info.capHeight = capHeight
    master.info.unitsPerEm = capHeight + abs(ascender)
    master.info.descender = descender
    master.info.ascender = ascender
    spacing = 50

    glyph_space(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_a(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_b(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_d(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_h(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_ı(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_i(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_l(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_n(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_o(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_ö(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_p(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_q(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_u(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_ü(master, xHeight, ascender, descender, width, thickness, spacing, roundness)
    glyph_y(master, xHeight, ascender, descender, width, thickness, spacing, roundness)

    source = doc.newSourceDescriptor()
    source.font = master.naked()
    source.location = dict(Width = width)
    if width == 1 and thickness == 50 :
        source.copyLib = True
    doc.addSource(source)

minW = 1
maxW = 9

minT = 1
maxT = 50

doc = DesignSpaceDocument()

axisW = doc.newAxisDescriptor()
axisW.name = "Width"
axisW.tag = "wdth"
axisW.minimum = minW
axisW.default = 1
axisW.maximum = maxW
doc.addAxis(axisW)

axisT = doc.newAxisDescriptor()
axisT.name = "Thickness"
axisT.tag = "thcknss"
axisT.minimum = minT
axisT.default = 1
axisT.maximum = maxT
doc.addAxis(axisT)


familyName = "Ext"
styleName = "Regular"
xHeight = 300
capHeight = 400

def testing():
    a = 0
    d = 1
    r = 1
    w = 6
    t = 10
    generateSource(f"masterW{w}T{t}R{r}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*100, (t+1)*5, 1/(r+1))

def export():  
    master.showInterface = false
    for w in range(8):
        for t in range(9):
            for r in range(4):
                for a in range(2):
                    for d in range(2):
                        generateSource(f"masterW{w}T{t}R{r}A{a}D{d}", xHeight, xHeight+(a+1)*100, -(d+1)*100, (w+1)*100, (t+1)*5, 1/(r+1))

    varFont = ufo2ft.compileVariableTTF(doc)
    varFont.save(f"export/{familyName} variable {datetime.now()}.ttf")

    print(f"Done exporting {familyName} variable {datetime.now()}.ttf")
    
export() 
