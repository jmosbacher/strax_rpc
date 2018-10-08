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

class JsonSerializer(Serializer):
    @staticmethod
    def array_to_bytes(arr):
        d = {n:arr[n].tolist() for n in arr.dtype.names}
        return json.dumps(d)

    @staticmethod   
    def bytes_to_array(bytes):
        d = json.loads(bytes)
        


serializers = {
    "pickle": PickleSerializer,

}