# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .fsu_goal_version_details import FsuGoalVersionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageIdFsuTargetDetails(FsuGoalVersionDetails):
    """
    Exadata Fleet Update Cycle Target Image Id details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageIdFsuTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.ImageIdFsuTargetDetails.type` attribute
        of this class is ``IMAGE_ID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ImageIdFsuTargetDetails.
            Allowed values for this property are: "VERSION", "IMAGE_ID"
        :type type: str

        :param home_policy:
            The value to assign to the home_policy property of this ImageIdFsuTargetDetails.
            Allowed values for this property are: "CREATE_NEW", "USE_EXISTING"
        :type home_policy: str

        :param new_home_prefix:
            The value to assign to the new_home_prefix property of this ImageIdFsuTargetDetails.
        :type new_home_prefix: str

        :param software_image_id:
            The value to assign to the software_image_id property of this ImageIdFsuTargetDetails.
        :type software_image_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'home_policy': 'str',
            'new_home_prefix': 'str',
            'software_image_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'home_policy': 'homePolicy',
            'new_home_prefix': 'newHomePrefix',
            'software_image_id': 'softwareImageId'
        }

        self._type = None
        self._home_policy = None
        self._new_home_prefix = None
        self._software_image_id = None
        self._type = 'IMAGE_ID'

    @property
    def software_image_id(self):
        """
        **[Required]** Gets the software_image_id of this ImageIdFsuTargetDetails.
        Target database software image OCID.


        :return: The software_image_id of this ImageIdFsuTargetDetails.
        :rtype: str
        """
        return self._software_image_id

    @software_image_id.setter
    def software_image_id(self, software_image_id):
        """
        Sets the software_image_id of this ImageIdFsuTargetDetails.
        Target database software image OCID.


        :param software_image_id: The software_image_id of this ImageIdFsuTargetDetails.
        :type: str
        """
        self._software_image_id = software_image_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
