#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Seong Heon Lee and Kynan Barton
# Course: CS510 Fall 2017
###

"""Testing the ListComplexPlane Class
This module contains five test functions to keep the class safe from errors.
"""

from cplane import ListComplexPlane

def test_cplane():
    """test class instantiation with the default attributes (xmin=-4,
    xmax=4, ymin=-4, ymax=4)
    
    """
    LCP = ListComplexPlane()
    assert LCP.plane == [[(-4-4j), (-3-4j), (-2-4j), (-1-4j), -4j, (1-4j), (2-4j), (3-4j), (4-4j)], [(-4-3j), (-3-3j), (-2-3j), (-1-3j), -3j, (1-3j), (2-3j), (3-3j), (4-3j)], [(-4-2j), (-3-2j), (-2-2j), (-1-2j), -2j, (1-2j), (2-2j), (3-2j), (4-2j)], [(-4-1j), (-3-1j), (-2-1j), (-1-1j), -1j, (1-1j), (2-1j), (3-1j), (4-1j)], [(-4+0j), (-3+0j), (-2+0j), (-1+0j), 0j, (1+0j), (2+0j), (3+0j), (4+0j)], [(-4+1j), (-3+1j), (-2+1j), (-1+1j), 1j, (1+1j), (2+1j), (3+1j), (4+1j)], [(-4+2j), (-3+2j), (-2+2j), (-1+2j), 2j, (1+2j), (2+2j), (3+2j), (4+2j)], [(-4+3j), (-3+3j), (-2+3j), (-1+3j), 3j, (1+3j), (2+3j), (3+3j), (4+3j)], [(-4+4j), (-3+4j), (-2+4j), (-1+4j), 4j, (1+4j), (2+4j), (3+4j), (4+4j)]]

def f2(c): return 2*c
def f3(c): return c*c

def test_cplane2():
    """test the transformation function f2"""
    LCP = ListComplexPlane()
    LCP.apply(f2)
    assert LCP.plane == [[(-8-8j), (-8-6j), (-8-4j), (-8-2j), (-8+0j), (-8+2j), (-8+4j), (-8+6j), (-8+8j)], [(-6-8j), (-6-6j), (-6-4j), (-6-2j), (-6+0j), (-6+2j), (-6+4j), (-6+6j), (-6+8j)], [(-4-8j), (-4-6j), (-4-4j), (-4-2j), (-4+0j), (-4+2j), (-4+4j), (-4+6j), (-4+8j)], [(-2-8j), (-2-6j), (-2-4j), (-2-2j), (-2+0j), (-2+2j), (-2+4j), (-2+6j), (-2+8j)], [-8j, -6j, -4j, -2j, 0j, 2j, 4j, 6j, 8j], [(2-8j), (2-6j), (2-4j), (2-2j), (2+0j), (2+2j), (2+4j), (2+6j), (2+8j)], [(4-8j), (4-6j), (4-4j), (4-2j), (4+0j), (4+2j), (4+4j), (4+6j), (4+8j)], [(6-8j), (6-6j), (6-4j), (6-2j), (6+0j), (6+2j), (6+4j), (6+6j), (6+8j)], [(8-8j), (8-6j), (8-4j), (8-2j), (8+0j), (8+2j), (8+4j), (8+6j), (8+8j)]]

def test_cplane3():
    """test if a new function added to self.fs when self.apply is called"""
    LCP = ListComplexPlane()
    LCP.apply(f2)
    LCP.apply(f3)
    assert LCP.fs == [f2, f3]


def test_cplane4():
    """ test the self.zoom function
    The function will take new values of attributes and generate a new plane """
    LCP = ListComplexPlane()
    LCP.apply(f2)
    LCP.apply(f3)
    LCP.zoom(-2, 2, 4, -2, 2, 4)
    assert LCP.plane == [[32j, (-12+16j), (-16-0j), (-12-16j), -32j], [(12+16j), 8j, (-4-0j), -8j, (12-16j)], [(16-0j), (4-0j), 0j, (4+0j), (16+0j)], [(12-16j), -8j, (-4+0j), 8j, (12+16j)], [-32j, (-12-16j), (-16+0j), (-12+16j), 32j]]


def test_cplane5():
    """ test the self.refresh function
    The function should reset self.fs to an empty list"""
    LCP = ListComplexPlane()
    LCP.apply(f2)
    LCP.apply(f3)
    LCP.refresh()
    assert LCP.fs == []


