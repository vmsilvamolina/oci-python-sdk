# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionPasswordlessUser(object):
    """
    This extension defines attributes used to manage Passwordless-Factor Authentication within a service provider. The extension is typically applied to a User resource, but MAY be applied to other resources that use MFA.
    """

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "EMAIL"
    FACTOR_TYPE_EMAIL = "EMAIL"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "SMS"
    FACTOR_TYPE_SMS = "SMS"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "PHONE_CALL"
    FACTOR_TYPE_PHONE_CALL = "PHONE_CALL"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "TOTP"
    FACTOR_TYPE_TOTP = "TOTP"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "PUSH"
    FACTOR_TYPE_PUSH = "PUSH"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "OFFLINETOTP"
    FACTOR_TYPE_OFFLINETOTP = "OFFLINETOTP"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "SECURITY_QUESTIONS"
    FACTOR_TYPE_SECURITY_QUESTIONS = "SECURITY_QUESTIONS"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "VOICE"
    FACTOR_TYPE_VOICE = "VOICE"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "USERNAME_PASSWORD"
    FACTOR_TYPE_USERNAME_PASSWORD = "USERNAME_PASSWORD"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "THIRDPARTY"
    FACTOR_TYPE_THIRDPARTY = "THIRDPARTY"

    #: A constant which can be used with the factor_type property of a ExtensionPasswordlessUser.
    #: This constant has a value of "FIDO_AUTHENTICATOR"
    FACTOR_TYPE_FIDO_AUTHENTICATOR = "FIDO_AUTHENTICATOR"

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionPasswordlessUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param factor_type:
            The value to assign to the factor_type property of this ExtensionPasswordlessUser.
            Allowed values for this property are: "EMAIL", "SMS", "PHONE_CALL", "TOTP", "PUSH", "OFFLINETOTP", "SECURITY_QUESTIONS", "VOICE", "USERNAME_PASSWORD", "THIRDPARTY", "FIDO_AUTHENTICATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type factor_type: str

        :param factor_method:
            The value to assign to the factor_method property of this ExtensionPasswordlessUser.
        :type factor_method: str

        :param factor_identifier:
            The value to assign to the factor_identifier property of this ExtensionPasswordlessUser.
        :type factor_identifier: oci.identity_domains.models.UserExtFactorIdentifier

        """
        self.swagger_types = {
            'factor_type': 'str',
            'factor_method': 'str',
            'factor_identifier': 'UserExtFactorIdentifier'
        }

        self.attribute_map = {
            'factor_type': 'factorType',
            'factor_method': 'factorMethod',
            'factor_identifier': 'factorIdentifier'
        }

        self._factor_type = None
        self._factor_method = None
        self._factor_identifier = None

    @property
    def factor_type(self):
        """
        Gets the factor_type of this ExtensionPasswordlessUser.
        Authentication Factor Type

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "EMAIL", "SMS", "PHONE_CALL", "TOTP", "PUSH", "OFFLINETOTP", "SECURITY_QUESTIONS", "VOICE", "USERNAME_PASSWORD", "THIRDPARTY", "FIDO_AUTHENTICATOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The factor_type of this ExtensionPasswordlessUser.
        :rtype: str
        """
        return self._factor_type

    @factor_type.setter
    def factor_type(self, factor_type):
        """
        Sets the factor_type of this ExtensionPasswordlessUser.
        Authentication Factor Type

        **Added In:** 20.1.3

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param factor_type: The factor_type of this ExtensionPasswordlessUser.
        :type: str
        """
        allowed_values = ["EMAIL", "SMS", "PHONE_CALL", "TOTP", "PUSH", "OFFLINETOTP", "SECURITY_QUESTIONS", "VOICE", "USERNAME_PASSWORD", "THIRDPARTY", "FIDO_AUTHENTICATOR"]
        if not value_allowed_none_or_none_sentinel(factor_type, allowed_values):
            factor_type = 'UNKNOWN_ENUM_VALUE'
        self._factor_type = factor_type

    @property
    def factor_method(self):
        """
        Gets the factor_method of this ExtensionPasswordlessUser.
        Authentication Factor Method

        **Added In:** 2009232244

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The factor_method of this ExtensionPasswordlessUser.
        :rtype: str
        """
        return self._factor_method

    @factor_method.setter
    def factor_method(self, factor_method):
        """
        Sets the factor_method of this ExtensionPasswordlessUser.
        Authentication Factor Method

        **Added In:** 2009232244

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param factor_method: The factor_method of this ExtensionPasswordlessUser.
        :type: str
        """
        self._factor_method = factor_method

    @property
    def factor_identifier(self):
        """
        Gets the factor_identifier of this ExtensionPasswordlessUser.

        :return: The factor_identifier of this ExtensionPasswordlessUser.
        :rtype: oci.identity_domains.models.UserExtFactorIdentifier
        """
        return self._factor_identifier

    @factor_identifier.setter
    def factor_identifier(self, factor_identifier):
        """
        Sets the factor_identifier of this ExtensionPasswordlessUser.

        :param factor_identifier: The factor_identifier of this ExtensionPasswordlessUser.
        :type: oci.identity_domains.models.UserExtFactorIdentifier
        """
        self._factor_identifier = factor_identifier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
