import numpy as np
import pandas as pd
import pickle
import json


class Serializer:

    @staticmethod
    def array_to_bytes(arr):
        raise NotImplementedError

    @staticmethod
    def bytes_to_array(bytes):
        raise NotImplementedError


class PickleSerializer(Serializer):
    @staticmethod
    def array_to_bytes(arr):
        return pickle.dumps(arr)

    @staticmethod   
    def bytes_to_array(bytes):
        return pickle.loads(bytes)

class JsonSerializer:
    @staticmethod
    def array_to_bytes(arr):
        
        d = {
            "dtype": {"names": arr.dtype.names,
                 "formats": [str(arr.dtype[n])for n in arr.dtype.names ],# 
                },
        "__ndarray__":arr.tolist()}
        return json.dumps(d)

    @staticmethod   
    def bytes_to_array(bytes):
        d = json.loads(bytes)
        ts = [tuple(t) for t in d["__ndarray__"]]
        return np.array(ts, dtype=d["dtype"])


class MsgpackSerializer(Serializer):
    @staticmethod
    def array_to_bytes(arr):
        pass

    @staticmethod   
    def bytes_to_array(bytes):
       pass


serializers = {
    "pickle": PickleSerializer,
    "json": JsonSerializer,
    "msgpack": MsgpackSerializer,

}