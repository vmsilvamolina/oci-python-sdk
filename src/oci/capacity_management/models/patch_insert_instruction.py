# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107

from .patch_instruction import PatchInstruction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchInsertInstruction(PatchInstruction):
    """
    An operation that inserts a value into an array, shifting array items as necessary and handling NOT_FOUND exceptions by creating the implied containing structure.
    """

    #: A constant which can be used with the position property of a PatchInsertInstruction.
    #: This constant has a value of "BEFORE"
    POSITION_BEFORE = "BEFORE"

    #: A constant which can be used with the position property of a PatchInsertInstruction.
    #: This constant has a value of "AFTER"
    POSITION_AFTER = "AFTER"

    def __init__(self, **kwargs):
        """
        Initializes a new PatchInsertInstruction object with values from keyword arguments. The default value of the :py:attr:`~oci.capacity_management.models.PatchInsertInstruction.operation` attribute
        of this class is ``INSERT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PatchInsertInstruction.
            Allowed values for this property are: "REQUIRE", "PROHIBIT", "REPLACE", "INSERT", "REMOVE", "MOVE", "MERGE"
        :type operation: str

        :param selection:
            The value to assign to the selection property of this PatchInsertInstruction.
        :type selection: str

        :param value:
            The value to assign to the value property of this PatchInsertInstruction.
        :type value: object

        :param selected_item:
            The value to assign to the selected_item property of this PatchInsertInstruction.
        :type selected_item: str

        :param position:
            The value to assign to the position property of this PatchInsertInstruction.
            Allowed values for this property are: "BEFORE", "AFTER"
        :type position: str

        """
        self.swagger_types = {
            'operation': 'str',
            'selection': 'str',
            'value': 'object',
            'selected_item': 'str',
            'position': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'selection': 'selection',
            'value': 'value',
            'selected_item': 'selectedItem',
            'position': 'position'
        }

        self._operation = None
        self._selection = None
        self._value = None
        self._selected_item = None
        self._position = None
        self._operation = 'INSERT'

    @property
    def value(self):
        """
        **[Required]** Gets the value of this PatchInsertInstruction.
        A value to be inserted into the target.


        :return: The value of this PatchInsertInstruction.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PatchInsertInstruction.
        A value to be inserted into the target.


        :param value: The value of this PatchInsertInstruction.
        :type: object
        """
        self._value = value

    @property
    def selected_item(self):
        """
        Gets the selected_item of this PatchInsertInstruction.
        A selection to be evaluated against the array for identifying a particular reference item within it, with the same format and semantics as `selection`.


        :return: The selected_item of this PatchInsertInstruction.
        :rtype: str
        """
        return self._selected_item

    @selected_item.setter
    def selected_item(self, selected_item):
        """
        Sets the selected_item of this PatchInsertInstruction.
        A selection to be evaluated against the array for identifying a particular reference item within it, with the same format and semantics as `selection`.


        :param selected_item: The selected_item of this PatchInsertInstruction.
        :type: str
        """
        self._selected_item = selected_item

    @property
    def position(self):
        """
        Gets the position of this PatchInsertInstruction.
        Where to insert the value, relative to the first item matched by `selectedItem`.
        If `selectedItem` is unspecified, then \"BEFORE\" specifies insertion at the first position in an array and \"AFTER\" specifies insertion at the last position.
        If `selectedItem` is specified but results in an empty selection, then both values specify insertion at the last position.

        Allowed values for this property are: "BEFORE", "AFTER"


        :return: The position of this PatchInsertInstruction.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this PatchInsertInstruction.
        Where to insert the value, relative to the first item matched by `selectedItem`.
        If `selectedItem` is unspecified, then \"BEFORE\" specifies insertion at the first position in an array and \"AFTER\" specifies insertion at the last position.
        If `selectedItem` is specified but results in an empty selection, then both values specify insertion at the last position.


        :param position: The position of this PatchInsertInstruction.
        :type: str
        """
        allowed_values = ["BEFORE", "AFTER"]
        if not value_allowed_none_or_none_sentinel(position, allowed_values):
            raise ValueError(
                f"Invalid value for `position`, must be None or one of {allowed_values}"
            )
        self._position = position

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
