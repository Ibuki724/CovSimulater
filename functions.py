# all functions here

import json


def read_json(filename):
      with open(filename,mode = 'r',encoding = "utf-8") as file:
        data = json.loads(file.read())
        file.close
        return data

def write_json(dictname,filename):
    with open(filename,mode = 'w',encoding = "utf-8") as file:
        json.dump(dictname,file)


def get_language_option():
    language_option_data = read_json("option_and_flags.json")
    language_option_flag = language_option_data["language_option_flag"]
    if language_option_flag:
        pass
    else:
        language_option = input("Chose your language, \"ENG\" for English and \"CN\" for Chinese.\n")
        dict = read_json('option_and_flags.json')
        dict['language_option_flag'] = 1
        dict['language_option'] = language_option
        write_json(dict,'option_and_flags.json')
# 一次性函数，练习使用json文件