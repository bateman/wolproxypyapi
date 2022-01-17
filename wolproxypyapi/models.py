"""Pydantic models for the WolProxyPy API."""

from typing import Optional

from pydantic import BaseModel, Field, IPvAnyAddress
from pydantic.class_validators import validator

from config import API_KEY

# Regex to check valid MAC address
VALID_MAC_RE = r"^(?:[0-9A-Fa-f]{2}([:-]?)[0-9A-Fa-f]{2})(?:(?:\1|\.)(?:[0-9A-Fa-f]{2}([:-]?)[0-9A-Fa-f]{2})){2}$"


class Host(BaseModel):
    """Model to represent a host to wake up.

    Attributes:
        mac_address: The MAC address of the host to wake up.
        port: The port to use to wake up the host.
        ip_address: The IP address of the host to wake up.
        interface: The interface to use to wake up the host.

    Extends:
        BaseModel
    """

    mac_address: str = Field(
        ...,
        example="00:11:22:33:44:55",
        regex=VALID_MAC_RE,
        min_length=12,
        max_length=18,
        title="MAC address",
        description="The MAC address of the host to wake up.",
    )
    port: Optional[int] = Field(
        gt=0, lt=65536, example="9", title="Port", description="The port to use to wake up the host."
    )
    ip_address: Optional[IPvAnyAddress] = Field(
        example="192.168.0.2", title="IP address", description="The IP address of the host to wake up."
    )
    interface: Optional[IPvAnyAddress] = Field(
        example="192.168.0.1", title="Interface", description="The interface to send the packet to."
    )

    @validator("ip_address", pre=True)
    def ip_address_validator_empty_str(cls, v):
        """Validate an IP address as empty string."""
        if v == "":
            v = None
        return v

    @validator("ip_address", pre=False)
    def ip_address_validator_to_str(cls, v):
        """Turn a valid IP address into string."""
        if v is not None:
            v = str(v)
        return v

    @validator("interface", pre=True)
    def interface_validator_empty_Str(cls, v):
        """Validate an interface as empty string."""
        if v == "":
            v = None
        return v

    @validator("interface", pre=False)
    def interface_validator_to_str(cls, v):
        """Turn a valid IP address into string."""
        if v is not None:
            v = str(v)
        return v

    def __str__(self) -> str:
        """Return a string representation of the host."""
        return f"mac: {self.mac_address}, port: {self.port}, " f"ip: {self.ip_address}, interface: {self.interface}"


class ApiKey(BaseModel):
    """Model to represent an API key.

    Attributes:
        key: The API key.

    Extends:
        BaseModel
    """

    key: str = Field(
        ...,
        example="123456789",
        title="API key",
        description="The API key to use to authenticate the request.",
    )

    @validator("key")
    def key_validator(cls, v):
        """Validate the API key."""
        if v != API_KEY:
            raise ValueError("Invalid API key")
        return v
