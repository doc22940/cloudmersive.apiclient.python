# coding: utf-8

"""
    validateapi

    The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WhoisResponse(object):
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
        'valid_domain': 'bool',
        'whois_server': 'str',
        'raw_text_record': 'str',
        'created_dt': 'datetime'
    }

    attribute_map = {
        'valid_domain': 'ValidDomain',
        'whois_server': 'WhoisServer',
        'raw_text_record': 'RawTextRecord',
        'created_dt': 'CreatedDt'
    }

    def __init__(self, valid_domain=None, whois_server=None, raw_text_record=None, created_dt=None):  # noqa: E501
        """WhoisResponse - a model defined in Swagger"""  # noqa: E501

        self._valid_domain = None
        self._whois_server = None
        self._raw_text_record = None
        self._created_dt = None
        self.discriminator = None

        if valid_domain is not None:
            self.valid_domain = valid_domain
        if whois_server is not None:
            self.whois_server = whois_server
        if raw_text_record is not None:
            self.raw_text_record = raw_text_record
        if created_dt is not None:
            self.created_dt = created_dt

    @property
    def valid_domain(self):
        """Gets the valid_domain of this WhoisResponse.  # noqa: E501

        True if the domain is valid, false if it is not  # noqa: E501

        :return: The valid_domain of this WhoisResponse.  # noqa: E501
        :rtype: bool
        """
        return self._valid_domain

    @valid_domain.setter
    def valid_domain(self, valid_domain):
        """Sets the valid_domain of this WhoisResponse.

        True if the domain is valid, false if it is not  # noqa: E501

        :param valid_domain: The valid_domain of this WhoisResponse.  # noqa: E501
        :type: bool
        """

        self._valid_domain = valid_domain

    @property
    def whois_server(self):
        """Gets the whois_server of this WhoisResponse.  # noqa: E501

        Server used to lookup WHOIS information (may change based on lookup).  # noqa: E501

        :return: The whois_server of this WhoisResponse.  # noqa: E501
        :rtype: str
        """
        return self._whois_server

    @whois_server.setter
    def whois_server(self, whois_server):
        """Sets the whois_server of this WhoisResponse.

        Server used to lookup WHOIS information (may change based on lookup).  # noqa: E501

        :param whois_server: The whois_server of this WhoisResponse.  # noqa: E501
        :type: str
        """

        self._whois_server = whois_server

    @property
    def raw_text_record(self):
        """Gets the raw_text_record of this WhoisResponse.  # noqa: E501

        WHOIS raw text record  # noqa: E501

        :return: The raw_text_record of this WhoisResponse.  # noqa: E501
        :rtype: str
        """
        return self._raw_text_record

    @raw_text_record.setter
    def raw_text_record(self, raw_text_record):
        """Sets the raw_text_record of this WhoisResponse.

        WHOIS raw text record  # noqa: E501

        :param raw_text_record: The raw_text_record of this WhoisResponse.  # noqa: E501
        :type: str
        """

        self._raw_text_record = raw_text_record

    @property
    def created_dt(self):
        """Gets the created_dt of this WhoisResponse.  # noqa: E501

        Creation date for the record  # noqa: E501

        :return: The created_dt of this WhoisResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this WhoisResponse.

        Creation date for the record  # noqa: E501

        :param created_dt: The created_dt of this WhoisResponse.  # noqa: E501
        :type: datetime
        """

        self._created_dt = created_dt

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
        if issubclass(WhoisResponse, dict):
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
        if not isinstance(other, WhoisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
