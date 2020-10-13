# coding: utf-8

"""
    OpenDota API

    # Introduction The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.  You can find data that can be used to convert hero and ability IDs and other information provided by the API from the [dotaconstants](https://github.com/odota/dotaconstants) repository.  **Beginning 2018-04-22, the OpenDota API is limited to 50,000 free calls per month and 60 requests/minute** We offer a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more.   # noqa: E501

    OpenAPI spec version: 18.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse200BuybackLog(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'time': 'int',
        'slot': 'int',
        'player_slot': 'int'
    }

    attribute_map = {
        'time': 'time',
        'slot': 'slot',
        'player_slot': 'player_slot'
    }

    def __init__(self, time=None, slot=None, player_slot=None):  # noqa: E501
        """InlineResponse200BuybackLog - a model defined in Swagger"""  # noqa: E501

        self._time = None
        self._slot = None
        self._player_slot = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if slot is not None:
            self.slot = slot
        if player_slot is not None:
            self.player_slot = player_slot

    @property
    def time(self):
        """Gets the time of this InlineResponse200BuybackLog.  # noqa: E501

        Time in seconds the buyback occurred  # noqa: E501

        :return: The time of this InlineResponse200BuybackLog.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse200BuybackLog.

        Time in seconds the buyback occurred  # noqa: E501

        :param time: The time of this InlineResponse200BuybackLog.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def slot(self):
        """Gets the slot of this InlineResponse200BuybackLog.  # noqa: E501

        slot  # noqa: E501

        :return: The slot of this InlineResponse200BuybackLog.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this InlineResponse200BuybackLog.

        slot  # noqa: E501

        :param slot: The slot of this InlineResponse200BuybackLog.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def player_slot(self):
        """Gets the player_slot of this InlineResponse200BuybackLog.  # noqa: E501

        Which slot the player is in. 0-127 are Radiant, 128-255 are Dire  # noqa: E501

        :return: The player_slot of this InlineResponse200BuybackLog.  # noqa: E501
        :rtype: int
        """
        return self._player_slot

    @player_slot.setter
    def player_slot(self, player_slot):
        """Sets the player_slot of this InlineResponse200BuybackLog.

        Which slot the player is in. 0-127 are Radiant, 128-255 are Dire  # noqa: E501

        :param player_slot: The player_slot of this InlineResponse200BuybackLog.  # noqa: E501
        :type: int
        """

        self._player_slot = player_slot

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse200BuybackLog, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200BuybackLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
