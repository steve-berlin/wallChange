#!/bin/bash

wallnum="$1"
amount=11
if ! [[ "$wallnum" =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 <wallpaper_number>"
  exit 1
fi
if [[ "$wallnum" -gt "$amount" ]]; then
  wallnum=$amount
fi

# Find the absolute path
WALLPAPER_PATH="$(realpath "wallpapers/$wallnum.jpg")"
DBUS_PATH="file://$WALLPAPER_PATH"

qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "
var allDesktops = desktops();
for (i = 0; i < allDesktops.length; i++) {
  d = allDesktops[i];
  d.wallpaperPlugin = 'org.kde.image';
  d.currentConfigGroup = ['Wallpaper', 'org.kde.image', 'General'];
  d.writeConfig('Image', '$DBUS_PATH');
}"
