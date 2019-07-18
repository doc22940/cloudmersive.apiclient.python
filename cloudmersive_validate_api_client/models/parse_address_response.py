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


class ParseAddressResponse(object):
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
        'successful': 'bool',
        'building': 'str',
        'street_number': 'str',
        'street': 'str',
        'city': 'str',
        'state_or_province': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'successful': 'Successful',
        'building': 'Building',
        'street_number': 'StreetNumber',
        'street': 'Street',
        'city': 'City',
        'state_or_province': 'StateOrProvince',
        'postal_code': 'PostalCode',
        'country': 'Country'
    }

    def __init__(self, successful=None, building=None, street_number=None, street=None, city=None, state_or_province=None, postal_code=None, country=None):  # noqa: E501
        """ParseAddressResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._building = None
        self._street_number = None
        self._street = None
        self._city = None
        self._state_or_province = None
        self._postal_code = None
        self._country = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if building is not None:
            self.building = building
        if street_number is not None:
            self.street_number = street_number
        if street is not None:
            self.street = street
        if city is not None:
            self.city = city
        if state_or_province is not None:
            self.state_or_province = state_or_province
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country

    @property
    def successful(self):
        """Gets the successful of this ParseAddressResponse.  # noqa: E501

        True if the parsing operation was successful, false otherwise  # noqa: E501

        :return: The successful of this ParseAddressResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this ParseAddressResponse.

        True if the parsing operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this ParseAddressResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def building(self):
        """Gets the building of this ParseAddressResponse.  # noqa: E501

        The name of the building, house or structure if applicable, such as \"Cloudmersive Building 2\".  This will often by null.  # noqa: E501

        :return: The building of this ParseAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._building

    @building.setter
    def building(self, building):
        """Sets the building of this ParseAddressResponse.

        The name of the building, house or structure if applicable, such as \"Cloudmersive Building 2\".  This will often by null.  # noqa: E501

        :param building: The building of this ParseAddressResponse.  # noqa: E501
        :type: str
        """

        self._building = building

    @property
    def street_number(self):
        """Gets the street_number of this ParseAddressResponse.  # noqa: E501

        The street number or house number of the address.  For example, in the address \"1600 Pennsylvania Avenue NW\" the street number would be \"1600\".  This value will typically be populated for most addresses.  # noqa: E501

        :return: The street_number of this ParseAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._street_number

    @street_number.setter
    def street_number(self, street_number):
        """Sets the street_number of this ParseAddressResponse.

        The street number or house number of the address.  For example, in the address \"1600 Pennsylvania Avenue NW\" the street number would be \"1600\".  This value will typically be populated for most addresses.  # noqa: E501

        :param street_number: The street_number of this ParseAddressResponse.  # noqa: E501
        :type: str
        """

        self._street_number = street_number

    @property
    def street(self):
        """Gets the street of this ParseAddressResponse.  # noqa: E501

        The name of the street or road of the address.  For example, in the address \"1600 Pennsylvania Avenue NW\" the street number would be \"Pennsylvania Avenue NW\".  # noqa: E501

        :return: The street of this ParseAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this ParseAddressResponse.

        The name of the street or road of the address.  For example, in the address \"1600 Pennsylvania Avenue NW\" the street number would be \"Pennsylvania Avenue NW\".  # noqa: E501

        :param street: The street of this ParseAddressResponse.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def city(self):
        """Gets the city of this ParseAddressResponse.  # noqa: E501

        The city of the address.  # noqa: E501

        :return: The city of this ParseAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ParseAddressResponse.

        The city of the address.  # noqa: E501

        :param city: The city of this ParseAddressResponse.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_or_province(self):
        """Gets the state_or_province of this ParseAddressResponse.  # noqa: E501

        The state or province of the address.  # noqa: E501

        :return: The state_or_province of this ParseAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this ParseAddressResponse.

        The state or province of the address.  # noqa: E501

        :param state_or_province: The state_or_province of this ParseAddressResponse.  # noqa: E501
        :type: str
        """

        self._state_or_province = state_or_province

    @property
    def postal_code(self):
        """Gets the postal_code of this ParseAddressResponse.  # noqa: E501

        The postal code or zip code of the address.  # noqa: E501

        :return: The postal_code of this ParseAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ParseAddressResponse.

        The postal code or zip code of the address.  # noqa: E501

        :param postal_code: The postal_code of this ParseAddressResponse.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this ParseAddressResponse.  # noqa: E501

        Country of the address, if present in the address.  If not included in the address it will be null.  # noqa: E501

        :return: The country of this ParseAddressResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ParseAddressResponse.

        Country of the address, if present in the address.  If not included in the address it will be null.  # noqa: E501

        :param country: The country of this ParseAddressResponse.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if issubclass(ParseAddressResponse, dict):
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
        if not isinstance(other, ParseAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other