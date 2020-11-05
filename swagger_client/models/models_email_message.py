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


class ModelsEmailMessage(object):
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
        'amp_body': 'str',
        '_from': 'ModelsFrom',
        'groups': 'object',
        'headers': 'object',
        'html_body': 'str',
        'ippool': 'str',
        'pre_text': 'str',
        'reply_to': 'ModelsReplyTo',
        'subject': 'str',
        'text_body': 'str',
        'to': 'list[ModelsTo]',
        'track_clicks': 'bool',
        'track_opens': 'bool'
    }

    attribute_map = {
        'amp_body': 'ampBody',
        '_from': 'from',
        'groups': 'groups',
        'headers': 'headers',
        'html_body': 'htmlBody',
        'ippool': 'ippool',
        'pre_text': 'preText',
        'reply_to': 'replyTo',
        'subject': 'subject',
        'text_body': 'textBody',
        'to': 'to',
        'track_clicks': 'trackClicks',
        'track_opens': 'trackOpens'
    }

    def __init__(self, amp_body=None, _from=None, groups=None, headers=None, html_body=None, ippool=None, pre_text=None, reply_to=None, subject=None, text_body=None, to=None, track_clicks=None, track_opens=None):  # noqa: E501
        """ModelsEmailMessage - a model defined in Swagger"""  # noqa: E501

        self._amp_body = None
        self.__from = None
        self._groups = None
        self._headers = None
        self._html_body = None
        self._ippool = None
        self._pre_text = None
        self._reply_to = None
        self._subject = None
        self._text_body = None
        self._to = None
        self._track_clicks = None
        self._track_opens = None
        self.discriminator = None

        if amp_body is not None:
            self.amp_body = amp_body
        if _from is not None:
            self._from = _from
        if groups is not None:
            self.groups = groups
        if headers is not None:
            self.headers = headers
        if html_body is not None:
            self.html_body = html_body
        if ippool is not None:
            self.ippool = ippool
        if pre_text is not None:
            self.pre_text = pre_text
        if reply_to is not None:
            self.reply_to = reply_to
        if subject is not None:
            self.subject = subject
        if text_body is not None:
            self.text_body = text_body
        if to is not None:
            self.to = to
        if track_clicks is not None:
            self.track_clicks = track_clicks
        if track_opens is not None:
            self.track_opens = track_opens

    @property
    def amp_body(self):
        """Gets the amp_body of this ModelsEmailMessage.  # noqa: E501


        :return: The amp_body of this ModelsEmailMessage.  # noqa: E501
        :rtype: str
        """
        return self._amp_body

    @amp_body.setter
    def amp_body(self, amp_body):
        """Sets the amp_body of this ModelsEmailMessage.


        :param amp_body: The amp_body of this ModelsEmailMessage.  # noqa: E501
        :type: str
        """

        self._amp_body = amp_body

    @property
    def _from(self):
        """Gets the _from of this ModelsEmailMessage.  # noqa: E501


        :return: The _from of this ModelsEmailMessage.  # noqa: E501
        :rtype: ModelsFrom
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ModelsEmailMessage.


        :param _from: The _from of this ModelsEmailMessage.  # noqa: E501
        :type: ModelsFrom
        """

        self.__from = _from

    @property
    def groups(self):
        """Gets the groups of this ModelsEmailMessage.  # noqa: E501


        :return: The groups of this ModelsEmailMessage.  # noqa: E501
        :rtype: object
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ModelsEmailMessage.


        :param groups: The groups of this ModelsEmailMessage.  # noqa: E501
        :type: object
        """

        self._groups = groups

    @property
    def headers(self):
        """Gets the headers of this ModelsEmailMessage.  # noqa: E501


        :return: The headers of this ModelsEmailMessage.  # noqa: E501
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ModelsEmailMessage.


        :param headers: The headers of this ModelsEmailMessage.  # noqa: E501
        :type: object
        """

        self._headers = headers

    @property
    def html_body(self):
        """Gets the html_body of this ModelsEmailMessage.  # noqa: E501


        :return: The html_body of this ModelsEmailMessage.  # noqa: E501
        :rtype: str
        """
        return self._html_body

    @html_body.setter
    def html_body(self, html_body):
        """Sets the html_body of this ModelsEmailMessage.


        :param html_body: The html_body of this ModelsEmailMessage.  # noqa: E501
        :type: str
        """

        self._html_body = html_body

    @property
    def ippool(self):
        """Gets the ippool of this ModelsEmailMessage.  # noqa: E501


        :return: The ippool of this ModelsEmailMessage.  # noqa: E501
        :rtype: str
        """
        return self._ippool

    @ippool.setter
    def ippool(self, ippool):
        """Sets the ippool of this ModelsEmailMessage.


        :param ippool: The ippool of this ModelsEmailMessage.  # noqa: E501
        :type: str
        """

        self._ippool = ippool

    @property
    def pre_text(self):
        """Gets the pre_text of this ModelsEmailMessage.  # noqa: E501


        :return: The pre_text of this ModelsEmailMessage.  # noqa: E501
        :rtype: str
        """
        return self._pre_text

    @pre_text.setter
    def pre_text(self, pre_text):
        """Sets the pre_text of this ModelsEmailMessage.


        :param pre_text: The pre_text of this ModelsEmailMessage.  # noqa: E501
        :type: str
        """

        self._pre_text = pre_text

    @property
    def reply_to(self):
        """Gets the reply_to of this ModelsEmailMessage.  # noqa: E501


        :return: The reply_to of this ModelsEmailMessage.  # noqa: E501
        :rtype: ModelsReplyTo
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this ModelsEmailMessage.


        :param reply_to: The reply_to of this ModelsEmailMessage.  # noqa: E501
        :type: ModelsReplyTo
        """

        self._reply_to = reply_to

    @property
    def subject(self):
        """Gets the subject of this ModelsEmailMessage.  # noqa: E501


        :return: The subject of this ModelsEmailMessage.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ModelsEmailMessage.


        :param subject: The subject of this ModelsEmailMessage.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def text_body(self):
        """Gets the text_body of this ModelsEmailMessage.  # noqa: E501


        :return: The text_body of this ModelsEmailMessage.  # noqa: E501
        :rtype: str
        """
        return self._text_body

    @text_body.setter
    def text_body(self, text_body):
        """Sets the text_body of this ModelsEmailMessage.


        :param text_body: The text_body of this ModelsEmailMessage.  # noqa: E501
        :type: str
        """

        self._text_body = text_body

    @property
    def to(self):
        """Gets the to of this ModelsEmailMessage.  # noqa: E501


        :return: The to of this ModelsEmailMessage.  # noqa: E501
        :rtype: list[ModelsTo]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ModelsEmailMessage.


        :param to: The to of this ModelsEmailMessage.  # noqa: E501
        :type: list[ModelsTo]
        """

        self._to = to

    @property
    def track_clicks(self):
        """Gets the track_clicks of this ModelsEmailMessage.  # noqa: E501


        :return: The track_clicks of this ModelsEmailMessage.  # noqa: E501
        :rtype: bool
        """
        return self._track_clicks

    @track_clicks.setter
    def track_clicks(self, track_clicks):
        """Sets the track_clicks of this ModelsEmailMessage.


        :param track_clicks: The track_clicks of this ModelsEmailMessage.  # noqa: E501
        :type: bool
        """

        self._track_clicks = track_clicks

    @property
    def track_opens(self):
        """Gets the track_opens of this ModelsEmailMessage.  # noqa: E501


        :return: The track_opens of this ModelsEmailMessage.  # noqa: E501
        :rtype: bool
        """
        return self._track_opens

    @track_opens.setter
    def track_opens(self, track_opens):
        """Sets the track_opens of this ModelsEmailMessage.


        :param track_opens: The track_opens of this ModelsEmailMessage.  # noqa: E501
        :type: bool
        """

        self._track_opens = track_opens

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
        if issubclass(ModelsEmailMessage, dict):
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
        if not isinstance(other, ModelsEmailMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
