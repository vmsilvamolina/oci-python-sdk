# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101

from .discovered_external_db_system_component import DiscoveredExternalDbSystemComponent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveredExternalDatabase(DiscoveredExternalDbSystemComponent):
    """
    The details of an external Oracle Database discovered in an external DB system discovery run.
    """

    #: A constant which can be used with the db_type property of a DiscoveredExternalDatabase.
    #: This constant has a value of "CDB"
    DB_TYPE_CDB = "CDB"

    #: A constant which can be used with the db_type property of a DiscoveredExternalDatabase.
    #: This constant has a value of "PDB"
    DB_TYPE_PDB = "PDB"

    #: A constant which can be used with the db_type property of a DiscoveredExternalDatabase.
    #: This constant has a value of "NON_CDB"
    DB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the db_type property of a DiscoveredExternalDatabase.
    #: This constant has a value of "ACD"
    DB_TYPE_ACD = "ACD"

    #: A constant which can be used with the db_type property of a DiscoveredExternalDatabase.
    #: This constant has a value of "ADB"
    DB_TYPE_ADB = "ADB"

    #: A constant which can be used with the db_role property of a DiscoveredExternalDatabase.
    #: This constant has a value of "LOGICAL_STANDBY"
    DB_ROLE_LOGICAL_STANDBY = "LOGICAL_STANDBY"

    #: A constant which can be used with the db_role property of a DiscoveredExternalDatabase.
    #: This constant has a value of "PHYSICAL_STANDBY"
    DB_ROLE_PHYSICAL_STANDBY = "PHYSICAL_STANDBY"

    #: A constant which can be used with the db_role property of a DiscoveredExternalDatabase.
    #: This constant has a value of "SNAPSHOT_STANDBY"
    DB_ROLE_SNAPSHOT_STANDBY = "SNAPSHOT_STANDBY"

    #: A constant which can be used with the db_role property of a DiscoveredExternalDatabase.
    #: This constant has a value of "PRIMARY"
    DB_ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the db_role property of a DiscoveredExternalDatabase.
    #: This constant has a value of "FAR_SYNC"
    DB_ROLE_FAR_SYNC = "FAR_SYNC"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveredExternalDatabase object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.DiscoveredExternalDatabase.component_type` attribute
        of this class is ``DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param component_id:
            The value to assign to the component_id property of this DiscoveredExternalDatabase.
        :type component_id: str

        :param display_name:
            The value to assign to the display_name property of this DiscoveredExternalDatabase.
        :type display_name: str

        :param component_name:
            The value to assign to the component_name property of this DiscoveredExternalDatabase.
        :type component_name: str

        :param component_type:
            The value to assign to the component_type property of this DiscoveredExternalDatabase.
            Allowed values for this property are: "ASM", "ASM_INSTANCE", "CLUSTER", "CLUSTER_INSTANCE", "DATABASE", "DATABASE_INSTANCE", "DATABASE_HOME", "DATABASE_NODE", "DBSYSTEM", "LISTENER", "PLUGGABLE_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type component_type: str

        :param resource_id:
            The value to assign to the resource_id property of this DiscoveredExternalDatabase.
        :type resource_id: str

        :param is_selected_for_monitoring:
            The value to assign to the is_selected_for_monitoring property of this DiscoveredExternalDatabase.
        :type is_selected_for_monitoring: bool

        :param status:
            The value to assign to the status property of this DiscoveredExternalDatabase.
            Allowed values for this property are: "NEW", "EXISTING", "MARKED_FOR_DELETION", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param associated_components:
            The value to assign to the associated_components property of this DiscoveredExternalDatabase.
        :type associated_components: list[oci.database_management.models.AssociatedComponent]

        :param compartment_id:
            The value to assign to the compartment_id property of this DiscoveredExternalDatabase.
        :type compartment_id: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this DiscoveredExternalDatabase.
        :type db_unique_name: str

        :param db_type:
            The value to assign to the db_type property of this DiscoveredExternalDatabase.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_type: str

        :param is_cluster:
            The value to assign to the is_cluster property of this DiscoveredExternalDatabase.
        :type is_cluster: bool

        :param db_edition:
            The value to assign to the db_edition property of this DiscoveredExternalDatabase.
        :type db_edition: str

        :param db_id:
            The value to assign to the db_id property of this DiscoveredExternalDatabase.
        :type db_id: str

        :param db_packs:
            The value to assign to the db_packs property of this DiscoveredExternalDatabase.
        :type db_packs: str

        :param db_role:
            The value to assign to the db_role property of this DiscoveredExternalDatabase.
            Allowed values for this property are: "LOGICAL_STANDBY", "PHYSICAL_STANDBY", "SNAPSHOT_STANDBY", "PRIMARY", "FAR_SYNC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_role: str

        :param db_version:
            The value to assign to the db_version property of this DiscoveredExternalDatabase.
        :type db_version: str

        :param pluggable_databases:
            The value to assign to the pluggable_databases property of this DiscoveredExternalDatabase.
        :type pluggable_databases: list[oci.database_management.models.DiscoveredExternalPluggableDatabase]

        :param connector:
            The value to assign to the connector property of this DiscoveredExternalDatabase.
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
            'compartment_id': 'str',
            'db_unique_name': 'str',
            'db_type': 'str',
            'is_cluster': 'bool',
            'db_edition': 'str',
            'db_id': 'str',
            'db_packs': 'str',
            'db_role': 'str',
            'db_version': 'str',
            'pluggable_databases': 'list[DiscoveredExternalPluggableDatabase]',
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
            'compartment_id': 'compartmentId',
            'db_unique_name': 'dbUniqueName',
            'db_type': 'dbType',
            'is_cluster': 'isCluster',
            'db_edition': 'dbEdition',
            'db_id': 'dbId',
            'db_packs': 'dbPacks',
            'db_role': 'dbRole',
            'db_version': 'dbVersion',
            'pluggable_databases': 'pluggableDatabases',
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
        self._compartment_id = None
        self._db_unique_name = None
        self._db_type = None
        self._is_cluster = None
        self._db_edition = None
        self._db_id = None
        self._db_packs = None
        self._db_role = None
        self._db_version = None
        self._pluggable_databases = None
        self._connector = None
        self._component_type = 'DATABASE'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DiscoveredExternalDatabase.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DiscoveredExternalDatabase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DiscoveredExternalDatabase.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DiscoveredExternalDatabase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_unique_name(self):
        """
        **[Required]** Gets the db_unique_name of this DiscoveredExternalDatabase.
        The `DB_UNIQUE_NAME` of the external database.


        :return: The db_unique_name of this DiscoveredExternalDatabase.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this DiscoveredExternalDatabase.
        The `DB_UNIQUE_NAME` of the external database.


        :param db_unique_name: The db_unique_name of this DiscoveredExternalDatabase.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def db_type(self):
        """
        Gets the db_type of this DiscoveredExternalDatabase.
        The type of Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, or a Non-container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_type of this DiscoveredExternalDatabase.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """
        Sets the db_type of this DiscoveredExternalDatabase.
        The type of Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, or a Non-container Database.


        :param db_type: The db_type of this DiscoveredExternalDatabase.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB", "ACD", "ADB"]
        if not value_allowed_none_or_none_sentinel(db_type, allowed_values):
            db_type = 'UNKNOWN_ENUM_VALUE'
        self._db_type = db_type

    @property
    def is_cluster(self):
        """
        Gets the is_cluster of this DiscoveredExternalDatabase.
        Indicates whether the Oracle Database is part of a cluster.


        :return: The is_cluster of this DiscoveredExternalDatabase.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this DiscoveredExternalDatabase.
        Indicates whether the Oracle Database is part of a cluster.


        :param is_cluster: The is_cluster of this DiscoveredExternalDatabase.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def db_edition(self):
        """
        Gets the db_edition of this DiscoveredExternalDatabase.
        The Oracle Database edition.


        :return: The db_edition of this DiscoveredExternalDatabase.
        :rtype: str
        """
        return self._db_edition

    @db_edition.setter
    def db_edition(self, db_edition):
        """
        Sets the db_edition of this DiscoveredExternalDatabase.
        The Oracle Database edition.


        :param db_edition: The db_edition of this DiscoveredExternalDatabase.
        :type: str
        """
        self._db_edition = db_edition

    @property
    def db_id(self):
        """
        Gets the db_id of this DiscoveredExternalDatabase.
        The Oracle Database ID.


        :return: The db_id of this DiscoveredExternalDatabase.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        """
        Sets the db_id of this DiscoveredExternalDatabase.
        The Oracle Database ID.


        :param db_id: The db_id of this DiscoveredExternalDatabase.
        :type: str
        """
        self._db_id = db_id

    @property
    def db_packs(self):
        """
        Gets the db_packs of this DiscoveredExternalDatabase.
        The database packs licensed for the external Oracle Database.


        :return: The db_packs of this DiscoveredExternalDatabase.
        :rtype: str
        """
        return self._db_packs

    @db_packs.setter
    def db_packs(self, db_packs):
        """
        Sets the db_packs of this DiscoveredExternalDatabase.
        The database packs licensed for the external Oracle Database.


        :param db_packs: The db_packs of this DiscoveredExternalDatabase.
        :type: str
        """
        self._db_packs = db_packs

    @property
    def db_role(self):
        """
        Gets the db_role of this DiscoveredExternalDatabase.
        The role of the Oracle Database in Oracle Data Guard configuration.

        Allowed values for this property are: "LOGICAL_STANDBY", "PHYSICAL_STANDBY", "SNAPSHOT_STANDBY", "PRIMARY", "FAR_SYNC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_role of this DiscoveredExternalDatabase.
        :rtype: str
        """
        return self._db_role

    @db_role.setter
    def db_role(self, db_role):
        """
        Sets the db_role of this DiscoveredExternalDatabase.
        The role of the Oracle Database in Oracle Data Guard configuration.


        :param db_role: The db_role of this DiscoveredExternalDatabase.
        :type: str
        """
        allowed_values = ["LOGICAL_STANDBY", "PHYSICAL_STANDBY", "SNAPSHOT_STANDBY", "PRIMARY", "FAR_SYNC"]
        if not value_allowed_none_or_none_sentinel(db_role, allowed_values):
            db_role = 'UNKNOWN_ENUM_VALUE'
        self._db_role = db_role

    @property
    def db_version(self):
        """
        Gets the db_version of this DiscoveredExternalDatabase.
        The Oracle Database version.


        :return: The db_version of this DiscoveredExternalDatabase.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this DiscoveredExternalDatabase.
        The Oracle Database version.


        :param db_version: The db_version of this DiscoveredExternalDatabase.
        :type: str
        """
        self._db_version = db_version

    @property
    def pluggable_databases(self):
        """
        Gets the pluggable_databases of this DiscoveredExternalDatabase.
        The list of Pluggable Databases.


        :return: The pluggable_databases of this DiscoveredExternalDatabase.
        :rtype: list[oci.database_management.models.DiscoveredExternalPluggableDatabase]
        """
        return self._pluggable_databases

    @pluggable_databases.setter
    def pluggable_databases(self, pluggable_databases):
        """
        Sets the pluggable_databases of this DiscoveredExternalDatabase.
        The list of Pluggable Databases.


        :param pluggable_databases: The pluggable_databases of this DiscoveredExternalDatabase.
        :type: list[oci.database_management.models.DiscoveredExternalPluggableDatabase]
        """
        self._pluggable_databases = pluggable_databases

    @property
    def connector(self):
        """
        Gets the connector of this DiscoveredExternalDatabase.

        :return: The connector of this DiscoveredExternalDatabase.
        :rtype: oci.database_management.models.ExternalDbSystemDiscoveryConnector
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """
        Sets the connector of this DiscoveredExternalDatabase.

        :param connector: The connector of this DiscoveredExternalDatabase.
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
