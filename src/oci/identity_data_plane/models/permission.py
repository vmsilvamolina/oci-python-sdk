# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Permission(object):
    """
    Permission model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Permission object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param p:
            The value to assign to the p property of this Permission.
        :type p: str

        """
        self.swagger_types = {
            'p': 'str'
        }

        self.attribute_map = {
            'p': 'p'
        }

        self._p = None

    @property
    def p(self):
        """
        **[Required]** Gets the p of this Permission.
        The name of the permission.


        :return: The p of this Permission.
        :rtype: str
        """
        return self._p

    @p.setter
    def p(self, p):
        """
        Sets the p of this Permission.
        The name of the permission.


        :param p: The p of this Permission.
        :type: str
        """
        self._p = p

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
