from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


vertices = [

    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

angleX = 0.0
angleY = 0.0


def resize(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30.0, w/h, 2.0, 50.0)
    glMatrixMode(GL_MODELVIEW)


def drawObjs():
    global X, angleY

    glLoadIdentity()
    gluLookAt(3.0, 4.0, 5.0, 0.0, 0.0, 0.0, 0.3, 1.0, 0.2)
    glRotated(angleX, 1.0, 0.5, 0.0);
    glRotated(angleY, 1.0, 1.0, 1.0);

    glBegin(GL_LINES)
    glColor3f( 0.2, 0.7,0.6)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def drawing():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    drawObjs()

    glFlush()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(700, 600)
glutCreateWindow("Cube")
glutDisplayFunc(drawing)
glutReshapeFunc(resize)

glutMainLoop()
