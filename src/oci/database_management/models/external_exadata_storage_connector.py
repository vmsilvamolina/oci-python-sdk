# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .dbm_resource import DbmResource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalExadataStorageConnector(DbmResource):
    """
    The details of the Exadata storage server connector.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalExadataStorageConnector object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalExadataStorageConnector.resource_type` attribute
        of this class is ``STORAGE_CONNECTOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalExadataStorageConnector.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalExadataStorageConnector.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ExternalExadataStorageConnector.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this ExternalExadataStorageConnector.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this ExternalExadataStorageConnector.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalExadataStorageConnector.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ExternalExadataStorageConnector.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalExadataStorageConnector.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalExadataStorageConnector.
        :type lifecycle_details: str

        :param additional_details:
            The value to assign to the additional_details property of this ExternalExadataStorageConnector.
        :type additional_details: dict(str, str)

        :param resource_type:
            The value to assign to the resource_type property of this ExternalExadataStorageConnector.
            Allowed values for this property are: "INFRASTRUCTURE_SUMMARY", "INFRASTRUCTURE", "STORAGE_SERVER_SUMMARY", "STORAGE_SERVER", "STORAGE_GRID_SUMMARY", "STORAGE_GRID", "STORAGE_CONNECTOR_SUMMARY", "STORAGE_CONNECTOR", "DATABASE_SYSTEM_SUMMARY", "DATABASE_SUMMARY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this ExternalExadataStorageConnector.
        :type exadata_infrastructure_id: str

        :param agent_id:
            The value to assign to the agent_id property of this ExternalExadataStorageConnector.
        :type agent_id: str

        :param connection_uri:
            The value to assign to the connection_uri property of this ExternalExadataStorageConnector.
        :type connection_uri: str

        :param storage_server_id:
            The value to assign to the storage_server_id property of this ExternalExadataStorageConnector.
        :type storage_server_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExternalExadataStorageConnector.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExternalExadataStorageConnector.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'version': 'str',
            'internal_id': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'additional_details': 'dict(str, str)',
            'resource_type': 'str',
            'exadata_infrastructure_id': 'str',
            'agent_id': 'str',
            'connection_uri': 'str',
            'storage_server_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'version': 'version',
            'internal_id': 'internalId',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'additional_details': 'additionalDetails',
            'resource_type': 'resourceType',
            'exadata_infrastructure_id': 'exadataInfrastructureId',
            'agent_id': 'agentId',
            'connection_uri': 'connectionUri',
            'storage_server_id': 'storageServerId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._version = None
        self._internal_id = None
        self._status = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_details = None
        self._additional_details = None
        self._resource_type = None
        self._exadata_infrastructure_id = None
        self._agent_id = None
        self._connection_uri = None
        self._storage_server_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._resource_type = 'STORAGE_CONNECTOR'

    @property
    def exadata_infrastructure_id(self):
        """
        Gets the exadata_infrastructure_id of this ExternalExadataStorageConnector.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this ExternalExadataStorageConnector.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this ExternalExadataStorageConnector.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this ExternalExadataStorageConnector.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    @property
    def agent_id(self):
        """
        Gets the agent_id of this ExternalExadataStorageConnector.
        The `OCID`__ of the agent for the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this ExternalExadataStorageConnector.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this ExternalExadataStorageConnector.
        The `OCID`__ of the agent for the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this ExternalExadataStorageConnector.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def connection_uri(self):
        """
        Gets the connection_uri of this ExternalExadataStorageConnector.
        The unique string of the connection. For example, \"https://<storage-server-name>/MS/RESTService/\".


        :return: The connection_uri of this ExternalExadataStorageConnector.
        :rtype: str
        """
        return self._connection_uri

    @connection_uri.setter
    def connection_uri(self, connection_uri):
        """
        Sets the connection_uri of this ExternalExadataStorageConnector.
        The unique string of the connection. For example, \"https://<storage-server-name>/MS/RESTService/\".


        :param connection_uri: The connection_uri of this ExternalExadataStorageConnector.
        :type: str
        """
        self._connection_uri = connection_uri

    @property
    def storage_server_id(self):
        """
        Gets the storage_server_id of this ExternalExadataStorageConnector.
        The `OCID`__ of the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The storage_server_id of this ExternalExadataStorageConnector.
        :rtype: str
        """
        return self._storage_server_id

    @storage_server_id.setter
    def storage_server_id(self, storage_server_id):
        """
        Sets the storage_server_id of this ExternalExadataStorageConnector.
        The `OCID`__ of the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param storage_server_id: The storage_server_id of this ExternalExadataStorageConnector.
        :type: str
        """
        self._storage_server_id = storage_server_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExternalExadataStorageConnector.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExternalExadataStorageConnector.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExternalExadataStorageConnector.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExternalExadataStorageConnector.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExternalExadataStorageConnector.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExternalExadataStorageConnector.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExternalExadataStorageConnector.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExternalExadataStorageConnector.
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
