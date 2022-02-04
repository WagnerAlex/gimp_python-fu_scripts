#!/usr/bin/env python

# colorize function (drawable, hue in degrees, saturation in percent, lightness in percent)
## hue color in degrees is 360/number from gimp colorize menu. 
## 100 saturation is percent and 1.00 in gimp colorize menu.
## 0 lightness is 0 percent plus/minus

from gimpfu import *

def layers(image, layer) :
    g = gimp.pdb
    images = gimp.image_list() 
    image = images[0] # position 0 of list - only one image is open
    layers = image.layers
    
    if (len(layers) != 3) or (image == None): # image must contain 3 layers
      currenth = pdb.gimp_message_get_handler()
      pdb.gimp_message_set_handler(2) # write to error-console
      gimp.message("INFO: Save 3 image planes (rgb) from FITS-Liberator and open in GIMP as layers into one image. FITS-Liberator plane 1 = red.tif, plane 2 = green.tif plane 3 = blue.tif")
      pdb.gimp_message_set_handler(currenth) # change handler back to normal
      return
    
    g.gimp_image_undo_group_start(image)
    g.gimp_image_convert_rgb(image)
    g.gimp_image_set_filename(image, "rgb")
    
    try:
      for l in layers: l.mode=LAYER_MODE_SCREEN # change mode of all layers to screen
      for l in layers: 
        if l.name == "red.tif":
          l.name="red"
          g.gimp_item_set_color_tag(l, 6)
          g.gimp_drawable_colorize_hsl(l, 0, 100, 0) 
        if l.name == "green.tif":
          l.name="green"
          g.gimp_item_set_color_tag(l, 2)
          g.gimp_drawable_colorize_hsl(l, 120, 100, 0) 
        if l.name == "blue.tif":
          l.name="blue"
          g.gimp_item_set_color_tag(l, 1)
          g.gimp_drawable_colorize_hsl(l, 240, 100, 0) 
    except Exception as err:
       gimp.message("Error: " + str(err))
       
    g.gimp_image_undo_group_end(image)
    gimp.message("Reached end of script :)")


register(
    "python_fu_layers",
    "Colorize separate RGB-Layers",
    "Rename layers, convert image to rgb, colorize layers",
    "Alexander Wagner",
    "BSD 3-Clause",
    "2022",
    "<Image>/Filters/Layers/Colorize Layers",
    "GRAY",
    [],
    [],
    layers)

main()
