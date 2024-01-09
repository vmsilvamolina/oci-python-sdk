# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportStatus(object):
    """
    Attributes of fleet's export status.
    """

    #: A constant which can be used with the latest_run_status property of a ExportStatus.
    #: This constant has a value of "SCHEDULED"
    LATEST_RUN_STATUS_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the latest_run_status property of a ExportStatus.
    #: This constant has a value of "PENDING"
    LATEST_RUN_STATUS_PENDING = "PENDING"

    #: A constant which can be used with the latest_run_status property of a ExportStatus.
    #: This constant has a value of "IN_PROGRESS"
    LATEST_RUN_STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the latest_run_status property of a ExportStatus.
    #: This constant has a value of "FAILED"
    LATEST_RUN_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the latest_run_status property of a ExportStatus.
    #: This constant has a value of "RETRYING"
    LATEST_RUN_STATUS_RETRYING = "RETRYING"

    #: A constant which can be used with the latest_run_status property of a ExportStatus.
    #: This constant has a value of "SUCCEEDED"
    LATEST_RUN_STATUS_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExportStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fleet_id:
            The value to assign to the fleet_id property of this ExportStatus.
        :type fleet_id: str

        :param time_last_run:
            The value to assign to the time_last_run property of this ExportStatus.
        :type time_last_run: datetime

        :param time_next_run:
            The value to assign to the time_next_run property of this ExportStatus.
        :type time_next_run: datetime

        :param latest_run_status:
            The value to assign to the latest_run_status property of this ExportStatus.
            Allowed values for this property are: "SCHEDULED", "PENDING", "IN_PROGRESS", "FAILED", "RETRYING", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type latest_run_status: str

        """
        self.swagger_types = {
            'fleet_id': 'str',
            'time_last_run': 'datetime',
            'time_next_run': 'datetime',
            'latest_run_status': 'str'
        }

        self.attribute_map = {
            'fleet_id': 'fleetId',
            'time_last_run': 'timeLastRun',
            'time_next_run': 'timeNextRun',
            'latest_run_status': 'latestRunStatus'
        }

        self._fleet_id = None
        self._time_last_run = None
        self._time_next_run = None
        self._latest_run_status = None

    @property
    def fleet_id(self):
        """
        **[Required]** Gets the fleet_id of this ExportStatus.
        The `OCID`__ of the fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this ExportStatus.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this ExportStatus.
        The `OCID`__ of the fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this ExportStatus.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def time_last_run(self):
        """
        **[Required]** Gets the time_last_run of this ExportStatus.
        The date and time of the last export run.


        :return: The time_last_run of this ExportStatus.
        :rtype: datetime
        """
        return self._time_last_run

    @time_last_run.setter
    def time_last_run(self, time_last_run):
        """
        Sets the time_last_run of this ExportStatus.
        The date and time of the last export run.


        :param time_last_run: The time_last_run of this ExportStatus.
        :type: datetime
        """
        self._time_last_run = time_last_run

    @property
    def time_next_run(self):
        """
        **[Required]** Gets the time_next_run of this ExportStatus.
        The date and time of the next export run.


        :return: The time_next_run of this ExportStatus.
        :rtype: datetime
        """
        return self._time_next_run

    @time_next_run.setter
    def time_next_run(self, time_next_run):
        """
        Sets the time_next_run of this ExportStatus.
        The date and time of the next export run.


        :param time_next_run: The time_next_run of this ExportStatus.
        :type: datetime
        """
        self._time_next_run = time_next_run

    @property
    def latest_run_status(self):
        """
        **[Required]** Gets the latest_run_status of this ExportStatus.
        The status of the latest export run.

        Allowed values for this property are: "SCHEDULED", "PENDING", "IN_PROGRESS", "FAILED", "RETRYING", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The latest_run_status of this ExportStatus.
        :rtype: str
        """
        return self._latest_run_status

    @latest_run_status.setter
    def latest_run_status(self, latest_run_status):
        """
        Sets the latest_run_status of this ExportStatus.
        The status of the latest export run.


        :param latest_run_status: The latest_run_status of this ExportStatus.
        :type: str
        """
        allowed_values = ["SCHEDULED", "PENDING", "IN_PROGRESS", "FAILED", "RETRYING", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(latest_run_status, allowed_values):
            latest_run_status = 'UNKNOWN_ENUM_VALUE'
        self._latest_run_status = latest_run_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
