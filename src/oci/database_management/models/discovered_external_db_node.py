# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .discovered_external_db_system_component import DiscoveredExternalDbSystemComponent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveredExternalDbNode(DiscoveredExternalDbSystemComponent):
    """
    The details of an Oracle DB node discovered in an external DB system discovery run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveredExternalDbNode object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.DiscoveredExternalDbNode.component_type` attribute
        of this class is ``DATABASE_NODE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param component_id:
            The value to assign to the component_id property of this DiscoveredExternalDbNode.
        :type component_id: str

        :param display_name:
            The value to assign to the display_name property of this DiscoveredExternalDbNode.
        :type display_name: str

        :param component_name:
            The value to assign to the component_name property of this DiscoveredExternalDbNode.
        :type component_name: str

        :param component_type:
            The value to assign to the component_type property of this DiscoveredExternalDbNode.
            Allowed values for this property are: "ASM", "ASM_INSTANCE", "CLUSTER", "CLUSTER_INSTANCE", "DATABASE", "DATABASE_INSTANCE", "DATABASE_HOME", "DATABASE_NODE", "DBSYSTEM", "LISTENER", "PLUGGABLE_DATABASE"
        :type component_type: str

        :param resource_id:
            The value to assign to the resource_id property of this DiscoveredExternalDbNode.
        :type resource_id: str

        :param is_selected_for_monitoring:
            The value to assign to the is_selected_for_monitoring property of this DiscoveredExternalDbNode.
        :type is_selected_for_monitoring: bool

        :param status:
            The value to assign to the status property of this DiscoveredExternalDbNode.
            Allowed values for this property are: "NEW", "EXISTING", "MARKED_FOR_DELETION", "UNKNOWN"
        :type status: str

        :param associated_components:
            The value to assign to the associated_components property of this DiscoveredExternalDbNode.
        :type associated_components: list[oci.database_management.models.AssociatedComponent]

        :param host_name:
            The value to assign to the host_name property of this DiscoveredExternalDbNode.
        :type host_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this DiscoveredExternalDbNode.
        :type cpu_core_count: float

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this DiscoveredExternalDbNode.
        :type memory_size_in_gbs: float

        :param connector:
            The value to assign to the connector property of this DiscoveredExternalDbNode.
        :type connector: oci.database_management.models.ExternalDbSystemDiscoveryConnector

        """
        self.swagger_types = {
            'component_id': 'str',
            'display_name': 'str',
            'component_name': 'str',
            'component_type': 'str',
            'resource_id': 'str',
            'is_selected_for_monitoring': 'bool',
            'status': 'str',
            'associated_components': 'list[AssociatedComponent]',
            'host_name': 'str',
            'cpu_core_count': 'float',
            'memory_size_in_gbs': 'float',
            'connector': 'ExternalDbSystemDiscoveryConnector'
        }

        self.attribute_map = {
            'component_id': 'componentId',
            'display_name': 'displayName',
            'component_name': 'componentName',
            'component_type': 'componentType',
            'resource_id': 'resourceId',
            'is_selected_for_monitoring': 'isSelectedForMonitoring',
            'status': 'status',
            'associated_components': 'associatedComponents',
            'host_name': 'hostName',
            'cpu_core_count': 'cpuCoreCount',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'connector': 'connector'
        }

        self._component_id = None
        self._display_name = None
        self._component_name = None
        self._component_type = None
        self._resource_id = None
        self._is_selected_for_monitoring = None
        self._status = None
        self._associated_components = None
        self._host_name = None
        self._cpu_core_count = None
        self._memory_size_in_gbs = None
        self._connector = None
        self._component_type = 'DATABASE_NODE'

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this DiscoveredExternalDbNode.
        The name of the host on which the ASM instance is running.


        :return: The host_name of this DiscoveredExternalDbNode.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this DiscoveredExternalDbNode.
        The name of the host on which the ASM instance is running.


        :param host_name: The host_name of this DiscoveredExternalDbNode.
        :type: str
        """
        self._host_name = host_name

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this DiscoveredExternalDbNode.
        The number of CPU cores available on the DB node.


        :return: The cpu_core_count of this DiscoveredExternalDbNode.
        :rtype: float
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this DiscoveredExternalDbNode.
        The number of CPU cores available on the DB node.


        :param cpu_core_count: The cpu_core_count of this DiscoveredExternalDbNode.
        :type: float
        """
        self._cpu_core_count = cpu_core_count

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this DiscoveredExternalDbNode.
        The total memory in gigabytes (GB) on the DB node.


        :return: The memory_size_in_gbs of this DiscoveredExternalDbNode.
        :rtype: float
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this DiscoveredExternalDbNode.
        The total memory in gigabytes (GB) on the DB node.


        :param memory_size_in_gbs: The memory_size_in_gbs of this DiscoveredExternalDbNode.
        :type: float
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def connector(self):
        """
        Gets the connector of this DiscoveredExternalDbNode.

        :return: The connector of this DiscoveredExternalDbNode.
        :rtype: oci.database_management.models.ExternalDbSystemDiscoveryConnector
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """
        Sets the connector of this DiscoveredExternalDbNode.

        :param connector: The connector of this DiscoveredExternalDbNode.
        :type: oci.database_management.models.ExternalDbSystemDiscoveryConnector
        """
        self._connector = connector

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
