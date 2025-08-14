# wallChange

A desktop utility for KDE plasma that runs via the cli and changes the
desktop wallpaper on a regular base in the background.

# TODO

## How to run on your machine

1. Ensure you have `nohup` installed, it's necessary for running scripts.
2. Clone the repo.
3. In your shell's configuration file (`.zshrc`,`.bashrc` or other)
   add `nohup python3 path/to/project/files < /dev/null &> nohup.out &`.
4. Enjoy!

## Setting up the `wallrc.py` file

In the `wallrc.py` file,
the configuration file of this project,
you will find 3 variables:
`minutes`, for controlling
how much each wallpaper is displayed,
`path`, for providing
the path you cloned
this repo into,
and `theme`, for
choosing a 'theme' of wallpapers
(as of now, there are
two themes: 'default' and 'animals').

## _NOTE_

_If you enjoyed using this repo, consider giving the project a star, it will be very appreciated!_

## WARNING: PLEASE READ

The project is still in early beta,
and is designed exclusively for
systems that have KDE plasma on them
