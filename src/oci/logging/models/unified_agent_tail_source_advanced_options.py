# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentTailSourceAdvancedOptions(object):
    """
    Advanced options for logging configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentTailSourceAdvancedOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_read_from_head:
            The value to assign to the is_read_from_head property of this UnifiedAgentTailSourceAdvancedOptions.
        :type is_read_from_head: bool

        """
        self.swagger_types = {
            'is_read_from_head': 'bool'
        }

        self.attribute_map = {
            'is_read_from_head': 'isReadFromHead'
        }

        self._is_read_from_head = None

    @property
    def is_read_from_head(self):
        """
        Gets the is_read_from_head of this UnifiedAgentTailSourceAdvancedOptions.
        Starts to read the logs from the head of the file or the last read position recorded in pos_file, not tail.


        :return: The is_read_from_head of this UnifiedAgentTailSourceAdvancedOptions.
        :rtype: bool
        """
        return self._is_read_from_head

    @is_read_from_head.setter
    def is_read_from_head(self, is_read_from_head):
        """
        Sets the is_read_from_head of this UnifiedAgentTailSourceAdvancedOptions.
        Starts to read the logs from the head of the file or the last read position recorded in pos_file, not tail.


        :param is_read_from_head: The is_read_from_head of this UnifiedAgentTailSourceAdvancedOptions.
        :type: bool
        """
        self._is_read_from_head = is_read_from_head

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
