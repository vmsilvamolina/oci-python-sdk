# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveFsuCollectionTargetsDetails(object):
    """
    Remove targets from a Exadata Fleet Update Collection.
    """

    #: A constant which can be used with the removal_strategy property of a RemoveFsuCollectionTargetsDetails.
    #: This constant has a value of "TARGET_IDS"
    REMOVAL_STRATEGY_TARGET_IDS = "TARGET_IDS"

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveFsuCollectionTargetsDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fleet_software_update.models.TargetIdsRemoveTargetsDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param removal_strategy:
            The value to assign to the removal_strategy property of this RemoveFsuCollectionTargetsDetails.
            Allowed values for this property are: "TARGET_IDS"
        :type removal_strategy: str

        """
        self.swagger_types = {
            'removal_strategy': 'str'
        }

        self.attribute_map = {
            'removal_strategy': 'removalStrategy'
        }

        self._removal_strategy = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['removalStrategy']

        if type == 'TARGET_IDS':
            return 'TargetIdsRemoveTargetsDetails'
        else:
            return 'RemoveFsuCollectionTargetsDetails'

    @property
    def removal_strategy(self):
        """
        **[Required]** Gets the removal_strategy of this RemoveFsuCollectionTargetsDetails.
        Strategy to follow for removal of targets:
        TARGET_IDS: Remove a list of targets

        Allowed values for this property are: "TARGET_IDS"


        :return: The removal_strategy of this RemoveFsuCollectionTargetsDetails.
        :rtype: str
        """
        return self._removal_strategy

    @removal_strategy.setter
    def removal_strategy(self, removal_strategy):
        """
        Sets the removal_strategy of this RemoveFsuCollectionTargetsDetails.
        Strategy to follow for removal of targets:
        TARGET_IDS: Remove a list of targets


        :param removal_strategy: The removal_strategy of this RemoveFsuCollectionTargetsDetails.
        :type: str
        """
        allowed_values = ["TARGET_IDS"]
        if not value_allowed_none_or_none_sentinel(removal_strategy, allowed_values):
            raise ValueError(
                f"Invalid value for `removal_strategy`, must be None or one of {allowed_values}"
            )
        self._removal_strategy = removal_strategy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
