import random
import math
import copy as cp

import stddraw as stddraw  # stddraw is used as a basic graphics library
from color import Color  # used for coloring the tile and the number on it

# Class used for modeling numbered tiles as in 2048
class Tile:
   # Class attributes shared among all Tile objects
   # ---------------------------------------------------------------------------
   # the value of the boundary thickness (for the boxes around the tiles)
   boundary_thickness = 0.004
   # font family and size used for displaying the tile number
   font_family, font_size = "Arial", 14

   # Constructor that creates a tile with 2 as the number on it
   def __init__(self):
      # set the number on the tile
      self.number = self.randomValue()
      # set the colors of the tile
      #self.background_color = Color(151, 178, 199) # background (tile) color
      self.background_color = Color(151, 178, 199)  # background (tile) color
      self.foreground_color = Color(0, 100, 200)  # foreground (number) color
      self.box_color = Color(0, 100, 200)  # box (boundary) color



   def draw(self, position, length = 1):


      if self.number == 2:
         self.background_color = Color(239, 230, 221)
      elif self.number == 4:
         self.background_color = Color(239, 227, 205)
      elif self.number == 8:
         self.background_color = Color(245, 179, 127)
      elif self.number == 16:
         self.background_color = Color(247, 152, 107)
      elif self.number == 32:
         self.background_color = Color(247, 124, 90)
      elif self.number == 64:
         self.background_color = Color(247, 93, 59)
      elif self.number == 128:
         self.background_color = Color(239, 205, 115)
      elif self.number == 256:
         self.background_color = Color(239, 206, 99)
      elif self.number == 512:
         self.background_color = Color(239, 198, 82)
      elif self.number == 1024:
         self.background_color = Color(238, 198, 66)
      elif self.number == 2048:
         self.background_color = Color(239, 194, 49)
      else:
         self.background_color = Color(61, 58, 51)


      self.boundary_color = Color(188, 174, 161)

      # draw the tile as a filled square
      stddraw.setPenColor(self.background_color)
      stddraw.filledSquare(position.x, position.y, length / 2)
      # draw the bounding box around the tile as a square
      stddraw.setPenColor(self.box_color)
      stddraw.setPenRadius(Tile.boundary_thickness)
      stddraw.square(position.x, position.y, length / 2)
      stddraw.setPenRadius()  # reset the pen radius to its default value
      # draw the number on the tile
      stddraw.setPenColor(self.foreground_color)
      stddraw.setFontFamily(Tile.font_family)
      stddraw.setFontSize(Tile.font_size)
      stddraw.text(position.x, position.y, str(self.number))



   def randomValue(self):
      values = [2, 4]
      random_indx = random.randint(0, len(values) - 1)
      random_value = values[random_indx]
      return random_value


