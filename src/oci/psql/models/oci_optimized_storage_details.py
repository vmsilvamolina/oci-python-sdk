# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915

from .storage_details import StorageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OciOptimizedStorageDetails(StorageDetails):
    """
    Storage details of the database system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OciOptimizedStorageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.psql.models.OciOptimizedStorageDetails.system_type` attribute
        of this class is ``OCI_OPTIMIZED_STORAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param system_type:
            The value to assign to the system_type property of this OciOptimizedStorageDetails.
        :type system_type: str

        :param is_regionally_durable:
            The value to assign to the is_regionally_durable property of this OciOptimizedStorageDetails.
        :type is_regionally_durable: bool

        :param availability_domain:
            The value to assign to the availability_domain property of this OciOptimizedStorageDetails.
        :type availability_domain: str

        :param iops:
            The value to assign to the iops property of this OciOptimizedStorageDetails.
        :type iops: int

        """
        self.swagger_types = {
            'system_type': 'str',
            'is_regionally_durable': 'bool',
            'availability_domain': 'str',
            'iops': 'int'
        }

        self.attribute_map = {
            'system_type': 'systemType',
            'is_regionally_durable': 'isRegionallyDurable',
            'availability_domain': 'availabilityDomain',
            'iops': 'iops'
        }

        self._system_type = None
        self._is_regionally_durable = None
        self._availability_domain = None
        self._iops = None
        self._system_type = 'OCI_OPTIMIZED_STORAGE'

    @property
    def iops(self):
        """
        Gets the iops of this OciOptimizedStorageDetails.
        Guaranteed input/output storage requests per second (IOPS) available to the database system.


        :return: The iops of this OciOptimizedStorageDetails.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """
        Sets the iops of this OciOptimizedStorageDetails.
        Guaranteed input/output storage requests per second (IOPS) available to the database system.


        :param iops: The iops of this OciOptimizedStorageDetails.
        :type: int
        """
        self._iops = iops

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
