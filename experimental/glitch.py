import math
from datetime import datetime

def createBase_o(path, xh, w, t, r):
    path.moveTo((r*w, xh+t/2))
    path.lineTo((w-w*r, xh+t/2))
    path.qCurveTo((w+t/2, xh+t/2), (w+t/2, xh-xh*r))
    path.lineTo((w+t/2, xh*r))
    path.qCurveTo((w+t/2, -t/2), (w-w*r, -t/2))
    path.lineTo((r*w, -t/2))
    path.qCurveTo((-t/2, -t/2), (-t/2, r*xh))
    path.lineTo((-t/2, xh-xh*r))
    path.qCurveTo((-t/2, xh + t/2),(r*w, xh+t/2))
    path.closePath()
    
    path.moveTo((r*w, xh-t/2))
    path.qCurveTo((t/2, xh-t/2), (t/2, xh-xh*r))
    path.lineTo((t/2, xh*r))
    path.qCurveTo((t/2, t/2), (r*w, t/2))
    path.lineTo((w-w*r, t/2))
    path.qCurveTo((w-t/2, t/2), (w-t/2, xh*r))
    path.lineTo((w-t/2, xh-xh*r))
    path.qCurveTo((w-t/2, xh-t/2), (w-w*r, xh-t/2))
    path.lineTo((w*r, xh-t/2))
    path.closePath()
        
def glyph_a(font, xh, a, w, t, s, r):    
    glyph = font.newGlyph("a")
    glyph.unicode = ord("a")
    
    path = glyph.getPen()
    
    path.moveTo((0,2/3*xh))
    path.qCurveTo((0, xh+t/2), (w*1/3, xh+t/2))
    path.lineTo((w*2/3,xh+t/2))
    path.qCurveTo((w, xh+t/2), (w, 2/3*xh))
    path.lineTo((w,0))
    
    path.lineTo((w-t, 0))
    path.lineTo((w-t, 2/3*xh))
    path.qCurveTo((w-t, xh-t/2),(w*2/3, xh-t/2))
    path.lineTo((w*1/3, xh-t/2))
    path.qCurveTo((t, xh-t/2), (t, 2/3*xh))
    path.closePath()
    
    path.moveTo((w-t,5/6*xh))
    path.qCurveTo((w-t, 2/3*xh), (w-t-50,2/3*xh))
    path.lineTo((w*1/3, 2/3*xh))
    path.qCurveTo((0, 2/3*xh), (0, 1/3*xh))
    path.qCurveTo((0, 0), (1/3*w, 0))
    path.lineTo((2/3*w, 0))
    path.qCurveTo((w-t, 0), (w-t, 1/6*xh))
    
    path.lineTo((w-t, 1/6*xh+t))
    path.qCurveTo((w-t, t), (2/3*w, t))
    path.lineTo((1/3*w,t))
    path.qCurveTo((t,t),(t, 1/3*xh))
    path.qCurveTo((t, 2/3*xh-t), (1/3*w, 2/3*xh-t))
    path.lineTo((w-t-50, 2/3*xh-t))
    path.qCurveTo((w-t, 2/3*xh-t), (w-t, 5/6*xh-t))
    path.closePath()
    
def glyph_o(font, xh, a, w, t, s, r):
    glyph = font.newGlyph("o")
    glyph.unicode = ord("o")
    
    path = glyph.getPen()
    createBase_o(path, xh, w, t, r)
    
    #metrics
    glyph.leftMargin = s
    glyph.rightMargin = s
    
def glyph_b(font, xh, a, w, t, s, r):
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
    

def glyph_space(font, xh, a, w, t, s, r):
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

def generateSource(masterName, xHeight, ascender, width, thickness, roundness):   
    master = RFont()
    master.info.familyName = familyName
    master.info.styleName = styleName
    master.info.xHeight = xHeight
    master.info.capHeight = capHeight
    master.info.unitsPerEm = capHeight + abs(ascender)
    master.info.descender = -ascender
    master.info.ascender = ascender
    spacing = 50

    glyph_space(master, xHeight, ascender, width, thickness, spacing, roundness)
    glyph_a(master, xHeight, ascender, width, thickness, spacing, roundness)
    glyph_b(master, xHeight, ascender, width, thickness, spacing, roundness)
    glyph_o(master, xHeight, ascender, width, thickness, spacing, roundness)

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
ascender = 400

def testing():
    r = 1
    w = 6
    t = 10
    generateSource(f"masterW{w}T{t}R{r}", xHeight, ascender, (w+1)*100, t*5, 1/r)

def export():  
    master.showInterface = false
    for w in range(8):
        for t in range(10):
            for r in range(5):
                generateSource(f"masterW{w}T{t}R{r}", xHeight, ascender, (w+1)*100, t*5, 1/r)

    varFont = ufo2ft.compileVariableTTF(doc)
    varFont.save(f"export/{familyName} variable {datetime.now()}.ttf")

    print(f"Done exporting {familyName} variable {datetime.now()}.ttf")
    
testing() 
