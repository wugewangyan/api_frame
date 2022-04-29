class Father:
    def setup_class(self):
        print("在类的前面执行的操作")


    def teardown_class(self):
        print("在类后面执行的操作")


    def setup(self):
        print("测试用例之前")


    def teardown(self):
        print("测试用例之后")