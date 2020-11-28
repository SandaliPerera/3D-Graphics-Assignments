#18020569

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def display():
    X_Axis = 0.0
    Y_Axis = 0.0

    glLoadIdentity()
    gluLookAt(0.0,0.0, 3, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotated(X_Axis, 0.0, 0.0, 0.0);
    glRotated(Y_Axis, 0.0, 0.0, 0.0);

  
    glBegin(GL_TRIANGLES)
    
   #front
    glColor3f (1.0, 0.0, 0.0) # Vertex 1 Red
    glVertex3f(-0.5, 0, 0.5)
    glColor3f (0.0, 1.0, 0.0)# Vertex 2 Green
    glVertex3f(0.5,0,0.5)
    glColor3f (0.0, 0.0, 1.0)# Vertex 3 Blue
    glVertex3f(0,1,0)
    
   
    
   #left
    glColor3f (1.0, 0.0, 0.0) # Vertex 1 Red
    glVertex3f(-0.5,0,-0.5)
    glColor3f (0.0, 1.0, 0.0)# Vertex 2 Green
    glVertex3f(-0.5,0,0.5)
    glColor3f (0.0, 0.0, 1.0)# Vertex 3 Blue
    glVertex3f(0,1,0)
    
    
    
   #right
    glColor3f (1.0, 0.0, 0.0) # Vertex 1 Red
    glVertex3f(0.5,0,0.5)
    glColor3f (0.0, 1.0, 0.0)# Vertex 2 Green
    glVertex3f(0.5,0,-0.5)
    glColor3f (0.0, 0.0, 1.0)# Vertex 3 Blue
    glVertex3f(0,1,0)
    
    
    glEnd()
    

def createPyramid():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glShadeModel (GL_SMOOTH)
   

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
        gluPerspective(50.0, float(x)/float(y), 1.0, 10.0)
        glMatrixMode(GL_MODELVIEW)
 

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500,500)
glutCreateWindow("First Pyramid")
glutInitWindowPosition(0,0)
glutDisplayFunc(createPyramid)
glutReshapeFunc(size)

glutMainLoop()
