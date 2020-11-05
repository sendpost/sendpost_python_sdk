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


class ModelsStat(object):
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
        'clicked': 'int',
        'delivered': 'int',
        'dropped': 'int',
        'hard_bounced': 'int',
        'opened': 'int',
        'processed': 'int',
        'soft_bounced': 'int',
        'spam': 'int',
        'unsubscribed': 'int'
    }

    attribute_map = {
        'clicked': 'clicked',
        'delivered': 'delivered',
        'dropped': 'dropped',
        'hard_bounced': 'hardBounced',
        'opened': 'opened',
        'processed': 'processed',
        'soft_bounced': 'softBounced',
        'spam': 'spam',
        'unsubscribed': 'unsubscribed'
    }

    def __init__(self, clicked=None, delivered=None, dropped=None, hard_bounced=None, opened=None, processed=None, soft_bounced=None, spam=None, unsubscribed=None):  # noqa: E501
        """ModelsStat - a model defined in Swagger"""  # noqa: E501

        self._clicked = None
        self._delivered = None
        self._dropped = None
        self._hard_bounced = None
        self._opened = None
        self._processed = None
        self._soft_bounced = None
        self._spam = None
        self._unsubscribed = None
        self.discriminator = None

        if clicked is not None:
            self.clicked = clicked
        if delivered is not None:
            self.delivered = delivered
        if dropped is not None:
            self.dropped = dropped
        if hard_bounced is not None:
            self.hard_bounced = hard_bounced
        if opened is not None:
            self.opened = opened
        if processed is not None:
            self.processed = processed
        if soft_bounced is not None:
            self.soft_bounced = soft_bounced
        if spam is not None:
            self.spam = spam
        if unsubscribed is not None:
            self.unsubscribed = unsubscribed

    @property
    def clicked(self):
        """Gets the clicked of this ModelsStat.  # noqa: E501


        :return: The clicked of this ModelsStat.  # noqa: E501
        :rtype: int
        """
        return self._clicked

    @clicked.setter
    def clicked(self, clicked):
        """Sets the clicked of this ModelsStat.


        :param clicked: The clicked of this ModelsStat.  # noqa: E501
        :type: int
        """

        self._clicked = clicked

    @property
    def delivered(self):
        """Gets the delivered of this ModelsStat.  # noqa: E501


        :return: The delivered of this ModelsStat.  # noqa: E501
        :rtype: int
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """Sets the delivered of this ModelsStat.


        :param delivered: The delivered of this ModelsStat.  # noqa: E501
        :type: int
        """

        self._delivered = delivered

    @property
    def dropped(self):
        """Gets the dropped of this ModelsStat.  # noqa: E501


        :return: The dropped of this ModelsStat.  # noqa: E501
        :rtype: int
        """
        return self._dropped

    @dropped.setter
    def dropped(self, dropped):
        """Sets the dropped of this ModelsStat.


        :param dropped: The dropped of this ModelsStat.  # noqa: E501
        :type: int
        """

        self._dropped = dropped

    @property
    def hard_bounced(self):
        """Gets the hard_bounced of this ModelsStat.  # noqa: E501


        :return: The hard_bounced of this ModelsStat.  # noqa: E501
        :rtype: int
        """
        return self._hard_bounced

    @hard_bounced.setter
    def hard_bounced(self, hard_bounced):
        """Sets the hard_bounced of this ModelsStat.


        :param hard_bounced: The hard_bounced of this ModelsStat.  # noqa: E501
        :type: int
        """

        self._hard_bounced = hard_bounced

    @property
    def opened(self):
        """Gets the opened of this ModelsStat.  # noqa: E501


        :return: The opened of this ModelsStat.  # noqa: E501
        :rtype: int
        """
        return self._opened

    @opened.setter
    def opened(self, opened):
        """Sets the opened of this ModelsStat.


        :param opened: The opened of this ModelsStat.  # noqa: E501
        :type: int
        """

        self._opened = opened

    @property
    def processed(self):
        """Gets the processed of this ModelsStat.  # noqa: E501


        :return: The processed of this ModelsStat.  # noqa: E501
        :rtype: int
        """
        return self._processed

    @processed.setter
    def processed(self, processed):
        """Sets the processed of this ModelsStat.


        :param processed: The processed of this ModelsStat.  # noqa: E501
        :type: int
        """

        self._processed = processed

    @property
    def soft_bounced(self):
        """Gets the soft_bounced of this ModelsStat.  # noqa: E501


        :return: The soft_bounced of this ModelsStat.  # noqa: E501
        :rtype: int
        """
        return self._soft_bounced

    @soft_bounced.setter
    def soft_bounced(self, soft_bounced):
        """Sets the soft_bounced of this ModelsStat.


        :param soft_bounced: The soft_bounced of this ModelsStat.  # noqa: E501
        :type: int
        """

        self._soft_bounced = soft_bounced

    @property
    def spam(self):
        """Gets the spam of this ModelsStat.  # noqa: E501


        :return: The spam of this ModelsStat.  # noqa: E501
        :rtype: int
        """
        return self._spam

    @spam.setter
    def spam(self, spam):
        """Sets the spam of this ModelsStat.


        :param spam: The spam of this ModelsStat.  # noqa: E501
        :type: int
        """

        self._spam = spam

    @property
    def unsubscribed(self):
        """Gets the unsubscribed of this ModelsStat.  # noqa: E501


        :return: The unsubscribed of this ModelsStat.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribed

    @unsubscribed.setter
    def unsubscribed(self, unsubscribed):
        """Sets the unsubscribed of this ModelsStat.


        :param unsubscribed: The unsubscribed of this ModelsStat.  # noqa: E501
        :type: int
        """

        self._unsubscribed = unsubscribed

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
        if issubclass(ModelsStat, dict):
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
        if not isinstance(other, ModelsStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
