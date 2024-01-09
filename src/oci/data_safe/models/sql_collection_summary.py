# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlCollectionSummary(object):
    """
    The resource represents SQL collection for a specific database user in a target.
    SqlCollection encapsulates the SQL commands issued in the user\u2019s database sessions, and its execution context.
    """

    #: A constant which can be used with the status property of a SqlCollectionSummary.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a SqlCollectionSummary.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the sql_level property of a SqlCollectionSummary.
    #: This constant has a value of "USER_ISSUED_SQL"
    SQL_LEVEL_USER_ISSUED_SQL = "USER_ISSUED_SQL"

    #: A constant which can be used with the sql_level property of a SqlCollectionSummary.
    #: This constant has a value of "ALL_SQL"
    SQL_LEVEL_ALL_SQL = "ALL_SQL"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionSummary.
    #: This constant has a value of "COLLECTING"
    LIFECYCLE_STATE_COLLECTING = "COLLECTING"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionSummary.
    #: This constant has a value of "COMPLETED"
    LIFECYCLE_STATE_COMPLETED = "COMPLETED"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SqlCollectionSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlCollectionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SqlCollectionSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SqlCollectionSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SqlCollectionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SqlCollectionSummary.
        :type description: str

        :param target_id:
            The value to assign to the target_id property of this SqlCollectionSummary.
        :type target_id: str

        :param status:
            The value to assign to the status property of this SqlCollectionSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param db_user_name:
            The value to assign to the db_user_name property of this SqlCollectionSummary.
        :type db_user_name: str

        :param time_last_started:
            The value to assign to the time_last_started property of this SqlCollectionSummary.
        :type time_last_started: datetime

        :param time_last_stopped:
            The value to assign to the time_last_stopped property of this SqlCollectionSummary.
        :type time_last_stopped: datetime

        :param sql_level:
            The value to assign to the sql_level property of this SqlCollectionSummary.
            Allowed values for this property are: "USER_ISSUED_SQL", "ALL_SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type sql_level: str

        :param time_created:
            The value to assign to the time_created property of this SqlCollectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SqlCollectionSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SqlCollectionSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "COLLECTING", "COMPLETED", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this SqlCollectionSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SqlCollectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SqlCollectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'target_id': 'str',
            'status': 'str',
            'db_user_name': 'str',
            'time_last_started': 'datetime',
            'time_last_stopped': 'datetime',
            'sql_level': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'target_id': 'targetId',
            'status': 'status',
            'db_user_name': 'dbUserName',
            'time_last_started': 'timeLastStarted',
            'time_last_stopped': 'timeLastStopped',
            'sql_level': 'sqlLevel',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._target_id = None
        self._status = None
        self._db_user_name = None
        self._time_last_started = None
        self._time_last_stopped = None
        self._sql_level = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SqlCollectionSummary.
        The OCID of the SQL collection.


        :return: The id of this SqlCollectionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SqlCollectionSummary.
        The OCID of the SQL collection.


        :param id: The id of this SqlCollectionSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SqlCollectionSummary.
        The OCID of the compartment containing the SQL collection.


        :return: The compartment_id of this SqlCollectionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SqlCollectionSummary.
        The OCID of the compartment containing the SQL collection.


        :param compartment_id: The compartment_id of this SqlCollectionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SqlCollectionSummary.
        The display name of the SQL collection.


        :return: The display_name of this SqlCollectionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SqlCollectionSummary.
        The display name of the SQL collection.


        :param display_name: The display_name of this SqlCollectionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SqlCollectionSummary.
        The description of the SQL collection.


        :return: The description of this SqlCollectionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SqlCollectionSummary.
        The description of the SQL collection.


        :param description: The description of this SqlCollectionSummary.
        :type: str
        """
        self._description = description

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this SqlCollectionSummary.
        The OCID of the target corresponding to the security policy deployment.


        :return: The target_id of this SqlCollectionSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this SqlCollectionSummary.
        The OCID of the target corresponding to the security policy deployment.


        :param target_id: The target_id of this SqlCollectionSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this SqlCollectionSummary.
        Specifies if the status of the SqlCollection. Enabled indicates that the collecting is in progress.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SqlCollectionSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SqlCollectionSummary.
        Specifies if the status of the SqlCollection. Enabled indicates that the collecting is in progress.


        :param status: The status of this SqlCollectionSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def db_user_name(self):
        """
        **[Required]** Gets the db_user_name of this SqlCollectionSummary.
        The database user name.


        :return: The db_user_name of this SqlCollectionSummary.
        :rtype: str
        """
        return self._db_user_name

    @db_user_name.setter
    def db_user_name(self, db_user_name):
        """
        Sets the db_user_name of this SqlCollectionSummary.
        The database user name.


        :param db_user_name: The db_user_name of this SqlCollectionSummary.
        :type: str
        """
        self._db_user_name = db_user_name

    @property
    def time_last_started(self):
        """
        Gets the time_last_started of this SqlCollectionSummary.
        The timestamp of the most recent SqlCollection start operation, in the format defined by RFC3339.


        :return: The time_last_started of this SqlCollectionSummary.
        :rtype: datetime
        """
        return self._time_last_started

    @time_last_started.setter
    def time_last_started(self, time_last_started):
        """
        Sets the time_last_started of this SqlCollectionSummary.
        The timestamp of the most recent SqlCollection start operation, in the format defined by RFC3339.


        :param time_last_started: The time_last_started of this SqlCollectionSummary.
        :type: datetime
        """
        self._time_last_started = time_last_started

    @property
    def time_last_stopped(self):
        """
        Gets the time_last_stopped of this SqlCollectionSummary.
        The timestamp of the most recent SqlCollection stop operation, in the format defined by RFC3339.


        :return: The time_last_stopped of this SqlCollectionSummary.
        :rtype: datetime
        """
        return self._time_last_stopped

    @time_last_stopped.setter
    def time_last_stopped(self, time_last_stopped):
        """
        Sets the time_last_stopped of this SqlCollectionSummary.
        The timestamp of the most recent SqlCollection stop operation, in the format defined by RFC3339.


        :param time_last_stopped: The time_last_stopped of this SqlCollectionSummary.
        :type: datetime
        """
        self._time_last_stopped = time_last_stopped

    @property
    def sql_level(self):
        """
        Gets the sql_level of this SqlCollectionSummary.
        Specifies the level of SQL that will be collected.
        USER_ISSUED_SQL - User issued SQL statements only.
        ALL_SQL - Includes all SQL statements including SQL statement issued inside PL/SQL units.

        Allowed values for this property are: "USER_ISSUED_SQL", "ALL_SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The sql_level of this SqlCollectionSummary.
        :rtype: str
        """
        return self._sql_level

    @sql_level.setter
    def sql_level(self, sql_level):
        """
        Sets the sql_level of this SqlCollectionSummary.
        Specifies the level of SQL that will be collected.
        USER_ISSUED_SQL - User issued SQL statements only.
        ALL_SQL - Includes all SQL statements including SQL statement issued inside PL/SQL units.


        :param sql_level: The sql_level of this SqlCollectionSummary.
        :type: str
        """
        allowed_values = ["USER_ISSUED_SQL", "ALL_SQL"]
        if not value_allowed_none_or_none_sentinel(sql_level, allowed_values):
            sql_level = 'UNKNOWN_ENUM_VALUE'
        self._sql_level = sql_level

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SqlCollectionSummary.
        The time that the SQL collection was created, in the format defined by RFC3339.


        :return: The time_created of this SqlCollectionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SqlCollectionSummary.
        The time that the SQL collection was created, in the format defined by RFC3339.


        :param time_created: The time_created of this SqlCollectionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SqlCollectionSummary.
        The last date and time the SQL collection was updated, in the format defined by RFC3339.


        :return: The time_updated of this SqlCollectionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SqlCollectionSummary.
        The last date and time the SQL collection was updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this SqlCollectionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SqlCollectionSummary.
        The current state of the SQL collection.

        Allowed values for this property are: "CREATING", "UPDATING", "COLLECTING", "COMPLETED", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SqlCollectionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SqlCollectionSummary.
        The current state of the SQL collection.


        :param lifecycle_state: The lifecycle_state of this SqlCollectionSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "COLLECTING", "COMPLETED", "INACTIVE", "FAILED", "DELETING", "DELETED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this SqlCollectionSummary.
        Details about the current state of the SQL collection in Data Safe.


        :return: The lifecycle_details of this SqlCollectionSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this SqlCollectionSummary.
        Details about the current state of the SQL collection in Data Safe.


        :param lifecycle_details: The lifecycle_details of this SqlCollectionSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SqlCollectionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SqlCollectionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SqlCollectionSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SqlCollectionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SqlCollectionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SqlCollectionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SqlCollectionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SqlCollectionSummary.
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
