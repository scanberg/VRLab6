# task10.py
from H3D import *
from H3DInterface import *
from H3DUtils import *
import math

radius = 0.1
springConstant = 100.0

class Force( TypedField( SFVec3f, ( SFVec3f, SFRotation )  ) ):
	def update( self, event ):
		routes_in = self.getRoutesIn()
		stylusPosition = routes_in[0].getValue()
		stylusOrientation = routes_in[1].getValue()
		dist = stylusPosition.length()
		if dist < radius and dist > 0:
			return stylusPosition.normalize()*(radius-dist)*springConstant
		else:
			return stylusPosition*0

force = Force()
