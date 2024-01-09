# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppProtectableSecondaryAudiences(object):
    """
    A list of secondary audiences--additional URIs to be added automatically to any OAuth token that allows access to this App. Note: This attribute is used mainly for backward compatibility in certain Oracle Public Cloud Apps.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppProtectableSecondaryAudiences object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this AppProtectableSecondaryAudiences.
        :type value: str

        :param read_only:
            The value to assign to the read_only property of this AppProtectableSecondaryAudiences.
        :type read_only: bool

        """
        self.swagger_types = {
            'value': 'str',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'value': 'value',
            'read_only': 'readOnly'
        }

        self._value = None
        self._read_only = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AppProtectableSecondaryAudiences.
        The value of an secondary audience--additional URI to be added automatically to any OAuth token that allows access to this App.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this AppProtectableSecondaryAudiences.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppProtectableSecondaryAudiences.
        The value of an secondary audience--additional URI to be added automatically to any OAuth token that allows access to this App.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this AppProtectableSecondaryAudiences.
        :type: str
        """
        self._value = value

    @property
    def read_only(self):
        """
        Gets the read_only of this AppProtectableSecondaryAudiences.
        If true, indicates that this value must be protected.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :return: The read_only of this AppProtectableSecondaryAudiences.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this AppProtectableSecondaryAudiences.
        If true, indicates that this value must be protected.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: boolean
         - uniqueness: none


        :param read_only: The read_only of this AppProtectableSecondaryAudiences.
        :type: bool
        """
        self._read_only = read_only

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
