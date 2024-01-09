# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430

from .abstract_format_attribute import AbstractFormatAttribute
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JsonFormatAttribute(AbstractFormatAttribute):
    """
    The JSON file format attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JsonFormatAttribute object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.JsonFormatAttribute.model_type` attribute
        of this class is ``JSON_FORMAT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this JsonFormatAttribute.
            Allowed values for this property are: "JSON_FORMAT", "CSV_FORMAT", "AVRO_FORMAT"
        :type model_type: str

        :param is_file_pattern:
            The value to assign to the is_file_pattern property of this JsonFormatAttribute.
        :type is_file_pattern: bool

        :param encoding:
            The value to assign to the encoding property of this JsonFormatAttribute.
        :type encoding: str

        :param sample_entity_data:
            The value to assign to the sample_entity_data property of this JsonFormatAttribute.
        :type sample_entity_data: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'is_file_pattern': 'bool',
            'encoding': 'str',
            'sample_entity_data': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'is_file_pattern': 'isFilePattern',
            'encoding': 'encoding',
            'sample_entity_data': 'sampleEntityData'
        }

        self._model_type = None
        self._is_file_pattern = None
        self._encoding = None
        self._sample_entity_data = None
        self._model_type = 'JSON_FORMAT'

    @property
    def encoding(self):
        """
        Gets the encoding of this JsonFormatAttribute.
        The encoding for the file.


        :return: The encoding of this JsonFormatAttribute.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this JsonFormatAttribute.
        The encoding for the file.


        :param encoding: The encoding of this JsonFormatAttribute.
        :type: str
        """
        self._encoding = encoding

    @property
    def sample_entity_data(self):
        """
        Gets the sample_entity_data of this JsonFormatAttribute.
        Sample JSON with all fields of JSON schema specified in it for the JSON data files used in Data Flow, Data Loader or Data Preview and should be specified in Base64 encoded format. Maximum size is 2 MB.


        :return: The sample_entity_data of this JsonFormatAttribute.
        :rtype: str
        """
        return self._sample_entity_data

    @sample_entity_data.setter
    def sample_entity_data(self, sample_entity_data):
        """
        Sets the sample_entity_data of this JsonFormatAttribute.
        Sample JSON with all fields of JSON schema specified in it for the JSON data files used in Data Flow, Data Loader or Data Preview and should be specified in Base64 encoded format. Maximum size is 2 MB.


        :param sample_entity_data: The sample_entity_data of this JsonFormatAttribute.
        :type: str
        """
        self._sample_entity_data = sample_entity_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
