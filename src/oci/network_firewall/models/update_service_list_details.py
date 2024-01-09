# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateServiceListDetails(object):
    """
    Request for updating an existing service in context to the network firewall policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateServiceListDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param services:
            The value to assign to the services property of this UpdateServiceListDetails.
        :type services: list[str]

        """
        self.swagger_types = {
            'services': 'list[str]'
        }

        self.attribute_map = {
            'services': 'services'
        }

        self._services = None

    @property
    def services(self):
        """
        **[Required]** Gets the services of this UpdateServiceListDetails.
        Collection of service names.


        :return: The services of this UpdateServiceListDetails.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this UpdateServiceListDetails.
        Collection of service names.


        :param services: The services of this UpdateServiceListDetails.
        :type: list[str]
        """
        self._services = services

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
