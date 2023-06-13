# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatasetSummary(object):
    """
    Summary of count of samples used during model training.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatasetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param training_sample_count:
            The value to assign to the training_sample_count property of this DatasetSummary.
        :type training_sample_count: int

        :param validation_sample_count:
            The value to assign to the validation_sample_count property of this DatasetSummary.
        :type validation_sample_count: int

        :param test_sample_count:
            The value to assign to the test_sample_count property of this DatasetSummary.
        :type test_sample_count: int

        """
        self.swagger_types = {
            'training_sample_count': 'int',
            'validation_sample_count': 'int',
            'test_sample_count': 'int'
        }

        self.attribute_map = {
            'training_sample_count': 'trainingSampleCount',
            'validation_sample_count': 'validationSampleCount',
            'test_sample_count': 'testSampleCount'
        }

        self._training_sample_count = None
        self._validation_sample_count = None
        self._test_sample_count = None

    @property
    def training_sample_count(self):
        """
        Gets the training_sample_count of this DatasetSummary.
        Number of samples used for training the model.


        :return: The training_sample_count of this DatasetSummary.
        :rtype: int
        """
        return self._training_sample_count

    @training_sample_count.setter
    def training_sample_count(self, training_sample_count):
        """
        Sets the training_sample_count of this DatasetSummary.
        Number of samples used for training the model.


        :param training_sample_count: The training_sample_count of this DatasetSummary.
        :type: int
        """
        self._training_sample_count = training_sample_count

    @property
    def validation_sample_count(self):
        """
        Gets the validation_sample_count of this DatasetSummary.
        Number of samples used for validating the model.


        :return: The validation_sample_count of this DatasetSummary.
        :rtype: int
        """
        return self._validation_sample_count

    @validation_sample_count.setter
    def validation_sample_count(self, validation_sample_count):
        """
        Sets the validation_sample_count of this DatasetSummary.
        Number of samples used for validating the model.


        :param validation_sample_count: The validation_sample_count of this DatasetSummary.
        :type: int
        """
        self._validation_sample_count = validation_sample_count

    @property
    def test_sample_count(self):
        """
        Gets the test_sample_count of this DatasetSummary.
        Number of samples used for testing the model.


        :return: The test_sample_count of this DatasetSummary.
        :rtype: int
        """
        return self._test_sample_count

    @test_sample_count.setter
    def test_sample_count(self, test_sample_count):
        """
        Sets the test_sample_count of this DatasetSummary.
        Number of samples used for testing the model.


        :param test_sample_count: The test_sample_count of this DatasetSummary.
        :type: int
        """
        self._test_sample_count = test_sample_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
