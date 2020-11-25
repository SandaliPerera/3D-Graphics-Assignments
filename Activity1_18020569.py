#IndexNo_18020569_Activity2

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 

def display():
    X_Axis = 0.0
    Y_Axis = 0.0

    glLoadIdentity()
    gluLookAt(0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0)
    glRotated(X_Axis, 0.0, 0.0, 0.0);
    glRotated(Y_Axis, 0.0, 0.0, 0.0);

    
   #whiteFront
    glBegin(GL_POLYGON) 
    glColor3f( 1.0, 1.0, 1.0)
    glVertex3f(-0.4, -0.2, 0)
    glVertex3f(-0.4, 0.2, 0)
    glVertex3f(0, 0.2, 0)
    glVertex3f(0, -0.2, 0)
    glEnd()
    
   #purpleBack
    glBegin(GL_POLYGON)
    glColor3f( 1.0, 0.0, 1.0)
    glVertex3f(-0.2, 0, -0.4)
    glVertex3f(-0.2, 0.4, -0.4)
    glVertex3f(0.2, 0.4, -0.4)
    glVertex3f(0.2, 0, -0.4)
    glEnd()

   #blueTop
    glBegin(GL_POLYGON)
    glColor3f( 0.0, 0.0, 1.0)
    glVertex3f(-0.4, 0.2, 0)
    glVertex3f(-0.2, 0.4, -0.4)
    glVertex3f(0.2, 0.4, -0.4)
    glVertex3f(0, 0.2, 0)
    glEnd()

   #redBottom
    glBegin(GL_POLYGON) 
    glColor3f( 1.0, 0.0, 0.0)
    glVertex3f(-0.4, -0.2, 0)
    glVertex3f(-0.2, 0, -0.4)
    glVertex3f(0.2, 0, -0.4)
    glVertex3f(0, -0.2, 0)
    glEnd()
 
   #greenLeft
    glBegin(GL_POLYGON)
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(-0.2,0,-0.4)
    glVertex3f(-0.2,0.4,-0.4)
    glVertex3f(-0.4,0.2,0)
    glVertex3f(-0.4,-0.2,0)
    glEnd()
    
   #greenRight
    glBegin(GL_POLYGON) 
    glColor3f( 0.0, 1.0, 0.0)
    glVertex3f(0,-0.2,0)
    glVertex3f(0,0.2,0)
    glVertex3f(0.2,0.4,-0.4)
    glVertex3f(0.2,0,-0.4)
    glEnd()
    

    
def createCube():      
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
        gluPerspective(50.0, float(x)/float(y), 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(1500,1500)   
glutCreateWindow("My Cube")     
glutInitWindowPosition(0,0)    
glutDisplayFunc(createCube)      
glutReshapeFunc(size)

glutMainLoop()
