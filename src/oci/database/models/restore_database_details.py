# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RestoreDatabaseDetails(object):
    """
    RestoreDatabaseDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RestoreDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_scn:
            The value to assign to the database_scn property of this RestoreDatabaseDetails.
        :type database_scn: str

        :param timestamp:
            The value to assign to the timestamp property of this RestoreDatabaseDetails.
        :type timestamp: datetime

        :param latest:
            The value to assign to the latest property of this RestoreDatabaseDetails.
        :type latest: bool

        :param pluggable_database_name:
            The value to assign to the pluggable_database_name property of this RestoreDatabaseDetails.
        :type pluggable_database_name: str

        """
        self.swagger_types = {
            'database_scn': 'str',
            'timestamp': 'datetime',
            'latest': 'bool',
            'pluggable_database_name': 'str'
        }

        self.attribute_map = {
            'database_scn': 'databaseSCN',
            'timestamp': 'timestamp',
            'latest': 'latest',
            'pluggable_database_name': 'pluggableDatabaseName'
        }

        self._database_scn = None
        self._timestamp = None
        self._latest = None
        self._pluggable_database_name = None

    @property
    def database_scn(self):
        """
        Gets the database_scn of this RestoreDatabaseDetails.
        Restores using the backup with the System Change Number (SCN) specified.
        This field is applicable for both use cases - Restoring Container Database or Restoring specific Pluggable Database.


        :return: The database_scn of this RestoreDatabaseDetails.
        :rtype: str
        """
        return self._database_scn

    @database_scn.setter
    def database_scn(self, database_scn):
        """
        Sets the database_scn of this RestoreDatabaseDetails.
        Restores using the backup with the System Change Number (SCN) specified.
        This field is applicable for both use cases - Restoring Container Database or Restoring specific Pluggable Database.


        :param database_scn: The database_scn of this RestoreDatabaseDetails.
        :type: str
        """
        self._database_scn = database_scn

    @property
    def timestamp(self):
        """
        Gets the timestamp of this RestoreDatabaseDetails.
        Restores to the timestamp specified.


        :return: The timestamp of this RestoreDatabaseDetails.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this RestoreDatabaseDetails.
        Restores to the timestamp specified.


        :param timestamp: The timestamp of this RestoreDatabaseDetails.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def latest(self):
        """
        Gets the latest of this RestoreDatabaseDetails.
        Restores to the last known good state with the least possible data loss.


        :return: The latest of this RestoreDatabaseDetails.
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """
        Sets the latest of this RestoreDatabaseDetails.
        Restores to the last known good state with the least possible data loss.


        :param latest: The latest of this RestoreDatabaseDetails.
        :type: bool
        """
        self._latest = latest

    @property
    def pluggable_database_name(self):
        """
        Gets the pluggable_database_name of this RestoreDatabaseDetails.
        Restores only the Pluggable Database (if specified) using the inputs provided in request.


        :return: The pluggable_database_name of this RestoreDatabaseDetails.
        :rtype: str
        """
        return self._pluggable_database_name

    @pluggable_database_name.setter
    def pluggable_database_name(self, pluggable_database_name):
        """
        Sets the pluggable_database_name of this RestoreDatabaseDetails.
        Restores only the Pluggable Database (if specified) using the inputs provided in request.


        :param pluggable_database_name: The pluggable_database_name of this RestoreDatabaseDetails.
        :type: str
        """
        self._pluggable_database_name = pluggable_database_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
