# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from .authorization_details import AuthorizationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InternalAuthorizationDetails(AuthorizationDetails):
    """
    Specifies the credentials to access the source Oracle Cloud Infrastructure - Classic environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InternalAuthorizationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.application_migration.models.InternalAuthorizationDetails.type` attribute
        of this class is ``INTERNAL_COMPUTE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this InternalAuthorizationDetails.
            Allowed values for this property are: "OCIC", "INTERNAL_COMPUTE"
        :type type: str

        :param username:
            The value to assign to the username property of this InternalAuthorizationDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this InternalAuthorizationDetails.
        :type password: str

        """
        self.swagger_types = {
            'type': 'str',
            'username': 'str',
            'password': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'username': 'username',
            'password': 'password'
        }

        self._type = None
        self._username = None
        self._password = None
        self._type = 'INTERNAL_COMPUTE'

    @property
    def username(self):
        """
        **[Required]** Gets the username of this InternalAuthorizationDetails.
        User with Compute Operations role in Oracle Cloud Infrastructure - Classic.


        :return: The username of this InternalAuthorizationDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this InternalAuthorizationDetails.
        User with Compute Operations role in Oracle Cloud Infrastructure - Classic.


        :param username: The username of this InternalAuthorizationDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this InternalAuthorizationDetails.
        Password for this user.


        :return: The password of this InternalAuthorizationDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this InternalAuthorizationDetails.
        Password for this user.


        :param password: The password of this InternalAuthorizationDetails.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
