# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125

from .image_feature import ImageFeature
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FaceDetectionFeature(ImageFeature):
    """
    The face detection parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FaceDetectionFeature object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.FaceDetectionFeature.feature_type` attribute
        of this class is ``FACE_DETECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_type:
            The value to assign to the feature_type property of this FaceDetectionFeature.
            Allowed values for this property are: "IMAGE_CLASSIFICATION", "OBJECT_DETECTION", "TEXT_DETECTION", "FACE_DETECTION"
        :type feature_type: str

        :param max_results:
            The value to assign to the max_results property of this FaceDetectionFeature.
        :type max_results: int

        :param should_return_landmarks:
            The value to assign to the should_return_landmarks property of this FaceDetectionFeature.
        :type should_return_landmarks: bool

        """
        self.swagger_types = {
            'feature_type': 'str',
            'max_results': 'int',
            'should_return_landmarks': 'bool'
        }

        self.attribute_map = {
            'feature_type': 'featureType',
            'max_results': 'maxResults',
            'should_return_landmarks': 'shouldReturnLandmarks'
        }

        self._feature_type = None
        self._max_results = None
        self._should_return_landmarks = None
        self._feature_type = 'FACE_DETECTION'

    @property
    def max_results(self):
        """
        Gets the max_results of this FaceDetectionFeature.
        The maximum number of results to return.


        :return: The max_results of this FaceDetectionFeature.
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """
        Sets the max_results of this FaceDetectionFeature.
        The maximum number of results to return.


        :param max_results: The max_results of this FaceDetectionFeature.
        :type: int
        """
        self._max_results = max_results

    @property
    def should_return_landmarks(self):
        """
        Gets the should_return_landmarks of this FaceDetectionFeature.
        Whether or not return face landmarks.


        :return: The should_return_landmarks of this FaceDetectionFeature.
        :rtype: bool
        """
        return self._should_return_landmarks

    @should_return_landmarks.setter
    def should_return_landmarks(self, should_return_landmarks):
        """
        Sets the should_return_landmarks of this FaceDetectionFeature.
        Whether or not return face landmarks.


        :param should_return_landmarks: The should_return_landmarks of this FaceDetectionFeature.
        :type: bool
        """
        self._should_return_landmarks = should_return_landmarks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
