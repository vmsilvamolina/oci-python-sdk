# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SettingsTenantCustomClaims(object):
    """
    Custom claims associated with the specific tenant
    """

    #: A constant which can be used with the mode property of a SettingsTenantCustomClaims.
    #: This constant has a value of "always"
    MODE_ALWAYS = "always"

    #: A constant which can be used with the mode property of a SettingsTenantCustomClaims.
    #: This constant has a value of "request"
    MODE_REQUEST = "request"

    #: A constant which can be used with the mode property of a SettingsTenantCustomClaims.
    #: This constant has a value of "never"
    MODE_NEVER = "never"

    #: A constant which can be used with the token_type property of a SettingsTenantCustomClaims.
    #: This constant has a value of "AT"
    TOKEN_TYPE_AT = "AT"

    #: A constant which can be used with the token_type property of a SettingsTenantCustomClaims.
    #: This constant has a value of "IT"
    TOKEN_TYPE_IT = "IT"

    #: A constant which can be used with the token_type property of a SettingsTenantCustomClaims.
    #: This constant has a value of "BOTH"
    TOKEN_TYPE_BOTH = "BOTH"

    def __init__(self, **kwargs):
        """
        Initializes a new SettingsTenantCustomClaims object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SettingsTenantCustomClaims.
        :type name: str

        :param value:
            The value to assign to the value property of this SettingsTenantCustomClaims.
        :type value: str

        :param mode:
            The value to assign to the mode property of this SettingsTenantCustomClaims.
            Allowed values for this property are: "always", "request", "never", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mode: str

        :param expression:
            The value to assign to the expression property of this SettingsTenantCustomClaims.
        :type expression: bool

        :param all_scopes:
            The value to assign to the all_scopes property of this SettingsTenantCustomClaims.
        :type all_scopes: bool

        :param token_type:
            The value to assign to the token_type property of this SettingsTenantCustomClaims.
            Allowed values for this property are: "AT", "IT", "BOTH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type token_type: str

        :param scopes:
            The value to assign to the scopes property of this SettingsTenantCustomClaims.
        :type scopes: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'value': 'str',
            'mode': 'str',
            'expression': 'bool',
            'all_scopes': 'bool',
            'token_type': 'str',
            'scopes': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value',
            'mode': 'mode',
            'expression': 'expression',
            'all_scopes': 'allScopes',
            'token_type': 'tokenType',
            'scopes': 'scopes'
        }

        self._name = None
        self._value = None
        self._mode = None
        self._expression = None
        self._all_scopes = None
        self._token_type = None
        self._scopes = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SettingsTenantCustomClaims.
        Custom claim name

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: server


        :return: The name of this SettingsTenantCustomClaims.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SettingsTenantCustomClaims.
        Custom claim name

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: server


        :param name: The name of this SettingsTenantCustomClaims.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this SettingsTenantCustomClaims.
        Custom claim value

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this SettingsTenantCustomClaims.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SettingsTenantCustomClaims.
        Custom claim value

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this SettingsTenantCustomClaims.
        :type: str
        """
        self._value = value

    @property
    def mode(self):
        """
        **[Required]** Gets the mode of this SettingsTenantCustomClaims.
        Indicates under what scenario the custom claim will be return

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "always", "request", "never", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The mode of this SettingsTenantCustomClaims.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this SettingsTenantCustomClaims.
        Indicates under what scenario the custom claim will be return

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param mode: The mode of this SettingsTenantCustomClaims.
        :type: str
        """
        allowed_values = ["always", "request", "never"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            mode = 'UNKNOWN_ENUM_VALUE'
        self._mode = mode

    @property
    def expression(self):
        """
        **[Required]** Gets the expression of this SettingsTenantCustomClaims.
        Indicates if the custom claim is an expression

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The expression of this SettingsTenantCustomClaims.
        :rtype: bool
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this SettingsTenantCustomClaims.
        Indicates if the custom claim is an expression

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param expression: The expression of this SettingsTenantCustomClaims.
        :type: bool
        """
        self._expression = expression

    @property
    def all_scopes(self):
        """
        **[Required]** Gets the all_scopes of this SettingsTenantCustomClaims.
        Indicates if the custom claim is associated with all scopes

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The all_scopes of this SettingsTenantCustomClaims.
        :rtype: bool
        """
        return self._all_scopes

    @all_scopes.setter
    def all_scopes(self, all_scopes):
        """
        Sets the all_scopes of this SettingsTenantCustomClaims.
        Indicates if the custom claim is associated with all scopes

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param all_scopes: The all_scopes of this SettingsTenantCustomClaims.
        :type: bool
        """
        self._all_scopes = all_scopes

    @property
    def token_type(self):
        """
        **[Required]** Gets the token_type of this SettingsTenantCustomClaims.
        Indicates what type of token the custom claim will be embedded

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "AT", "IT", "BOTH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The token_type of this SettingsTenantCustomClaims.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this SettingsTenantCustomClaims.
        Indicates what type of token the custom claim will be embedded

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param token_type: The token_type of this SettingsTenantCustomClaims.
        :type: str
        """
        allowed_values = ["AT", "IT", "BOTH"]
        if not value_allowed_none_or_none_sentinel(token_type, allowed_values):
            token_type = 'UNKNOWN_ENUM_VALUE'
        self._token_type = token_type

    @property
    def scopes(self):
        """
        Gets the scopes of this SettingsTenantCustomClaims.
        Scopes associated with a specific custom claim

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The scopes of this SettingsTenantCustomClaims.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this SettingsTenantCustomClaims.
        Scopes associated with a specific custom claim

        **Added In:** 18.4.2

        **SCIM++ Properties:**
         - multiValued: true
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param scopes: The scopes of this SettingsTenantCustomClaims.
        :type: list[str]
        """
        self._scopes = scopes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
