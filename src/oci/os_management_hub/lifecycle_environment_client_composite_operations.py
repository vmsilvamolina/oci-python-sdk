# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

import oci  # noqa: F401
from oci.util import WAIT_RESOURCE_NOT_FOUND  # noqa: F401


class LifecycleEnvironmentClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.os_management_hub.LifecycleEnvironmentClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new LifecycleEnvironmentClientCompositeOperations object

        :param LifecycleEnvironmentClient client:
            The service client which will be wrapped by this object
        """
        self.client = client

    def attach_managed_instances_to_lifecycle_stage_and_wait_for_state(self, lifecycle_stage_id, attach_managed_instances_to_lifecycle_stage_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.attach_managed_instances_to_lifecycle_stage` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str lifecycle_stage_id: (required)
            The OCID of the lifecycle stage.

        :param oci.os_management_hub.models.AttachManagedInstancesToLifecycleStageDetails attach_managed_instances_to_lifecycle_stage_details: (required)
            Details for managed instances to attach to the lifecycle stage.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.attach_managed_instances_to_lifecycle_stage`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.attach_managed_instances_to_lifecycle_stage(lifecycle_stage_id, attach_managed_instances_to_lifecycle_stage_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def create_lifecycle_environment_and_wait_for_state(self, create_lifecycle_environment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.create_lifecycle_environment` and waits for the :py:class:`~oci.os_management_hub.models.LifecycleEnvironment` acted upon
        to enter the given state(s).

        :param oci.os_management_hub.models.CreateLifecycleEnvironmentDetails create_lifecycle_environment_details: (required)
            Details for the new lifecycle environment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.LifecycleEnvironment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.create_lifecycle_environment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.create_lifecycle_environment(create_lifecycle_environment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        lifecycle_environment_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_lifecycle_environment(lifecycle_environment_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def delete_lifecycle_environment_and_wait_for_state(self, lifecycle_environment_id, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.delete_lifecycle_environment` and waits for the :py:class:`~oci.os_management_hub.models.LifecycleEnvironment` acted upon
        to enter the given state(s).

        :param str lifecycle_environment_id: (required)
            The OCID of the lifecycle environment.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.LifecycleEnvironment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.delete_lifecycle_environment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        initial_get_result = self.client.get_lifecycle_environment(lifecycle_environment_id)
        operation_result = None
        try:
            operation_result = self.client.delete_lifecycle_environment(lifecycle_environment_id, **operation_kwargs)
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return WAIT_RESOURCE_NOT_FOUND
            else:
                raise e

        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]

        try:
            if ("succeed_on_not_found" in waiter_kwargs) and (waiter_kwargs["succeed_on_not_found"] is False):
                self.client.base_client.logger.warning("The waiter kwarg succeed_on_not_found was passed as False for the delete composite operation delete_lifecycle_environment, this would result in the operation to fail if the resource is not found! Please, do not pass this kwarg if this was not intended")
            else:
                """
                If the user does not send in this value, we set it to True by default.
                We are doing this because during a delete resource scenario and waiting on its state, the service can
                return a 404 NOT FOUND exception as the resource was deleted and a get on its state would fail
                """
                waiter_kwargs["succeed_on_not_found"] = True
            waiter_result = oci.wait_until(
                self.client,
                initial_get_result,  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def detach_managed_instances_from_lifecycle_stage_and_wait_for_state(self, lifecycle_stage_id, detach_managed_instances_from_lifecycle_stage_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.detach_managed_instances_from_lifecycle_stage` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str lifecycle_stage_id: (required)
            The OCID of the lifecycle stage.

        :param oci.os_management_hub.models.DetachManagedInstancesFromLifecycleStageDetails detach_managed_instances_from_lifecycle_stage_details: (required)
            Details for managed instances to detach from the lifecycle stage.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.detach_managed_instances_from_lifecycle_stage`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.detach_managed_instances_from_lifecycle_stage(lifecycle_stage_id, detach_managed_instances_from_lifecycle_stage_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def promote_software_source_to_lifecycle_stage_and_wait_for_state(self, lifecycle_stage_id, promote_software_source_to_lifecycle_stage_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.promote_software_source_to_lifecycle_stage` and waits for the :py:class:`~oci.os_management_hub.models.WorkRequest`
        to enter the given state(s).

        :param str lifecycle_stage_id: (required)
            The OCID of the lifecycle stage.

        :param oci.os_management_hub.models.PromoteSoftwareSourceToLifecycleStageDetails promote_software_source_to_lifecycle_stage_details: (required)
            Details for the software source promotion job.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.WorkRequest.status`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.promote_software_source_to_lifecycle_stage`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.promote_software_source_to_lifecycle_stage(lifecycle_stage_id, promote_software_source_to_lifecycle_stage_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        wait_for_resource_id = operation_result.headers['opc-work-request-id']

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_work_request(wait_for_resource_id),
                evaluate_response=lambda r: getattr(r.data, 'status') and getattr(r.data, 'status').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)

    def update_lifecycle_environment_and_wait_for_state(self, lifecycle_environment_id, update_lifecycle_environment_details, wait_for_states=[], operation_kwargs={}, waiter_kwargs={}):
        """
        Calls :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.update_lifecycle_environment` and waits for the :py:class:`~oci.os_management_hub.models.LifecycleEnvironment` acted upon
        to enter the given state(s).

        :param str lifecycle_environment_id: (required)
            The OCID of the lifecycle environment.

        :param oci.os_management_hub.models.UpdateLifecycleEnvironmentDetails update_lifecycle_environment_details: (required)
            The information to be updated.

        :param list[str] wait_for_states:
            An array of states to wait on. These should be valid values for :py:attr:`~oci.os_management_hub.models.LifecycleEnvironment.lifecycle_state`

        :param dict operation_kwargs:
            A dictionary of keyword arguments to pass to :py:func:`~oci.os_management_hub.LifecycleEnvironmentClient.update_lifecycle_environment`

        :param dict waiter_kwargs:
            A dictionary of keyword arguments to pass to the :py:func:`oci.wait_until` function. For example, you could pass ``max_interval_seconds`` or ``max_interval_seconds``
            as dictionary keys to modify how long the waiter function will wait between retries and the maximum amount of time it will wait
        """
        operation_result = self.client.update_lifecycle_environment(lifecycle_environment_id, update_lifecycle_environment_details, **operation_kwargs)
        if not wait_for_states:
            return operation_result

        lowered_wait_for_states = [w.lower() for w in wait_for_states]
        lifecycle_environment_id = operation_result.data.id

        try:
            waiter_result = oci.wait_until(
                self.client,
                self.client.get_lifecycle_environment(lifecycle_environment_id),  # noqa: F821
                evaluate_response=lambda r: getattr(r.data, 'lifecycle_state') and getattr(r.data, 'lifecycle_state').lower() in lowered_wait_for_states,
                **waiter_kwargs
            )
            result_to_return = waiter_result

            return result_to_return
        except (NameError, TypeError) as e:
            if not e.args:
                e.args = ('',)
            e.args = e.args + ('This composite operation is currently not supported in the SDK. Please use the operation from the service client and use waiters as an alternative. For more information on waiters, visit: "https://docs.oracle.com/en-us/iaas/tools/python/latest/api/waiters.html"', )
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
        except Exception as e:
            raise oci.exceptions.CompositeOperationError(partial_results=[operation_result], cause=e)
