
"""
MAP Client Plugin - Generated from MAP Client v0.17.3
"""

__version__ = '0.1.0'
__author__ = 'Hugh Sorby'
__stepname__ = 'Ex to Exf'
__location__ = ''

# import class that derives itself from the step mountpoint.
from mapclientplugins.extoexfstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc