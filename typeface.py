import math
from datetime import datetime

def createBase_o(path, xHeight, width, thickness):
    path.moveTo((1/3*width, xHeight+thickness/2))
    path.lineTo((2/3*width, xHeight+thickness/2))
    path.qCurveTo((width+thickness/2, xHeight+thickness/2), (width+thickness/2, xHeight*2/3))
    path.lineTo((width+thickness/2, xHeight*1/3))
    path.qCurveTo((width+thickness/2, -thickness/2), (2/3*width, -thickness/2))
    path.lineTo((1/3*width, -thickness/2))
    path.qCurveTo((-thickness/2, -thickness/2), (-thickness/2, 1/3*xHeight))
    path.lineTo((-thickness/2, xHeight*2/3))
    path.qCurveTo((-thickness/2, xHeight + thickness/2),(1/3*width, xHeight+thickness/2))
    path.closePath()
    
    path.moveTo((1/3*width, xHeight-thickness/2))
    path.lineTo((2/3*width, xHeight-thickness/2))
    path.qCurveTo((width-thickness/2, xHeight-thickness/2), (width-thickness/2, xHeight*2/3))
    path.lineTo((width-thickness/2, xHeight*1/3))
    path.qCurveTo((width-thickness/2, thickness/2), (2/3*width, thickness/2))
    path.lineTo((1/3*width, thickness/2))
    path.qCurveTo((thickness/2, thickness/2), (thickness/2, 1/3*xHeight))
    path.lineTo((thickness/2, xHeight*2/3))
    path.qCurveTo((thickness/2, xHeight - thickness/2),(1/3*width, xHeight-thickness/2))
    path.closePath()
        
def glyph_a(font, xHeight, ascender, width, thickness, spacing):    
    glyph = font.newGlyph("a")
    glyph.unicode = ord("a")
    
    path = glyph.getPen()
    
    path.moveTo((0,2/3*xHeight))
    path.qCurveTo((0, xHeight+thickness/2), (width*1/3, xHeight+thickness/2))
    path.lineTo((width*2/3,xHeight+thickness/2))
    path.qCurveTo((width, xHeight+thickness/2), (width, 2/3*xHeight))
    path.lineTo((width,0))
    
    path.lineTo((width-thickness, 0))
    path.lineTo((width-thickness, 2/3*xHeight))
    path.qCurveTo((width-thickness, xHeight-thickness/2),(width*2/3, xHeight-thickness/2))
    path.lineTo((width*1/3, xHeight-thickness/2))
    path.qCurveTo((thickness, xHeight-thickness/2), (thickness, 2/3*xHeight))
    path.closePath()
    
    path.moveTo((width-thickness,5/6*xHeight))
    path.qCurveTo((width-thickness, 2/3*xHeight), (width-thickness-50,2/3*xHeight))
    path.lineTo((width*1/3, 2/3*xHeight))
    path.qCurveTo((0, 2/3*xHeight), (0, 1/3*xHeight))
    path.qCurveTo((0, 0), (1/3*width, 0))
    path.lineTo((2/3*width, 0))
    path.qCurveTo((width-thickness, 0), (width-thickness, 1/6*xHeight))
    
    path.lineTo((width-thickness, 1/6*xHeight+thickness))
    path.qCurveTo((width-thickness, thickness), (2/3*width, thickness))
    path.lineTo((1/3*width,thickness))
    path.qCurveTo((thickness,thickness),(thickness, 1/3*xHeight))
    path.qCurveTo((thickness, 2/3*xHeight-thickness), (1/3*width, 2/3*xHeight-thickness))
    path.lineTo((width-thickness-50, 2/3*xHeight-thickness))
    
    path.closePath()
    
def glyph_o(font, xHeight, ascender, width, thickness, spacing):
    glyph = font.newGlyph("o")
    glyph.unicode = ord("o")
    
    path = glyph.getPen()
    createBase_o(path, xHeight, width,thickness)
    
    #metrics
    glyph.leftMargin = spacing
    glyph.rightMargin = spacing
    
def glyph_b(font, xHeight, ascender, width, thickness, spacing):
    glyph = font.newGlyph("b")
    glyph.unicode = ord("b")
    
    path = glyph.getPen()
    createBase_o(path, xHeight, width,thickness)
    
    path.moveTo((-thickness/2, 0))
    path.lineTo((-thickness/2,ascender))
    path.lineTo((thickness/2, ascender))
    path.lineTo((thickness/2, 0))
    path.closePath()
    
    #metrics
    glyph.leftMargin = spacing
    glyph.rightMargin = spacing
    

def glyph_space(font, xHeight, ascender, width, thickness, spacing):
    glyph = font.newGlyph("space")
    glyph.unicode = ord(" ")
    
    # metrics
    glyph.leftMargin = spacing
    glyph.rightMargin = spacing
    
def calculateDiagonal(thickness, p1, p2):
    angle = math.atan2((p2[1] - p1[1]), (p2[0] - p1[0])) 
    # substract 90°
    anglex = angle - math.radians(90)

    x, y = p1
    # pythagoras
    ax = thickness
    bx = thickness * math.tan(anglex)
    cx = math.sqrt(ax**2 + bx**2)
    
    angley = angle
    
    ay = thickness
    by = thickness * math.tan(angley)
    cy = math.sqrt(ay**2 + by**2)
    
    return cx, cy, bx, by
    
from fontParts.world import RFont
from fontTools.designspaceLib import DesignSpaceDocument
import ufo2ft

def generateSource(masterName, xHeight, ascender, width, thickness):   
    master = RFont()
    master.info.familyName = familyName
    master.info.styleName = styleName
    master.info.xHeight = xHeight
    master.info.capHeight = capHeight
    master.info.unitsPerEm = capHeight + abs(ascender)
    master.info.descender = -ascender
    master.info.ascender = ascender
    spacing = 50

    glyph_space(master, xHeight, ascender, width, thickness, spacing)
    glyph_a(master, xHeight, ascender, width, thickness, spacing)
    glyph_b(master, xHeight, ascender, width, thickness, spacing)
    glyph_o(master, xHeight, ascender, width, thickness, spacing)

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

roundness = 0.55

def testing():
    w = 6
    t = 10
    generateSource(f"masterW{w}", xHeight, ascender, (w+1)*100, t*5)

def export():  
    master.showInterface = false
    for w in range(8):
        for t in range(10):
            generateSource(f"masterW{w}T{t}", xHeight, ascender, (w+1)*100, t*5)

    varFont = ufo2ft.compileVariableTTF(doc)
    varFont.save(f"export/{familyName} variable {datetime.now()}.ttf")

    print(f"Done exporting {familyName} variable {datetime.now()}.ttf")
    
testing() 

