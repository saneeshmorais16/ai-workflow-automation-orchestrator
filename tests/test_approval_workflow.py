import pytest
from orchestrator.approval_workflow import transition
def test_approval():assert transition("Needs Review","Approved")=="Approved"
def test_invalid():
    with pytest.raises(ValueError):transition("Approved","Rejected")
