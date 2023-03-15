# List of 3rd-party  

Under every package name, there will be information about availability of some form of official (or unofficial but better) installation method. Do consider them.

It is recommended to read the content of pspec.xml by clicking the URL instead of blindly running the command. Do take note that we use `--ignore-safety` flag.


## Sublime Merge

No universal packages are available. There is .tar.xz archive available which you can manually extract and run.
```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/Abhinav1217/Solus-3rd-Party/main/packages/sublime-merge/pspec.xml

sudo eopkg it sublime-merge*.eopkg; sudo rm sublime-merge*.eopkg
```

## Microsoft Edge (Stable)
An official flatpak is available [Link](https://flathub.org/apps/details/com.microsoft.Edge), but no tar archive. There are few appimages from some reliable* 3rd party that you can try. [Link](https://gitlab.com/linuxappimage/microsoft_edge) [Link](https://apprepo.de/appimage/edge)

```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/Abhinav1217/Solus-3rd-Party/main/packages/ms-edge/pspec.xml

sudo eopkg it microsoft-edge*.eopkg; sudo rm microsoft-edge*.eopkg
```

## Zoom Client 

There are no snap or flatpak available but they do provide tar archive for other OSes. There are few appimages available from reliable* 3rd party that you can try. [Link](https://github.com/probonopd/Zoom.AppImage) Since Zoom client updates quite frequently, they might be better option.

```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/Abhinav1217/Solus-3rd-Party/main/packages/zoom/pspec.xml

sudo eopkg it zoom*.eopkg; sudo rm zoom*.eopkg
```

## Darling (alpha)

There are no snap or flatpak or appimage available.

```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/Abhinav1217/Solus-3rd-Party/main/packages/darling/pspec.xml

sudo eopkg it darling*.eopkg; sudo rm darling*.eopkg
```