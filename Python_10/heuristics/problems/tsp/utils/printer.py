# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:00:21 2021

Use this class to generate visual representations of a solution.

@author: beer
"""

import sys
import os
from pathlib import Path

import heuristics.problems.tsp.utils.helpers as hlp

class Printer:

    """
    Export an instance and it's corresponding solution to a HTML file containing an SVG representing the solution.
    @param instance
    @param solution 
    @param filePath Path to the file to write to.
    @throws OSError
    """


    def writeToSVG(instance, solution, filePath):
        margin = 200.
        minX = sys.float_info.max
        minY = sys.float_info.max
        maxX = 0.
        maxY = 0.
        
        for point in solution:
            maxX = max(maxX, point.getX())
            maxY = max(maxY, point.getY())
            
            minX = min(minX, point.getX())
            minY = min(minY, point.getY())


        xTransform = margin - minX;
        yTransform = margin - minY;

        def mirrorY(y):
            #return y
            return minY + maxY - y

        height = int(maxY + margin + yTransform)
        width = int(maxX + xTransform + margin)

        try:
            path = Path(filePath)
            os.makedirs(path.parent.absolute())
        except OSError:
            pass
        
        try:
            with open(filePath, 'w') as svgWriter:
                svgWriter.write("<html>")
                svgWriter.write("<head>")
                svgWriter.write("<style>")
                svgWriter.write(".hoverbg {background:rgba(255,255,255,0.3);}")
                svgWriter.write(".hoverbg:hover {background:rgba(255,255,255,1.0);}")
                svgWriter.write("</style>")
                svgWriter.write("<title>" + instance.getName() + "</title>")
                svgWriter.write("</head>")
                svgWriter.write("<body>")
                svgWriter.write("<div class=\"hoverbg\" style=\"position:absolute; top:10;left:10; z-index:100;\">")
                svgWriter.write("<p style=\"font-size:12px\">" + instance.getName() + "</p>")
                svgWriter.write("<p style=\"font-size:12px\">" + instance.getComment() + "</p>")
                svgWriter.write("<p style=\"font-size:12px\">Total distance: " + str(int(round(hlp.Helpers.euclideanDistance2DList(solution)))) + "</p>")
                svgWriter.write("</div>")

                svgWriter.write("<svg viewBox=\"0 0 " + str(width) + " " + str(height) + "\" style=\"position:absolute; top:0; left:0; bottom:0; right:0; z-index:1;\">")

                for point in solution:
                    svgWriter.write("<circle cx=\"" + str(int(round(point.getX() + xTransform))) + "\" cy=\"" + str(int(round(mirrorY(point.getY()) + yTransform))) + "\" r=\"10\" stroke=\"black\" stroke-width=\"1\" fill=\"black\"/>")
			
                point = solution[0]
                svgWriter.write("<circle cx=\"" + str(int(round(point.getX() + xTransform))) + "\" cy=\"" + str(int(round(mirrorY(point.getY()) + yTransform))) + "\" r=\"10\" stroke=\"black\" stroke-width=\"2\" fill=\"blue\"/>")

                currentPoint = solution[0]
            
                for i in range(1, len(solution)):
                    nextPoint = solution[i]
                    svgWriter.write("<line x1=\"" + str(int(round(currentPoint.getX() + xTransform))) + "\" y1=\"" + str(int(round(mirrorY(currentPoint.getY()) + yTransform))) + "\" x2=\"" + str(int(round(nextPoint.getX() + xTransform))) + "\" y2=\"" + str(int(round(mirrorY(nextPoint.getY()) + yTransform))) + "\" style=\"stroke:rgb(255,0,0);stroke-width:5\"/>")
                    currentPoint = nextPoint
			
                nextPoint = solution[0]
                svgWriter.write("<line x1=\"" + str(int(round(currentPoint.getX() + xTransform))) + "\" y1=\"" + str(int(round(mirrorY(currentPoint.getY()) + yTransform))) + "\" x2=\"" + str(int(round(nextPoint.getX() + xTransform))) + "\" y2=\"" + str(int(round(mirrorY(nextPoint.getY()) + yTransform))) + "\" style=\"stroke:rgb(255,0,0);stroke-width:5\"/>")
            
                svgWriter.write("</svg>")
                svgWriter.write("</body>")
                svgWriter.write("</html>")
        except OSError as err:
            print('OS error: {0}'.format(err))
            
        return
