import pytest

from commons.requests_util import RequestsUtil
from commons.yaml_util import read_testcase_yaml


class TestProductApi:

    @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_get_token.yaml'))
    def test_get_token(self, case_info):
        RequestsUtil(two_node='base_spgl_url').send_request(case_info)

    @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_select_flag.yaml'))
    def test_select_flag(self, case_info):
        RequestsUtil(two_node='base_spgl_url').send_request(case_info)

    @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_create_flag.yaml'))
    def test_create_flag(self, case_info):
        RequestsUtil(two_node='base_spgl_url').send_request(case_info)

    @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_delete_flag.yaml'))
    def test_delete_flag(self, case_info):
        RequestsUtil(two_node='base_spgl_url').send_request(case_info)

    @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_file_upload.yaml'))
    def test_file_upload(self, case_info):
        RequestsUtil(two_node='base_spgl_url').send_request(case_info)