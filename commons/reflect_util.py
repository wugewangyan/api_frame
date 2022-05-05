def invoke(method, args, clazz='HotLoadUtil', package='commons.hot_load_util'):
    # 1,动态导入package模块
    module = __import__(package, fromlist=package)  # 参数是模块的路径字符串
    # 1.1判断模块是否有对应的类
    if hasattr(module, clazz):
        # 如果存在，就获取这个类 getattr
        obj = getattr(module, clazz)
        # 判断这个类是否有这个方法
        if hasattr(obj, method):
            # 如果存在，就获取这个类的实例方法
            method_obj = getattr(obj, method)
            # 执行该方法
            return method_obj(obj, *args)
        else:
            print('没有找到' + clazz + '中的' + method + '方法')
    else:
        print('没有找到' + package + '包下的' + clazz + '类')


def invoke_hot_load(full_clazz):
    try:
        package = 'commons.hot_load_util'
        clazz = 'HotLoadUtil'
        method = None
        args = None
        clazz_info = str(full_clazz).split('::')
        if len(clazz_info) == 3:
            package = clazz_info[0]
            clazz = clazz_info[1]
            method_args = clazz_info[2]
            method = get_method(method_args)
            args = get_params(method_args, None)
        elif len(clazz_info) == 2:
            clazz = clazz_info[0]
            method_args = clazz_info[1]
            method = get_method(method_args)
            args = get_params(method_args, None)
        elif len(clazz_info) == 1:
            method_args = clazz_info[0]
            method = get_method(method_args)
            args = get_params(method_args, None)
        else:
            print('热加载字符串有误，请检查')
        return invoke(method=method, args=args, clazz=clazz, package=package)
    except Exception as e:
        msg = "热加载处理出现异常"
        raise Exception(msg)


def get_method(method_args):
    return method_args[:method_args.index('(')]


def get_params(method_args, default_value):
    res = []
    if default_value:
        res.append(default_value)
    args_str = method_args[method_args.index("(") + 1: method_args.index(")")]
    if str(args_str).strip():
        args_list = str(args_str).split(',')
        for arg in args_list:
            res.append(arg.strip())
    return res
