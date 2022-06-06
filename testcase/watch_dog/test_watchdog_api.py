import pytest
from commons.requests_util import RequestsUtil
from commons.yaml_util import read_testcase_yaml

class TestWatchdogApi():
    @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/watch_dog/test_get_login.yaml'))
    def test_get_login(self, case_info):
        RequestsUtil(two_node='base_url').send_request(case_info)
    # @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/watch_dog/test_delete_watchdog.yaml'))
    # def test_delete_watchdog(self, case_info):
    #     RequestsUtil(two_node='base_url').send_request(case_info)



    # @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/watch_dog/test_add_watchdog.yaml'))
    # def test_add_watchdog(self, case_info):
    #     RequestsUtil(two_node='base_url').send_request(case_info)

    # @pytest.mark.parametrize('case_info', read_testcase_yaml('/testcase/watch_dog/test_edit_watchdog.yaml'))
    # def test_edit_watchdog(self,case_info):
    #     RequestsUtil(two_node='base_url').send_request(case_info)


