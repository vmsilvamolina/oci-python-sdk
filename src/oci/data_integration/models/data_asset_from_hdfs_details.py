# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .data_asset import DataAsset
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAssetFromHdfsDetails(DataAsset):
    """
    Details for the HDFS data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAssetFromHdfsDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DataAssetFromHdfsDetails.model_type` attribute
        of this class is ``HDFS_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataAssetFromHdfsDetails.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_DATA_ASSET", "ORACLE_PEOPLESOFT_DATA_ASSET", "ORACLE_SIEBEL_DATA_ASSET", "ORACLE_EBS_DATA_ASSET", "HDFS_DATA_ASSET", "MYSQL_HEATWAVE_DATA_ASSET", "REST_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataAssetFromHdfsDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataAssetFromHdfsDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DataAssetFromHdfsDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this DataAssetFromHdfsDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DataAssetFromHdfsDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataAssetFromHdfsDetails.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this DataAssetFromHdfsDetails.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this DataAssetFromHdfsDetails.
        :type asset_properties: dict(str, str)

        :param native_type_system:
            The value to assign to the native_type_system property of this DataAssetFromHdfsDetails.
        :type native_type_system: oci.data_integration.models.TypeSystem

        :param object_version:
            The value to assign to the object_version property of this DataAssetFromHdfsDetails.
        :type object_version: int

        :param parent_ref:
            The value to assign to the parent_ref property of this DataAssetFromHdfsDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param metadata:
            The value to assign to the metadata property of this DataAssetFromHdfsDetails.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this DataAssetFromHdfsDetails.
        :type key_map: dict(str, str)

        :param host:
            The value to assign to the host property of this DataAssetFromHdfsDetails.
        :type host: str

        :param port:
            The value to assign to the port property of this DataAssetFromHdfsDetails.
        :type port: str

        :param protocol:
            The value to assign to the protocol property of this DataAssetFromHdfsDetails.
        :type protocol: str

        :param validate_certificate:
            The value to assign to the validate_certificate property of this DataAssetFromHdfsDetails.
        :type validate_certificate: bool

        :param default_connection:
            The value to assign to the default_connection property of this DataAssetFromHdfsDetails.
        :type default_connection: oci.data_integration.models.ConnectionFromHdfsDetails

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'native_type_system': 'TypeSystem',
            'object_version': 'int',
            'parent_ref': 'ParentReference',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)',
            'host': 'str',
            'port': 'str',
            'protocol': 'str',
            'validate_certificate': 'bool',
            'default_connection': 'ConnectionFromHdfsDetails'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'native_type_system': 'nativeTypeSystem',
            'object_version': 'objectVersion',
            'parent_ref': 'parentRef',
            'metadata': 'metadata',
            'key_map': 'keyMap',
            'host': 'host',
            'port': 'port',
            'protocol': 'protocol',
            'validate_certificate': 'validateCertificate',
            'default_connection': 'defaultConnection'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._native_type_system = None
        self._object_version = None
        self._parent_ref = None
        self._metadata = None
        self._key_map = None
        self._host = None
        self._port = None
        self._protocol = None
        self._validate_certificate = None
        self._default_connection = None
        self._model_type = 'HDFS_DATA_ASSET'

    @property
    def host(self):
        """
        **[Required]** Gets the host of this DataAssetFromHdfsDetails.
        The HDFS hostname.


        :return: The host of this DataAssetFromHdfsDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this DataAssetFromHdfsDetails.
        The HDFS hostname.


        :param host: The host of this DataAssetFromHdfsDetails.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        **[Required]** Gets the port of this DataAssetFromHdfsDetails.
        The HDFS port.


        :return: The port of this DataAssetFromHdfsDetails.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this DataAssetFromHdfsDetails.
        The HDFS port.


        :param port: The port of this DataAssetFromHdfsDetails.
        :type: str
        """
        self._port = port

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this DataAssetFromHdfsDetails.
        The HDFS Protocol name.


        :return: The protocol of this DataAssetFromHdfsDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this DataAssetFromHdfsDetails.
        The HDFS Protocol name.


        :param protocol: The protocol of this DataAssetFromHdfsDetails.
        :type: str
        """
        self._protocol = protocol

    @property
    def validate_certificate(self):
        """
        Gets the validate_certificate of this DataAssetFromHdfsDetails.
        Specifies whether certificate validation is needed


        :return: The validate_certificate of this DataAssetFromHdfsDetails.
        :rtype: bool
        """
        return self._validate_certificate

    @validate_certificate.setter
    def validate_certificate(self, validate_certificate):
        """
        Sets the validate_certificate of this DataAssetFromHdfsDetails.
        Specifies whether certificate validation is needed


        :param validate_certificate: The validate_certificate of this DataAssetFromHdfsDetails.
        :type: bool
        """
        self._validate_certificate = validate_certificate

    @property
    def default_connection(self):
        """
        **[Required]** Gets the default_connection of this DataAssetFromHdfsDetails.

        :return: The default_connection of this DataAssetFromHdfsDetails.
        :rtype: oci.data_integration.models.ConnectionFromHdfsDetails
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this DataAssetFromHdfsDetails.

        :param default_connection: The default_connection of this DataAssetFromHdfsDetails.
        :type: oci.data_integration.models.ConnectionFromHdfsDetails
        """
        self._default_connection = default_connection

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
