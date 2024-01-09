# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TraceServiceSummary(object):
    """
    Summary of the spans in a trace by service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TraceServiceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param span_service_name:
            The value to assign to the span_service_name property of this TraceServiceSummary.
        :type span_service_name: str

        :param total_spans:
            The value to assign to the total_spans property of this TraceServiceSummary.
        :type total_spans: int

        :param error_spans:
            The value to assign to the error_spans property of this TraceServiceSummary.
        :type error_spans: int

        """
        self.swagger_types = {
            'span_service_name': 'str',
            'total_spans': 'int',
            'error_spans': 'int'
        }

        self.attribute_map = {
            'span_service_name': 'spanServiceName',
            'total_spans': 'totalSpans',
            'error_spans': 'errorSpans'
        }

        self._span_service_name = None
        self._total_spans = None
        self._error_spans = None

    @property
    def span_service_name(self):
        """
        **[Required]** Gets the span_service_name of this TraceServiceSummary.
        Name associated with the service.


        :return: The span_service_name of this TraceServiceSummary.
        :rtype: str
        """
        return self._span_service_name

    @span_service_name.setter
    def span_service_name(self, span_service_name):
        """
        Sets the span_service_name of this TraceServiceSummary.
        Name associated with the service.


        :param span_service_name: The span_service_name of this TraceServiceSummary.
        :type: str
        """
        self._span_service_name = span_service_name

    @property
    def total_spans(self):
        """
        **[Required]** Gets the total_spans of this TraceServiceSummary.
        Number of spans for serviceName in the trace.


        :return: The total_spans of this TraceServiceSummary.
        :rtype: int
        """
        return self._total_spans

    @total_spans.setter
    def total_spans(self, total_spans):
        """
        Sets the total_spans of this TraceServiceSummary.
        Number of spans for serviceName in the trace.


        :param total_spans: The total_spans of this TraceServiceSummary.
        :type: int
        """
        self._total_spans = total_spans

    @property
    def error_spans(self):
        """
        **[Required]** Gets the error_spans of this TraceServiceSummary.
        Number of spans with errors for serviceName in the trace.


        :return: The error_spans of this TraceServiceSummary.
        :rtype: int
        """
        return self._error_spans

    @error_spans.setter
    def error_spans(self, error_spans):
        """
        Sets the error_spans of this TraceServiceSummary.
        Number of spans with errors for serviceName in the trace.


        :param error_spans: The error_spans of this TraceServiceSummary.
        :type: int
        """
        self._error_spans = error_spans

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
