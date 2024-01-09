# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PolicyRules(object):
    """
    Rules assigned to this policy
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PolicyRules object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this PolicyRules.
        :type value: str

        :param ref:
            The value to assign to the ref property of this PolicyRules.
        :type ref: str

        :param sequence:
            The value to assign to the sequence property of this PolicyRules.
        :type sequence: int

        :param name:
            The value to assign to the name property of this PolicyRules.
        :type name: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'sequence': 'int',
            'name': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'sequence': 'sequence',
            'name': 'name'
        }

        self._value = None
        self._ref = None
        self._sequence = None
        self._name = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this PolicyRules.
        Rule identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this PolicyRules.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PolicyRules.
        Rule identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this PolicyRules.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this PolicyRules.
        Rule URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this PolicyRules.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this PolicyRules.
        Rule URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this PolicyRules.
        :type: str
        """
        self._ref = ref

    @property
    def sequence(self):
        """
        **[Required]** Gets the sequence of this PolicyRules.
        Position of the rule in evaluation order. No duplicates allowed.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The sequence of this PolicyRules.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """
        Sets the sequence of this PolicyRules.
        Position of the rule in evaluation order. No duplicates allowed.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param sequence: The sequence of this PolicyRules.
        :type: int
        """
        self._sequence = sequence

    @property
    def name(self):
        """
        Gets the name of this PolicyRules.
        Rule name

        **Added In:** 17.4.2

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :return: The name of this PolicyRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyRules.
        Rule name

        **Added In:** 17.4.2

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: request
         - type: string
         - uniqueness: none


        :param name: The name of this PolicyRules.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
