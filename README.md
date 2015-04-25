# SourceMod Socket Extension [![Build Status](http://ci.nexisonline.net/job/sourcemod-socket/badge/icon)](http://ci.nexisonline.net/job/sourcemod-socket/)

This has been forked from [sfPlayer's original Git repository](http://player.to/gitweb/index.cgi?p=sm-ext-socket.git). Get to the [AlliedModders forum thread](https://forums.alliedmods.net/showthread.php?t=67640) for more information.

## Dependencies for building

 * [AMBuild](https://github.com/alliedmodders/ambuild)
 * [SourceMod](https://github.com/alliedmodders/sourcemod)
  * Note: Requires that you have installed the dependency repositories, especially metamod.
 * [Boost](http://www.boost.org/)
 * [msinttypes](https://code.google.com/p/msinttypes/)

## Building on Windows

Set the following environment variables on your system:

 * `SOURCEMOD` - path to SourceMod (>= 1.5.x)
 * `BOOST155` - path to boost libraries (>= 1.5.5)
 * `MSINTTYPES` - path to latest version of msinttypes

The solution is in the `msvc10/` directory.

## Building on Linux

```bash
# Make a build directory
mkdir -p build

# Enter it
cd build

# Configure and build ambuild.
python ../configure.py
ambuild
```

The results will be in the `dist/` directory.

## Prebuilt Packages


Packages and SHA512 hashes are available [here](http://dedi.nexisonline.net/drop/). You can view our Jenkins continuous integration build status [here](http://ci.nexisonline.net/job/sourcemod-socket/).
