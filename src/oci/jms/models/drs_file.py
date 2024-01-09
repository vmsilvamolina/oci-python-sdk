# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrsFile(object):
    """
    A Deployment Rule Set(DRS) is a JAR (Java ARchive) file used in Java applications to enforce security and manage compatibility
    between different versions of Java applets and web start applications
    (https://docs.oracle.com/javase/8/docs/technotes/guides/deploy/deployment_rules.html).
    """

    #: A constant which can be used with the checksum_type property of a DrsFile.
    #: This constant has a value of "SHA256"
    CHECKSUM_TYPE_SHA256 = "SHA256"

    def __init__(self, **kwargs):
        """
        Initializes a new DrsFile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bucket_name:
            The value to assign to the bucket_name property of this DrsFile.
        :type bucket_name: str

        :param namespace:
            The value to assign to the namespace property of this DrsFile.
        :type namespace: str

        :param drs_file_name:
            The value to assign to the drs_file_name property of this DrsFile.
        :type drs_file_name: str

        :param drs_file_key:
            The value to assign to the drs_file_key property of this DrsFile.
        :type drs_file_key: str

        :param checksum_type:
            The value to assign to the checksum_type property of this DrsFile.
            Allowed values for this property are: "SHA256", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type checksum_type: str

        :param checksum_value:
            The value to assign to the checksum_value property of this DrsFile.
        :type checksum_value: str

        :param is_default:
            The value to assign to the is_default property of this DrsFile.
        :type is_default: bool

        """
        self.swagger_types = {
            'bucket_name': 'str',
            'namespace': 'str',
            'drs_file_name': 'str',
            'drs_file_key': 'str',
            'checksum_type': 'str',
            'checksum_value': 'str',
            'is_default': 'bool'
        }

        self.attribute_map = {
            'bucket_name': 'bucketName',
            'namespace': 'namespace',
            'drs_file_name': 'drsFileName',
            'drs_file_key': 'drsFileKey',
            'checksum_type': 'checksumType',
            'checksum_value': 'checksumValue',
            'is_default': 'isDefault'
        }

        self._bucket_name = None
        self._namespace = None
        self._drs_file_name = None
        self._drs_file_key = None
        self._checksum_type = None
        self._checksum_value = None
        self._is_default = None

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this DrsFile.
        The Object Storage bucket name where the DRS file is located.


        :return: The bucket_name of this DrsFile.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this DrsFile.
        The Object Storage bucket name where the DRS file is located.


        :param bucket_name: The bucket_name of this DrsFile.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this DrsFile.
        The namespace for Object Storage.


        :return: The namespace of this DrsFile.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this DrsFile.
        The namespace for Object Storage.


        :param namespace: The namespace of this DrsFile.
        :type: str
        """
        self._namespace = namespace

    @property
    def drs_file_name(self):
        """
        **[Required]** Gets the drs_file_name of this DrsFile.
        The name of the DRS file in Object Store.


        :return: The drs_file_name of this DrsFile.
        :rtype: str
        """
        return self._drs_file_name

    @drs_file_name.setter
    def drs_file_name(self, drs_file_name):
        """
        Sets the drs_file_name of this DrsFile.
        The name of the DRS file in Object Store.


        :param drs_file_name: The drs_file_name of this DrsFile.
        :type: str
        """
        self._drs_file_name = drs_file_name

    @property
    def drs_file_key(self):
        """
        **[Required]** Gets the drs_file_key of this DrsFile.
        The unique identifier of the DRS file in Object Storage.


        :return: The drs_file_key of this DrsFile.
        :rtype: str
        """
        return self._drs_file_key

    @drs_file_key.setter
    def drs_file_key(self, drs_file_key):
        """
        Sets the drs_file_key of this DrsFile.
        The unique identifier of the DRS file in Object Storage.


        :param drs_file_key: The drs_file_key of this DrsFile.
        :type: str
        """
        self._drs_file_key = drs_file_key

    @property
    def checksum_type(self):
        """
        **[Required]** Gets the checksum_type of this DrsFile.
        The checksum type for the DRS file in Object Storage.

        Allowed values for this property are: "SHA256", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The checksum_type of this DrsFile.
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """
        Sets the checksum_type of this DrsFile.
        The checksum type for the DRS file in Object Storage.


        :param checksum_type: The checksum_type of this DrsFile.
        :type: str
        """
        allowed_values = ["SHA256"]
        if not value_allowed_none_or_none_sentinel(checksum_type, allowed_values):
            checksum_type = 'UNKNOWN_ENUM_VALUE'
        self._checksum_type = checksum_type

    @property
    def checksum_value(self):
        """
        **[Required]** Gets the checksum_value of this DrsFile.
        The checksum value for the DRS file in Object Storage.


        :return: The checksum_value of this DrsFile.
        :rtype: str
        """
        return self._checksum_value

    @checksum_value.setter
    def checksum_value(self, checksum_value):
        """
        Sets the checksum_value of this DrsFile.
        The checksum value for the DRS file in Object Storage.


        :param checksum_value: The checksum_value of this DrsFile.
        :type: str
        """
        self._checksum_value = checksum_value

    @property
    def is_default(self):
        """
        **[Required]** Gets the is_default of this DrsFile.
        To check if the DRS file is the detfault ones.


        :return: The is_default of this DrsFile.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this DrsFile.
        To check if the DRS file is the detfault ones.


        :param is_default: The is_default of this DrsFile.
        :type: bool
        """
        self._is_default = is_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
