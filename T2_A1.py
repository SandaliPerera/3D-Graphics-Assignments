from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 500, 500


def drawing():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0, 1.0, 0.0, 0.0) 
    glLoadIdentity()
    iterate()
    glColor3f(0.2, 0.5, 0.4)
    square()
    points()
    triangle()
    glutSwapBuffers()

def points():
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(100,100)
    glVertex2f(300,200)
    glEnd()

# Triangle
def triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(100,210)
    glVertex2f(300,210)
    glVertex2f(300,310)
    glEnd()

# Square
def square(): 
    glBegin(GL_QUADS)
    glVertex2f(100,100)
    glVertex2f(300,100)
    glVertex2f(300,200)
    glVertex2f(100,200)
    glEnd()


def iterate(): 
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


glutInit()
glutInitDisplayMode(GLUT_RGB) 
glutInitWindowSize(width, height) 
glutInitWindowPosition(100,100) 
glutCreateWindow("Python Code 1")
glutDisplayFunc(drawing) 
glutIdleFunc(drawing) 
glutMainLoop()



