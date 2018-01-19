#!/usr/bin/env python
user_0 = {
    'username': 'zhanglg',
    'firest':'zhang',
    'last':'ligui',
    }

for key, value in user_0.items():
    print("\nkey:" + key)
    print("value:" + value)

user_1 = {
    'zlg':'C',
    'wh':'C++',
    'wd':'Java',
    'hwb':'python',
    }

for name in user_1.keys():
    print("\nname:" + name.title())

for language in user_1.values():
    print("\nlaunguage:" + language.title())