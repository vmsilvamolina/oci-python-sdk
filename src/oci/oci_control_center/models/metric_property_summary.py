# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricPropertySummary(object):
    """
    A summary of the properties that define a metric.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetricPropertySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this MetricPropertySummary.
        :type metric_name: str

        :param dimensions:
            The value to assign to the dimensions property of this MetricPropertySummary.
        :type dimensions: dict(str, DimensionValue)

        """
        self.swagger_types = {
            'metric_name': 'str',
            'dimensions': 'dict(str, DimensionValue)'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'dimensions': 'dimensions'
        }

        self._metric_name = None
        self._dimensions = None

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this MetricPropertySummary.
        The name of the metric.


        :return: The metric_name of this MetricPropertySummary.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this MetricPropertySummary.
        The name of the metric.


        :param metric_name: The metric_name of this MetricPropertySummary.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def dimensions(self):
        """
        Gets the dimensions of this MetricPropertySummary.
        Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.


        :return: The dimensions of this MetricPropertySummary.
        :rtype: dict(str, DimensionValue)
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this MetricPropertySummary.
        Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.


        :param dimensions: The dimensions of this MetricPropertySummary.
        :type: dict(str, DimensionValue)
        """
        self._dimensions = dimensions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
