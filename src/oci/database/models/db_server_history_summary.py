# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbServerHistorySummary(object):
    """
    Details of a database server maintenance history.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbServerHistorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbServerHistorySummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DbServerHistorySummary.
        :type display_name: str

        :param db_server_patching_details:
            The value to assign to the db_server_patching_details property of this DbServerHistorySummary.
        :type db_server_patching_details: oci.database.models.DbServerPatchingDetails

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'db_server_patching_details': 'DbServerPatchingDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'db_server_patching_details': 'dbServerPatchingDetails'
        }

        self._id = None
        self._display_name = None
        self._db_server_patching_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbServerHistorySummary.
        The OCID of the database server.


        :return: The id of this DbServerHistorySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbServerHistorySummary.
        The OCID of the database server.


        :param id: The id of this DbServerHistorySummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this DbServerHistorySummary.
        The user-friendly name for the database server. The name does not need to be unique.


        :return: The display_name of this DbServerHistorySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DbServerHistorySummary.
        The user-friendly name for the database server. The name does not need to be unique.


        :param display_name: The display_name of this DbServerHistorySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def db_server_patching_details(self):
        """
        Gets the db_server_patching_details of this DbServerHistorySummary.

        :return: The db_server_patching_details of this DbServerHistorySummary.
        :rtype: oci.database.models.DbServerPatchingDetails
        """
        return self._db_server_patching_details

    @db_server_patching_details.setter
    def db_server_patching_details(self, db_server_patching_details):
        """
        Sets the db_server_patching_details of this DbServerHistorySummary.

        :param db_server_patching_details: The db_server_patching_details of this DbServerHistorySummary.
        :type: oci.database.models.DbServerPatchingDetails
        """
        self._db_server_patching_details = db_server_patching_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
