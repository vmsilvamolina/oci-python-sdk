# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmReport(object):
    """
    ADDM Tasks.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddmReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this AddmReport.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this AddmReport.
        :type time_interval_end: datetime

        :param task_identifier:
            The value to assign to the task_identifier property of this AddmReport.
        :type task_identifier: str

        :param database_identifier:
            The value to assign to the database_identifier property of this AddmReport.
        :type database_identifier: str

        :param snapshot_interval_start:
            The value to assign to the snapshot_interval_start property of this AddmReport.
        :type snapshot_interval_start: str

        :param snapshot_interval_end:
            The value to assign to the snapshot_interval_end property of this AddmReport.
        :type snapshot_interval_end: str

        :param addm_report:
            The value to assign to the addm_report property of this AddmReport.
        :type addm_report: str

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'task_identifier': 'str',
            'database_identifier': 'str',
            'snapshot_interval_start': 'str',
            'snapshot_interval_end': 'str',
            'addm_report': 'str'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'task_identifier': 'taskIdentifier',
            'database_identifier': 'databaseIdentifier',
            'snapshot_interval_start': 'snapshotIntervalStart',
            'snapshot_interval_end': 'snapshotIntervalEnd',
            'addm_report': 'addmReport'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._task_identifier = None
        self._database_identifier = None
        self._snapshot_interval_start = None
        self._snapshot_interval_end = None
        self._addm_report = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this AddmReport.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this AddmReport.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this AddmReport.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this AddmReport.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this AddmReport.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this AddmReport.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this AddmReport.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this AddmReport.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def task_identifier(self):
        """
        **[Required]** Gets the task_identifier of this AddmReport.
        TASK_ID in the oracle database view DBA_ADDM_TASKS


        :return: The task_identifier of this AddmReport.
        :rtype: str
        """
        return self._task_identifier

    @task_identifier.setter
    def task_identifier(self, task_identifier):
        """
        Sets the task_identifier of this AddmReport.
        TASK_ID in the oracle database view DBA_ADDM_TASKS


        :param task_identifier: The task_identifier of this AddmReport.
        :type: str
        """
        self._task_identifier = task_identifier

    @property
    def database_identifier(self):
        """
        **[Required]** Gets the database_identifier of this AddmReport.
        Internal id of the database.


        :return: The database_identifier of this AddmReport.
        :rtype: str
        """
        return self._database_identifier

    @database_identifier.setter
    def database_identifier(self, database_identifier):
        """
        Sets the database_identifier of this AddmReport.
        Internal id of the database.


        :param database_identifier: The database_identifier of this AddmReport.
        :type: str
        """
        self._database_identifier = database_identifier

    @property
    def snapshot_interval_start(self):
        """
        **[Required]** Gets the snapshot_interval_start of this AddmReport.
        AWR snapshot id.


        :return: The snapshot_interval_start of this AddmReport.
        :rtype: str
        """
        return self._snapshot_interval_start

    @snapshot_interval_start.setter
    def snapshot_interval_start(self, snapshot_interval_start):
        """
        Sets the snapshot_interval_start of this AddmReport.
        AWR snapshot id.


        :param snapshot_interval_start: The snapshot_interval_start of this AddmReport.
        :type: str
        """
        self._snapshot_interval_start = snapshot_interval_start

    @property
    def snapshot_interval_end(self):
        """
        **[Required]** Gets the snapshot_interval_end of this AddmReport.
        AWR snapshot id.


        :return: The snapshot_interval_end of this AddmReport.
        :rtype: str
        """
        return self._snapshot_interval_end

    @snapshot_interval_end.setter
    def snapshot_interval_end(self, snapshot_interval_end):
        """
        Sets the snapshot_interval_end of this AddmReport.
        AWR snapshot id.


        :param snapshot_interval_end: The snapshot_interval_end of this AddmReport.
        :type: str
        """
        self._snapshot_interval_end = snapshot_interval_end

    @property
    def addm_report(self):
        """
        **[Required]** Gets the addm_report of this AddmReport.
        The complete ADDM report


        :return: The addm_report of this AddmReport.
        :rtype: str
        """
        return self._addm_report

    @addm_report.setter
    def addm_report(self, addm_report):
        """
        Sets the addm_report of this AddmReport.
        The complete ADDM report


        :param addm_report: The addm_report of this AddmReport.
        :type: str
        """
        self._addm_report = addm_report

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
