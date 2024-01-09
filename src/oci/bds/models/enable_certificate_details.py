# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnableCertificateDetails(object):
    """
    The request body info about configure certificate service list.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EnableCertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this EnableCertificateDetails.
        :type cluster_admin_password: str

        :param services:
            The value to assign to the services property of this EnableCertificateDetails.
        :type services: list[oci.bds.models.Service]

        :param root_certificate:
            The value to assign to the root_certificate property of this EnableCertificateDetails.
        :type root_certificate: str

        :param host_cert_details:
            The value to assign to the host_cert_details property of this EnableCertificateDetails.
        :type host_cert_details: list[oci.bds.models.HostCertDetails]

        :param server_key_password:
            The value to assign to the server_key_password property of this EnableCertificateDetails.
        :type server_key_password: str

        """
        self.swagger_types = {
            'cluster_admin_password': 'str',
            'services': 'list[Service]',
            'root_certificate': 'str',
            'host_cert_details': 'list[HostCertDetails]',
            'server_key_password': 'str'
        }

        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword',
            'services': 'services',
            'root_certificate': 'rootCertificate',
            'host_cert_details': 'hostCertDetails',
            'server_key_password': 'serverKeyPassword'
        }

        self._cluster_admin_password = None
        self._services = None
        self._root_certificate = None
        self._host_cert_details = None
        self._server_key_password = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this EnableCertificateDetails.
        Base-64 encoded password for the cluster admin user.


        :return: The cluster_admin_password of this EnableCertificateDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this EnableCertificateDetails.
        Base-64 encoded password for the cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this EnableCertificateDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def services(self):
        """
        **[Required]** Gets the services of this EnableCertificateDetails.
        List of services for which certificate needs to be enabled.


        :return: The services of this EnableCertificateDetails.
        :rtype: list[oci.bds.models.Service]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this EnableCertificateDetails.
        List of services for which certificate needs to be enabled.


        :param services: The services of this EnableCertificateDetails.
        :type: list[oci.bds.models.Service]
        """
        self._services = services

    @property
    def root_certificate(self):
        """
        Gets the root_certificate of this EnableCertificateDetails.
        Plain text certificate/s in order, separated by new line character. If not provided in request a self-signed root certificate is generated inside the cluster. In case hostCertDetails is provided, root certificate is mandatory.


        :return: The root_certificate of this EnableCertificateDetails.
        :rtype: str
        """
        return self._root_certificate

    @root_certificate.setter
    def root_certificate(self, root_certificate):
        """
        Sets the root_certificate of this EnableCertificateDetails.
        Plain text certificate/s in order, separated by new line character. If not provided in request a self-signed root certificate is generated inside the cluster. In case hostCertDetails is provided, root certificate is mandatory.


        :param root_certificate: The root_certificate of this EnableCertificateDetails.
        :type: str
        """
        self._root_certificate = root_certificate

    @property
    def host_cert_details(self):
        """
        Gets the host_cert_details of this EnableCertificateDetails.
        List of leaf certificates to use for services on each host. If custom host certificate is provided the root certificate becomes required.


        :return: The host_cert_details of this EnableCertificateDetails.
        :rtype: list[oci.bds.models.HostCertDetails]
        """
        return self._host_cert_details

    @host_cert_details.setter
    def host_cert_details(self, host_cert_details):
        """
        Sets the host_cert_details of this EnableCertificateDetails.
        List of leaf certificates to use for services on each host. If custom host certificate is provided the root certificate becomes required.


        :param host_cert_details: The host_cert_details of this EnableCertificateDetails.
        :type: list[oci.bds.models.HostCertDetails]
        """
        self._host_cert_details = host_cert_details

    @property
    def server_key_password(self):
        """
        Gets the server_key_password of this EnableCertificateDetails.
        Base-64 encoded password for CA certificate's private key. This value can be empty.


        :return: The server_key_password of this EnableCertificateDetails.
        :rtype: str
        """
        return self._server_key_password

    @server_key_password.setter
    def server_key_password(self, server_key_password):
        """
        Sets the server_key_password of this EnableCertificateDetails.
        Base-64 encoded password for CA certificate's private key. This value can be empty.


        :param server_key_password: The server_key_password of this EnableCertificateDetails.
        :type: str
        """
        self._server_key_password = server_key_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
