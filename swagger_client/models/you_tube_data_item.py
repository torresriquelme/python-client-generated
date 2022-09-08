# coding: utf-8

"""
    IMDb-API

    The IMDb-API Documentation. You need a <a href='/Identity/Account/Manage' target='_blank'><code>API Key</code></a> for testing APIs.<br/><a class='link' href='/API'>Back to API Tester</a>  # noqa: E501

    OpenAPI spec version: 1.8.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class YouTubeDataItem(object):
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
        'quality': 'str',
        'mime_type': 'str',
        'extension': 'str',
        'url': 'str'
    }

    attribute_map = {
        'quality': 'quality',
        'mime_type': 'mimeType',
        'extension': 'extension',
        'url': 'url'
    }

    def __init__(self, quality=None, mime_type=None, extension=None, url=None):  # noqa: E501
        """YouTubeDataItem - a model defined in Swagger"""  # noqa: E501
        self._quality = None
        self._mime_type = None
        self._extension = None
        self._url = None
        self.discriminator = None
        if quality is not None:
            self.quality = quality
        if mime_type is not None:
            self.mime_type = mime_type
        if extension is not None:
            self.extension = extension
        if url is not None:
            self.url = url

    @property
    def quality(self):
        """Gets the quality of this YouTubeDataItem.  # noqa: E501


        :return: The quality of this YouTubeDataItem.  # noqa: E501
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this YouTubeDataItem.


        :param quality: The quality of this YouTubeDataItem.  # noqa: E501
        :type: str
        """

        self._quality = quality

    @property
    def mime_type(self):
        """Gets the mime_type of this YouTubeDataItem.  # noqa: E501


        :return: The mime_type of this YouTubeDataItem.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this YouTubeDataItem.


        :param mime_type: The mime_type of this YouTubeDataItem.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def extension(self):
        """Gets the extension of this YouTubeDataItem.  # noqa: E501


        :return: The extension of this YouTubeDataItem.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this YouTubeDataItem.


        :param extension: The extension of this YouTubeDataItem.  # noqa: E501
        :type: str
        """

        self._extension = extension

    @property
    def url(self):
        """Gets the url of this YouTubeDataItem.  # noqa: E501


        :return: The url of this YouTubeDataItem.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this YouTubeDataItem.


        :param url: The url of this YouTubeDataItem.  # noqa: E501
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
        if issubclass(YouTubeDataItem, dict):
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
        if not isinstance(other, YouTubeDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other