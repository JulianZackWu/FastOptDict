# FastOptDict Document

## 0x00 Introduction

FastOptDict is a simple dictionary library. It allows you to find all the keys, values, and paths in the dictionary variable. 

For example, we have a dictionary variable and we have to find out the value for the key "test".

```python

>>> import FastOptDict
>>> dict_data = {"a": "b", "c": "d", "e": [{"f": "a"}, "e", {"h": ["tt", "dd"]}], "h": ["tt", "dd"], "i": "c","z": {"f": "a","t":{"x":"z"}}}

>>> value_list = FastOptDict.get_value_by_key("a")
>>> print(value_list)
```

It uses a path generation algorithm to finish the task instead of using regex.


## 0x01 Install

```
pip install FastOptDict
```

## 0x02 Usage

1. Find all values from the dictionary variable, and return all the values by the key.

   ```python
   dict_data = {"a": "b", "c": "d", "e": [{"f": "a"}, "e", {"h": ["tt", "dd"]}], "h": ["tt", "dd"], "i": "c","z": {"f": "a","t":{"x":"z"}}}
   value_list = FastOptDict.get_value_by_key("a")
   print(value_list)
   
   [['tt', 'dd'], ['tt', 'dd']]
   ```

2. Find all keys from the dictionary variable, and return all the values of the keys equal to what you input. You can also convert the result into an easy way to read.

   ```python
   value_list = FastOptDict.get_value_by_key("a")
   print(value_list)
   
   ['/z/f', '/e/setoptlist(0)/f']
   
   value_list = FastOptDict.get_value_by_key("a",convert=True)
   print(value_list)
   
   ["dict['e'][0]['f']", "dict['z']['f']"]
   
   
   value_list = get_key_by_value(dict_data, [{"f": "a"}, "e", {"h": ["tt", "dd"]}], convert=True)
   print(value_list)
   
   ["dict['e']"]
   ```

3. Find all keys and values from the dictionary variable, Even though what you input is a dictionary variable.

   ```python
   value_list = FastOptDict.get_all_by_key(dict_data,"f")
   print(value_list)
   
   value_list = FastOptDict.get_all_by_key(dict_data, "f",convert=True)
   print(value_list)
   
   
   [{'path': '/z/f', 'value': 'a'}, {'path': '/e/setoptlist(0)/f', 'value': 'a'}]
   [{'path': "dict['z']['f']", 'value': 'a'}, {'path': "dict['e'][0]['f']", 'value': 'a'}]
   
   value_list = FastOptDict.get_all_by_key(dict_data, "e",convert=True)
   print(value_list)
   
   [{'path': "dict['e']", 'value': [{'f': 'a'}, 'e', {'h': ['tt', 'dd']}]}]
   
   ```

4. Find paths from the dictionary variable by key. For example, the dictionary variable is {"a":{"b":"c","d":"e"}}, the path of key "b" is dict["a"], and we can use dict\["a"]["d"] to get the value finally.

   ```python
   value_list = FastOptDict.get_path_by_key(dict_data, "f")
   print(value_list)
   
   value_list = FastOptDict.get_path_by_key(dict_data, "f",convert=True)
   print(value_list)
   
   ['/z/f', '/e/setoptlist(0)/f']
   ["dict['e'][0]['f']", "dict['z']['f']"]
   ```

5. Find paths from the dictionary variable by values.

   ```python
   value_list = get_path_by_value(dict_data,[{"f": "a"}, "e", {"h": ["tt", "dd"]}])
   print(value_list)
   
   value_list = get_path_by_value(dict_data, [{"f": "a"}, "e", {"h": ["tt", "dd"]}],convert=True)
   print(value_list)
   
   ['/e/setoptlist(2)', '/', '/e/setoptlist(0)']
   ["dict['']", "dict['e'][0]", "dict['e'][2]"]
   ```

6. Find keyword from keynames and values

   ```python
   print(search_all_by_str(dict_data,"dd"))
   print(search_all_by_str(dict_data, "dd",True))
   
   ['/h/setoptlist(1)', '/h', '/e/setoptlist(2)/h', '/e/setoptlist(2)/h/setoptlist(1)']
   ["dict['h']", "dict['e'][2]['h'][1]", "dict['e'][2]['h']", "dict['h'][1]"]
   ```

7. Find keyword in keynames

   ```python
   print(search_key_in_value(dict_data, ["tt", "dd"],convert=True))
   
   ["dict['e'][2]['h']", "dict['h']"]
   ```

8. Get value from path

   ```python
   print(get_value_by_path(dict_data,"/e"))
   [{'f': 'a'}, 'e', {'h': ['tt', 'dd']}]
   ```

   

## 0x03 MIT License

Copyright (c) 2022 JulianZackWu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
