# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .external_db_system_connector import ExternalDbSystemConnector
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDbSystemMacsConnector(ExternalDbSystemConnector):
    """
    The details of an external DB system connector that uses the
    `Management Agent Cloud Service (MACS)`__
    to connect to an external DB system component.

    __ https://docs.cloud.oracle.com/iaas/management-agents/index.html
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDbSystemMacsConnector object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalDbSystemMacsConnector.connector_type` attribute
        of this class is ``MACS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connector_type:
            The value to assign to the connector_type property of this ExternalDbSystemMacsConnector.
            Allowed values for this property are: "MACS"
        :type connector_type: str

        :param id:
            The value to assign to the id property of this ExternalDbSystemMacsConnector.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalDbSystemMacsConnector.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalDbSystemMacsConnector.
        :type compartment_id: str

        :param external_db_system_id:
            The value to assign to the external_db_system_id property of this ExternalDbSystemMacsConnector.
        :type external_db_system_id: str

        :param connection_status:
            The value to assign to the connection_status property of this ExternalDbSystemMacsConnector.
        :type connection_status: str

        :param connection_failure_message:
            The value to assign to the connection_failure_message property of this ExternalDbSystemMacsConnector.
        :type connection_failure_message: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalDbSystemMacsConnector.
            Allowed values for this property are: "CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalDbSystemMacsConnector.
        :type lifecycle_details: str

        :param time_connection_status_last_updated:
            The value to assign to the time_connection_status_last_updated property of this ExternalDbSystemMacsConnector.
        :type time_connection_status_last_updated: datetime

        :param time_created:
            The value to assign to the time_created property of this ExternalDbSystemMacsConnector.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalDbSystemMacsConnector.
        :type time_updated: datetime

        :param agent_id:
            The value to assign to the agent_id property of this ExternalDbSystemMacsConnector.
        :type agent_id: str

        :param connection_info:
            The value to assign to the connection_info property of this ExternalDbSystemMacsConnector.
        :type connection_info: oci.database_management.models.ExternalDbSystemConnectionInfo

        """
        self.swagger_types = {
            'connector_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'external_db_system_id': 'str',
            'connection_status': 'str',
            'connection_failure_message': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_connection_status_last_updated': 'datetime',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'agent_id': 'str',
            'connection_info': 'ExternalDbSystemConnectionInfo'
        }

        self.attribute_map = {
            'connector_type': 'connectorType',
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'external_db_system_id': 'externalDbSystemId',
            'connection_status': 'connectionStatus',
            'connection_failure_message': 'connectionFailureMessage',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_connection_status_last_updated': 'timeConnectionStatusLastUpdated',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'agent_id': 'agentId',
            'connection_info': 'connectionInfo'
        }

        self._connector_type = None
        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._external_db_system_id = None
        self._connection_status = None
        self._connection_failure_message = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_connection_status_last_updated = None
        self._time_created = None
        self._time_updated = None
        self._agent_id = None
        self._connection_info = None
        self._connector_type = 'MACS'

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this ExternalDbSystemMacsConnector.
        The `OCID`__ of the management agent
        used for the external DB system connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this ExternalDbSystemMacsConnector.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this ExternalDbSystemMacsConnector.
        The `OCID`__ of the management agent
        used for the external DB system connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this ExternalDbSystemMacsConnector.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def connection_info(self):
        """
        Gets the connection_info of this ExternalDbSystemMacsConnector.

        :return: The connection_info of this ExternalDbSystemMacsConnector.
        :rtype: oci.database_management.models.ExternalDbSystemConnectionInfo
        """
        return self._connection_info

    @connection_info.setter
    def connection_info(self, connection_info):
        """
        Sets the connection_info of this ExternalDbSystemMacsConnector.

        :param connection_info: The connection_info of this ExternalDbSystemMacsConnector.
        :type: oci.database_management.models.ExternalDbSystemConnectionInfo
        """
        self._connection_info = connection_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
