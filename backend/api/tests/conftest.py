import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# api/src를 경로에 넣어서 main 임포트 가능하게
tests_dir = Path(__file__).resolve().parent
api_src = tests_dir.parent / "src"
sys.path.insert(0, str(api_src))

from main import app


@pytest.fixture
def client():
    return TestClient(app)