import pytest

from commons.requests_util import RequestsUtil
from commons.yaml_util import read_testcase_yaml


class TestProductApi:

    @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_get_token.yaml'))
    def test_get_token(self, case_info):
        # if 'parameterize' in case_info.keys():
        #     print(case_info)
        #     for param_key,param_value in case_info['parameterize'].items():
        #         key_list = param_key.split('-')
        #         print(key_list,param_value)
        # else:
        #     print('不需要驱动')
        # print(case_info)

        RequestsUtil(two_node='base_spgl_url').send_request(case_info)

    # @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_select_flag.yaml'))
    # def test_select_flag(self, case_info):
    #     RequestsUtil(two_node='base_spgl_url').send_request(case_info)
    #
    # @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_create_flag.yaml'))
    # def test_create_flag(self, case_info):
    #     RequestsUtil(two_node='base_spgl_url').send_request(case_info)
    #
    # @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_delete_flag.yaml'))
    # def test_delete_flag(self, case_info):
    #     RequestsUtil(two_node='base_spgl_url').send_request(case_info)
    #
    # @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/product_manage/test_file_upload.yaml'))
    # def test_file_upload(self, case_info):
    #     RequestsUtil(two_node='base_spgl_url').send_request(case_info)