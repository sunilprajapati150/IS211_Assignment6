#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" temperature conversion  """

import decimal


def convertCelsiusToKelvin(degrees):
    """Performs arithmetic to convert given temperature in degrees celsius to
    degrees Kelvin.
    Args:
        degrees(int, float): an int or float representing the number of degrees
        Celsius to convert to degrees Kelvin.
    Returns:
        float: A numerical float value of degrees Kelvin equivalent to given
        degrees Celsius.
    Example:
        >>> convertCelsiusToKelvin(100)
        373.15
    """
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) + decimal.Decimal('273.15'))
    return float(convert)


def convertCelsiusToFahrenheit(degrees):
    """Performs arithmetic to convert given temperature in degrees Celsius to
    degrees Fahrenheit.
    Args:
        degrees(int, float): an int or float representing the number of degrees
        Celsius to convert to degrees Fahrenheit.
    Returns:
        float: A numerical float value of degrees Fahrenheit equivalent to given
        degrees Celsius.
    Example:
        >>> convertCelsiusToFahrenheit(85)
        185.0
    """
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) / decimal.Decimal('5') * 9) + 32
    return float(convert)


def convertFahrenheitToCelsius(degrees):
    """Performs arithmetic to convert given temperature in degrees Fahrenheit to
    degrees Celsius.
    Args:
        degrees(int, float): an int or float representing the number of degrees
        Fahrenheit to convert to degrees Celsius.
    Returns:
        float: A numerical float value of degrees Celsius equivalent to given
        degrees Fahrenheit.
    Example:
        >>> convertFahrenheitToCelsius(212)
        100.0
    """
    degrees = str(degrees)
    convert = ((decimal.Decimal(degrees) - 32) * 5) / decimal.Decimal('9')
    return float(convert)


def convertFahrenheitToKelvin(degrees):
    """Perfroms arithmetic to convert given temperature in degrees Fahrenheit to
    degrees Kelvin.
    Args:
        degrees(int, float): an int or float representing the number of degrees
        Fahrenheit to convert to degrees Kelvin.
    Returns:
        float: A numerical float value of degrees Kelvin equivalent to given
        degrees Fahrenheit.
    Example:
        >>> convertFahrenheitToKelvin(100)
        310.9277777777778
    """
    degrees = str(degrees)
    convert = (((decimal.Decimal(degrees) + decimal.Decimal('459.67')) * 5) /
               decimal.Decimal('9'))
    return float(convert)


def convertKelvinToCelsius(degrees):
    """Performs arithmetic to convert given temperature in degrees Kelvin to
    degrees Celsius.
    Args:
        degrees(int, float): an int or float representing the number of degrees
        Kelvin to convert to degrees Celcius.
    Returns:
        float: A numerical float value of degrees Celsius equivalent to given
        degrees Kelvin.
    Example:
        >>> convertKelvinToCelsius(100)
        -173.15
    """
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) - decimal.Decimal('273.15'))
    return float(convert)


def convertKelvinToFahrenheit(degrees):
    """Performs artimethic to convert given temperature in degrees Kelvin to
    degrees Fahrenheit.
        
    Args:
        degrees(int, float): an int or float representing the number of degrees
        Kelvin to convert to degrees Fahrenheit.
    Returns:
        float: A numerical float value of degrees Fahrenheit equivalent to given
        degrees Kelvin.
    Example:
        >>> convertKelvinToFahrenheit(100)
        -279.67
    """
    degrees = str(degrees)
    convert = (((decimal.Decimal(degrees) * 9) / decimal.Decimal('5'))
               - decimal.Decimal('459.67'))
    return float(convert)
