# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506

from __future__ import absolute_import

from .android_channel import AndroidChannel
from .app_event_channel import AppEventChannel
from .application_channel import ApplicationChannel
from .authentication_provider import AuthenticationProvider
from .authentication_provider_collection import AuthenticationProviderCollection
from .authentication_provider_summary import AuthenticationProviderSummary
from .bot import Bot
from .bulk_create_skill_entities_details import BulkCreateSkillEntitiesDetails
from .change_oda_instance_compartment_details import ChangeOdaInstanceCompartmentDetails
from .change_oda_private_endpoint_compartment_details import ChangeOdaPrivateEndpointCompartmentDetails
from .channel import Channel
from .channel_collection import ChannelCollection
from .channel_summary import ChannelSummary
from .clone_digital_assistant_details import CloneDigitalAssistantDetails
from .clone_skill_details import CloneSkillDetails
from .composite_entity import CompositeEntity
from .configure_digital_assistant_parameters_details import ConfigureDigitalAssistantParametersDetails
from .cortana_channel import CortanaChannel
from .create_android_channel_details import CreateAndroidChannelDetails
from .create_android_channel_result import CreateAndroidChannelResult
from .create_app_event_channel_details import CreateAppEventChannelDetails
from .create_app_event_channel_result import CreateAppEventChannelResult
from .create_application_channel_details import CreateApplicationChannelDetails
from .create_application_channel_result import CreateApplicationChannelResult
from .create_authentication_provider_details import CreateAuthenticationProviderDetails
from .create_channel_details import CreateChannelDetails
from .create_channel_result import CreateChannelResult
from .create_cortana_channel_details import CreateCortanaChannelDetails
from .create_cortana_channel_result import CreateCortanaChannelResult
from .create_digital_assistant_details import CreateDigitalAssistantDetails
from .create_digital_assistant_version_details import CreateDigitalAssistantVersionDetails
from .create_facebook_channel_details import CreateFacebookChannelDetails
from .create_facebook_channel_result import CreateFacebookChannelResult
from .create_imported_package_details import CreateImportedPackageDetails
from .create_ios_channel_details import CreateIosChannelDetails
from .create_ios_channel_result import CreateIosChannelResult
from .create_ms_teams_channel_details import CreateMSTeamsChannelDetails
from .create_ms_teams_channel_result import CreateMSTeamsChannelResult
from .create_new_digital_assistant_details import CreateNewDigitalAssistantDetails
from .create_new_skill_details import CreateNewSkillDetails
from .create_oss_channel_details import CreateOSSChannelDetails
from .create_oss_channel_result import CreateOSSChannelResult
from .create_oda_instance_attachment_details import CreateOdaInstanceAttachmentDetails
from .create_oda_instance_details import CreateOdaInstanceDetails
from .create_oda_private_endpoint_attachment_details import CreateOdaPrivateEndpointAttachmentDetails
from .create_oda_private_endpoint_details import CreateOdaPrivateEndpointDetails
from .create_oda_private_endpoint_scan_proxy_details import CreateOdaPrivateEndpointScanProxyDetails
from .create_osvc_channel_details import CreateOsvcChannelDetails
from .create_osvc_channel_result import CreateOsvcChannelResult
from .create_service_cloud_channel_details import CreateServiceCloudChannelDetails
from .create_service_cloud_channel_result import CreateServiceCloudChannelResult
from .create_skill_composite_entity_details import CreateSkillCompositeEntityDetails
from .create_skill_details import CreateSkillDetails
from .create_skill_entity_details import CreateSkillEntityDetails
from .create_skill_parameter_details import CreateSkillParameterDetails
from .create_skill_value_list_entity_details import CreateSkillValueListEntityDetails
from .create_skill_version_details import CreateSkillVersionDetails
from .create_slack_channel_details import CreateSlackChannelDetails
from .create_slack_channel_result import CreateSlackChannelResult
from .create_test_channel_result import CreateTestChannelResult
from .create_translator_details import CreateTranslatorDetails
from .create_twilio_channel_details import CreateTwilioChannelDetails
from .create_twilio_channel_result import CreateTwilioChannelResult
from .create_web_channel_details import CreateWebChannelDetails
from .create_web_channel_result import CreateWebChannelResult
from .create_webhook_channel_details import CreateWebhookChannelDetails
from .create_webhook_channel_result import CreateWebhookChannelResult
from .default_parameter_values import DefaultParameterValues
from .digital_assistant import DigitalAssistant
from .digital_assistant_collection import DigitalAssistantCollection
from .digital_assistant_parameter import DigitalAssistantParameter
from .digital_assistant_parameter_collection import DigitalAssistantParameterCollection
from .digital_assistant_parameter_summary import DigitalAssistantParameterSummary
from .digital_assistant_parameter_value import DigitalAssistantParameterValue
from .digital_assistant_summary import DigitalAssistantSummary
from .entity import Entity
from .entity_action import EntityAction
from .entity_action_argument import EntityActionArgument
from .entity_action_argument_natural_language_mapping import EntityActionArgumentNaturalLanguageMapping
from .entity_action_natural_language_mapping import EntityActionNaturalLanguageMapping
from .entity_attribute import EntityAttribute
from .entity_attribute_natural_language_mapping import EntityAttributeNaturalLanguageMapping
from .entity_natural_language_mapping import EntityNaturalLanguageMapping
from .error_body import ErrorBody
from .export_bot_details import ExportBotDetails
from .export_digital_assistant_details import ExportDigitalAssistantDetails
from .export_skill_details import ExportSkillDetails
from .extend_digital_assistant_details import ExtendDigitalAssistantDetails
from .extend_skill_details import ExtendSkillDetails
from .facebook_channel import FacebookChannel
from .import_bot_details import ImportBotDetails
from .import_contract import ImportContract
from .imported_package import ImportedPackage
from .imported_package_summary import ImportedPackageSummary
from .ios_channel import IosChannel
from .language_mapping import LanguageMapping
from .ms_teams_channel import MSTeamsChannel
from .metadata_property import MetadataProperty
from .name_mapping import NameMapping
from .oss_channel import OSSChannel
from .oda_instance import OdaInstance
from .oda_instance_attachment import OdaInstanceAttachment
from .oda_instance_attachment_collection import OdaInstanceAttachmentCollection
from .oda_instance_attachment_owner import OdaInstanceAttachmentOwner
from .oda_instance_attachment_summary import OdaInstanceAttachmentSummary
from .oda_instance_owner import OdaInstanceOwner
from .oda_instance_summary import OdaInstanceSummary
from .oda_private_endpoint import OdaPrivateEndpoint
from .oda_private_endpoint_attachment import OdaPrivateEndpointAttachment
from .oda_private_endpoint_attachment_collection import OdaPrivateEndpointAttachmentCollection
from .oda_private_endpoint_attachment_summary import OdaPrivateEndpointAttachmentSummary
from .oda_private_endpoint_collection import OdaPrivateEndpointCollection
from .oda_private_endpoint_scan_proxy import OdaPrivateEndpointScanProxy
from .oda_private_endpoint_scan_proxy_collection import OdaPrivateEndpointScanProxyCollection
from .oda_private_endpoint_scan_proxy_summary import OdaPrivateEndpointScanProxySummary
from .oda_private_endpoint_summary import OdaPrivateEndpointSummary
from .osvc_channel import OsvcChannel
from .package import Package
from .package_summary import PackageSummary
from .parameter import Parameter
from .parameter_definition import ParameterDefinition
from .resource_type_default_parameter_values import ResourceTypeDefaultParameterValues
from .resource_type_import_contract import ResourceTypeImportContract
from .resource_type_metadata import ResourceTypeMetadata
from .restricted_operation import RestrictedOperation
from .scan_listener_info import ScanListenerInfo
from .service_cloud_channel import ServiceCloudChannel
from .skill import Skill
from .skill_collection import SkillCollection
from .skill_parameter import SkillParameter
from .skill_parameter_collection import SkillParameterCollection
from .skill_parameter_summary import SkillParameterSummary
from .skill_summary import SkillSummary
from .slack_channel import SlackChannel
from .static_entity_value import StaticEntityValue
from .static_entity_value_natural_language_mapping import StaticEntityValueNaturalLanguageMapping
from .storage_location import StorageLocation
from .test_channel import TestChannel
from .train_skill_details import TrainSkillDetails
from .train_skill_parameter import TrainSkillParameter
from .train_skill_query_entity_parameter import TrainSkillQueryEntityParameter
from .translator import Translator
from .translator_collection import TranslatorCollection
from .translator_summary import TranslatorSummary
from .twilio_channel import TwilioChannel
from .update_android_channel_details import UpdateAndroidChannelDetails
from .update_app_event_channel_details import UpdateAppEventChannelDetails
from .update_application_channel_details import UpdateApplicationChannelDetails
from .update_authentication_provider_details import UpdateAuthenticationProviderDetails
from .update_channel_details import UpdateChannelDetails
from .update_cortana_channel_details import UpdateCortanaChannelDetails
from .update_digital_assistant_details import UpdateDigitalAssistantDetails
from .update_digital_assistant_parameter_details import UpdateDigitalAssistantParameterDetails
from .update_facebook_channel_details import UpdateFacebookChannelDetails
from .update_imported_package_details import UpdateImportedPackageDetails
from .update_ios_channel_details import UpdateIosChannelDetails
from .update_ms_teams_channel_details import UpdateMSTeamsChannelDetails
from .update_oss_channel_details import UpdateOSSChannelDetails
from .update_oda_instance_attachment_details import UpdateOdaInstanceAttachmentDetails
from .update_oda_instance_details import UpdateOdaInstanceDetails
from .update_oda_private_endpoint_details import UpdateOdaPrivateEndpointDetails
from .update_osvc_channel_details import UpdateOsvcChannelDetails
from .update_service_cloud_channel_details import UpdateServiceCloudChannelDetails
from .update_skill_details import UpdateSkillDetails
from .update_skill_parameter_details import UpdateSkillParameterDetails
from .update_slack_channel_details import UpdateSlackChannelDetails
from .update_translator_details import UpdateTranslatorDetails
from .update_twilio_channel_details import UpdateTwilioChannelDetails
from .update_web_channel_details import UpdateWebChannelDetails
from .update_webhook_channel_details import UpdateWebhookChannelDetails
from .value_list_entity import ValueListEntity
from .web_channel import WebChannel
from .webhook_channel import WebhookChannel
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for oda services.
oda_type_mapping = {
    "AndroidChannel": AndroidChannel,
    "AppEventChannel": AppEventChannel,
    "ApplicationChannel": ApplicationChannel,
    "AuthenticationProvider": AuthenticationProvider,
    "AuthenticationProviderCollection": AuthenticationProviderCollection,
    "AuthenticationProviderSummary": AuthenticationProviderSummary,
    "Bot": Bot,
    "BulkCreateSkillEntitiesDetails": BulkCreateSkillEntitiesDetails,
    "ChangeOdaInstanceCompartmentDetails": ChangeOdaInstanceCompartmentDetails,
    "ChangeOdaPrivateEndpointCompartmentDetails": ChangeOdaPrivateEndpointCompartmentDetails,
    "Channel": Channel,
    "ChannelCollection": ChannelCollection,
    "ChannelSummary": ChannelSummary,
    "CloneDigitalAssistantDetails": CloneDigitalAssistantDetails,
    "CloneSkillDetails": CloneSkillDetails,
    "CompositeEntity": CompositeEntity,
    "ConfigureDigitalAssistantParametersDetails": ConfigureDigitalAssistantParametersDetails,
    "CortanaChannel": CortanaChannel,
    "CreateAndroidChannelDetails": CreateAndroidChannelDetails,
    "CreateAndroidChannelResult": CreateAndroidChannelResult,
    "CreateAppEventChannelDetails": CreateAppEventChannelDetails,
    "CreateAppEventChannelResult": CreateAppEventChannelResult,
    "CreateApplicationChannelDetails": CreateApplicationChannelDetails,
    "CreateApplicationChannelResult": CreateApplicationChannelResult,
    "CreateAuthenticationProviderDetails": CreateAuthenticationProviderDetails,
    "CreateChannelDetails": CreateChannelDetails,
    "CreateChannelResult": CreateChannelResult,
    "CreateCortanaChannelDetails": CreateCortanaChannelDetails,
    "CreateCortanaChannelResult": CreateCortanaChannelResult,
    "CreateDigitalAssistantDetails": CreateDigitalAssistantDetails,
    "CreateDigitalAssistantVersionDetails": CreateDigitalAssistantVersionDetails,
    "CreateFacebookChannelDetails": CreateFacebookChannelDetails,
    "CreateFacebookChannelResult": CreateFacebookChannelResult,
    "CreateImportedPackageDetails": CreateImportedPackageDetails,
    "CreateIosChannelDetails": CreateIosChannelDetails,
    "CreateIosChannelResult": CreateIosChannelResult,
    "CreateMSTeamsChannelDetails": CreateMSTeamsChannelDetails,
    "CreateMSTeamsChannelResult": CreateMSTeamsChannelResult,
    "CreateNewDigitalAssistantDetails": CreateNewDigitalAssistantDetails,
    "CreateNewSkillDetails": CreateNewSkillDetails,
    "CreateOSSChannelDetails": CreateOSSChannelDetails,
    "CreateOSSChannelResult": CreateOSSChannelResult,
    "CreateOdaInstanceAttachmentDetails": CreateOdaInstanceAttachmentDetails,
    "CreateOdaInstanceDetails": CreateOdaInstanceDetails,
    "CreateOdaPrivateEndpointAttachmentDetails": CreateOdaPrivateEndpointAttachmentDetails,
    "CreateOdaPrivateEndpointDetails": CreateOdaPrivateEndpointDetails,
    "CreateOdaPrivateEndpointScanProxyDetails": CreateOdaPrivateEndpointScanProxyDetails,
    "CreateOsvcChannelDetails": CreateOsvcChannelDetails,
    "CreateOsvcChannelResult": CreateOsvcChannelResult,
    "CreateServiceCloudChannelDetails": CreateServiceCloudChannelDetails,
    "CreateServiceCloudChannelResult": CreateServiceCloudChannelResult,
    "CreateSkillCompositeEntityDetails": CreateSkillCompositeEntityDetails,
    "CreateSkillDetails": CreateSkillDetails,
    "CreateSkillEntityDetails": CreateSkillEntityDetails,
    "CreateSkillParameterDetails": CreateSkillParameterDetails,
    "CreateSkillValueListEntityDetails": CreateSkillValueListEntityDetails,
    "CreateSkillVersionDetails": CreateSkillVersionDetails,
    "CreateSlackChannelDetails": CreateSlackChannelDetails,
    "CreateSlackChannelResult": CreateSlackChannelResult,
    "CreateTestChannelResult": CreateTestChannelResult,
    "CreateTranslatorDetails": CreateTranslatorDetails,
    "CreateTwilioChannelDetails": CreateTwilioChannelDetails,
    "CreateTwilioChannelResult": CreateTwilioChannelResult,
    "CreateWebChannelDetails": CreateWebChannelDetails,
    "CreateWebChannelResult": CreateWebChannelResult,
    "CreateWebhookChannelDetails": CreateWebhookChannelDetails,
    "CreateWebhookChannelResult": CreateWebhookChannelResult,
    "DefaultParameterValues": DefaultParameterValues,
    "DigitalAssistant": DigitalAssistant,
    "DigitalAssistantCollection": DigitalAssistantCollection,
    "DigitalAssistantParameter": DigitalAssistantParameter,
    "DigitalAssistantParameterCollection": DigitalAssistantParameterCollection,
    "DigitalAssistantParameterSummary": DigitalAssistantParameterSummary,
    "DigitalAssistantParameterValue": DigitalAssistantParameterValue,
    "DigitalAssistantSummary": DigitalAssistantSummary,
    "Entity": Entity,
    "EntityAction": EntityAction,
    "EntityActionArgument": EntityActionArgument,
    "EntityActionArgumentNaturalLanguageMapping": EntityActionArgumentNaturalLanguageMapping,
    "EntityActionNaturalLanguageMapping": EntityActionNaturalLanguageMapping,
    "EntityAttribute": EntityAttribute,
    "EntityAttributeNaturalLanguageMapping": EntityAttributeNaturalLanguageMapping,
    "EntityNaturalLanguageMapping": EntityNaturalLanguageMapping,
    "ErrorBody": ErrorBody,
    "ExportBotDetails": ExportBotDetails,
    "ExportDigitalAssistantDetails": ExportDigitalAssistantDetails,
    "ExportSkillDetails": ExportSkillDetails,
    "ExtendDigitalAssistantDetails": ExtendDigitalAssistantDetails,
    "ExtendSkillDetails": ExtendSkillDetails,
    "FacebookChannel": FacebookChannel,
    "ImportBotDetails": ImportBotDetails,
    "ImportContract": ImportContract,
    "ImportedPackage": ImportedPackage,
    "ImportedPackageSummary": ImportedPackageSummary,
    "IosChannel": IosChannel,
    "LanguageMapping": LanguageMapping,
    "MSTeamsChannel": MSTeamsChannel,
    "MetadataProperty": MetadataProperty,
    "NameMapping": NameMapping,
    "OSSChannel": OSSChannel,
    "OdaInstance": OdaInstance,
    "OdaInstanceAttachment": OdaInstanceAttachment,
    "OdaInstanceAttachmentCollection": OdaInstanceAttachmentCollection,
    "OdaInstanceAttachmentOwner": OdaInstanceAttachmentOwner,
    "OdaInstanceAttachmentSummary": OdaInstanceAttachmentSummary,
    "OdaInstanceOwner": OdaInstanceOwner,
    "OdaInstanceSummary": OdaInstanceSummary,
    "OdaPrivateEndpoint": OdaPrivateEndpoint,
    "OdaPrivateEndpointAttachment": OdaPrivateEndpointAttachment,
    "OdaPrivateEndpointAttachmentCollection": OdaPrivateEndpointAttachmentCollection,
    "OdaPrivateEndpointAttachmentSummary": OdaPrivateEndpointAttachmentSummary,
    "OdaPrivateEndpointCollection": OdaPrivateEndpointCollection,
    "OdaPrivateEndpointScanProxy": OdaPrivateEndpointScanProxy,
    "OdaPrivateEndpointScanProxyCollection": OdaPrivateEndpointScanProxyCollection,
    "OdaPrivateEndpointScanProxySummary": OdaPrivateEndpointScanProxySummary,
    "OdaPrivateEndpointSummary": OdaPrivateEndpointSummary,
    "OsvcChannel": OsvcChannel,
    "Package": Package,
    "PackageSummary": PackageSummary,
    "Parameter": Parameter,
    "ParameterDefinition": ParameterDefinition,
    "ResourceTypeDefaultParameterValues": ResourceTypeDefaultParameterValues,
    "ResourceTypeImportContract": ResourceTypeImportContract,
    "ResourceTypeMetadata": ResourceTypeMetadata,
    "RestrictedOperation": RestrictedOperation,
    "ScanListenerInfo": ScanListenerInfo,
    "ServiceCloudChannel": ServiceCloudChannel,
    "Skill": Skill,
    "SkillCollection": SkillCollection,
    "SkillParameter": SkillParameter,
    "SkillParameterCollection": SkillParameterCollection,
    "SkillParameterSummary": SkillParameterSummary,
    "SkillSummary": SkillSummary,
    "SlackChannel": SlackChannel,
    "StaticEntityValue": StaticEntityValue,
    "StaticEntityValueNaturalLanguageMapping": StaticEntityValueNaturalLanguageMapping,
    "StorageLocation": StorageLocation,
    "TestChannel": TestChannel,
    "TrainSkillDetails": TrainSkillDetails,
    "TrainSkillParameter": TrainSkillParameter,
    "TrainSkillQueryEntityParameter": TrainSkillQueryEntityParameter,
    "Translator": Translator,
    "TranslatorCollection": TranslatorCollection,
    "TranslatorSummary": TranslatorSummary,
    "TwilioChannel": TwilioChannel,
    "UpdateAndroidChannelDetails": UpdateAndroidChannelDetails,
    "UpdateAppEventChannelDetails": UpdateAppEventChannelDetails,
    "UpdateApplicationChannelDetails": UpdateApplicationChannelDetails,
    "UpdateAuthenticationProviderDetails": UpdateAuthenticationProviderDetails,
    "UpdateChannelDetails": UpdateChannelDetails,
    "UpdateCortanaChannelDetails": UpdateCortanaChannelDetails,
    "UpdateDigitalAssistantDetails": UpdateDigitalAssistantDetails,
    "UpdateDigitalAssistantParameterDetails": UpdateDigitalAssistantParameterDetails,
    "UpdateFacebookChannelDetails": UpdateFacebookChannelDetails,
    "UpdateImportedPackageDetails": UpdateImportedPackageDetails,
    "UpdateIosChannelDetails": UpdateIosChannelDetails,
    "UpdateMSTeamsChannelDetails": UpdateMSTeamsChannelDetails,
    "UpdateOSSChannelDetails": UpdateOSSChannelDetails,
    "UpdateOdaInstanceAttachmentDetails": UpdateOdaInstanceAttachmentDetails,
    "UpdateOdaInstanceDetails": UpdateOdaInstanceDetails,
    "UpdateOdaPrivateEndpointDetails": UpdateOdaPrivateEndpointDetails,
    "UpdateOsvcChannelDetails": UpdateOsvcChannelDetails,
    "UpdateServiceCloudChannelDetails": UpdateServiceCloudChannelDetails,
    "UpdateSkillDetails": UpdateSkillDetails,
    "UpdateSkillParameterDetails": UpdateSkillParameterDetails,
    "UpdateSlackChannelDetails": UpdateSlackChannelDetails,
    "UpdateTranslatorDetails": UpdateTranslatorDetails,
    "UpdateTwilioChannelDetails": UpdateTwilioChannelDetails,
    "UpdateWebChannelDetails": UpdateWebChannelDetails,
    "UpdateWebhookChannelDetails": UpdateWebhookChannelDetails,
    "ValueListEntity": ValueListEntity,
    "WebChannel": WebChannel,
    "WebhookChannel": WebhookChannel,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
