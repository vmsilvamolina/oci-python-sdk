# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeReplaceConfigurationSummary(object):
    """
    The information about the NodeReplaceConfigurationSummary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeReplaceConfigurationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this NodeReplaceConfigurationSummary.
        :type id: str

        :param bds_instance_id:
            The value to assign to the bds_instance_id property of this NodeReplaceConfigurationSummary.
        :type bds_instance_id: str

        :param display_name:
            The value to assign to the display_name property of this NodeReplaceConfigurationSummary.
        :type display_name: str

        :param level_type_details:
            The value to assign to the level_type_details property of this NodeReplaceConfigurationSummary.
        :type level_type_details: oci.bds.models.LevelTypeDetails

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this NodeReplaceConfigurationSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this NodeReplaceConfigurationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this NodeReplaceConfigurationSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'bds_instance_id': 'str',
            'display_name': 'str',
            'level_type_details': 'LevelTypeDetails',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'bds_instance_id': 'bdsInstanceId',
            'display_name': 'displayName',
            'level_type_details': 'levelTypeDetails',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._bds_instance_id = None
        self._display_name = None
        self._level_type_details = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this NodeReplaceConfigurationSummary.
        The id of the NodeReplaceConfiguration.


        :return: The id of this NodeReplaceConfigurationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NodeReplaceConfigurationSummary.
        The id of the NodeReplaceConfiguration.


        :param id: The id of this NodeReplaceConfigurationSummary.
        :type: str
        """
        self._id = id

    @property
    def bds_instance_id(self):
        """
        **[Required]** Gets the bds_instance_id of this NodeReplaceConfigurationSummary.
        The OCID of the bdsInstance which is the parent resource id.


        :return: The bds_instance_id of this NodeReplaceConfigurationSummary.
        :rtype: str
        """
        return self._bds_instance_id

    @bds_instance_id.setter
    def bds_instance_id(self, bds_instance_id):
        """
        Sets the bds_instance_id of this NodeReplaceConfigurationSummary.
        The OCID of the bdsInstance which is the parent resource id.


        :param bds_instance_id: The bds_instance_id of this NodeReplaceConfigurationSummary.
        :type: str
        """
        self._bds_instance_id = bds_instance_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this NodeReplaceConfigurationSummary.
        A user-friendly name. Only ASCII alphanumeric characters with no spaces allowed. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :return: The display_name of this NodeReplaceConfigurationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this NodeReplaceConfigurationSummary.
        A user-friendly name. Only ASCII alphanumeric characters with no spaces allowed. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :param display_name: The display_name of this NodeReplaceConfigurationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def level_type_details(self):
        """
        **[Required]** Gets the level_type_details of this NodeReplaceConfigurationSummary.

        :return: The level_type_details of this NodeReplaceConfigurationSummary.
        :rtype: oci.bds.models.LevelTypeDetails
        """
        return self._level_type_details

    @level_type_details.setter
    def level_type_details(self, level_type_details):
        """
        Sets the level_type_details of this NodeReplaceConfigurationSummary.

        :param level_type_details: The level_type_details of this NodeReplaceConfigurationSummary.
        :type: oci.bds.models.LevelTypeDetails
        """
        self._level_type_details = level_type_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this NodeReplaceConfigurationSummary.
        The state of the NodeReplaceConfiguration.


        :return: The lifecycle_state of this NodeReplaceConfigurationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this NodeReplaceConfigurationSummary.
        The state of the NodeReplaceConfiguration.


        :param lifecycle_state: The lifecycle_state of this NodeReplaceConfigurationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this NodeReplaceConfigurationSummary.
        The time the NodeReplaceConfiguration was created, shown as an RFC 3339 formatted datetime string.


        :return: The time_created of this NodeReplaceConfigurationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this NodeReplaceConfigurationSummary.
        The time the NodeReplaceConfiguration was created, shown as an RFC 3339 formatted datetime string.


        :param time_created: The time_created of this NodeReplaceConfigurationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this NodeReplaceConfigurationSummary.
        The time the NodeReplaceConfiguration was updated, shown as an RFC 3339 formatted datetime string.


        :return: The time_updated of this NodeReplaceConfigurationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this NodeReplaceConfigurationSummary.
        The time the NodeReplaceConfiguration was updated, shown as an RFC 3339 formatted datetime string.


        :param time_updated: The time_updated of this NodeReplaceConfigurationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
