[app]
title = FaceApp
package.name = faceapp
package.domain = org.archtech
source.dir = .                  # ✅ Add this line — use current directory as source
version = 1.0.0                 # ✅ Add this line — set your app version
source.include_exts = py,png,jpg,kv,atlas,html,mp3,json,xml
source.include_patterns = assets/*,templates/*
requirements = python3,flask,flask_cors,opencv-python,numpy,requests,android
presplash.filename = assets/logo.jpg
icon.filename = assets/logo.jpg
orientation = portrait
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.minapi = 21
android.api = 33
android.target = 33

[buildozer]
log_level = 2
warn_on_root = 1
