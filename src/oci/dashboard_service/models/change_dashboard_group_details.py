# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeDashboardGroupDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeDashboardGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dashboard_group_id:
            The value to assign to the dashboard_group_id property of this ChangeDashboardGroupDetails.
        :type dashboard_group_id: str

        """
        self.swagger_types = {
            'dashboard_group_id': 'str'
        }

        self.attribute_map = {
            'dashboard_group_id': 'dashboardGroupId'
        }

        self._dashboard_group_id = None

    @property
    def dashboard_group_id(self):
        """
        **[Required]** Gets the dashboard_group_id of this ChangeDashboardGroupDetails.
        The `OCID`__ of the dashboardGroup
        into which the resource should be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The dashboard_group_id of this ChangeDashboardGroupDetails.
        :rtype: str
        """
        return self._dashboard_group_id

    @dashboard_group_id.setter
    def dashboard_group_id(self, dashboard_group_id):
        """
        Sets the dashboard_group_id of this ChangeDashboardGroupDetails.
        The `OCID`__ of the dashboardGroup
        into which the resource should be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param dashboard_group_id: The dashboard_group_id of this ChangeDashboardGroupDetails.
        :type: str
        """
        self._dashboard_group_id = dashboard_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
