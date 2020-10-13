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


class InlineResponse20020(object):
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
        'account_id': 'int',
        'avatarfull': 'str',
        'personaname': 'str',
        'last_match_time': 'str',
        'similarity': 'float'
    }

    attribute_map = {
        'account_id': 'account_id',
        'avatarfull': 'avatarfull',
        'personaname': 'personaname',
        'last_match_time': 'last_match_time',
        'similarity': 'similarity'
    }

    def __init__(self, account_id=None, avatarfull=None, personaname=None, last_match_time=None, similarity=None):  # noqa: E501
        """InlineResponse20020 - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._avatarfull = None
        self._personaname = None
        self._last_match_time = None
        self._similarity = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if avatarfull is not None:
            self.avatarfull = avatarfull
        if personaname is not None:
            self.personaname = personaname
        if last_match_time is not None:
            self.last_match_time = last_match_time
        if similarity is not None:
            self.similarity = similarity

    @property
    def account_id(self):
        """Gets the account_id of this InlineResponse20020.  # noqa: E501

        account_id  # noqa: E501

        :return: The account_id of this InlineResponse20020.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InlineResponse20020.

        account_id  # noqa: E501

        :param account_id: The account_id of this InlineResponse20020.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def avatarfull(self):
        """Gets the avatarfull of this InlineResponse20020.  # noqa: E501

        avatarfull  # noqa: E501

        :return: The avatarfull of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._avatarfull

    @avatarfull.setter
    def avatarfull(self, avatarfull):
        """Sets the avatarfull of this InlineResponse20020.

        avatarfull  # noqa: E501

        :param avatarfull: The avatarfull of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._avatarfull = avatarfull

    @property
    def personaname(self):
        """Gets the personaname of this InlineResponse20020.  # noqa: E501

        personaname  # noqa: E501

        :return: The personaname of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._personaname

    @personaname.setter
    def personaname(self, personaname):
        """Sets the personaname of this InlineResponse20020.

        personaname  # noqa: E501

        :param personaname: The personaname of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._personaname = personaname

    @property
    def last_match_time(self):
        """Gets the last_match_time of this InlineResponse20020.  # noqa: E501

        last_match_time. May not be present or null.  # noqa: E501

        :return: The last_match_time of this InlineResponse20020.  # noqa: E501
        :rtype: str
        """
        return self._last_match_time

    @last_match_time.setter
    def last_match_time(self, last_match_time):
        """Sets the last_match_time of this InlineResponse20020.

        last_match_time. May not be present or null.  # noqa: E501

        :param last_match_time: The last_match_time of this InlineResponse20020.  # noqa: E501
        :type: str
        """

        self._last_match_time = last_match_time

    @property
    def similarity(self):
        """Gets the similarity of this InlineResponse20020.  # noqa: E501

        similarity  # noqa: E501

        :return: The similarity of this InlineResponse20020.  # noqa: E501
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this InlineResponse20020.

        similarity  # noqa: E501

        :param similarity: The similarity of this InlineResponse20020.  # noqa: E501
        :type: float
        """

        self._similarity = similarity

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
        if issubclass(InlineResponse20020, dict):
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
        if not isinstance(other, InlineResponse20020):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
