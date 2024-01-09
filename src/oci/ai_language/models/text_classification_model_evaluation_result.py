# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001

from .evaluation_result_summary import EvaluationResultSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextClassificationModelEvaluationResult(EvaluationResultSummary):
    """
    Possible TXTC model error analysis
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextClassificationModelEvaluationResult object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_language.models.TextClassificationModelEvaluationResult.model_type` attribute
        of this class is ``TEXT_CLASSIFICATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TextClassificationModelEvaluationResult.
        :type model_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TextClassificationModelEvaluationResult.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TextClassificationModelEvaluationResult.
        :type defined_tags: dict(str, dict(str, object))

        :param location:
            The value to assign to the location property of this TextClassificationModelEvaluationResult.
        :type location: str

        :param true_labels:
            The value to assign to the true_labels property of this TextClassificationModelEvaluationResult.
        :type true_labels: list[str]

        :param predicted_labels:
            The value to assign to the predicted_labels property of this TextClassificationModelEvaluationResult.
        :type predicted_labels: list[str]

        """
        self.swagger_types = {
            'model_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'location': 'str',
            'true_labels': 'list[str]',
            'predicted_labels': 'list[str]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'location': 'location',
            'true_labels': 'trueLabels',
            'predicted_labels': 'predictedLabels'
        }

        self._model_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._location = None
        self._true_labels = None
        self._predicted_labels = None
        self._model_type = 'TEXT_CLASSIFICATION'

    @property
    def location(self):
        """
        **[Required]** Gets the location of this TextClassificationModelEvaluationResult.
        For CSV format location is rowId(1 is header) and for JSONL location is jsonL line sequence(1 is metadata)


        :return: The location of this TextClassificationModelEvaluationResult.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this TextClassificationModelEvaluationResult.
        For CSV format location is rowId(1 is header) and for JSONL location is jsonL line sequence(1 is metadata)


        :param location: The location of this TextClassificationModelEvaluationResult.
        :type: str
        """
        self._location = location

    @property
    def true_labels(self):
        """
        **[Required]** Gets the true_labels of this TextClassificationModelEvaluationResult.
        List of true(actual) labels in test data for multi class or multi label TextClassification


        :return: The true_labels of this TextClassificationModelEvaluationResult.
        :rtype: list[str]
        """
        return self._true_labels

    @true_labels.setter
    def true_labels(self, true_labels):
        """
        Sets the true_labels of this TextClassificationModelEvaluationResult.
        List of true(actual) labels in test data for multi class or multi label TextClassification


        :param true_labels: The true_labels of this TextClassificationModelEvaluationResult.
        :type: list[str]
        """
        self._true_labels = true_labels

    @property
    def predicted_labels(self):
        """
        Gets the predicted_labels of this TextClassificationModelEvaluationResult.
        List of predicted labels by custom multi class or multi label TextClassification model


        :return: The predicted_labels of this TextClassificationModelEvaluationResult.
        :rtype: list[str]
        """
        return self._predicted_labels

    @predicted_labels.setter
    def predicted_labels(self, predicted_labels):
        """
        Sets the predicted_labels of this TextClassificationModelEvaluationResult.
        List of predicted labels by custom multi class or multi label TextClassification model


        :param predicted_labels: The predicted_labels of this TextClassificationModelEvaluationResult.
        :type: list[str]
        """
        self._predicted_labels = predicted_labels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
