"""
Module with dataclasses and functions to serialize/deserialize
data from/to B3 archive files.
"""
import re
from typing import Dict
from dataclasses import asdict, dataclass

from pybov import errors, helpers, jsonlib


@dataclass
class HeaderData:
    """
    Header data class with the sole purpose of
    storing and validate B3 header data.
    """
    reg_type: str
    fname: str
    source_type: str
    date: str

    def __post_init__(self) -> None:
        """
        Post initalization dataclass method used
        to validate object properties.

        Invokes `self.validate()`.
        """
        if self.reg_type != '00':
            raise errors.PybovValidationError(
                    'Validation error',
                    **{'reg_type': f'expected "00" but got "{self.reg_type}"'}
            )

        if not re.match(r'COTAHIST\.[0-9]+', self.fname):
            raise errors.PybovValidationError(
                    'Validation error',
                    **{'fname': f'Invalid fname format: "{self.fname}"'}
            )
        
        if self.source_type != 'BOVESPA':
            raise errors.PybovValidationError(
                    'Validation error',
                    **{'source_type': f'Expected "BOVESPA" but got: "{self.source_type}"'}
            )

        if not re.match(r'\d{4}\d{2}\d{2}', self.date):
            raise errors.PybovValidationError(
                    'Validation error',
                    **{'fname': f'Invalid date format: "{self.date}"'}
            )


class Header:
    """
    Header class that encapsulates a HeaderData
    and apply some builder methods to work with it.
    """
    data: HeaderData

    def __init__(self, data: HeaderData) -> None:
        """
        Create a new Header object instance, using
        HeaderData as an argument to be used by
        other methods.
        """
        self.data = data

    @classmethod
    def from_b3str(cls, data: str) -> 'Header':
        """
        Create a new B3 Header object from a B3 string record.
        """
        return cls(
            HeaderData(
                data[0:2],
                data[2:15],
                data[15:23].strip(),
                data[23:31]
            )
         )
    
    def to_b3str(self) -> str:
        """
        Return the original B3 header string.
        """
        return ''.join([
            self.data.reg_type,
            self.data.fname,
            helpers.fill_str(self.data.source_type, 23 - 15),
            self.data.date,
            helpers.fill_str('', 214)
        ])

    @classmethod
    def from_json(cls, data: str) -> 'Header':
        """
        Return a Header object instance from a json string.
        """
        parsed = jsonlib.decode(data)
        
        return cls(HeaderData(**parsed))

    def to_json(self) -> str:
        """
        Return a json string representation of a B3 header.
        """
        parsed = asdict(self.data)

        return jsonlib.encode(parsed)
