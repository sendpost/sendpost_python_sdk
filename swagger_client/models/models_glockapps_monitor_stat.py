# coding: utf-8

"""
    SendPost API

    SendPost API to send transactional emails reliably  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hello@sendx.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelsGlockappsMonitorStat(object):
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
        'day': 'int',
        'listed_count': 'int',
        'listed_in': 'list[ModelsGlockappsBlacklist]',
        'month': 'int',
        'sender_score': 'int',
        'year': 'int'
    }

    attribute_map = {
        'day': 'day',
        'listed_count': 'listedCount',
        'listed_in': 'listedIn',
        'month': 'month',
        'sender_score': 'senderScore',
        'year': 'year'
    }

    def __init__(self, day=None, listed_count=None, listed_in=None, month=None, sender_score=None, year=None):  # noqa: E501
        """ModelsGlockappsMonitorStat - a model defined in Swagger"""  # noqa: E501

        self._day = None
        self._listed_count = None
        self._listed_in = None
        self._month = None
        self._sender_score = None
        self._year = None
        self.discriminator = None

        if day is not None:
            self.day = day
        if listed_count is not None:
            self.listed_count = listed_count
        if listed_in is not None:
            self.listed_in = listed_in
        if month is not None:
            self.month = month
        if sender_score is not None:
            self.sender_score = sender_score
        if year is not None:
            self.year = year

    @property
    def day(self):
        """Gets the day of this ModelsGlockappsMonitorStat.  # noqa: E501


        :return: The day of this ModelsGlockappsMonitorStat.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this ModelsGlockappsMonitorStat.


        :param day: The day of this ModelsGlockappsMonitorStat.  # noqa: E501
        :type: int
        """

        self._day = day

    @property
    def listed_count(self):
        """Gets the listed_count of this ModelsGlockappsMonitorStat.  # noqa: E501


        :return: The listed_count of this ModelsGlockappsMonitorStat.  # noqa: E501
        :rtype: int
        """
        return self._listed_count

    @listed_count.setter
    def listed_count(self, listed_count):
        """Sets the listed_count of this ModelsGlockappsMonitorStat.


        :param listed_count: The listed_count of this ModelsGlockappsMonitorStat.  # noqa: E501
        :type: int
        """

        self._listed_count = listed_count

    @property
    def listed_in(self):
        """Gets the listed_in of this ModelsGlockappsMonitorStat.  # noqa: E501


        :return: The listed_in of this ModelsGlockappsMonitorStat.  # noqa: E501
        :rtype: list[ModelsGlockappsBlacklist]
        """
        return self._listed_in

    @listed_in.setter
    def listed_in(self, listed_in):
        """Sets the listed_in of this ModelsGlockappsMonitorStat.


        :param listed_in: The listed_in of this ModelsGlockappsMonitorStat.  # noqa: E501
        :type: list[ModelsGlockappsBlacklist]
        """

        self._listed_in = listed_in

    @property
    def month(self):
        """Gets the month of this ModelsGlockappsMonitorStat.  # noqa: E501


        :return: The month of this ModelsGlockappsMonitorStat.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this ModelsGlockappsMonitorStat.


        :param month: The month of this ModelsGlockappsMonitorStat.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def sender_score(self):
        """Gets the sender_score of this ModelsGlockappsMonitorStat.  # noqa: E501


        :return: The sender_score of this ModelsGlockappsMonitorStat.  # noqa: E501
        :rtype: int
        """
        return self._sender_score

    @sender_score.setter
    def sender_score(self, sender_score):
        """Sets the sender_score of this ModelsGlockappsMonitorStat.


        :param sender_score: The sender_score of this ModelsGlockappsMonitorStat.  # noqa: E501
        :type: int
        """

        self._sender_score = sender_score

    @property
    def year(self):
        """Gets the year of this ModelsGlockappsMonitorStat.  # noqa: E501


        :return: The year of this ModelsGlockappsMonitorStat.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this ModelsGlockappsMonitorStat.


        :param year: The year of this ModelsGlockappsMonitorStat.  # noqa: E501
        :type: int
        """

        self._year = year

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
        if issubclass(ModelsGlockappsMonitorStat, dict):
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
        if not isinstance(other, ModelsGlockappsMonitorStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
