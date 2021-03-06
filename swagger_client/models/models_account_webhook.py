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


class ModelsAccountWebhook(object):
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
        'clicked': 'bool',
        'created': 'int',
        'delivered': 'bool',
        'dropped': 'bool',
        'enabled': 'bool',
        'hard_bounced': 'bool',
        'id': 'int',
        'opened': 'bool',
        'processed': 'bool',
        'soft_bounced': 'bool',
        'spam': 'bool',
        'unsubscribed': 'bool',
        'url': 'str'
    }

    attribute_map = {
        'clicked': 'clicked',
        'created': 'created',
        'delivered': 'delivered',
        'dropped': 'dropped',
        'enabled': 'enabled',
        'hard_bounced': 'hardBounced',
        'id': 'id',
        'opened': 'opened',
        'processed': 'processed',
        'soft_bounced': 'softBounced',
        'spam': 'spam',
        'unsubscribed': 'unsubscribed',
        'url': 'url'
    }

    def __init__(self, clicked=None, created=None, delivered=None, dropped=None, enabled=None, hard_bounced=None, id=None, opened=None, processed=None, soft_bounced=None, spam=None, unsubscribed=None, url=None):  # noqa: E501
        """ModelsAccountWebhook - a model defined in Swagger"""  # noqa: E501

        self._clicked = None
        self._created = None
        self._delivered = None
        self._dropped = None
        self._enabled = None
        self._hard_bounced = None
        self._id = None
        self._opened = None
        self._processed = None
        self._soft_bounced = None
        self._spam = None
        self._unsubscribed = None
        self._url = None
        self.discriminator = None

        if clicked is not None:
            self.clicked = clicked
        if created is not None:
            self.created = created
        if delivered is not None:
            self.delivered = delivered
        if dropped is not None:
            self.dropped = dropped
        if enabled is not None:
            self.enabled = enabled
        if hard_bounced is not None:
            self.hard_bounced = hard_bounced
        if id is not None:
            self.id = id
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
        if url is not None:
            self.url = url

    @property
    def clicked(self):
        """Gets the clicked of this ModelsAccountWebhook.  # noqa: E501


        :return: The clicked of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._clicked

    @clicked.setter
    def clicked(self, clicked):
        """Sets the clicked of this ModelsAccountWebhook.


        :param clicked: The clicked of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._clicked = clicked

    @property
    def created(self):
        """Gets the created of this ModelsAccountWebhook.  # noqa: E501


        :return: The created of this ModelsAccountWebhook.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ModelsAccountWebhook.


        :param created: The created of this ModelsAccountWebhook.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def delivered(self):
        """Gets the delivered of this ModelsAccountWebhook.  # noqa: E501


        :return: The delivered of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """Sets the delivered of this ModelsAccountWebhook.


        :param delivered: The delivered of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._delivered = delivered

    @property
    def dropped(self):
        """Gets the dropped of this ModelsAccountWebhook.  # noqa: E501


        :return: The dropped of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._dropped

    @dropped.setter
    def dropped(self, dropped):
        """Sets the dropped of this ModelsAccountWebhook.


        :param dropped: The dropped of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._dropped = dropped

    @property
    def enabled(self):
        """Gets the enabled of this ModelsAccountWebhook.  # noqa: E501


        :return: The enabled of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ModelsAccountWebhook.


        :param enabled: The enabled of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def hard_bounced(self):
        """Gets the hard_bounced of this ModelsAccountWebhook.  # noqa: E501


        :return: The hard_bounced of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._hard_bounced

    @hard_bounced.setter
    def hard_bounced(self, hard_bounced):
        """Sets the hard_bounced of this ModelsAccountWebhook.


        :param hard_bounced: The hard_bounced of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._hard_bounced = hard_bounced

    @property
    def id(self):
        """Gets the id of this ModelsAccountWebhook.  # noqa: E501


        :return: The id of this ModelsAccountWebhook.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsAccountWebhook.


        :param id: The id of this ModelsAccountWebhook.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def opened(self):
        """Gets the opened of this ModelsAccountWebhook.  # noqa: E501


        :return: The opened of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._opened

    @opened.setter
    def opened(self, opened):
        """Sets the opened of this ModelsAccountWebhook.


        :param opened: The opened of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._opened = opened

    @property
    def processed(self):
        """Gets the processed of this ModelsAccountWebhook.  # noqa: E501


        :return: The processed of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._processed

    @processed.setter
    def processed(self, processed):
        """Sets the processed of this ModelsAccountWebhook.


        :param processed: The processed of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._processed = processed

    @property
    def soft_bounced(self):
        """Gets the soft_bounced of this ModelsAccountWebhook.  # noqa: E501


        :return: The soft_bounced of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._soft_bounced

    @soft_bounced.setter
    def soft_bounced(self, soft_bounced):
        """Sets the soft_bounced of this ModelsAccountWebhook.


        :param soft_bounced: The soft_bounced of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._soft_bounced = soft_bounced

    @property
    def spam(self):
        """Gets the spam of this ModelsAccountWebhook.  # noqa: E501


        :return: The spam of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._spam

    @spam.setter
    def spam(self, spam):
        """Sets the spam of this ModelsAccountWebhook.


        :param spam: The spam of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._spam = spam

    @property
    def unsubscribed(self):
        """Gets the unsubscribed of this ModelsAccountWebhook.  # noqa: E501


        :return: The unsubscribed of this ModelsAccountWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._unsubscribed

    @unsubscribed.setter
    def unsubscribed(self, unsubscribed):
        """Sets the unsubscribed of this ModelsAccountWebhook.


        :param unsubscribed: The unsubscribed of this ModelsAccountWebhook.  # noqa: E501
        :type: bool
        """

        self._unsubscribed = unsubscribed

    @property
    def url(self):
        """Gets the url of this ModelsAccountWebhook.  # noqa: E501


        :return: The url of this ModelsAccountWebhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ModelsAccountWebhook.


        :param url: The url of this ModelsAccountWebhook.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(ModelsAccountWebhook, dict):
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
        if not isinstance(other, ModelsAccountWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
