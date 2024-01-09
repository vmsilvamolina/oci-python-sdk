# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230701


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InitialConfiguration(object):
    """
    Details of SDDC initial configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InitialConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param initial_cluster_configurations:
            The value to assign to the initial_cluster_configurations property of this InitialConfiguration.
        :type initial_cluster_configurations: list[oci.ocvp.models.InitialClusterConfiguration]

        """
        self.swagger_types = {
            'initial_cluster_configurations': 'list[InitialClusterConfiguration]'
        }

        self.attribute_map = {
            'initial_cluster_configurations': 'initialClusterConfigurations'
        }

        self._initial_cluster_configurations = None

    @property
    def initial_cluster_configurations(self):
        """
        **[Required]** Gets the initial_cluster_configurations of this InitialConfiguration.
        The configurations for Clusters initially created in the SDDC.


        :return: The initial_cluster_configurations of this InitialConfiguration.
        :rtype: list[oci.ocvp.models.InitialClusterConfiguration]
        """
        return self._initial_cluster_configurations

    @initial_cluster_configurations.setter
    def initial_cluster_configurations(self, initial_cluster_configurations):
        """
        Sets the initial_cluster_configurations of this InitialConfiguration.
        The configurations for Clusters initially created in the SDDC.


        :param initial_cluster_configurations: The initial_cluster_configurations of this InitialConfiguration.
        :type: list[oci.ocvp.models.InitialClusterConfiguration]
        """
        self._initial_cluster_configurations = initial_cluster_configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
