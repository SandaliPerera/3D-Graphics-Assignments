from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def size(x, y):
        glClearColor(1.0, 1.0, 0.0, 1.0)
        glClearDepth(1.0) 
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)   
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(50.0, float(x)/float(y), 1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
 
 

def display():
    X = 0.0
    Y = 0.0

    glLoadIdentity()
    gluLookAt(0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0)
    glRotated(X, 0.0, 0.0, 0.0);
    glRotated(Y, 0.0, 0.0, 0.0);

   #White Side - Front
    glBegin(GL_POLYGON)  #Part (iv) 
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.4, -0.2, 0)
    glVertex3f(-0.4, 0.2, 0)
    glVertex3f(0, 0.2, 0)
    glVertex3f(0, -0.2, 0)
    glEnd()
    
   #Purple Side - Back
    glBegin(GL_POLYGON)  #Part (iv)
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.2, 0, -0.4)
    glVertex3f(-0.2, 0.4, -0.4)
    glVertex3f(0.2, 0.4, -0.4)
    glVertex3f(0.2, 0, -0.4)
    glEnd()
    
  #Green Side - Left
    glBegin(GL_POLYGON)  #Part (iv)
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.2,0,-0.4)
    glVertex3f(-0.2,0.4,-0.4)
    glVertex3f(-0.4,0.2,0)
    glVertex3f(-0.4,-0.2,0)
    glEnd()
    
   #Green Side - Right
    glBegin(GL_POLYGON)  #Part (iv)
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(0,-0.2,0)
    glVertex3f(0,0.2,0)
    glVertex3f(0.2,0.4,-0.4)
    glVertex3f(0.2,0,-0.4)
    glEnd()
    
   #Blue Side - Top
    glBegin(GL_POLYGON)  #Part (iv)
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.4, 0.2, 0)
    glVertex3f(-0.2, 0.4, -0.4)
    glVertex3f(0.2, 0.4, -0.4)
    glVertex3f(0, 0.2, 0)
    glEnd()

  #Red Side - Bottom
    glBegin(GL_POLYGON)  #Part (iv)
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.4, -0.2, 0)
    glVertex3f(-0.2, 0, -0.4)
    glVertex3f(0.2, 0, -0.4)
    glVertex3f(0, -0.2, 0)
    glEnd()
 
    
def createCube():      #Part (d)  #Part (e) 
    glClearColor(0.0, 0.0, 0.0, 1.0)             #Part(i) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)     #Part(ii) 
    display()
    glFlush()      #Part (v) 
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500,500)    #Part (b) 
glutCreateWindow("My Cube")      #Part (a) 
glutInitWindowPosition(0,0)      #Part (c) 
glutDisplayFunc(createCube)      #Part (f) 
glutReshapeFunc(size)

glutMainLoop()
