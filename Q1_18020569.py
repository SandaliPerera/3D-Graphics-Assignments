#18020569
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

    glBegin(GL_POLYGON) 
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.4, -0.2, 0)
    glVertex3f(-0.4, 0.2, 0)
    glVertex3f(0, 0.2, 0)
    glVertex3f(0, -0.2, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.2, 0, -0.4)
    glVertex3f(-0.2, 0.4, -0.4)
    glVertex3f(0.2, 0.4, -0.4)
    glVertex3f(0.2, 0, -0.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.2,0,-0.4)
    glVertex3f(-0.2,0.4,-0.4)
    glVertex3f(-0.4,0.2,0)
    glVertex3f(-0.4,-0.2,0)
    glEnd()
    
    glBegin(GL_POLYGON) 
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(0,-0.2,0)
    glVertex3f(0,0.2,0)
    glVertex3f(0.2,0.4,-0.4)
    glVertex3f(0.2,0,-0.4)
    glEnd()
    
    glBegin(GL_POLYGON)  
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.4, 0.2, 0)
    glVertex3f(-0.2, 0.4, -0.4)
    glVertex3f(0.2, 0.4, -0.4)
    glVertex3f(0, 0.2, 0)
    glEnd()

    glBegin(GL_POLYGON)  
    glColor3f( 0.0, 1.0, 1.0)
    glVertex3f(-0.4, -0.2, 0)
    glVertex3f(-0.2, 0, -0.4)
    glVertex3f(0.2, 0, -0.4)
    glVertex3f(0, -0.2, 0)
    glEnd()
 
    
def createCube():    
    glClearColor(0.0, 0.0, 0.0, 1.0)        
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)     
    display()
    glFlush()      
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500,500)   
glutCreateWindow("My Cube")   
glutInitWindowPosition(0,0)   
glutDisplayFunc(createCube)   
glutReshapeFunc(size)

glutMainLoop()
