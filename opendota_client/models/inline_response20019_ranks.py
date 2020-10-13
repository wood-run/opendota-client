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


class InlineResponse20019Ranks(object):
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
        'commmand': 'str',
        'row_count': 'int',
        'rows': 'list[InlineResponse20019RanksRows]',
        'fields': 'list[InlineResponse20019RanksFields]',
        'row_as_array': 'bool',
        'sum': 'InlineResponse20019RanksSum'
    }

    attribute_map = {
        'commmand': 'commmand',
        'row_count': 'rowCount',
        'rows': 'rows',
        'fields': 'fields',
        'row_as_array': 'rowAsArray',
        'sum': 'sum'
    }

    def __init__(self, commmand=None, row_count=None, rows=None, fields=None, row_as_array=None, sum=None):  # noqa: E501
        """InlineResponse20019Ranks - a model defined in Swagger"""  # noqa: E501

        self._commmand = None
        self._row_count = None
        self._rows = None
        self._fields = None
        self._row_as_array = None
        self._sum = None
        self.discriminator = None

        if commmand is not None:
            self.commmand = commmand
        if row_count is not None:
            self.row_count = row_count
        if rows is not None:
            self.rows = rows
        if fields is not None:
            self.fields = fields
        if row_as_array is not None:
            self.row_as_array = row_as_array
        if sum is not None:
            self.sum = sum

    @property
    def commmand(self):
        """Gets the commmand of this InlineResponse20019Ranks.  # noqa: E501

        command  # noqa: E501

        :return: The commmand of this InlineResponse20019Ranks.  # noqa: E501
        :rtype: str
        """
        return self._commmand

    @commmand.setter
    def commmand(self, commmand):
        """Sets the commmand of this InlineResponse20019Ranks.

        command  # noqa: E501

        :param commmand: The commmand of this InlineResponse20019Ranks.  # noqa: E501
        :type: str
        """

        self._commmand = commmand

    @property
    def row_count(self):
        """Gets the row_count of this InlineResponse20019Ranks.  # noqa: E501

        rowCount  # noqa: E501

        :return: The row_count of this InlineResponse20019Ranks.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this InlineResponse20019Ranks.

        rowCount  # noqa: E501

        :param row_count: The row_count of this InlineResponse20019Ranks.  # noqa: E501
        :type: int
        """

        self._row_count = row_count

    @property
    def rows(self):
        """Gets the rows of this InlineResponse20019Ranks.  # noqa: E501

        rows  # noqa: E501

        :return: The rows of this InlineResponse20019Ranks.  # noqa: E501
        :rtype: list[InlineResponse20019RanksRows]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this InlineResponse20019Ranks.

        rows  # noqa: E501

        :param rows: The rows of this InlineResponse20019Ranks.  # noqa: E501
        :type: list[InlineResponse20019RanksRows]
        """

        self._rows = rows

    @property
    def fields(self):
        """Gets the fields of this InlineResponse20019Ranks.  # noqa: E501

        fields  # noqa: E501

        :return: The fields of this InlineResponse20019Ranks.  # noqa: E501
        :rtype: list[InlineResponse20019RanksFields]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this InlineResponse20019Ranks.

        fields  # noqa: E501

        :param fields: The fields of this InlineResponse20019Ranks.  # noqa: E501
        :type: list[InlineResponse20019RanksFields]
        """

        self._fields = fields

    @property
    def row_as_array(self):
        """Gets the row_as_array of this InlineResponse20019Ranks.  # noqa: E501

        rowAsArray  # noqa: E501

        :return: The row_as_array of this InlineResponse20019Ranks.  # noqa: E501
        :rtype: bool
        """
        return self._row_as_array

    @row_as_array.setter
    def row_as_array(self, row_as_array):
        """Sets the row_as_array of this InlineResponse20019Ranks.

        rowAsArray  # noqa: E501

        :param row_as_array: The row_as_array of this InlineResponse20019Ranks.  # noqa: E501
        :type: bool
        """

        self._row_as_array = row_as_array

    @property
    def sum(self):
        """Gets the sum of this InlineResponse20019Ranks.  # noqa: E501


        :return: The sum of this InlineResponse20019Ranks.  # noqa: E501
        :rtype: InlineResponse20019RanksSum
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this InlineResponse20019Ranks.


        :param sum: The sum of this InlineResponse20019Ranks.  # noqa: E501
        :type: InlineResponse20019RanksSum
        """

        self._sum = sum

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
        if issubclass(InlineResponse20019Ranks, dict):
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
        if not isinstance(other, InlineResponse20019Ranks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
