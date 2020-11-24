#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/chadsrover/robotics_ws/src/baxter_pykdl"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/chadsrover/robotics_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/chadsrover/robotics_ws/install/lib/python2.7/dist-packages:/home/chadsrover/robotics_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/chadsrover/robotics_ws/build" \
    "/usr/bin/python2" \
    "/home/chadsrover/robotics_ws/src/baxter_pykdl/setup.py" \
     \
    build --build-base "/home/chadsrover/robotics_ws/build/baxter_pykdl" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/chadsrover/robotics_ws/install" --install-scripts="/home/chadsrover/robotics_ws/install/bin"