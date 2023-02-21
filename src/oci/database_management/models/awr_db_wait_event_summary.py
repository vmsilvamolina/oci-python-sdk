# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDbWaitEventSummary(object):
    """
    The summary of the AWR wait event time series data for one event.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDbWaitEventSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrDbWaitEventSummary.
        :type name: str

        :param time_begin:
            The value to assign to the time_begin property of this AwrDbWaitEventSummary.
        :type time_begin: datetime

        :param time_end:
            The value to assign to the time_end property of this AwrDbWaitEventSummary.
        :type time_end: datetime

        :param waits_per_sec:
            The value to assign to the waits_per_sec property of this AwrDbWaitEventSummary.
        :type waits_per_sec: float

        :param avg_wait_time_per_sec:
            The value to assign to the avg_wait_time_per_sec property of this AwrDbWaitEventSummary.
        :type avg_wait_time_per_sec: float

        :param avg_wait_time_per_wait:
            The value to assign to the avg_wait_time_per_wait property of this AwrDbWaitEventSummary.
        :type avg_wait_time_per_wait: float

        :param snapshot_id:
            The value to assign to the snapshot_id property of this AwrDbWaitEventSummary.
        :type snapshot_id: int

        """
        self.swagger_types = {
            'name': 'str',
            'time_begin': 'datetime',
            'time_end': 'datetime',
            'waits_per_sec': 'float',
            'avg_wait_time_per_sec': 'float',
            'avg_wait_time_per_wait': 'float',
            'snapshot_id': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'time_begin': 'timeBegin',
            'time_end': 'timeEnd',
            'waits_per_sec': 'waitsPerSec',
            'avg_wait_time_per_sec': 'avgWaitTimePerSec',
            'avg_wait_time_per_wait': 'avgWaitTimePerWait',
            'snapshot_id': 'snapshotId'
        }

        self._name = None
        self._time_begin = None
        self._time_end = None
        self._waits_per_sec = None
        self._avg_wait_time_per_sec = None
        self._avg_wait_time_per_wait = None
        self._snapshot_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AwrDbWaitEventSummary.
        The name of the event.


        :return: The name of this AwrDbWaitEventSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AwrDbWaitEventSummary.
        The name of the event.


        :param name: The name of this AwrDbWaitEventSummary.
        :type: str
        """
        self._name = name

    @property
    def time_begin(self):
        """
        Gets the time_begin of this AwrDbWaitEventSummary.
        The begin time of the wait event.


        :return: The time_begin of this AwrDbWaitEventSummary.
        :rtype: datetime
        """
        return self._time_begin

    @time_begin.setter
    def time_begin(self, time_begin):
        """
        Sets the time_begin of this AwrDbWaitEventSummary.
        The begin time of the wait event.


        :param time_begin: The time_begin of this AwrDbWaitEventSummary.
        :type: datetime
        """
        self._time_begin = time_begin

    @property
    def time_end(self):
        """
        Gets the time_end of this AwrDbWaitEventSummary.
        The end time of the wait event.


        :return: The time_end of this AwrDbWaitEventSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this AwrDbWaitEventSummary.
        The end time of the wait event.


        :param time_end: The time_end of this AwrDbWaitEventSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def waits_per_sec(self):
        """
        Gets the waits_per_sec of this AwrDbWaitEventSummary.
        The wait count per second.


        :return: The waits_per_sec of this AwrDbWaitEventSummary.
        :rtype: float
        """
        return self._waits_per_sec

    @waits_per_sec.setter
    def waits_per_sec(self, waits_per_sec):
        """
        Sets the waits_per_sec of this AwrDbWaitEventSummary.
        The wait count per second.


        :param waits_per_sec: The waits_per_sec of this AwrDbWaitEventSummary.
        :type: float
        """
        self._waits_per_sec = waits_per_sec

    @property
    def avg_wait_time_per_sec(self):
        """
        Gets the avg_wait_time_per_sec of this AwrDbWaitEventSummary.
        The average wait time per second.


        :return: The avg_wait_time_per_sec of this AwrDbWaitEventSummary.
        :rtype: float
        """
        return self._avg_wait_time_per_sec

    @avg_wait_time_per_sec.setter
    def avg_wait_time_per_sec(self, avg_wait_time_per_sec):
        """
        Sets the avg_wait_time_per_sec of this AwrDbWaitEventSummary.
        The average wait time per second.


        :param avg_wait_time_per_sec: The avg_wait_time_per_sec of this AwrDbWaitEventSummary.
        :type: float
        """
        self._avg_wait_time_per_sec = avg_wait_time_per_sec

    @property
    def avg_wait_time_per_wait(self):
        """
        Gets the avg_wait_time_per_wait of this AwrDbWaitEventSummary.
        The average wait time in milliseconds per wait.


        :return: The avg_wait_time_per_wait of this AwrDbWaitEventSummary.
        :rtype: float
        """
        return self._avg_wait_time_per_wait

    @avg_wait_time_per_wait.setter
    def avg_wait_time_per_wait(self, avg_wait_time_per_wait):
        """
        Sets the avg_wait_time_per_wait of this AwrDbWaitEventSummary.
        The average wait time in milliseconds per wait.


        :param avg_wait_time_per_wait: The avg_wait_time_per_wait of this AwrDbWaitEventSummary.
        :type: float
        """
        self._avg_wait_time_per_wait = avg_wait_time_per_wait

    @property
    def snapshot_id(self):
        """
        Gets the snapshot_id of this AwrDbWaitEventSummary.
        The ID of the snapshot. The snapshot ID is not the `OCID`__.
        It can be retrieved from the following endpoint:
        /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The snapshot_id of this AwrDbWaitEventSummary.
        :rtype: int
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """
        Sets the snapshot_id of this AwrDbWaitEventSummary.
        The ID of the snapshot. The snapshot ID is not the `OCID`__.
        It can be retrieved from the following endpoint:
        /managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbSnapshots

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param snapshot_id: The snapshot_id of this AwrDbWaitEventSummary.
        :type: int
        """
        self._snapshot_id = snapshot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
