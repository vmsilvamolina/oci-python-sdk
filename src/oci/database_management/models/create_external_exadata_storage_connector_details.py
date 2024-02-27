# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateExternalExadataStorageConnectorDetails(object):
    """
    The details required to create the connector to the Exadata storage server.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateExternalExadataStorageConnectorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param storage_server_id:
            The value to assign to the storage_server_id property of this CreateExternalExadataStorageConnectorDetails.
        :type storage_server_id: str

        :param agent_id:
            The value to assign to the agent_id property of this CreateExternalExadataStorageConnectorDetails.
        :type agent_id: str

        :param connector_name:
            The value to assign to the connector_name property of this CreateExternalExadataStorageConnectorDetails.
        :type connector_name: str

        :param connection_uri:
            The value to assign to the connection_uri property of this CreateExternalExadataStorageConnectorDetails.
        :type connection_uri: str

        :param credential_info:
            The value to assign to the credential_info property of this CreateExternalExadataStorageConnectorDetails.
        :type credential_info: oci.database_management.models.RestCredential

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateExternalExadataStorageConnectorDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateExternalExadataStorageConnectorDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'storage_server_id': 'str',
            'agent_id': 'str',
            'connector_name': 'str',
            'connection_uri': 'str',
            'credential_info': 'RestCredential',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'storage_server_id': 'storageServerId',
            'agent_id': 'agentId',
            'connector_name': 'connectorName',
            'connection_uri': 'connectionUri',
            'credential_info': 'credentialInfo',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._storage_server_id = None
        self._agent_id = None
        self._connector_name = None
        self._connection_uri = None
        self._credential_info = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def storage_server_id(self):
        """
        **[Required]** Gets the storage_server_id of this CreateExternalExadataStorageConnectorDetails.
        The `OCID`__ of the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The storage_server_id of this CreateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._storage_server_id

    @storage_server_id.setter
    def storage_server_id(self, storage_server_id):
        """
        Sets the storage_server_id of this CreateExternalExadataStorageConnectorDetails.
        The `OCID`__ of the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param storage_server_id: The storage_server_id of this CreateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._storage_server_id = storage_server_id

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this CreateExternalExadataStorageConnectorDetails.
        The `OCID`__ of the agent for the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this CreateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this CreateExternalExadataStorageConnectorDetails.
        The `OCID`__ of the agent for the Exadata storage server.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this CreateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def connector_name(self):
        """
        **[Required]** Gets the connector_name of this CreateExternalExadataStorageConnectorDetails.
        The name of the Exadata storage server connector.


        :return: The connector_name of this CreateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """
        Sets the connector_name of this CreateExternalExadataStorageConnectorDetails.
        The name of the Exadata storage server connector.


        :param connector_name: The connector_name of this CreateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._connector_name = connector_name

    @property
    def connection_uri(self):
        """
        **[Required]** Gets the connection_uri of this CreateExternalExadataStorageConnectorDetails.
        The unique string of the connection. For example, \"https://<storage-server-name>/MS/RESTService/\".


        :return: The connection_uri of this CreateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._connection_uri

    @connection_uri.setter
    def connection_uri(self, connection_uri):
        """
        Sets the connection_uri of this CreateExternalExadataStorageConnectorDetails.
        The unique string of the connection. For example, \"https://<storage-server-name>/MS/RESTService/\".


        :param connection_uri: The connection_uri of this CreateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._connection_uri = connection_uri

    @property
    def credential_info(self):
        """
        **[Required]** Gets the credential_info of this CreateExternalExadataStorageConnectorDetails.

        :return: The credential_info of this CreateExternalExadataStorageConnectorDetails.
        :rtype: oci.database_management.models.RestCredential
        """
        return self._credential_info

    @credential_info.setter
    def credential_info(self, credential_info):
        """
        Sets the credential_info of this CreateExternalExadataStorageConnectorDetails.

        :param credential_info: The credential_info of this CreateExternalExadataStorageConnectorDetails.
        :type: oci.database_management.models.RestCredential
        """
        self._credential_info = credential_info

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateExternalExadataStorageConnectorDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateExternalExadataStorageConnectorDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateExternalExadataStorageConnectorDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateExternalExadataStorageConnectorDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateExternalExadataStorageConnectorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateExternalExadataStorageConnectorDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateExternalExadataStorageConnectorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateExternalExadataStorageConnectorDetails.
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
