#!/usr/bin/env python3

import abscplane

""" The module includes a new class ListComplexPlane that subclasses the abstract base class AbsComplexPlane which is imported from the abscplane.py module. 
"""

class ListComplexPlane(abscplane.AbsComplexPlane):
    """ This class implements the complex plane with given attributes. 
    It uses a list comprehension to represent the 2D grid needed to store 
    the complex plane. The complex plane is a 2D grid of complex numbers, 
    having the form (x + y*1j), where 1j is the unit imaginary number in 
    Python, and one can think of x and y as the coordinates for the horizontal 
    axis and the vertical axis of the plane respectively. All attributes will
    be set during the __init__ constructor, and initialize the plane immediately 
    upon class instantiation.

    Methods:
        __create_plane : a private method that creates or refreshs plane
        refresh        : regenerate plane
        apply          : apply a given function f
        zoom           : transform planes going through all functions lists 



    """
    def __init__(self, xmin=-4,xmax=4,xlen=8,ymin=-4,ymax=4,ylen=8):
        """all attributes will be automatically set when the class becomes 
        instantiated. 

        Attributes:
            xmax (float) : maximum horizontal axis value
            xmin (float) : minimum horizontal axis value
            xlen (int)   : number of horizontal points
            ymax (float) : maximum vertical axis value
            ymin (float) : minimum vertical axis value
            xunit (int)  : grid unit value of x axis
            yunit (int)  : grid unit value of y axis 
            ylen (int)   : number of vertical points
            plane        : a list of stored complex plane
            fs (list[function]) : function sequence to transform plane

        """
        self.xmin  = xmin
        self.xmax  = xmax
        self.xlen  = xlen
        self.ymin  = ymin
        self.ymax  = ymax
        self.ylen  = ylen
        self.xunit = (self.xmax - self.xmin) / self.xlen
        self.yunit = (self.ymax - self.ymin) / self.ylen

        # See the implementation details of creating a complex plane  below 
        # in  _create_plane function.
        self.plane = []
        self._create_plane()

        # store a list of functions that are being applied 
        # in order to each point of the complex plane, initially empty
        self.fs = []

    def _create_plane(self):
        """This ia a private method to create a list of complex plane 
        at the time of class initiation with the default attributes
        (xmax, xmin, xlen, ymax, ymin,ylen). The method self.refresh also uses 
        this private method to refresh each point in comlext planes using
        the stored attributes. 

        Returns:
            a list of complex plane
        """
        self.plane = [[(self.xmin + x*self.xunit) + (self.ymin + y*self.yunit)*1j for x in range(self.xlen+1)] for y in range(self.ylen+1)]
 
    def refresh(self):
        """Regenerate complex plane.
        Populate self.plane with new points (x + y*1j), using
        the stored attributes of xmax, xmin, xlen, ymax, ymin,
        and ylen to set plane dimensions and resolution. Reset
        the attribute fs to an empty list so that no functions 
        are transforming the fresh plane.
        """
        self._create_plane()
        self.fs = []
    
    def apply(self, f):
        """Add the function f as the last element of self.fs. 
        Apply f to every point of the plane, so that the resulting
        value of self.plane is the final output of the sequence of
        transformations collected in the list self.fs.
        """
        self.fs.append(f)
        self.plane = [[f(self.plane[x][y]) for x in range(self.xlen+1)] for y in range(self.ylen+1)]
    
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """Reset self.xmin, self.xmax, and self.xlen.
        Also reset self.ymin, self.ymax, and self.ylen.
        Regenerate the plane with the new range of the x- and y-axes,
        then apply all transformations in fs in the correct order to
        the new points so that the resulting value of self.plane is the
        final output of the sequence of transformations collected in
        the list self.fs.

        Attributes:
            xmax (float) : maximum horizontal axis value
            xmin (float) : minimum horizontal axis value
            xlen (int)   : number of horizontal points
            ymax (float) : maximum vertical axis value
            ymin (float) : minimum vertical axis value
            xunit (int)  : grid unit value of x axis
            yunit (int)  : grid unit value of y axis 
            ylen (int)   : number of vertical points
            plane        : a list of stored complex plane
            fs (list[function]) : function sequence to transform plane

        """
        self.xmin = xmin
        self.xmax = xmax
        self.xlen  = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen  = ylen
        self.xunit = (self.xmax - self.xmin) / self.xlen
        self.yunit = (self.ymax - self.ymin) / self.ylen
        
        self._create_plane()
        for i, f in enumerate(self.fs):
            print("running the function "+str(i+1))
            self.plane = [[f(self.plane[x][y]) for x in range(self.xlen+1)] for y in range(self.ylen+1)] 
            
    
def main():
    cplane = ListComplexPlane()
    print(cplane.plane)

if __name__ == "__main__":
    main()





