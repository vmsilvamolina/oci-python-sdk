# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FsuDiscovery(object):
    """
    Exadata Fleet Update Discovery resource details.
    """

    #: A constant which can be used with the lifecycle_state property of a FsuDiscovery.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a FsuDiscovery.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a FsuDiscovery.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a FsuDiscovery.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a FsuDiscovery.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a FsuDiscovery.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a FsuDiscovery.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a FsuDiscovery.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new FsuDiscovery object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FsuDiscovery.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this FsuDiscovery.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this FsuDiscovery.
        :type compartment_id: str

        :param details:
            The value to assign to the details property of this FsuDiscovery.
        :type details: oci.fleet_software_update.models.DiscoveryDetails

        :param time_created:
            The value to assign to the time_created property of this FsuDiscovery.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this FsuDiscovery.
        :type time_updated: datetime

        :param time_finished:
            The value to assign to the time_finished property of this FsuDiscovery.
        :type time_finished: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FsuDiscovery.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this FsuDiscovery.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FsuDiscovery.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FsuDiscovery.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this FsuDiscovery.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'details': 'DiscoveryDetails',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_finished': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'details': 'details',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_finished': 'timeFinished',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._details = None
        self._time_created = None
        self._time_updated = None
        self._time_finished = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FsuDiscovery.
        OCID identifier for the Exadata Fleet Update Discovery.


        :return: The id of this FsuDiscovery.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FsuDiscovery.
        OCID identifier for the Exadata Fleet Update Discovery.


        :param id: The id of this FsuDiscovery.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this FsuDiscovery.
        Exadata Fleet Update Discovery display name.


        :return: The display_name of this FsuDiscovery.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FsuDiscovery.
        Exadata Fleet Update Discovery display name.


        :param display_name: The display_name of this FsuDiscovery.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FsuDiscovery.
        Compartment Identifier.


        :return: The compartment_id of this FsuDiscovery.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FsuDiscovery.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this FsuDiscovery.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def details(self):
        """
        **[Required]** Gets the details of this FsuDiscovery.

        :return: The details of this FsuDiscovery.
        :rtype: oci.fleet_software_update.models.DiscoveryDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this FsuDiscovery.

        :param details: The details of this FsuDiscovery.
        :type: oci.fleet_software_update.models.DiscoveryDetails
        """
        self._details = details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this FsuDiscovery.
        The date and time the Exadata Fleet Update Discovery was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this FsuDiscovery.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FsuDiscovery.
        The date and time the Exadata Fleet Update Discovery was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this FsuDiscovery.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this FsuDiscovery.
        The date and time the Exadata Fleet Update Discovery was updated,
        as described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this FsuDiscovery.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this FsuDiscovery.
        The date and time the Exadata Fleet Update Discovery was updated,
        as described in `RFC 3339`__,
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this FsuDiscovery.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_finished(self):
        """
        Gets the time_finished of this FsuDiscovery.
        The date and time the Exadata Fleet Update Discovery was finished,
        as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_finished of this FsuDiscovery.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this FsuDiscovery.
        The date and time the Exadata Fleet Update Discovery was finished,
        as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_finished: The time_finished of this FsuDiscovery.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FsuDiscovery.
        The current state of the Exadata Fleet Update Discovery.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FsuDiscovery.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FsuDiscovery.
        The current state of the Exadata Fleet Update Discovery.


        :param lifecycle_state: The lifecycle_state of this FsuDiscovery.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this FsuDiscovery.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this FsuDiscovery.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this FsuDiscovery.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this FsuDiscovery.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FsuDiscovery.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this FsuDiscovery.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FsuDiscovery.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this FsuDiscovery.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FsuDiscovery.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this FsuDiscovery.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FsuDiscovery.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this FsuDiscovery.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this FsuDiscovery.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this FsuDiscovery.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this FsuDiscovery.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this FsuDiscovery.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
