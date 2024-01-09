# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220315


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRedisClusterDetails(object):
    """
    The configuration details for a new Redis cluster. A Redis cluster is a memory-based storage solution. For more information, see `OCI Caching Service with Redis`__.

    __ https://docs.cloud.oracle.com/iaas/Content/redis/home.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRedisClusterDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateRedisClusterDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRedisClusterDetails.
        :type compartment_id: str

        :param node_count:
            The value to assign to the node_count property of this CreateRedisClusterDetails.
        :type node_count: int

        :param software_version:
            The value to assign to the software_version property of this CreateRedisClusterDetails.
        :type software_version: str

        :param node_memory_in_gbs:
            The value to assign to the node_memory_in_gbs property of this CreateRedisClusterDetails.
        :type node_memory_in_gbs: float

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateRedisClusterDetails.
        :type subnet_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRedisClusterDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRedisClusterDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'node_count': 'int',
            'software_version': 'str',
            'node_memory_in_gbs': 'float',
            'subnet_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'node_count': 'nodeCount',
            'software_version': 'softwareVersion',
            'node_memory_in_gbs': 'nodeMemoryInGBs',
            'subnet_id': 'subnetId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._node_count = None
        self._software_version = None
        self._node_memory_in_gbs = None
        self._subnet_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateRedisClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateRedisClusterDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRedisClusterDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateRedisClusterDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRedisClusterDetails.
        The `OCID`__ of the compartment that contains the Redis cluster.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :return: The compartment_id of this CreateRedisClusterDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRedisClusterDetails.
        The `OCID`__ of the compartment that contains the Redis cluster.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :param compartment_id: The compartment_id of this CreateRedisClusterDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def node_count(self):
        """
        **[Required]** Gets the node_count of this CreateRedisClusterDetails.
        The number of nodes in the Redis cluster.


        :return: The node_count of this CreateRedisClusterDetails.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this CreateRedisClusterDetails.
        The number of nodes in the Redis cluster.


        :param node_count: The node_count of this CreateRedisClusterDetails.
        :type: int
        """
        self._node_count = node_count

    @property
    def software_version(self):
        """
        **[Required]** Gets the software_version of this CreateRedisClusterDetails.
        The Redis version that the cluster is running.


        :return: The software_version of this CreateRedisClusterDetails.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """
        Sets the software_version of this CreateRedisClusterDetails.
        The Redis version that the cluster is running.


        :param software_version: The software_version of this CreateRedisClusterDetails.
        :type: str
        """
        self._software_version = software_version

    @property
    def node_memory_in_gbs(self):
        """
        **[Required]** Gets the node_memory_in_gbs of this CreateRedisClusterDetails.
        The amount of memory allocated to the Redis cluster's nodes, in gigabytes.


        :return: The node_memory_in_gbs of this CreateRedisClusterDetails.
        :rtype: float
        """
        return self._node_memory_in_gbs

    @node_memory_in_gbs.setter
    def node_memory_in_gbs(self, node_memory_in_gbs):
        """
        Sets the node_memory_in_gbs of this CreateRedisClusterDetails.
        The amount of memory allocated to the Redis cluster's nodes, in gigabytes.


        :param node_memory_in_gbs: The node_memory_in_gbs of this CreateRedisClusterDetails.
        :type: float
        """
        self._node_memory_in_gbs = node_memory_in_gbs

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateRedisClusterDetails.
        The `OCID`__ of the Redis cluster's subnet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :return: The subnet_id of this CreateRedisClusterDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateRedisClusterDetails.
        The `OCID`__ of the Redis cluster's subnet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle


        :param subnet_id: The subnet_id of this CreateRedisClusterDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRedisClusterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateRedisClusterDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRedisClusterDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateRedisClusterDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRedisClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateRedisClusterDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRedisClusterDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateRedisClusterDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
