# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200129


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangePrivateEndpointCompartmentDetails(object):
    """
    The details required to change a private endpoint compartment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangePrivateEndpointCompartmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ChangePrivateEndpointCompartmentDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId'
        }

        self._compartment_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ChangePrivateEndpointCompartmentDetails.
        The OCID of a compartment.


        :return: The compartment_id of this ChangePrivateEndpointCompartmentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ChangePrivateEndpointCompartmentDetails.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this ChangePrivateEndpointCompartmentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
