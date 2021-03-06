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


class ModelsRStat(object):
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
        '_date': 'str',
        'stat': 'ModelsStat'
    }

    attribute_map = {
        '_date': 'date',
        'stat': 'stat'
    }

    def __init__(self, _date=None, stat=None):  # noqa: E501
        """ModelsRStat - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._stat = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if stat is not None:
            self.stat = stat

    @property
    def _date(self):
        """Gets the _date of this ModelsRStat.  # noqa: E501


        :return: The _date of this ModelsRStat.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ModelsRStat.


        :param _date: The _date of this ModelsRStat.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def stat(self):
        """Gets the stat of this ModelsRStat.  # noqa: E501


        :return: The stat of this ModelsRStat.  # noqa: E501
        :rtype: ModelsStat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this ModelsRStat.


        :param stat: The stat of this ModelsRStat.  # noqa: E501
        :type: ModelsStat
        """

        self._stat = stat

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
        if issubclass(ModelsRStat, dict):
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
        if not isinstance(other, ModelsRStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
