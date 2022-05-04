from commons.yaml_util import read_extract_yaml


# start_str : $After{{
# end_str : }}
def replace_extract_param(str_value, start_str, end_str):
    replace_str = str_value
    while True:
        if start_str in replace_str and end_str in replace_str:
            start_index = replace_str.index(start_str)
            end_index = replace_str.index(end_str, start_index)
            old_value = replace_str[start_index: end_index + len(end_str)]
            if is_need_hot_load(old_value):
                pass
            else:
                new_value = read_extract_yaml(old_value[len(start_str):-len(end_str)])
                replace_str = replace_str.replace(old_value, new_value)
        else:
            break
    return replace_str


# 判断字符串是否需要使用反射(热加载 hot_load)来替换参数
def is_need_hot_load(str_value):
    if "(" in str_value and ")" in str_value:
        return True
    else:
        return False
