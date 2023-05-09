# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateGovernanceInstanceDetails(object):
    """
    The details of a GovernanceInstance to be updated.
    """

    #: A constant which can be used with the license_type property of a UpdateGovernanceInstanceDetails.
    #: This constant has a value of "NEW_LICENSE"
    LICENSE_TYPE_NEW_LICENSE = "NEW_LICENSE"

    #: A constant which can be used with the license_type property of a UpdateGovernanceInstanceDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the license_type property of a UpdateGovernanceInstanceDetails.
    #: This constant has a value of "AG_ORACLE_WORKLOADS"
    LICENSE_TYPE_AG_ORACLE_WORKLOADS = "AG_ORACLE_WORKLOADS"

    #: A constant which can be used with the license_type property of a UpdateGovernanceInstanceDetails.
    #: This constant has a value of "AG_OCI"
    LICENSE_TYPE_AG_OCI = "AG_OCI"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateGovernanceInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateGovernanceInstanceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateGovernanceInstanceDetails.
        :type description: str

        :param license_type:
            The value to assign to the license_type property of this UpdateGovernanceInstanceDetails.
            Allowed values for this property are: "NEW_LICENSE", "BRING_YOUR_OWN_LICENSE", "AG_ORACLE_WORKLOADS", "AG_OCI"
        :type license_type: str

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateGovernanceInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateGovernanceInstanceDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'license_type': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'license_type': 'licenseType',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._display_name = None
        self._description = None
        self._license_type = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateGovernanceInstanceDetails.
        The name for the GovernanceInstance.


        :return: The display_name of this UpdateGovernanceInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateGovernanceInstanceDetails.
        The name for the GovernanceInstance.


        :param display_name: The display_name of this UpdateGovernanceInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateGovernanceInstanceDetails.
        The description of the GovernanceInstance.


        :return: The description of this UpdateGovernanceInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateGovernanceInstanceDetails.
        The description of the GovernanceInstance.


        :param description: The description of this UpdateGovernanceInstanceDetails.
        :type: str
        """
        self._description = description

    @property
    def license_type(self):
        """
        Gets the license_type of this UpdateGovernanceInstanceDetails.
        The licenseType being used.

        Allowed values for this property are: "NEW_LICENSE", "BRING_YOUR_OWN_LICENSE", "AG_ORACLE_WORKLOADS", "AG_OCI"


        :return: The license_type of this UpdateGovernanceInstanceDetails.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this UpdateGovernanceInstanceDetails.
        The licenseType being used.


        :param license_type: The license_type of this UpdateGovernanceInstanceDetails.
        :type: str
        """
        allowed_values = ["NEW_LICENSE", "BRING_YOUR_OWN_LICENSE", "AG_ORACLE_WORKLOADS", "AG_OCI"]
        if not value_allowed_none_or_none_sentinel(license_type, allowed_values):
            raise ValueError(
                "Invalid value for `license_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._license_type = license_type

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateGovernanceInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateGovernanceInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateGovernanceInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateGovernanceInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateGovernanceInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateGovernanceInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateGovernanceInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateGovernanceInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
