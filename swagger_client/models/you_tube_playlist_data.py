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

class YouTubePlaylistData(object):
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
        'title': 'str',
        'auhtor': 'str',
        'videos': 'list[YouTubePlaylistDataItem]',
        'error_message': 'str'
    }

    attribute_map = {
        'title': 'title',
        'auhtor': 'auhtor',
        'videos': 'videos',
        'error_message': 'errorMessage'
    }

    def __init__(self, title=None, auhtor=None, videos=None, error_message=None):  # noqa: E501
        """YouTubePlaylistData - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._auhtor = None
        self._videos = None
        self._error_message = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if auhtor is not None:
            self.auhtor = auhtor
        if videos is not None:
            self.videos = videos
        if error_message is not None:
            self.error_message = error_message

    @property
    def title(self):
        """Gets the title of this YouTubePlaylistData.  # noqa: E501


        :return: The title of this YouTubePlaylistData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this YouTubePlaylistData.


        :param title: The title of this YouTubePlaylistData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def auhtor(self):
        """Gets the auhtor of this YouTubePlaylistData.  # noqa: E501


        :return: The auhtor of this YouTubePlaylistData.  # noqa: E501
        :rtype: str
        """
        return self._auhtor

    @auhtor.setter
    def auhtor(self, auhtor):
        """Sets the auhtor of this YouTubePlaylistData.


        :param auhtor: The auhtor of this YouTubePlaylistData.  # noqa: E501
        :type: str
        """

        self._auhtor = auhtor

    @property
    def videos(self):
        """Gets the videos of this YouTubePlaylistData.  # noqa: E501


        :return: The videos of this YouTubePlaylistData.  # noqa: E501
        :rtype: list[YouTubePlaylistDataItem]
        """
        return self._videos

    @videos.setter
    def videos(self, videos):
        """Sets the videos of this YouTubePlaylistData.


        :param videos: The videos of this YouTubePlaylistData.  # noqa: E501
        :type: list[YouTubePlaylistDataItem]
        """

        self._videos = videos

    @property
    def error_message(self):
        """Gets the error_message of this YouTubePlaylistData.  # noqa: E501


        :return: The error_message of this YouTubePlaylistData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this YouTubePlaylistData.


        :param error_message: The error_message of this YouTubePlaylistData.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(YouTubePlaylistData, dict):
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
        if not isinstance(other, YouTubePlaylistData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
