# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "controller_interface;control_toolbox;effort_controllers;baxter_core_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lbaxter_sim_controllers".split(';') if "-lbaxter_sim_controllers" != "" else []
PROJECT_NAME = "baxter_sim_controllers"
PROJECT_SPACE_DIR = "/home/chadsrover/robotics_ws/install"
PROJECT_VERSION = "1.2.12"
