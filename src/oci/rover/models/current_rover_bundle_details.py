# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CurrentRoverBundleDetails(object):
    """
    Information required to list all available valid rover bundle versions that can be upgraded based on current bundle version.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CurrentRoverBundleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param current_rover_bundle_version:
            The value to assign to the current_rover_bundle_version property of this CurrentRoverBundleDetails.
        :type current_rover_bundle_version: str

        """
        self.swagger_types = {
            'current_rover_bundle_version': 'str'
        }

        self.attribute_map = {
            'current_rover_bundle_version': 'currentRoverBundleVersion'
        }

        self._current_rover_bundle_version = None

    @property
    def current_rover_bundle_version(self):
        """
        **[Required]** Gets the current_rover_bundle_version of this CurrentRoverBundleDetails.
        The version of current rover bundle on customer's roverNode or roverCluster device.


        :return: The current_rover_bundle_version of this CurrentRoverBundleDetails.
        :rtype: str
        """
        return self._current_rover_bundle_version

    @current_rover_bundle_version.setter
    def current_rover_bundle_version(self, current_rover_bundle_version):
        """
        Sets the current_rover_bundle_version of this CurrentRoverBundleDetails.
        The version of current rover bundle on customer's roverNode or roverCluster device.


        :param current_rover_bundle_version: The current_rover_bundle_version of this CurrentRoverBundleDetails.
        :type: str
        """
        self._current_rover_bundle_version = current_rover_bundle_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
