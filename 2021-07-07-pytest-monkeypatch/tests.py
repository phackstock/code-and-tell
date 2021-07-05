
import pytest
from requests import Response


def test_check_resource_availability(monkeypatch):
    
    monkeypatch.delattr(Response, "status_code")
    
    assert 
