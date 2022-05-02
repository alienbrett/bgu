import typing
import collections

from collections import MutableSequence

from typing import List, Dict

from groupby import groupby


# Input type
T = typing.TypeVar('T')
T_hash = typing.Hashable

# Output type
S = typing.TypeVar('S')

# Argument function types
group_func_type = typing.Callable[[T], T_hash]
apply_func_type = typing.Callable[
    [T_hash, List[T]],
    List[S]
]


def shuffled_groupby_batch_apply(
        arr: MutableSequence[T],
        groupby_func: group_func_type,
        apply_func: apply_func_type,
    ) -> MutableSequence[S]:
    '''Transform an input sequence, when grouped by some tag.
    Does not preserve input order
    '''
    groups = groupby( arr, groupby_func )

    groups_after_apply = {
        tag : apply_func(tag, x_arr)
        for tag, x_arr in groups.items()
    }

    # Concat all results back together
    return_arr = sum( list(groups_after_apply.values()), start=[] )

    return return_arr



def groupby_batch_apply(
        arr: MutableSequence[T],
        groupby_func: group_func_type,
        apply_func: apply_func_type,
    ) -> MutableSequence[S]:
    '''Transform an input sequence, when grouped by some tag.
    Preserves input order
    '''
    strip_func = lambda obj: groupby_func(obj[1])
    def strip_apply_func(tag, objs):
        idxs, raw_objs = zip(*objs)
        new_objs = apply_func(tag, raw_objs)
        return list(zip(idxs, new_objs))

    shuffled_return_res = shuffled_groupby_batch_apply(
        arr = list(enumerate(arr)),
        groupby_func = strip_func,
        apply_func = strip_apply_func,
    )
    shuffled_return_res.sort()

    _, sorted_return_res = zip(*shuffled_return_res)
    return list(sorted_return_res)





if __name__ == '__main__':


    arr = ['tiger','gorilla','elephant','alligator', 'dog']
    groupby_func = lambda s: 'a' in s
    apply_func = lambda tag,objs: [str(tag) + obj for obj in objs]

    res = shuffled_groupby_batch_apply(arr, groupby_func, apply_func)
    print(res)

    res = groupby_batch_apply(arr, groupby_func, apply_func)
    print(res)

