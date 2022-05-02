from collections import MutableSequence, Iterator
from typing import Optional



class ChunkIterator(Iterator):
    pass



class ChunkIterator(Iterator):
    def __init__(self, arr: MutableSequence, chunk_size:int):
        self._arr = arr
        self._n = chunk_size
        print('chunk size:', chunk_size)
    
    def __iter__(self,) -> ChunkIterator:
        return self

    def __next__(self) -> MutableSequence:
        if len(self._arr) < 1:
            raise StopIteration()

        k = min(len(self._arr), self._n)
        ax = self._arr[:k]
        self._arr = self._arr[k:]
        
        return ax




def chunk(
        arr:        MutableSequence(),
        chunk_size: Optional[int] = None,
        num_chunks: Optional[int] = None,
    ) -> ChunkIterator:
    '''Makes iterator that chunks an input.
    '''

    assert (chunk_size is None)!=(num_chunks is None), "exactly one of chunk_size or num_chunks must be integer"

    if chunk_size is None:
        assert num_chunks > 0, "Must specify positive number of chunks"

        chunk_size = (len(arr) // num_chunks)


    return ChunkIterator(arr = arr, chunk_size = chunk_size)






if __name__ == '__main__':
    print(list(chunk(
        list(range(10)),
        num_chunks = 2
    )))

    print(list(chunk(
        list(range(11)),
        num_chunks = 2
    )))

    print(list(chunk(
        list(range(11)),
        chunk_size = 5
    )))
 