# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .external_listener_endpoint import ExternalListenerEndpoint
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalListenerIpcEndpoint(ExternalListenerEndpoint):
    """
    An `IPC`-based protocol address.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalListenerIpcEndpoint object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalListenerIpcEndpoint.protocol` attribute
        of this class is ``IPC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this ExternalListenerIpcEndpoint.
            Allowed values for this property are: "IPC", "TCP", "TCPS"
        :type protocol: str

        :param services:
            The value to assign to the services property of this ExternalListenerIpcEndpoint.
        :type services: list[str]

        :param key:
            The value to assign to the key property of this ExternalListenerIpcEndpoint.
        :type key: str

        """
        self.swagger_types = {
            'protocol': 'str',
            'services': 'list[str]',
            'key': 'str'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'services': 'services',
            'key': 'key'
        }

        self._protocol = None
        self._services = None
        self._key = None
        self._protocol = 'IPC'

    @property
    def key(self):
        """
        **[Required]** Gets the key of this ExternalListenerIpcEndpoint.
        The unique name of the service.


        :return: The key of this ExternalListenerIpcEndpoint.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ExternalListenerIpcEndpoint.
        The unique name of the service.


        :param key: The key of this ExternalListenerIpcEndpoint.
        :type: str
        """
        self._key = key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
