"""The base class of the Franka robot."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc

from robovat.robots import robot
from robovat.utils.yaml_config import YamlConfig


class FrankaPanda(robot.Robot):
