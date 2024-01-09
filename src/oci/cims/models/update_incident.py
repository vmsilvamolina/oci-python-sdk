# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIncident(object):
    """
    Details about the support ticket being updated.
    """

    #: A constant which can be used with the problem_type property of a UpdateIncident.
    #: This constant has a value of "LIMIT"
    PROBLEM_TYPE_LIMIT = "LIMIT"

    #: A constant which can be used with the problem_type property of a UpdateIncident.
    #: This constant has a value of "LEGACY_LIMIT"
    PROBLEM_TYPE_LEGACY_LIMIT = "LEGACY_LIMIT"

    #: A constant which can be used with the problem_type property of a UpdateIncident.
    #: This constant has a value of "TECH"
    PROBLEM_TYPE_TECH = "TECH"

    #: A constant which can be used with the problem_type property of a UpdateIncident.
    #: This constant has a value of "ACCOUNT"
    PROBLEM_TYPE_ACCOUNT = "ACCOUNT"

    #: A constant which can be used with the problem_type property of a UpdateIncident.
    #: This constant has a value of "TAXONOMY"
    PROBLEM_TYPE_TAXONOMY = "TAXONOMY"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIncident object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ticket:
            The value to assign to the ticket property of this UpdateIncident.
        :type ticket: oci.cims.models.UpdateTicketDetails

        :param problem_type:
            The value to assign to the problem_type property of this UpdateIncident.
            Allowed values for this property are: "LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT", "TAXONOMY"
        :type problem_type: str

        """
        self.swagger_types = {
            'ticket': 'UpdateTicketDetails',
            'problem_type': 'str'
        }

        self.attribute_map = {
            'ticket': 'ticket',
            'problem_type': 'problemType'
        }

        self._ticket = None
        self._problem_type = None

    @property
    def ticket(self):
        """
        **[Required]** Gets the ticket of this UpdateIncident.

        :return: The ticket of this UpdateIncident.
        :rtype: oci.cims.models.UpdateTicketDetails
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """
        Sets the ticket of this UpdateIncident.

        :param ticket: The ticket of this UpdateIncident.
        :type: oci.cims.models.UpdateTicketDetails
        """
        self._ticket = ticket

    @property
    def problem_type(self):
        """
        Gets the problem_type of this UpdateIncident.
        The kind of support ticket, such as a technical support request or a limit increase request.

        Allowed values for this property are: "LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT", "TAXONOMY"


        :return: The problem_type of this UpdateIncident.
        :rtype: str
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """
        Sets the problem_type of this UpdateIncident.
        The kind of support ticket, such as a technical support request or a limit increase request.


        :param problem_type: The problem_type of this UpdateIncident.
        :type: str
        """
        allowed_values = ["LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT", "TAXONOMY"]
        if not value_allowed_none_or_none_sentinel(problem_type, allowed_values):
            raise ValueError(
                f"Invalid value for `problem_type`, must be None or one of {allowed_values}"
            )
        self._problem_type = problem_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
