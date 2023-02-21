# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalClusterVipConfiguration(object):
    """
    The details of the Virtual IP (VIP) address for a node in an external cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalClusterVipConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param node_name:
            The value to assign to the node_name property of this ExternalClusterVipConfiguration.
        :type node_name: str

        :param address:
            The value to assign to the address property of this ExternalClusterVipConfiguration.
        :type address: str

        :param network_number:
            The value to assign to the network_number property of this ExternalClusterVipConfiguration.
        :type network_number: int

        """
        self.swagger_types = {
            'node_name': 'str',
            'address': 'str',
            'network_number': 'int'
        }

        self.attribute_map = {
            'node_name': 'nodeName',
            'address': 'address',
            'network_number': 'networkNumber'
        }

        self._node_name = None
        self._address = None
        self._network_number = None

    @property
    def node_name(self):
        """
        Gets the node_name of this ExternalClusterVipConfiguration.
        The name of the node with the VIP.


        :return: The node_name of this ExternalClusterVipConfiguration.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this ExternalClusterVipConfiguration.
        The name of the node with the VIP.


        :param node_name: The node_name of this ExternalClusterVipConfiguration.
        :type: str
        """
        self._node_name = node_name

    @property
    def address(self):
        """
        Gets the address of this ExternalClusterVipConfiguration.
        The VIP name or IP address.


        :return: The address of this ExternalClusterVipConfiguration.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ExternalClusterVipConfiguration.
        The VIP name or IP address.


        :param address: The address of this ExternalClusterVipConfiguration.
        :type: str
        """
        self._address = address

    @property
    def network_number(self):
        """
        Gets the network_number of this ExternalClusterVipConfiguration.
        The network number from which VIPs are obtained.


        :return: The network_number of this ExternalClusterVipConfiguration.
        :rtype: int
        """
        return self._network_number

    @network_number.setter
    def network_number(self, network_number):
        """
        Sets the network_number of this ExternalClusterVipConfiguration.
        The network number from which VIPs are obtained.


        :param network_number: The network_number of this ExternalClusterVipConfiguration.
        :type: int
        """
        self._network_number = network_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
