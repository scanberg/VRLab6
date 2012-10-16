# task9.py

# Import H3D specific functions.
from H3DInterface import *
 
# ChangeColor is a field that takes and MFBool as input and outputs an SFColor
# The field routed to this class is the isTouched field of X3DGeometryNode
class ChangeColor( TypedField( SFColor, MFBool ) ):
  # Only using routes for this field so  only override the update function.
  def update( self, event ):
    # The inputed field is initially zero length.
    if len(event.getValue()) > 0 and event.getValue()[0]:
      # If touched return white color
      return RGB(1, 1, 1)
    else:
      # If not touched return grey color
      return RGB(0.2, 0.2, 0.2)
 
# Create an instance of our field. This name is what will be used
# when routing to and from the field.
changeColor = ChangeColor()

# Get the references to the Material and Sphere node.
box, material, = references.getValue()
 
# Set up routes.
box.isTouched.route( changeColor )
changeColor.route( material.diffuseColor )
