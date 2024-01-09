# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190415


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeletionPolicyDetails(object):
    """
    The Deletion policy for the DB System.
    """

    #: A constant which can be used with the automatic_backup_retention property of a DeletionPolicyDetails.
    #: This constant has a value of "DELETE"
    AUTOMATIC_BACKUP_RETENTION_DELETE = "DELETE"

    #: A constant which can be used with the automatic_backup_retention property of a DeletionPolicyDetails.
    #: This constant has a value of "RETAIN"
    AUTOMATIC_BACKUP_RETENTION_RETAIN = "RETAIN"

    #: A constant which can be used with the final_backup property of a DeletionPolicyDetails.
    #: This constant has a value of "SKIP_FINAL_BACKUP"
    FINAL_BACKUP_SKIP_FINAL_BACKUP = "SKIP_FINAL_BACKUP"

    #: A constant which can be used with the final_backup property of a DeletionPolicyDetails.
    #: This constant has a value of "REQUIRE_FINAL_BACKUP"
    FINAL_BACKUP_REQUIRE_FINAL_BACKUP = "REQUIRE_FINAL_BACKUP"

    def __init__(self, **kwargs):
        """
        Initializes a new DeletionPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param automatic_backup_retention:
            The value to assign to the automatic_backup_retention property of this DeletionPolicyDetails.
            Allowed values for this property are: "DELETE", "RETAIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type automatic_backup_retention: str

        :param final_backup:
            The value to assign to the final_backup property of this DeletionPolicyDetails.
            Allowed values for this property are: "SKIP_FINAL_BACKUP", "REQUIRE_FINAL_BACKUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type final_backup: str

        :param is_delete_protected:
            The value to assign to the is_delete_protected property of this DeletionPolicyDetails.
        :type is_delete_protected: bool

        """
        self.swagger_types = {
            'automatic_backup_retention': 'str',
            'final_backup': 'str',
            'is_delete_protected': 'bool'
        }

        self.attribute_map = {
            'automatic_backup_retention': 'automaticBackupRetention',
            'final_backup': 'finalBackup',
            'is_delete_protected': 'isDeleteProtected'
        }

        self._automatic_backup_retention = None
        self._final_backup = None
        self._is_delete_protected = None

    @property
    def automatic_backup_retention(self):
        """
        **[Required]** Gets the automatic_backup_retention of this DeletionPolicyDetails.
        Specifies if any automatic backups created for a DB System should be retained or deleted when the DB System is deleted.

        Allowed values for this property are: "DELETE", "RETAIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The automatic_backup_retention of this DeletionPolicyDetails.
        :rtype: str
        """
        return self._automatic_backup_retention

    @automatic_backup_retention.setter
    def automatic_backup_retention(self, automatic_backup_retention):
        """
        Sets the automatic_backup_retention of this DeletionPolicyDetails.
        Specifies if any automatic backups created for a DB System should be retained or deleted when the DB System is deleted.


        :param automatic_backup_retention: The automatic_backup_retention of this DeletionPolicyDetails.
        :type: str
        """
        allowed_values = ["DELETE", "RETAIN"]
        if not value_allowed_none_or_none_sentinel(automatic_backup_retention, allowed_values):
            automatic_backup_retention = 'UNKNOWN_ENUM_VALUE'
        self._automatic_backup_retention = automatic_backup_retention

    @property
    def final_backup(self):
        """
        **[Required]** Gets the final_backup of this DeletionPolicyDetails.
        Specifies whether or not a backup is taken when the DB System is deleted.
          REQUIRE_FINAL_BACKUP: a backup is taken if the DB System is deleted.
          SKIP_FINAL_BACKUP: a backup is not taken if the DB System is deleted.

        Allowed values for this property are: "SKIP_FINAL_BACKUP", "REQUIRE_FINAL_BACKUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The final_backup of this DeletionPolicyDetails.
        :rtype: str
        """
        return self._final_backup

    @final_backup.setter
    def final_backup(self, final_backup):
        """
        Sets the final_backup of this DeletionPolicyDetails.
        Specifies whether or not a backup is taken when the DB System is deleted.
          REQUIRE_FINAL_BACKUP: a backup is taken if the DB System is deleted.
          SKIP_FINAL_BACKUP: a backup is not taken if the DB System is deleted.


        :param final_backup: The final_backup of this DeletionPolicyDetails.
        :type: str
        """
        allowed_values = ["SKIP_FINAL_BACKUP", "REQUIRE_FINAL_BACKUP"]
        if not value_allowed_none_or_none_sentinel(final_backup, allowed_values):
            final_backup = 'UNKNOWN_ENUM_VALUE'
        self._final_backup = final_backup

    @property
    def is_delete_protected(self):
        """
        **[Required]** Gets the is_delete_protected of this DeletionPolicyDetails.
        Specifies whether the DB System can be deleted. Set to true to prevent deletion, false (default) to allow.


        :return: The is_delete_protected of this DeletionPolicyDetails.
        :rtype: bool
        """
        return self._is_delete_protected

    @is_delete_protected.setter
    def is_delete_protected(self, is_delete_protected):
        """
        Sets the is_delete_protected of this DeletionPolicyDetails.
        Specifies whether the DB System can be deleted. Set to true to prevent deletion, false (default) to allow.


        :param is_delete_protected: The is_delete_protected of this DeletionPolicyDetails.
        :type: bool
        """
        self._is_delete_protected = is_delete_protected

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
