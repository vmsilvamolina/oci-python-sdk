# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedDatabaseSummary(object):
    """
    A summary of the Managed Database.
    """

    #: A constant which can be used with the database_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "CLOUD_SIDB"
    DATABASE_TYPE_CLOUD_SIDB = "CLOUD_SIDB"

    #: A constant which can be used with the database_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "CLOUD_RAC"
    DATABASE_TYPE_CLOUD_RAC = "CLOUD_RAC"

    #: A constant which can be used with the database_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "SHARED"
    DATABASE_TYPE_SHARED = "SHARED"

    #: A constant which can be used with the database_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "DEDICATED"
    DATABASE_TYPE_DEDICATED = "DEDICATED"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "ACD"
    DATABASE_SUB_TYPE_ACD = "ACD"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "ADB"
    DATABASE_SUB_TYPE_ADB = "ADB"

    #: A constant which can be used with the deployment_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "ONPREMISE"
    DEPLOYMENT_TYPE_ONPREMISE = "ONPREMISE"

    #: A constant which can be used with the deployment_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "BM"
    DEPLOYMENT_TYPE_BM = "BM"

    #: A constant which can be used with the deployment_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "VM"
    DEPLOYMENT_TYPE_VM = "VM"

    #: A constant which can be used with the deployment_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "EXADATA"
    DEPLOYMENT_TYPE_EXADATA = "EXADATA"

    #: A constant which can be used with the deployment_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "EXADATA_CC"
    DEPLOYMENT_TYPE_EXADATA_CC = "EXADATA_CC"

    #: A constant which can be used with the deployment_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "AUTONOMOUS"
    DEPLOYMENT_TYPE_AUTONOMOUS = "AUTONOMOUS"

    #: A constant which can be used with the management_option property of a ManagedDatabaseSummary.
    #: This constant has a value of "BASIC"
    MANAGEMENT_OPTION_BASIC = "BASIC"

    #: A constant which can be used with the management_option property of a ManagedDatabaseSummary.
    #: This constant has a value of "ADVANCED"
    MANAGEMENT_OPTION_ADVANCED = "ADVANCED"

    #: A constant which can be used with the workload_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "OLTP"
    WORKLOAD_TYPE_OLTP = "OLTP"

    #: A constant which can be used with the workload_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "DW"
    WORKLOAD_TYPE_DW = "DW"

    #: A constant which can be used with the workload_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "AJD"
    WORKLOAD_TYPE_AJD = "AJD"

    #: A constant which can be used with the workload_type property of a ManagedDatabaseSummary.
    #: This constant has a value of "APEX"
    WORKLOAD_TYPE_APEX = "APEX"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedDatabaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedDatabaseSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedDatabaseSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this ManagedDatabaseSummary.
        :type name: str

        :param database_type:
            The value to assign to the database_type property of this ManagedDatabaseSummary.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this ManagedDatabaseSummary.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param deployment_type:
            The value to assign to the deployment_type property of this ManagedDatabaseSummary.
            Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param management_option:
            The value to assign to the management_option property of this ManagedDatabaseSummary.
            Allowed values for this property are: "BASIC", "ADVANCED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type management_option: str

        :param workload_type:
            The value to assign to the workload_type property of this ManagedDatabaseSummary.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type workload_type: str

        :param is_cluster:
            The value to assign to the is_cluster property of this ManagedDatabaseSummary.
        :type is_cluster: bool

        :param parent_container_id:
            The value to assign to the parent_container_id property of this ManagedDatabaseSummary.
        :type parent_container_id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this ManagedDatabaseSummary.
        :type db_system_id: str

        :param storage_system_id:
            The value to assign to the storage_system_id property of this ManagedDatabaseSummary.
        :type storage_system_id: str

        :param time_created:
            The value to assign to the time_created property of this ManagedDatabaseSummary.
        :type time_created: datetime

        :param database_version:
            The value to assign to the database_version property of this ManagedDatabaseSummary.
        :type database_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagedDatabaseSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagedDatabaseSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'database_type': 'str',
            'database_sub_type': 'str',
            'deployment_type': 'str',
            'management_option': 'str',
            'workload_type': 'str',
            'is_cluster': 'bool',
            'parent_container_id': 'str',
            'db_system_id': 'str',
            'storage_system_id': 'str',
            'time_created': 'datetime',
            'database_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'deployment_type': 'deploymentType',
            'management_option': 'managementOption',
            'workload_type': 'workloadType',
            'is_cluster': 'isCluster',
            'parent_container_id': 'parentContainerId',
            'db_system_id': 'dbSystemId',
            'storage_system_id': 'storageSystemId',
            'time_created': 'timeCreated',
            'database_version': 'databaseVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._database_type = None
        self._database_sub_type = None
        self._deployment_type = None
        self._management_option = None
        self._workload_type = None
        self._is_cluster = None
        self._parent_container_id = None
        self._db_system_id = None
        self._storage_system_id = None
        self._time_created = None
        self._database_version = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedDatabaseSummary.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedDatabaseSummary.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ManagedDatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ManagedDatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedDatabaseSummary.
        The name of the Managed Database.


        :return: The name of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedDatabaseSummary.
        The name of the Managed Database.


        :param name: The name of this ManagedDatabaseSummary.
        :type: str
        """
        self._name = name

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this ManagedDatabaseSummary.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this ManagedDatabaseSummary.
        The type of Oracle Database installation.


        :param database_type: The database_type of this ManagedDatabaseSummary.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        **[Required]** Gets the database_sub_type of this ManagedDatabaseSummary.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this ManagedDatabaseSummary.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.


        :param database_sub_type: The database_sub_type of this ManagedDatabaseSummary.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB", "ACD", "ADB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def deployment_type(self):
        """
        Gets the deployment_type of this ManagedDatabaseSummary.
        The infrastructure used to deploy the Oracle Database.

        Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this ManagedDatabaseSummary.
        The infrastructure used to deploy the Oracle Database.


        :param deployment_type: The deployment_type of this ManagedDatabaseSummary.
        :type: str
        """
        allowed_values = ["ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def management_option(self):
        """
        Gets the management_option of this ManagedDatabaseSummary.
        The management option used when enabling Database Management.

        Allowed values for this property are: "BASIC", "ADVANCED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The management_option of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._management_option

    @management_option.setter
    def management_option(self, management_option):
        """
        Sets the management_option of this ManagedDatabaseSummary.
        The management option used when enabling Database Management.


        :param management_option: The management_option of this ManagedDatabaseSummary.
        :type: str
        """
        allowed_values = ["BASIC", "ADVANCED"]
        if not value_allowed_none_or_none_sentinel(management_option, allowed_values):
            management_option = 'UNKNOWN_ENUM_VALUE'
        self._management_option = management_option

    @property
    def workload_type(self):
        """
        Gets the workload_type of this ManagedDatabaseSummary.
        The workload type of the Autonomous Database.

        Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The workload_type of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """
        Sets the workload_type of this ManagedDatabaseSummary.
        The workload type of the Autonomous Database.


        :param workload_type: The workload_type of this ManagedDatabaseSummary.
        :type: str
        """
        allowed_values = ["OLTP", "DW", "AJD", "APEX"]
        if not value_allowed_none_or_none_sentinel(workload_type, allowed_values):
            workload_type = 'UNKNOWN_ENUM_VALUE'
        self._workload_type = workload_type

    @property
    def is_cluster(self):
        """
        **[Required]** Gets the is_cluster of this ManagedDatabaseSummary.
        Indicates whether the Oracle Database is part of a cluster.


        :return: The is_cluster of this ManagedDatabaseSummary.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this ManagedDatabaseSummary.
        Indicates whether the Oracle Database is part of a cluster.


        :param is_cluster: The is_cluster of this ManagedDatabaseSummary.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def parent_container_id(self):
        """
        Gets the parent_container_id of this ManagedDatabaseSummary.
        The `OCID`__ of the parent Container Database
        if the Managed Database is a Pluggable Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The parent_container_id of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._parent_container_id

    @parent_container_id.setter
    def parent_container_id(self, parent_container_id):
        """
        Sets the parent_container_id of this ManagedDatabaseSummary.
        The `OCID`__ of the parent Container Database
        if the Managed Database is a Pluggable Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param parent_container_id: The parent_container_id of this ManagedDatabaseSummary.
        :type: str
        """
        self._parent_container_id = parent_container_id

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this ManagedDatabaseSummary.
        The `OCID`__ of the external
        DB system that this Managed Database is part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_system_id of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this ManagedDatabaseSummary.
        The `OCID`__ of the external
        DB system that this Managed Database is part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_system_id: The db_system_id of this ManagedDatabaseSummary.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def storage_system_id(self):
        """
        Gets the storage_system_id of this ManagedDatabaseSummary.
        The `OCID`__ of the storage DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The storage_system_id of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._storage_system_id

    @storage_system_id.setter
    def storage_system_id(self, storage_system_id):
        """
        Sets the storage_system_id of this ManagedDatabaseSummary.
        The `OCID`__ of the storage DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param storage_system_id: The storage_system_id of this ManagedDatabaseSummary.
        :type: str
        """
        self._storage_system_id = storage_system_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ManagedDatabaseSummary.
        The date and time the Managed Database was created.


        :return: The time_created of this ManagedDatabaseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagedDatabaseSummary.
        The date and time the Managed Database was created.


        :param time_created: The time_created of this ManagedDatabaseSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def database_version(self):
        """
        Gets the database_version of this ManagedDatabaseSummary.
        The Oracle Database version.


        :return: The database_version of this ManagedDatabaseSummary.
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """
        Sets the database_version of this ManagedDatabaseSummary.
        The Oracle Database version.


        :param database_version: The database_version of this ManagedDatabaseSummary.
        :type: str
        """
        self._database_version = database_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ManagedDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ManagedDatabaseSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagedDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ManagedDatabaseSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ManagedDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ManagedDatabaseSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagedDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ManagedDatabaseSummary.
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
