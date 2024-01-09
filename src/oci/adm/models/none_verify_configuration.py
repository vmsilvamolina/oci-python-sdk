# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220421

from .verify_configuration import VerifyConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NoneVerifyConfiguration(VerifyConfiguration):
    """
    Empty verify configuration when no build was selected.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NoneVerifyConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.adm.models.NoneVerifyConfiguration.build_service_type` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param build_service_type:
            The value to assign to the build_service_type property of this NoneVerifyConfiguration.
            Allowed values for this property are: "OCI_DEVOPS_BUILD", "GITLAB_PIPELINE", "GITHUB_ACTIONS", "JENKINS_PIPELINE", "NONE"
        :type build_service_type: str

        """
        self.swagger_types = {
            'build_service_type': 'str'
        }

        self.attribute_map = {
            'build_service_type': 'buildServiceType'
        }

        self._build_service_type = None
        self._build_service_type = 'NONE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
