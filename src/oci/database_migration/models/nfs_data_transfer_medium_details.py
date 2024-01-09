# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210929

from .data_transfer_medium_details_v2 import DataTransferMediumDetailsV2
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NfsDataTransferMediumDetails(DataTransferMediumDetailsV2):
    """
    OCI Object Storage bucket will be used to store Data Pump dump files for the migration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NfsDataTransferMediumDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.NfsDataTransferMediumDetails.type` attribute
        of this class is ``NFS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this NfsDataTransferMediumDetails.
            Allowed values for this property are: "DBLINK", "OBJECT_STORAGE", "AWS_S3", "NFS"
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None
        self._type = 'NFS'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
