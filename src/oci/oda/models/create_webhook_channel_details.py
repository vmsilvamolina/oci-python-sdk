# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506

from .create_channel_details import CreateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateWebhookChannelDetails(CreateChannelDetails):
    """
    Properties required to create a Webhook channel.
    """

    #: A constant which can be used with the payload_version property of a CreateWebhookChannelDetails.
    #: This constant has a value of "1.0"
    PAYLOAD_VERSION_1_0 = "1.0"

    #: A constant which can be used with the payload_version property of a CreateWebhookChannelDetails.
    #: This constant has a value of "1.1"
    PAYLOAD_VERSION_1_1 = "1.1"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateWebhookChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.CreateWebhookChannelDetails.type` attribute
        of this class is ``WEBHOOK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateWebhookChannelDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateWebhookChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateWebhookChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this CreateWebhookChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateWebhookChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateWebhookChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param outbound_url:
            The value to assign to the outbound_url property of this CreateWebhookChannelDetails.
        :type outbound_url: str

        :param payload_version:
            The value to assign to the payload_version property of this CreateWebhookChannelDetails.
            Allowed values for this property are: "1.0", "1.1"
        :type payload_version: str

        :param bot_id:
            The value to assign to the bot_id property of this CreateWebhookChannelDetails.
        :type bot_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'outbound_url': 'str',
            'payload_version': 'str',
            'bot_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'outbound_url': 'outboundUrl',
            'payload_version': 'payloadVersion',
            'bot_id': 'botId'
        }

        self._name = None
        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._outbound_url = None
        self._payload_version = None
        self._bot_id = None
        self._type = 'WEBHOOK'

    @property
    def outbound_url(self):
        """
        **[Required]** Gets the outbound_url of this CreateWebhookChannelDetails.
        The URL to send responses to.


        :return: The outbound_url of this CreateWebhookChannelDetails.
        :rtype: str
        """
        return self._outbound_url

    @outbound_url.setter
    def outbound_url(self, outbound_url):
        """
        Sets the outbound_url of this CreateWebhookChannelDetails.
        The URL to send responses to.


        :param outbound_url: The outbound_url of this CreateWebhookChannelDetails.
        :type: str
        """
        self._outbound_url = outbound_url

    @property
    def payload_version(self):
        """
        **[Required]** Gets the payload_version of this CreateWebhookChannelDetails.
        The version for payloads.

        Allowed values for this property are: "1.0", "1.1"


        :return: The payload_version of this CreateWebhookChannelDetails.
        :rtype: str
        """
        return self._payload_version

    @payload_version.setter
    def payload_version(self, payload_version):
        """
        Sets the payload_version of this CreateWebhookChannelDetails.
        The version for payloads.


        :param payload_version: The payload_version of this CreateWebhookChannelDetails.
        :type: str
        """
        allowed_values = ["1.0", "1.1"]
        if not value_allowed_none_or_none_sentinel(payload_version, allowed_values):
            raise ValueError(
                f"Invalid value for `payload_version`, must be None or one of {allowed_values}"
            )
        self._payload_version = payload_version

    @property
    def bot_id(self):
        """
        Gets the bot_id of this CreateWebhookChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this CreateWebhookChannelDetails.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this CreateWebhookChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this CreateWebhookChannelDetails.
        :type: str
        """
        self._bot_id = bot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
