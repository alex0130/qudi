# -*- coding: utf-8 -*-

"""
This file contains the Qudi Interface for a camera.

Qudi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Qudi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Qudi. If not, see <http://www.gnu.org/licenses/>.

Copyright (c) the Qudi Developers. See the COPYRIGHT.txt file at the
top-level directory of this distribution and at <https://github.com/Ulm-IQO/qudi/>
"""

import abc
from core.util.interfaces import InterfaceMetaclass


class CameraInterface(metaclass=InterfaceMetaclass):
    """ Define the interface with a camera
    These camera can be cooled, used in image mode or Full Vertical Binning
    """

    _modtype = 'CameraInterface'
    _modclass = 'interface'

    @abc.abstractmethod
    def get_name(self):
        """ Retrieve an identifier of the camera that the GUI can print
        Maker, model, serial number, etc.
        @return string: name for the camera
        """
        pass

    @abc.abstractmethod
    def get_size(self):
        """ Retrieve size of the image

        @return Integer Tuple : (x,y)
        """
        pass

    @abc.abstractmethod
    def support_live_acquisition(self):
        """
        @return bool
        """
        pass

    @abc.abstractmethod
    def start_live_acquisition(self):
        """
        @return bool: True : Ok, False : Error
        """
        pass

    @abc.abstractmethod
    def start_single_acquisition(self):
        """
        @return bool: True : Ok, False : Error
        """
        pass

    @abc.abstractmethod
    def stop_acquisition(self):
        """
        @return bool: True : Ok, False : Error
        """
        pass


    @abc.abstractmethod
    def get_acquired_data(self):
        """
        @return: aquired data, 2d array
        Each pixel might be a float, integer or sub pixels
            [[row],[row]...] in IMAGE
        """
        pass

    @abc.abstractmethod
    def set_exposure(self, time):
        """ Set the exposure time in seconds

        @return float: new exposure time
        """
        pass

    @abc.abstractmethod
    def get_exposure(self):
        """ Get the exposure time in seconds

        @return float: exposure time
        """
        pass


    @abc.abstractmethod
    def set_gain(self, gain):
        """ Set the gain

        @return float: new gain
        """
        pass

    @abc.abstractmethod
    def get_gain(self):
        """ Get the gain

        @return float: gain
        """
        pass


    @abc.abstractmethod
    def get_ready_state(self):
        """ Is the camera ready for an acquisition ?

        @return: bool
        """
        pass


