# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Node(object):
    """
    Network node
    """

    #: A constant which can be used with the type property of a Node.
    #: This constant has a value of "SOURCE"
    TYPE_SOURCE = "SOURCE"

    #: A constant which can be used with the type property of a Node.
    #: This constant has a value of "DESTINATION"
    TYPE_DESTINATION = "DESTINATION"

    #: A constant which can be used with the type property of a Node.
    #: This constant has a value of "ANONYMOUS"
    TYPE_ANONYMOUS = "ANONYMOUS"

    #: A constant which can be used with the type property of a Node.
    #: This constant has a value of "INTERNAL"
    TYPE_INTERNAL = "INTERNAL"

    #: A constant which can be used with the type property of a Node.
    #: This constant has a value of "DANGLING"
    TYPE_DANGLING = "DANGLING"

    def __init__(self, **kwargs):
        """
        Initializes a new Node object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Node.
        :type id: str

        :param ip_address:
            The value to assign to the ip_address property of this Node.
        :type ip_address: str

        :param display_name:
            The value to assign to the display_name property of this Node.
        :type display_name: str

        :param geo_info:
            The value to assign to the geo_info property of this Node.
        :type geo_info: str

        :param outgoing_links:
            The value to assign to the outgoing_links property of this Node.
        :type outgoing_links: list[str]

        :param consecutive_anonymous_count:
            The value to assign to the consecutive_anonymous_count property of this Node.
        :type consecutive_anonymous_count: int

        :param level:
            The value to assign to the level property of this Node.
        :type level: int

        :param avg_packet_response_time_in_ms:
            The value to assign to the avg_packet_response_time_in_ms property of this Node.
        :type avg_packet_response_time_in_ms: float

        :param avg_packet_loss_percent:
            The value to assign to the avg_packet_loss_percent property of this Node.
        :type avg_packet_loss_percent: float

        :param type:
            The value to assign to the type property of this Node.
            Allowed values for this property are: "SOURCE", "DESTINATION", "ANONYMOUS", "INTERNAL", "DANGLING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'id': 'str',
            'ip_address': 'str',
            'display_name': 'str',
            'geo_info': 'str',
            'outgoing_links': 'list[str]',
            'consecutive_anonymous_count': 'int',
            'level': 'int',
            'avg_packet_response_time_in_ms': 'float',
            'avg_packet_loss_percent': 'float',
            'type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'ip_address': 'ipAddress',
            'display_name': 'displayName',
            'geo_info': 'geoInfo',
            'outgoing_links': 'outgoingLinks',
            'consecutive_anonymous_count': 'consecutiveAnonymousCount',
            'level': 'level',
            'avg_packet_response_time_in_ms': 'avgPacketResponseTimeInMs',
            'avg_packet_loss_percent': 'avgPacketLossPercent',
            'type': 'type'
        }

        self._id = None
        self._ip_address = None
        self._display_name = None
        self._geo_info = None
        self._outgoing_links = None
        self._consecutive_anonymous_count = None
        self._level = None
        self._avg_packet_response_time_in_ms = None
        self._avg_packet_loss_percent = None
        self._type = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Node.
        id of node


        :return: The id of this Node.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Node.
        id of node


        :param id: The id of this Node.
        :type: str
        """
        self._id = id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Node.
        ip address of node


        :return: The ip_address of this Node.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Node.
        ip address of node


        :param ip_address: The ip_address of this Node.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def display_name(self):
        """
        Gets the display_name of this Node.
        display name of node


        :return: The display_name of this Node.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Node.
        display name of node


        :param display_name: The display_name of this Node.
        :type: str
        """
        self._display_name = display_name

    @property
    def geo_info(self):
        """
        Gets the geo_info of this Node.
        geo info


        :return: The geo_info of this Node.
        :rtype: str
        """
        return self._geo_info

    @geo_info.setter
    def geo_info(self, geo_info):
        """
        Sets the geo_info of this Node.
        geo info


        :param geo_info: The geo_info of this Node.
        :type: str
        """
        self._geo_info = geo_info

    @property
    def outgoing_links(self):
        """
        Gets the outgoing_links of this Node.
        links outgoing from this node


        :return: The outgoing_links of this Node.
        :rtype: list[str]
        """
        return self._outgoing_links

    @outgoing_links.setter
    def outgoing_links(self, outgoing_links):
        """
        Sets the outgoing_links of this Node.
        links outgoing from this node


        :param outgoing_links: The outgoing_links of this Node.
        :type: list[str]
        """
        self._outgoing_links = outgoing_links

    @property
    def consecutive_anonymous_count(self):
        """
        Gets the consecutive_anonymous_count of this Node.
        consecutive anonymous node count


        :return: The consecutive_anonymous_count of this Node.
        :rtype: int
        """
        return self._consecutive_anonymous_count

    @consecutive_anonymous_count.setter
    def consecutive_anonymous_count(self, consecutive_anonymous_count):
        """
        Sets the consecutive_anonymous_count of this Node.
        consecutive anonymous node count


        :param consecutive_anonymous_count: The consecutive_anonymous_count of this Node.
        :type: int
        """
        self._consecutive_anonymous_count = consecutive_anonymous_count

    @property
    def level(self):
        """
        Gets the level of this Node.
        level of this node


        :return: The level of this Node.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this Node.
        level of this node


        :param level: The level of this Node.
        :type: int
        """
        self._level = level

    @property
    def avg_packet_response_time_in_ms(self):
        """
        Gets the avg_packet_response_time_in_ms of this Node.
        average packet response time in milli seconds


        :return: The avg_packet_response_time_in_ms of this Node.
        :rtype: float
        """
        return self._avg_packet_response_time_in_ms

    @avg_packet_response_time_in_ms.setter
    def avg_packet_response_time_in_ms(self, avg_packet_response_time_in_ms):
        """
        Sets the avg_packet_response_time_in_ms of this Node.
        average packet response time in milli seconds


        :param avg_packet_response_time_in_ms: The avg_packet_response_time_in_ms of this Node.
        :type: float
        """
        self._avg_packet_response_time_in_ms = avg_packet_response_time_in_ms

    @property
    def avg_packet_loss_percent(self):
        """
        Gets the avg_packet_loss_percent of this Node.
        average packet loss percentage


        :return: The avg_packet_loss_percent of this Node.
        :rtype: float
        """
        return self._avg_packet_loss_percent

    @avg_packet_loss_percent.setter
    def avg_packet_loss_percent(self, avg_packet_loss_percent):
        """
        Sets the avg_packet_loss_percent of this Node.
        average packet loss percentage


        :param avg_packet_loss_percent: The avg_packet_loss_percent of this Node.
        :type: float
        """
        self._avg_packet_loss_percent = avg_packet_loss_percent

    @property
    def type(self):
        """
        Gets the type of this Node.
        type of node

        Allowed values for this property are: "SOURCE", "DESTINATION", "ANONYMOUS", "INTERNAL", "DANGLING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Node.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Node.
        type of node


        :param type: The type of this Node.
        :type: str
        """
        allowed_values = ["SOURCE", "DESTINATION", "ANONYMOUS", "INTERNAL", "DANGLING"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
