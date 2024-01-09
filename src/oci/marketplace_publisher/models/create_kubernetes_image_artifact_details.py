# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from .create_artifact_details import CreateArtifactDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateKubernetesImageArtifactDetails(CreateArtifactDetails):
    """
    Details to create a new helm chart image artifact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateKubernetesImageArtifactDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.marketplace_publisher.models.CreateKubernetesImageArtifactDetails.artifact_type` attribute
        of this class is ``HELM_CHART`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateKubernetesImageArtifactDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateKubernetesImageArtifactDetails.
        :type display_name: str

        :param artifact_type:
            The value to assign to the artifact_type property of this CreateKubernetesImageArtifactDetails.
            Allowed values for this property are: "CONTAINER_IMAGE", "HELM_CHART"
        :type artifact_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateKubernetesImageArtifactDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateKubernetesImageArtifactDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param helm_chart:
            The value to assign to the helm_chart property of this CreateKubernetesImageArtifactDetails.
        :type helm_chart: oci.marketplace_publisher.models.CreateHelmChartImageDetails

        :param container_image_artifact_ids:
            The value to assign to the container_image_artifact_ids property of this CreateKubernetesImageArtifactDetails.
        :type container_image_artifact_ids: list[str]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'artifact_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'helm_chart': 'CreateHelmChartImageDetails',
            'container_image_artifact_ids': 'list[str]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'artifact_type': 'artifactType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'helm_chart': 'helmChart',
            'container_image_artifact_ids': 'containerImageArtifactIds'
        }

        self._compartment_id = None
        self._display_name = None
        self._artifact_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._helm_chart = None
        self._container_image_artifact_ids = None
        self._artifact_type = 'HELM_CHART'

    @property
    def helm_chart(self):
        """
        **[Required]** Gets the helm_chart of this CreateKubernetesImageArtifactDetails.

        :return: The helm_chart of this CreateKubernetesImageArtifactDetails.
        :rtype: oci.marketplace_publisher.models.CreateHelmChartImageDetails
        """
        return self._helm_chart

    @helm_chart.setter
    def helm_chart(self, helm_chart):
        """
        Sets the helm_chart of this CreateKubernetesImageArtifactDetails.

        :param helm_chart: The helm_chart of this CreateKubernetesImageArtifactDetails.
        :type: oci.marketplace_publisher.models.CreateHelmChartImageDetails
        """
        self._helm_chart = helm_chart

    @property
    def container_image_artifact_ids(self):
        """
        Gets the container_image_artifact_ids of this CreateKubernetesImageArtifactDetails.
        List of container image artifact uniquie identifiers included in the helm chart.


        :return: The container_image_artifact_ids of this CreateKubernetesImageArtifactDetails.
        :rtype: list[str]
        """
        return self._container_image_artifact_ids

    @container_image_artifact_ids.setter
    def container_image_artifact_ids(self, container_image_artifact_ids):
        """
        Sets the container_image_artifact_ids of this CreateKubernetesImageArtifactDetails.
        List of container image artifact uniquie identifiers included in the helm chart.


        :param container_image_artifact_ids: The container_image_artifact_ids of this CreateKubernetesImageArtifactDetails.
        :type: list[str]
        """
        self._container_image_artifact_ids = container_image_artifact_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
