from typing import List
def mostRepetitiveInteger(input_list: List) -> int:
    dict_ = {}
    if not input_list:
        raise ValueError
    for items in input_list:
        if not dict_.get(items):
            dict_[items]=0
        dict_[items]+=1

    return max(dict_,key=dict_.get)