# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditPolicyDimensions(object):
    """
    Details of aggregation dimensions used for summarizing audit policies.
    """

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "BASIC_ACTIVITY"
    AUDIT_POLICY_CATEGORY_BASIC_ACTIVITY = "BASIC_ACTIVITY"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "ADMIN_USER_ACTIVITY"
    AUDIT_POLICY_CATEGORY_ADMIN_USER_ACTIVITY = "ADMIN_USER_ACTIVITY"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "USER_ACTIVITY"
    AUDIT_POLICY_CATEGORY_USER_ACTIVITY = "USER_ACTIVITY"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "ORACLE_PREDEFINED"
    AUDIT_POLICY_CATEGORY_ORACLE_PREDEFINED = "ORACLE_PREDEFINED"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "COMPLIANCE_STANDARD"
    AUDIT_POLICY_CATEGORY_COMPLIANCE_STANDARD = "COMPLIANCE_STANDARD"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "CUSTOM"
    AUDIT_POLICY_CATEGORY_CUSTOM = "CUSTOM"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "SQL_FIREWALL_AUDITING"
    AUDIT_POLICY_CATEGORY_SQL_FIREWALL_AUDITING = "SQL_FIREWALL_AUDITING"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditPolicyDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audit_policy_category:
            The value to assign to the audit_policy_category property of this AuditPolicyDimensions.
            Allowed values for this property are: "BASIC_ACTIVITY", "ADMIN_USER_ACTIVITY", "USER_ACTIVITY", "ORACLE_PREDEFINED", "COMPLIANCE_STANDARD", "CUSTOM", "SQL_FIREWALL_AUDITING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type audit_policy_category: str

        :param audit_policy_name:
            The value to assign to the audit_policy_name property of this AuditPolicyDimensions.
        :type audit_policy_name: str

        :param target_id:
            The value to assign to the target_id property of this AuditPolicyDimensions.
        :type target_id: str

        """
        self.swagger_types = {
            'audit_policy_category': 'str',
            'audit_policy_name': 'str',
            'target_id': 'str'
        }

        self.attribute_map = {
            'audit_policy_category': 'auditPolicyCategory',
            'audit_policy_name': 'auditPolicyName',
            'target_id': 'targetId'
        }

        self._audit_policy_category = None
        self._audit_policy_name = None
        self._target_id = None

    @property
    def audit_policy_category(self):
        """
        Gets the audit_policy_category of this AuditPolicyDimensions.
        The category to which the audit policy belongs.

        Allowed values for this property are: "BASIC_ACTIVITY", "ADMIN_USER_ACTIVITY", "USER_ACTIVITY", "ORACLE_PREDEFINED", "COMPLIANCE_STANDARD", "CUSTOM", "SQL_FIREWALL_AUDITING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The audit_policy_category of this AuditPolicyDimensions.
        :rtype: str
        """
        return self._audit_policy_category

    @audit_policy_category.setter
    def audit_policy_category(self, audit_policy_category):
        """
        Sets the audit_policy_category of this AuditPolicyDimensions.
        The category to which the audit policy belongs.


        :param audit_policy_category: The audit_policy_category of this AuditPolicyDimensions.
        :type: str
        """
        allowed_values = ["BASIC_ACTIVITY", "ADMIN_USER_ACTIVITY", "USER_ACTIVITY", "ORACLE_PREDEFINED", "COMPLIANCE_STANDARD", "CUSTOM", "SQL_FIREWALL_AUDITING"]
        if not value_allowed_none_or_none_sentinel(audit_policy_category, allowed_values):
            audit_policy_category = 'UNKNOWN_ENUM_VALUE'
        self._audit_policy_category = audit_policy_category

    @property
    def audit_policy_name(self):
        """
        Gets the audit_policy_name of this AuditPolicyDimensions.
        The name of the audit policy. Refer to the `documentation`__ for seeded audit policy names. For custom policies, refer to the user-defined policy name created in the target database.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/data-safe&id=UDSCS-GUID-361A9A9A-7C21-4F5A-8945-9B3A0C472827


        :return: The audit_policy_name of this AuditPolicyDimensions.
        :rtype: str
        """
        return self._audit_policy_name

    @audit_policy_name.setter
    def audit_policy_name(self, audit_policy_name):
        """
        Sets the audit_policy_name of this AuditPolicyDimensions.
        The name of the audit policy. Refer to the `documentation`__ for seeded audit policy names. For custom policies, refer to the user-defined policy name created in the target database.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/data-safe&id=UDSCS-GUID-361A9A9A-7C21-4F5A-8945-9B3A0C472827


        :param audit_policy_name: The audit_policy_name of this AuditPolicyDimensions.
        :type: str
        """
        self._audit_policy_name = audit_policy_name

    @property
    def target_id(self):
        """
        Gets the target_id of this AuditPolicyDimensions.
        The OCID of the target database for which the audit policy will be created.


        :return: The target_id of this AuditPolicyDimensions.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this AuditPolicyDimensions.
        The OCID of the target database for which the audit policy will be created.


        :param target_id: The target_id of this AuditPolicyDimensions.
        :type: str
        """
        self._target_id = target_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
