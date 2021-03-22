# OrcaCNN Web-Application


### Things to take care of:

- Please input audio files which are significantly longer. 
- Currentl only supports `.wav` files.
- Put [convert2ycbcr](https://github.com/scikit-image/scikit-image/blob/main/skimage/restoration/_denoise.py#L724)
 : bool, optional 

 - audio files uploaded are stored in the `uploads` folder first and are then picked up by the pre-processing script.

 - is there a way to stop pre-processing scripy mid-way? refresh does not work.

 - THis app uses [blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints) and [application factories](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/)