# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetResponderRecipeResponderRule(object):
    """
    Details of ResponderRule.
    """

    #: A constant which can be used with the type property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "REMEDIATION"
    TYPE_REMEDIATION = "REMEDIATION"

    #: A constant which can be used with the type property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "NOTIFICATION"
    TYPE_NOTIFICATION = "NOTIFICATION"

    #: A constant which can be used with the supported_modes property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "AUTOACTION"
    SUPPORTED_MODES_AUTOACTION = "AUTOACTION"

    #: A constant which can be used with the supported_modes property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "USERACTION"
    SUPPORTED_MODES_USERACTION = "USERACTION"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TargetResponderRecipeResponderRule.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetResponderRecipeResponderRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param responder_rule_id:
            The value to assign to the responder_rule_id property of this TargetResponderRecipeResponderRule.
        :type responder_rule_id: str

        :param display_name:
            The value to assign to the display_name property of this TargetResponderRecipeResponderRule.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TargetResponderRecipeResponderRule.
        :type description: str

        :param type:
            The value to assign to the type property of this TargetResponderRecipeResponderRule.
            Allowed values for this property are: "REMEDIATION", "NOTIFICATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param policies:
            The value to assign to the policies property of this TargetResponderRecipeResponderRule.
        :type policies: list[str]

        :param supported_modes:
            The value to assign to the supported_modes property of this TargetResponderRecipeResponderRule.
            Allowed values for items in this list are: "AUTOACTION", "USERACTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type supported_modes: list[str]

        :param details:
            The value to assign to the details property of this TargetResponderRecipeResponderRule.
        :type details: oci.cloud_guard.models.ResponderRuleDetails

        :param compartment_id:
            The value to assign to the compartment_id property of this TargetResponderRecipeResponderRule.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this TargetResponderRecipeResponderRule.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TargetResponderRecipeResponderRule.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TargetResponderRecipeResponderRule.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TargetResponderRecipeResponderRule.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'responder_rule_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'type': 'str',
            'policies': 'list[str]',
            'supported_modes': 'list[str]',
            'details': 'ResponderRuleDetails',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'responder_rule_id': 'responderRuleId',
            'display_name': 'displayName',
            'description': 'description',
            'type': 'type',
            'policies': 'policies',
            'supported_modes': 'supportedModes',
            'details': 'details',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._responder_rule_id = None
        self._display_name = None
        self._description = None
        self._type = None
        self._policies = None
        self._supported_modes = None
        self._details = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def responder_rule_id(self):
        """
        **[Required]** Gets the responder_rule_id of this TargetResponderRecipeResponderRule.
        Unique ResponderRule identifier.


        :return: The responder_rule_id of this TargetResponderRecipeResponderRule.
        :rtype: str
        """
        return self._responder_rule_id

    @responder_rule_id.setter
    def responder_rule_id(self, responder_rule_id):
        """
        Sets the responder_rule_id of this TargetResponderRecipeResponderRule.
        Unique ResponderRule identifier.


        :param responder_rule_id: The responder_rule_id of this TargetResponderRecipeResponderRule.
        :type: str
        """
        self._responder_rule_id = responder_rule_id

    @property
    def display_name(self):
        """
        Gets the display_name of this TargetResponderRecipeResponderRule.
        ResponderRule display name.


        :return: The display_name of this TargetResponderRecipeResponderRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TargetResponderRecipeResponderRule.
        ResponderRule display name.


        :param display_name: The display_name of this TargetResponderRecipeResponderRule.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TargetResponderRecipeResponderRule.
        ResponderRule description.


        :return: The description of this TargetResponderRecipeResponderRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TargetResponderRecipeResponderRule.
        ResponderRule description.


        :param description: The description of this TargetResponderRecipeResponderRule.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        Gets the type of this TargetResponderRecipeResponderRule.
        Type of Responder

        Allowed values for this property are: "REMEDIATION", "NOTIFICATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this TargetResponderRecipeResponderRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TargetResponderRecipeResponderRule.
        Type of Responder


        :param type: The type of this TargetResponderRecipeResponderRule.
        :type: str
        """
        allowed_values = ["REMEDIATION", "NOTIFICATION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def policies(self):
        """
        Gets the policies of this TargetResponderRecipeResponderRule.
        List of Policy


        :return: The policies of this TargetResponderRecipeResponderRule.
        :rtype: list[str]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """
        Sets the policies of this TargetResponderRecipeResponderRule.
        List of Policy


        :param policies: The policies of this TargetResponderRecipeResponderRule.
        :type: list[str]
        """
        self._policies = policies

    @property
    def supported_modes(self):
        """
        Gets the supported_modes of this TargetResponderRecipeResponderRule.
        Supported Execution Modes

        Allowed values for items in this list are: "AUTOACTION", "USERACTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The supported_modes of this TargetResponderRecipeResponderRule.
        :rtype: list[str]
        """
        return self._supported_modes

    @supported_modes.setter
    def supported_modes(self, supported_modes):
        """
        Sets the supported_modes of this TargetResponderRecipeResponderRule.
        Supported Execution Modes


        :param supported_modes: The supported_modes of this TargetResponderRecipeResponderRule.
        :type: list[str]
        """
        allowed_values = ["AUTOACTION", "USERACTION"]
        if supported_modes:
            supported_modes[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in supported_modes]
        self._supported_modes = supported_modes

    @property
    def details(self):
        """
        Gets the details of this TargetResponderRecipeResponderRule.

        :return: The details of this TargetResponderRecipeResponderRule.
        :rtype: oci.cloud_guard.models.ResponderRuleDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this TargetResponderRecipeResponderRule.

        :param details: The details of this TargetResponderRecipeResponderRule.
        :type: oci.cloud_guard.models.ResponderRuleDetails
        """
        self._details = details

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TargetResponderRecipeResponderRule.
        Compartment Identifier


        :return: The compartment_id of this TargetResponderRecipeResponderRule.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TargetResponderRecipeResponderRule.
        Compartment Identifier


        :param compartment_id: The compartment_id of this TargetResponderRecipeResponderRule.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this TargetResponderRecipeResponderRule.
        The date and time the target responder recipe rule was created. Format defined by RFC3339.


        :return: The time_created of this TargetResponderRecipeResponderRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TargetResponderRecipeResponderRule.
        The date and time the target responder recipe rule was created. Format defined by RFC3339.


        :param time_created: The time_created of this TargetResponderRecipeResponderRule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TargetResponderRecipeResponderRule.
        The date and time the target responder recipe rule was updated. Format defined by RFC3339.


        :return: The time_updated of this TargetResponderRecipeResponderRule.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TargetResponderRecipeResponderRule.
        The date and time the target responder recipe rule was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this TargetResponderRecipeResponderRule.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TargetResponderRecipeResponderRule.
        The current state of the ResponderRule.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TargetResponderRecipeResponderRule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TargetResponderRecipeResponderRule.
        The current state of the ResponderRule.


        :param lifecycle_state: The lifecycle_state of this TargetResponderRecipeResponderRule.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TargetResponderRecipeResponderRule.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TargetResponderRecipeResponderRule.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TargetResponderRecipeResponderRule.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TargetResponderRecipeResponderRule.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
