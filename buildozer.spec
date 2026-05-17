[app]
title = X112
package.name = x112
package.domain = org.x112

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

# Android settings (IMPORTANT FIXES)
android.api = 33
android.minapi = 21

android.permissions = INTERNET,ACCESS_NETWORK_STATE

# stability flags
log_level = 2
warn_on_root = 1

# reduce build crashes
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
