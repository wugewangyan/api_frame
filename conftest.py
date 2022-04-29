import pytest
from commons.yaml_util import clear_extract_yaml,read_config_yaml

@pytest.fixture(scope='session',autouse=True)
def clear_extract():
    clear_extract_yaml()

# @pytest.fixture(scope='module',autouse=True)
# def read_base_url():
#     return read_config_yaml('base','base_spg1_url')
# @pytest.fixture(scope='module',autouse=True)
# def read_base_url1():
#     return read_config_yaml('base','base_uhg1_url')