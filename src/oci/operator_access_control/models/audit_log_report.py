# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditLogReport(object):
    """
    The auditLog report details.
    """

    #: A constant which can be used with the audit_report_status property of a AuditLogReport.
    #: This constant has a value of "NOTAVAILABLE"
    AUDIT_REPORT_STATUS_NOTAVAILABLE = "NOTAVAILABLE"

    #: A constant which can be used with the audit_report_status property of a AuditLogReport.
    #: This constant has a value of "AVAILABLE"
    AUDIT_REPORT_STATUS_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the audit_report_status property of a AuditLogReport.
    #: This constant has a value of "EXPIRED"
    AUDIT_REPORT_STATUS_EXPIRED = "EXPIRED"

    #: A constant which can be used with the audit_report_status property of a AuditLogReport.
    #: This constant has a value of "FAILED"
    AUDIT_REPORT_STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditLogReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param report:
            The value to assign to the report property of this AuditLogReport.
        :type report: str

        :param process_tree:
            The value to assign to the process_tree property of this AuditLogReport.
        :type process_tree: str

        :param audit_report_status:
            The value to assign to the audit_report_status property of this AuditLogReport.
            Allowed values for this property are: "NOTAVAILABLE", "AVAILABLE", "EXPIRED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type audit_report_status: str

        :param time_of_report_generation:
            The value to assign to the time_of_report_generation property of this AuditLogReport.
        :type time_of_report_generation: datetime

        """
        self.swagger_types = {
            'report': 'str',
            'process_tree': 'str',
            'audit_report_status': 'str',
            'time_of_report_generation': 'datetime'
        }

        self.attribute_map = {
            'report': 'report',
            'process_tree': 'processTree',
            'audit_report_status': 'auditReportStatus',
            'time_of_report_generation': 'timeOfReportGeneration'
        }

        self._report = None
        self._process_tree = None
        self._audit_report_status = None
        self._time_of_report_generation = None

    @property
    def report(self):
        """
        Gets the report of this AuditLogReport.
        Contains the report data.


        :return: The report of this AuditLogReport.
        :rtype: str
        """
        return self._report

    @report.setter
    def report(self, report):
        """
        Sets the report of this AuditLogReport.
        Contains the report data.


        :param report: The report of this AuditLogReport.
        :type: str
        """
        self._report = report

    @property
    def process_tree(self):
        """
        Gets the process_tree of this AuditLogReport.
        Contains the process tree data


        :return: The process_tree of this AuditLogReport.
        :rtype: str
        """
        return self._process_tree

    @process_tree.setter
    def process_tree(self, process_tree):
        """
        Sets the process_tree of this AuditLogReport.
        Contains the process tree data


        :param process_tree: The process_tree of this AuditLogReport.
        :type: str
        """
        self._process_tree = process_tree

    @property
    def audit_report_status(self):
        """
        **[Required]** Gets the audit_report_status of this AuditLogReport.
        auditReportStatus for the accessRequestId

        Allowed values for this property are: "NOTAVAILABLE", "AVAILABLE", "EXPIRED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The audit_report_status of this AuditLogReport.
        :rtype: str
        """
        return self._audit_report_status

    @audit_report_status.setter
    def audit_report_status(self, audit_report_status):
        """
        Sets the audit_report_status of this AuditLogReport.
        auditReportStatus for the accessRequestId


        :param audit_report_status: The audit_report_status of this AuditLogReport.
        :type: str
        """
        allowed_values = ["NOTAVAILABLE", "AVAILABLE", "EXPIRED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(audit_report_status, allowed_values):
            audit_report_status = 'UNKNOWN_ENUM_VALUE'
        self._audit_report_status = audit_report_status

    @property
    def time_of_report_generation(self):
        """
        Gets the time_of_report_generation of this AuditLogReport.
        Time when the audit report was generated `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_report_generation of this AuditLogReport.
        :rtype: datetime
        """
        return self._time_of_report_generation

    @time_of_report_generation.setter
    def time_of_report_generation(self, time_of_report_generation):
        """
        Sets the time_of_report_generation of this AuditLogReport.
        Time when the audit report was generated `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_report_generation: The time_of_report_generation of this AuditLogReport.
        :type: datetime
        """
        self._time_of_report_generation = time_of_report_generation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
