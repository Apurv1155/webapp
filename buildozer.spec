title = FaceApp
package.name = faceapp
package.domain = org.archtech

source.include_exts = py,png,jpg,html,mp3,json,xml
source.include_patterns = assets/*,templates/*

requirements = python3,flask,flask_cors,opencv-python,numpy,requests

orientation = portrait
android.permissions = INTERNET, CAMERA

presplash.filename = assets/logo.jpg
icon.filename = assets/logo.jpg
