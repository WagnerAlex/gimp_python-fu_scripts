# gimp_python-fu_scripts
Python Scripts for Astrophotography 

## ColorizeLayers.py
Script to create a colorized rgb image from 3 greyscale layers.
Copy file to plugins folder. (example: C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins)
The Script will be in "Filters/Layers/"-Menu

### Workflow: 
Capture FITS from DSLR and stack in DSS. 
Save DSS Output as FITS and stretch the image in FITS-Liberator.
Save all 3 image-planes from FITS-Liberator to tif files: plane 1 = red.tif, plane 2 = green.tif plane 3 = blue.tif

Open all 3 images in GIMP using "open as layers", so you have one greyscale image with the 3 layers.

Run script to rename layers, add color tags, change mode to screen, convert and rename image to rgb, colorize layers according to their name.

This script is experimental and still work in progress.
Also, it's my first day using python-fu in GIMP ;)


