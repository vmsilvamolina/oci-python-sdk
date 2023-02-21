# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .discovered_external_db_system_component import DiscoveredExternalDbSystemComponent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveredExternalListener(DiscoveredExternalDbSystemComponent):
    """
    The details of an Oracle listener discovered in an external DB system discovery run.
    """

    #: A constant which can be used with the listener_type property of a DiscoveredExternalListener.
    #: This constant has a value of "ASM"
    LISTENER_TYPE_ASM = "ASM"

    #: A constant which can be used with the listener_type property of a DiscoveredExternalListener.
    #: This constant has a value of "LOCAL"
    LISTENER_TYPE_LOCAL = "LOCAL"

    #: A constant which can be used with the listener_type property of a DiscoveredExternalListener.
    #: This constant has a value of "SCAN"
    LISTENER_TYPE_SCAN = "SCAN"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveredExternalListener object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.DiscoveredExternalListener.component_type` attribute
        of this class is ``LISTENER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param component_id:
            The value to assign to the component_id property of this DiscoveredExternalListener.
        :type component_id: str

        :param display_name:
            The value to assign to the display_name property of this DiscoveredExternalListener.
        :type display_name: str

        :param component_name:
            The value to assign to the component_name property of this DiscoveredExternalListener.
        :type component_name: str

        :param component_type:
            The value to assign to the component_type property of this DiscoveredExternalListener.
            Allowed values for this property are: "ASM", "ASM_INSTANCE", "CLUSTER", "CLUSTER_INSTANCE", "DATABASE", "DATABASE_INSTANCE", "DATABASE_HOME", "DATABASE_NODE", "DBSYSTEM", "LISTENER", "PLUGGABLE_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type component_type: str

        :param resource_id:
            The value to assign to the resource_id property of this DiscoveredExternalListener.
        :type resource_id: str

        :param is_selected_for_monitoring:
            The value to assign to the is_selected_for_monitoring property of this DiscoveredExternalListener.
        :type is_selected_for_monitoring: bool

        :param status:
            The value to assign to the status property of this DiscoveredExternalListener.
            Allowed values for this property are: "NEW", "EXISTING", "MARKED_FOR_DELETION", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param associated_components:
            The value to assign to the associated_components property of this DiscoveredExternalListener.
        :type associated_components: list[oci.database_management.models.AssociatedComponent]

        :param db_node_name:
            The value to assign to the db_node_name property of this DiscoveredExternalListener.
        :type db_node_name: str

        :param oracle_home:
            The value to assign to the oracle_home property of this DiscoveredExternalListener.
        :type oracle_home: str

        :param listener_alias:
            The value to assign to the listener_alias property of this DiscoveredExternalListener.
        :type listener_alias: str

        :param adr_home_directory:
            The value to assign to the adr_home_directory property of this DiscoveredExternalListener.
        :type adr_home_directory: str

        :param log_directory:
            The value to assign to the log_directory property of this DiscoveredExternalListener.
        :type log_directory: str

        :param trace_directory:
            The value to assign to the trace_directory property of this DiscoveredExternalListener.
        :type trace_directory: str

        :param version:
            The value to assign to the version property of this DiscoveredExternalListener.
        :type version: str

        :param listener_type:
            The value to assign to the listener_type property of this DiscoveredExternalListener.
            Allowed values for this property are: "ASM", "LOCAL", "SCAN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type listener_type: str

        :param host_name:
            The value to assign to the host_name property of this DiscoveredExternalListener.
        :type host_name: str

        :param endpoints:
            The value to assign to the endpoints property of this DiscoveredExternalListener.
        :type endpoints: list[oci.database_management.models.ExternalListenerEndpoint]

        :param connector:
            The value to assign to the connector property of this DiscoveredExternalListener.
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
            'db_node_name': 'str',
            'oracle_home': 'str',
            'listener_alias': 'str',
            'adr_home_directory': 'str',
            'log_directory': 'str',
            'trace_directory': 'str',
            'version': 'str',
            'listener_type': 'str',
            'host_name': 'str',
            'endpoints': 'list[ExternalListenerEndpoint]',
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
            'db_node_name': 'dbNodeName',
            'oracle_home': 'oracleHome',
            'listener_alias': 'listenerAlias',
            'adr_home_directory': 'adrHomeDirectory',
            'log_directory': 'logDirectory',
            'trace_directory': 'traceDirectory',
            'version': 'version',
            'listener_type': 'listenerType',
            'host_name': 'hostName',
            'endpoints': 'endpoints',
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
        self._db_node_name = None
        self._oracle_home = None
        self._listener_alias = None
        self._adr_home_directory = None
        self._log_directory = None
        self._trace_directory = None
        self._version = None
        self._listener_type = None
        self._host_name = None
        self._endpoints = None
        self._connector = None
        self._component_type = 'LISTENER'

    @property
    def db_node_name(self):
        """
        Gets the db_node_name of this DiscoveredExternalListener.
        The name of the DB node.


        :return: The db_node_name of this DiscoveredExternalListener.
        :rtype: str
        """
        return self._db_node_name

    @db_node_name.setter
    def db_node_name(self, db_node_name):
        """
        Sets the db_node_name of this DiscoveredExternalListener.
        The name of the DB node.


        :param db_node_name: The db_node_name of this DiscoveredExternalListener.
        :type: str
        """
        self._db_node_name = db_node_name

    @property
    def oracle_home(self):
        """
        Gets the oracle_home of this DiscoveredExternalListener.
        The Oracle home location of the listener.


        :return: The oracle_home of this DiscoveredExternalListener.
        :rtype: str
        """
        return self._oracle_home

    @oracle_home.setter
    def oracle_home(self, oracle_home):
        """
        Sets the oracle_home of this DiscoveredExternalListener.
        The Oracle home location of the listener.


        :param oracle_home: The oracle_home of this DiscoveredExternalListener.
        :type: str
        """
        self._oracle_home = oracle_home

    @property
    def listener_alias(self):
        """
        Gets the listener_alias of this DiscoveredExternalListener.
        The listener alias.


        :return: The listener_alias of this DiscoveredExternalListener.
        :rtype: str
        """
        return self._listener_alias

    @listener_alias.setter
    def listener_alias(self, listener_alias):
        """
        Sets the listener_alias of this DiscoveredExternalListener.
        The listener alias.


        :param listener_alias: The listener_alias of this DiscoveredExternalListener.
        :type: str
        """
        self._listener_alias = listener_alias

    @property
    def adr_home_directory(self):
        """
        Gets the adr_home_directory of this DiscoveredExternalListener.
        The directory that stores tracing and logging incidents when Automatic Diagnostic Repository (ADR) is enabled.


        :return: The adr_home_directory of this DiscoveredExternalListener.
        :rtype: str
        """
        return self._adr_home_directory

    @adr_home_directory.setter
    def adr_home_directory(self, adr_home_directory):
        """
        Sets the adr_home_directory of this DiscoveredExternalListener.
        The directory that stores tracing and logging incidents when Automatic Diagnostic Repository (ADR) is enabled.


        :param adr_home_directory: The adr_home_directory of this DiscoveredExternalListener.
        :type: str
        """
        self._adr_home_directory = adr_home_directory

    @property
    def log_directory(self):
        """
        Gets the log_directory of this DiscoveredExternalListener.
        The destination directory of the listener log file.


        :return: The log_directory of this DiscoveredExternalListener.
        :rtype: str
        """
        return self._log_directory

    @log_directory.setter
    def log_directory(self, log_directory):
        """
        Sets the log_directory of this DiscoveredExternalListener.
        The destination directory of the listener log file.


        :param log_directory: The log_directory of this DiscoveredExternalListener.
        :type: str
        """
        self._log_directory = log_directory

    @property
    def trace_directory(self):
        """
        Gets the trace_directory of this DiscoveredExternalListener.
        The destination directory of the listener trace file.


        :return: The trace_directory of this DiscoveredExternalListener.
        :rtype: str
        """
        return self._trace_directory

    @trace_directory.setter
    def trace_directory(self, trace_directory):
        """
        Sets the trace_directory of this DiscoveredExternalListener.
        The destination directory of the listener trace file.


        :param trace_directory: The trace_directory of this DiscoveredExternalListener.
        :type: str
        """
        self._trace_directory = trace_directory

    @property
    def version(self):
        """
        Gets the version of this DiscoveredExternalListener.
        The listener version.


        :return: The version of this DiscoveredExternalListener.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DiscoveredExternalListener.
        The listener version.


        :param version: The version of this DiscoveredExternalListener.
        :type: str
        """
        self._version = version

    @property
    def listener_type(self):
        """
        Gets the listener_type of this DiscoveredExternalListener.
        The type of listener.

        Allowed values for this property are: "ASM", "LOCAL", "SCAN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The listener_type of this DiscoveredExternalListener.
        :rtype: str
        """
        return self._listener_type

    @listener_type.setter
    def listener_type(self, listener_type):
        """
        Sets the listener_type of this DiscoveredExternalListener.
        The type of listener.


        :param listener_type: The listener_type of this DiscoveredExternalListener.
        :type: str
        """
        allowed_values = ["ASM", "LOCAL", "SCAN"]
        if not value_allowed_none_or_none_sentinel(listener_type, allowed_values):
            listener_type = 'UNKNOWN_ENUM_VALUE'
        self._listener_type = listener_type

    @property
    def host_name(self):
        """
        Gets the host_name of this DiscoveredExternalListener.
        The name of the host on which the external listener is running.


        :return: The host_name of this DiscoveredExternalListener.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this DiscoveredExternalListener.
        The name of the host on which the external listener is running.


        :param host_name: The host_name of this DiscoveredExternalListener.
        :type: str
        """
        self._host_name = host_name

    @property
    def endpoints(self):
        """
        Gets the endpoints of this DiscoveredExternalListener.
        The list of protocol addresses the listener is configured to listen on.


        :return: The endpoints of this DiscoveredExternalListener.
        :rtype: list[oci.database_management.models.ExternalListenerEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this DiscoveredExternalListener.
        The list of protocol addresses the listener is configured to listen on.


        :param endpoints: The endpoints of this DiscoveredExternalListener.
        :type: list[oci.database_management.models.ExternalListenerEndpoint]
        """
        self._endpoints = endpoints

    @property
    def connector(self):
        """
        Gets the connector of this DiscoveredExternalListener.

        :return: The connector of this DiscoveredExternalListener.
        :rtype: oci.database_management.models.ExternalDbSystemDiscoveryConnector
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """
        Sets the connector of this DiscoveredExternalListener.

        :param connector: The connector of this DiscoveredExternalListener.
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
