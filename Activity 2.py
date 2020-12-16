from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def display():
    X = 0.0
    Y = 0.0

    glLoadIdentity()
    gluLookAt(1.0, 1.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotated(X, 0.0, 0.0, 0.0);
    glRotated(Y, 0.0, 0.0, 0.0);

   #bottomSquare
    glBegin(GL_QUADS)
    glColor3f( 0.2, 0.0, 0.2)
    glVertex3f(-0.5,0,0.5)
    glVertex3f(-0.5,0,-0.5)
    glVertex3f(0.5,0,-0.5)
    glVertex3f(0.5,0,0.5)
    glEnd()

    glBegin(GL_TRIANGLES)
    
   #front
    glColor3f( 0.3, 0.7, 0.1)
    glVertex3f(-0.5, 0, 0.5)
    glVertex3f(0,1,0)
    glVertex3f(0.5,0,0.5)
   
    
   #back
    glColor3f( 0.2, 0.6, 0.0)
    glVertex3f(-0.5,0,-0.5)
    glVertex3f(0,1,0)
    glVertex3f(0.5,0,-0.5)
    
   #left
    glColor3f( 0.1, 1.0, 0.2)
    glVertex3f(-0.5,0,-0.5)
    glVertex3f(0,1,0)
    glVertex3f(-0.5,0,0.5)
    
    
   #right
    glColor3f( 0.0, 0.4, 0.1)
    glVertex3f(0.5,0,0.5)
    glVertex3f(0,1,0)
    glVertex3f(0.5,0,-0.5)
    
    glEnd()
    

def createPyramid():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   

    display()
    glFlush()
    glutSwapBuffers()

def size(x, y):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0) 
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)   
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(50.0, float(x)/float(y), 1.0, 50.0)
        glMatrixMode(GL_MODELVIEW)
 

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(700,700)
glutCreateWindow("First Pyramid")
glutInitWindowPosition(0,0)
glutDisplayFunc(createPyramid)
glutReshapeFunc(size)

glutMainLoop()
