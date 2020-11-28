#18020569

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def size(x, y):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0) 
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)   
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, float(x)/float(y), 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
 
 

def display():
    X = 0.0
    Y = 0.0

    glLoadIdentity()
    gluLookAt(0.0, 0.5, 9.0, 0.0, 0.5, 0.5, 0.0, 0.5, 0.0)
    glRotated(X, 0.0, 0.0, 0.0);
    glRotated(Y, 0.0, 0.0, 0.0);
    
    
 #Cube
    glBegin(GL_POLYGON)  
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glEnd()
    
   #Back
    glBegin(GL_POLYGON)  
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glEnd()
    
   #Left
    glBegin(GL_POLYGON) 
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glEnd()
    
   #Right
    glBegin(GL_POLYGON)  
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glEnd()
    
   #Top
    glBegin(GL_POLYGON) 
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glEnd()

   #Bottom
    glBegin(GL_POLYGON) 
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glEnd()
    
    
 #Pyramid(Top)
    glBegin(GL_TRIANGLES)
    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(0.5, 0.5, 0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(0, 1.5, 0.5)
    
    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(-0.5, 0.5, -0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(0, 1.5, 0.5)

    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(-0.5, 0.5, -0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(0.5, 0.5, -0)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(0, 1.5, 0.5)

    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(0.5, 0.5, 0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(0.5, 0.5, -0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(0, 1.5, 0.5)
    glEnd()
     
 #Pyramid(Left)
    glBegin(GL_TRIANGLES)
    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(-1.5, 0, 0.5)

    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(-1.5, 0, 0.5)

    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(-0.5, 0.5, -0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(-1.5, 0, 0.5)

    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(-0.5, 0.5, -0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(-1.5, 0, 0.5)
    glEnd()    
    
 #Pyramid(Right)
    glBegin(GL_TRIANGLES)
    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(0.5, 0.5, 0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(0.5, 0.5, -0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(1.5, 0, 0.5)

    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(0.5, 0.5, -0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(0.5, -0.5, -0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(1.5, 0, 0.5)

    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(0.5, -0.5, -0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(1.5, 0, 0.5)

    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(0.5, 0.5, 0.5)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.5)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(1.5, 0, 0.5)
    glEnd()
   

def createPyramid():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   

    display()
    glFlush()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800,800)
glutCreateWindow("Combined Model")
glutInitWindowPosition(0,0)
glutDisplayFunc(createPyramid)
glutReshapeFunc(size)

glutMainLoop()
