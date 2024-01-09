# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190131

from .network_endpoint_details import NetworkEndpointDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublicEndpointDetails(NetworkEndpointDetails):
    """
    Public endpoint configuration details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PublicEndpointDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.integration.models.PublicEndpointDetails.network_endpoint_type` attribute
        of this class is ``PUBLIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_endpoint_type:
            The value to assign to the network_endpoint_type property of this PublicEndpointDetails.
            Allowed values for this property are: "PUBLIC"
        :type network_endpoint_type: str

        :param allowlisted_http_ips:
            The value to assign to the allowlisted_http_ips property of this PublicEndpointDetails.
        :type allowlisted_http_ips: list[str]

        :param allowlisted_http_vcns:
            The value to assign to the allowlisted_http_vcns property of this PublicEndpointDetails.
        :type allowlisted_http_vcns: list[oci.integration.models.VirtualCloudNetwork]

        :param is_integration_vcn_allowlisted:
            The value to assign to the is_integration_vcn_allowlisted property of this PublicEndpointDetails.
        :type is_integration_vcn_allowlisted: bool

        """
        self.swagger_types = {
            'network_endpoint_type': 'str',
            'allowlisted_http_ips': 'list[str]',
            'allowlisted_http_vcns': 'list[VirtualCloudNetwork]',
            'is_integration_vcn_allowlisted': 'bool'
        }

        self.attribute_map = {
            'network_endpoint_type': 'networkEndpointType',
            'allowlisted_http_ips': 'allowlistedHttpIps',
            'allowlisted_http_vcns': 'allowlistedHttpVcns',
            'is_integration_vcn_allowlisted': 'isIntegrationVcnAllowlisted'
        }

        self._network_endpoint_type = None
        self._allowlisted_http_ips = None
        self._allowlisted_http_vcns = None
        self._is_integration_vcn_allowlisted = None
        self._network_endpoint_type = 'PUBLIC'

    @property
    def allowlisted_http_ips(self):
        """
        Gets the allowlisted_http_ips of this PublicEndpointDetails.
        Source IP addresses or IP address ranges ingress rules. (ex: \"168.122.59.5\", \"10.20.30.0/26\")
        An invalid IP or CIDR block will result in a 400 response.


        :return: The allowlisted_http_ips of this PublicEndpointDetails.
        :rtype: list[str]
        """
        return self._allowlisted_http_ips

    @allowlisted_http_ips.setter
    def allowlisted_http_ips(self, allowlisted_http_ips):
        """
        Sets the allowlisted_http_ips of this PublicEndpointDetails.
        Source IP addresses or IP address ranges ingress rules. (ex: \"168.122.59.5\", \"10.20.30.0/26\")
        An invalid IP or CIDR block will result in a 400 response.


        :param allowlisted_http_ips: The allowlisted_http_ips of this PublicEndpointDetails.
        :type: list[str]
        """
        self._allowlisted_http_ips = allowlisted_http_ips

    @property
    def allowlisted_http_vcns(self):
        """
        Gets the allowlisted_http_vcns of this PublicEndpointDetails.
        Virtual Cloud Networks allowed to access this network endpoint.


        :return: The allowlisted_http_vcns of this PublicEndpointDetails.
        :rtype: list[oci.integration.models.VirtualCloudNetwork]
        """
        return self._allowlisted_http_vcns

    @allowlisted_http_vcns.setter
    def allowlisted_http_vcns(self, allowlisted_http_vcns):
        """
        Sets the allowlisted_http_vcns of this PublicEndpointDetails.
        Virtual Cloud Networks allowed to access this network endpoint.


        :param allowlisted_http_vcns: The allowlisted_http_vcns of this PublicEndpointDetails.
        :type: list[oci.integration.models.VirtualCloudNetwork]
        """
        self._allowlisted_http_vcns = allowlisted_http_vcns

    @property
    def is_integration_vcn_allowlisted(self):
        """
        Gets the is_integration_vcn_allowlisted of this PublicEndpointDetails.
        The Integration service's VCN is allow-listed to allow integrations to call back into other integrations


        :return: The is_integration_vcn_allowlisted of this PublicEndpointDetails.
        :rtype: bool
        """
        return self._is_integration_vcn_allowlisted

    @is_integration_vcn_allowlisted.setter
    def is_integration_vcn_allowlisted(self, is_integration_vcn_allowlisted):
        """
        Sets the is_integration_vcn_allowlisted of this PublicEndpointDetails.
        The Integration service's VCN is allow-listed to allow integrations to call back into other integrations


        :param is_integration_vcn_allowlisted: The is_integration_vcn_allowlisted of this PublicEndpointDetails.
        :type: bool
        """
        self._is_integration_vcn_allowlisted = is_integration_vcn_allowlisted

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
