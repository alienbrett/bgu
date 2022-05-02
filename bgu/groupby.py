import typing
from typing import MutableSequence, Dict, List


T = typing.TypeVar('T')
T_hash = typing.Hashable
group_func = typing.Callable[[T], T_hash]


def groupby(
        arr: MutableSequence[T],
        groupby_func: group_func,
    ) -> Dict[T_hash, List[T]]:
        '''Aggregates sequence into dict, grouping by some function
        '''

        res_struct = {}

        for obj in arr:
            key = groupby_func(obj)
            small_arr = res_struct.get(key, [])
            small_arr.append(obj)
            res_struct[key] = small_arr
        
        return res_struct
