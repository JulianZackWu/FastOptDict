from FastOptDict.FastOptDict import *

dict_data = {"a": "b", "c": "d", "e": [{"f": "a"}, "e", {"h": ["tt", "dd"]}], "h": ["tt", "dd"], "i": "c",
                 "z": {"f": "a", "t": {"x": "z"}}}


def test_Get_Value_By_Key():
    pass


def test_Get_Key_By_Value():
    value_list = get_key_by_value(dict_data,"a")
    print(value_list)

    value_list = get_key_by_value(dict_data, "a",convert=True)
    print(value_list)

    value_list = get_key_by_value(dict_data, [{"f": "a"}, "e", {"h": ["tt", "dd"]}], convert=True)
    print(value_list)


def test_Get_All_By_Key():
    value_list = get_all_by_key(dict_data,"f")
    print(value_list)

    value_list = get_all_by_key(dict_data, "f",convert=True)
    print(value_list)

    value_list = get_all_by_key(dict_data, "e", convert=True)
    print(value_list)

def test_Get_Path_By_Key():
    value_list = get_path_by_key(dict_data, "f")
    print(value_list)

    value_list = get_path_by_key(dict_data, "f",convert=True)
    print(value_list)

def test_Get_Path_By_Value():
    value_list = get_path_by_value(dict_data,[{"f": "a"}, "e", {"h": ["tt", "dd"]}])
    print(value_list)

    value_list = get_path_by_value(dict_data, [{"f": "a"}, "e", {"h": ["tt", "dd"]}],convert=True)
    print(value_list)



if __name__ == "__main__":
    test_Get_Key_By_Value()
    test_Get_All_By_Key()
    test_Get_Path_By_Key()
    test_Get_Path_By_Value()
    print(search_all_by_str(dict_data,"dd"))
    print(search_all_by_str(dict_data, "dd",True))
    print(search_key_in_value(dict_data, ["tt", "dd"],convert=True))
    print(get_value_by_path(dict_data,"/e"))