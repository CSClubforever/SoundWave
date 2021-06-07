# wavefns.py
#By Tsering Tashi and Ryusei Mikami
#(It has the information about various standard form of wave such as squarewave,
#trianglewave, sawtoothwave, and whitenoise)
"""Simple periodic waveform functions.

 A "standard" wave function (such as sin) is a periodic function with
 period equal to 2*pi (also known as tau) and a amplitude of 1.
"""
import math
import random

def sinewave(t):
    """ Standard periodic sine wave generator
    pre: t >= 0
    post returns value of standard sine wave at time t
         (0 at t=0, 1 at t= pi/2, 0 at pi, -1 at 1.5*pi, 0 at 2*pi)
    """

    return math.sin(t)

def squarewave(t):
    """ Standard periodic square wave generator.

    pre: t >= 0
    post: returns value of standard square wave at time t.
          (1.0 for 0 <= t < pi and -1.0 for pi <= t < 2*pi)
    """
    phase = t % math.tau
    if phase < math.pi:
        return 1
    else:
        return -1


def trianglewave(t):
    """ Standard periodic triangle wave generator.

    pre: t >= 0
    post: returns value of standard triangle wave at time t.
          (0.0 at t=0, 1.0 at t=pi/2, 0.0 at t=pi, -1.0 at t=1.5*pi)
    """
    phase = t%math.tau
    if 0 <= phase < math.pi / 2:
        return (0 + phase) * 2/math.pi
    elif math.pi / 2 <= phase < (3*math.pi) / 2:
        return 1 + (phase - math.pi/2) * -2/math.pi
    elif (3*math.pi) / 2 <= phase <= math.tau:
        return -1 + (phase - 1.5 * math.pi) * 2/math.pi
    
    

def sawtoothwave(t):
    """ Standard periodic sawtooth wave generator.

    pre: t >= 0
    post: returns value of standard sawtooth wave at time t.
          (0.0 at t=0, rising to 1 near t=pi, -1.0 at t=pi, rising to 0.0 at t=pi)
    """
    phase = t % math.tau
    if 0 <= phase < math.pi:
        return 0 + (phase * 1 / math.pi)
    elif math.pi<= phase < 2*math.pi:
        return -1 + (phase - math.pi) * 1/math.pi 


def whitenoise(t):
    """ White noise "wave" generator

    post: returns random float value in range -1 to 1
    """
    
    return (2 * random.random()) - 1



######################################################################
# The rest of this is for testing purposes. No changes needed.
# Requires: graphics needed to visualize the wave forms

def _plot(wavefn):
    # test function plots 2 cycles of wavefunction
    win = GraphWin(wavefn.__name__, 600, 200)
    win.setCoords(0, -1, 2*math.tau, 1)
    Line(Point(0, 0), Point(2*math.tau, 0)).draw(win)
    npoints = 300
    dt = 2*math.tau/npoints
    t = 0
    last = Point(t, wavefn(t))
    for i in range(npoints):
        t += dt
        p = Point(t, wavefn(t))
        segment = Line(last, p).draw(win)
        segment.setFill("red")
        segment.setWidth(2)
        last = p
    win.getMouse()
    win.close()


if __name__ == "__main__":
    from graphics import *
    for wf in [sinewave, squarewave, trianglewave, sawtoothwave, whitenoise]:
        _plot(wf)
