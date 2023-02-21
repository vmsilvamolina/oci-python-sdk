# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchInstruction(object):
    """
    A single instruction to be included as part of Patch request content.
    """

    #: A constant which can be used with the operation property of a PatchInstruction.
    #: This constant has a value of "MERGE"
    OPERATION_MERGE = "MERGE"

    def __init__(self, **kwargs):
        """
        Initializes a new PatchInstruction object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.PatchMergeInstruction`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PatchInstruction.
            Allowed values for this property are: "MERGE"
        :type operation: str

        :param selection:
            The value to assign to the selection property of this PatchInstruction.
        :type selection: str

        """
        self.swagger_types = {
            'operation': 'str',
            'selection': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'selection': 'selection'
        }

        self._operation = None
        self._selection = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['operation']

        if type == 'MERGE':
            return 'PatchMergeInstruction'
        else:
            return 'PatchInstruction'

    @property
    def operation(self):
        """
        **[Required]** Gets the operation of this PatchInstruction.
        The type of operation.

        Allowed values for this property are: "MERGE"


        :return: The operation of this PatchInstruction.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this PatchInstruction.
        The type of operation.


        :param operation: The operation of this PatchInstruction.
        :type: str
        """
        allowed_values = ["MERGE"]
        if not value_allowed_none_or_none_sentinel(operation, allowed_values):
            raise ValueError(
                "Invalid value for `operation`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._operation = operation

    @property
    def selection(self):
        """
        **[Required]** Gets the selection of this PatchInstruction.
        The set of values to which the operation applies as a `JMESPath expression`__ for evaluation against the context resource.
        An operation fails if the selection yields an exception, except as otherwise specified.
        Note that comparisons involving non-primitive values (objects or arrays) are not supported and will always evaluate to false.

        __ https://jmespath.org/specification.html


        :return: The selection of this PatchInstruction.
        :rtype: str
        """
        return self._selection

    @selection.setter
    def selection(self, selection):
        """
        Sets the selection of this PatchInstruction.
        The set of values to which the operation applies as a `JMESPath expression`__ for evaluation against the context resource.
        An operation fails if the selection yields an exception, except as otherwise specified.
        Note that comparisons involving non-primitive values (objects or arrays) are not supported and will always evaluate to false.

        __ https://jmespath.org/specification.html


        :param selection: The selection of this PatchInstruction.
        :type: str
        """
        self._selection = selection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
