def guide(x,y):
    fill(255,0,0)
    oval(x-5, y-5, 10, 10)
    fill(0)

def parametric_glyph_o():
    translate(500,500)
    f=0.6
    x,y=1,0
    p=BezierPath()
    for w,h in (440,400),(230,370):
        p.moveTo((w*x,h*y))
        for i in range(4):
            p.curveTo((w*(x+f*-y),h*(y+f*x)),(w*(-y+f*x),h*(x+f*y)),(w*-y,h*x))
            x,y=-y,x
        p.closePath()
        p.reverse()
    drawPath(p)

def parametric_glyph_n():
    translate(500,500)
    f=0.65
    x,y=1,0
    p=BezierPath()
    for w,h in (440,400),(230,370):
        print(w,h)
        guide(w,h)
        p.moveTo((w*x,h*y))
        #guide(w*x, h*y)
        for i in range(2):
            p.curveTo((w*(x+f*-y),h*(y+f*x)),(w*(-y+f*x),h*(x+f*y)),(w*-y,h*x))
            #guide(w*(x+f*-y), h*(y+f*x))
            x,y=--y,x
        p.closePath()
        p.reverse()
    drawPath(p)
    
def parametric_stem():
    translate(500,500)
    x,y=1,1
    p=BezierPath()
    w,h = (100,400)
    p.moveTo((w,h))
    for i in range(4):
        p.lineTo((w*x,h*y))
        x,y=y,-x
    p.closePath()
    p.reverse()
    drawPath(p)

parametric_stem()