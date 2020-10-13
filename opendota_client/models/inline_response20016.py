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


class InlineResponse20016(object):
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
        'match_id': 'int',
        'match_seq_num': 'int',
        'radiant_win': 'bool',
        'start_time': 'int',
        'duration': 'int',
        'radiant_team': 'str',
        'dire_team': 'str'
    }

    attribute_map = {
        'match_id': 'match_id',
        'match_seq_num': 'match_seq_num',
        'radiant_win': 'radiant_win',
        'start_time': 'start_time',
        'duration': 'duration',
        'radiant_team': 'radiant_team',
        'dire_team': 'dire_team'
    }

    def __init__(self, match_id=None, match_seq_num=None, radiant_win=None, start_time=None, duration=None, radiant_team=None, dire_team=None):  # noqa: E501
        """InlineResponse20016 - a model defined in Swagger"""  # noqa: E501

        self._match_id = None
        self._match_seq_num = None
        self._radiant_win = None
        self._start_time = None
        self._duration = None
        self._radiant_team = None
        self._dire_team = None
        self.discriminator = None

        if match_id is not None:
            self.match_id = match_id
        if match_seq_num is not None:
            self.match_seq_num = match_seq_num
        if radiant_win is not None:
            self.radiant_win = radiant_win
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if radiant_team is not None:
            self.radiant_team = radiant_team
        if dire_team is not None:
            self.dire_team = dire_team

    @property
    def match_id(self):
        """Gets the match_id of this InlineResponse20016.  # noqa: E501

        match_id  # noqa: E501

        :return: The match_id of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id):
        """Sets the match_id of this InlineResponse20016.

        match_id  # noqa: E501

        :param match_id: The match_id of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._match_id = match_id

    @property
    def match_seq_num(self):
        """Gets the match_seq_num of this InlineResponse20016.  # noqa: E501

        match_seq_num  # noqa: E501

        :return: The match_seq_num of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._match_seq_num

    @match_seq_num.setter
    def match_seq_num(self, match_seq_num):
        """Sets the match_seq_num of this InlineResponse20016.

        match_seq_num  # noqa: E501

        :param match_seq_num: The match_seq_num of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._match_seq_num = match_seq_num

    @property
    def radiant_win(self):
        """Gets the radiant_win of this InlineResponse20016.  # noqa: E501

        Boolean indicating whether Radiant won the match  # noqa: E501

        :return: The radiant_win of this InlineResponse20016.  # noqa: E501
        :rtype: bool
        """
        return self._radiant_win

    @radiant_win.setter
    def radiant_win(self, radiant_win):
        """Sets the radiant_win of this InlineResponse20016.

        Boolean indicating whether Radiant won the match  # noqa: E501

        :param radiant_win: The radiant_win of this InlineResponse20016.  # noqa: E501
        :type: bool
        """

        self._radiant_win = radiant_win

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse20016.  # noqa: E501

        start_time  # noqa: E501

        :return: The start_time of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse20016.

        start_time  # noqa: E501

        :param start_time: The start_time of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this InlineResponse20016.  # noqa: E501

        Duration of the game in seconds  # noqa: E501

        :return: The duration of this InlineResponse20016.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse20016.

        Duration of the game in seconds  # noqa: E501

        :param duration: The duration of this InlineResponse20016.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def radiant_team(self):
        """Gets the radiant_team of this InlineResponse20016.  # noqa: E501

        radiant_team  # noqa: E501

        :return: The radiant_team of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._radiant_team

    @radiant_team.setter
    def radiant_team(self, radiant_team):
        """Sets the radiant_team of this InlineResponse20016.

        radiant_team  # noqa: E501

        :param radiant_team: The radiant_team of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._radiant_team = radiant_team

    @property
    def dire_team(self):
        """Gets the dire_team of this InlineResponse20016.  # noqa: E501

        dire_team  # noqa: E501

        :return: The dire_team of this InlineResponse20016.  # noqa: E501
        :rtype: str
        """
        return self._dire_team

    @dire_team.setter
    def dire_team(self, dire_team):
        """Sets the dire_team of this InlineResponse20016.

        dire_team  # noqa: E501

        :param dire_team: The dire_team of this InlineResponse20016.  # noqa: E501
        :type: str
        """

        self._dire_team = dire_team

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
        if issubclass(InlineResponse20016, dict):
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
        if not isinstance(other, InlineResponse20016):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other