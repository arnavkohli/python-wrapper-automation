import os
import json
import requests


class MyWrapper:


    BASE_URL = 'https://api.test.com/v1/'
    HEADERS = {'key': '1234'}


    @classmethod
    def userInfo(cls, **kwargs):
        url = cls.BASE_URL + '/user/info'
        response = requests.get(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def cartInfo(cls, **kwargs):
        url = cls.BASE_URL + '/cart/info'
        response = requests.get(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def productInfo(cls, **kwargs):
        url = cls.BASE_URL + '/product/info'
        response = requests.get(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def userRegister(cls, **kwargs):
        url = cls.BASE_URL + '/user/register'
        response = requests.post(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def userLogin(cls, **kwargs):
        url = cls.BASE_URL + '/user/login'
        response = requests.post(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def cartAddproduct(cls, **kwargs):
        url = cls.BASE_URL + '/cart/addProduct'
        response = requests.post(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def cartRemoveproduct(cls, **kwargs):
        url = cls.BASE_URL + '/cart/removeProduct'
        response = requests.post(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def userDelete(cls, **kwargs):
        url = cls.BASE_URL + '/user/delete'
        response = requests.delete(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def cartDelete(cls, **kwargs):
        url = cls.BASE_URL + '/cart/delete'
        response = requests.delete(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def productDelete(cls, **kwargs):
        url = cls.BASE_URL + '/product/delete'
        response = requests.delete(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def userUpdate(cls, **kwargs):
        url = cls.BASE_URL + '/user/update'
        response = requests.put(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response


    @classmethod
    def cartUpdate(cls, **kwargs):
        url = cls.BASE_URL + '/cart/update'
        response = requests.put(url=url, headers=cls.HEADERS, params=kwargs.get('params', None), data=kwargs.get('data', 'None'))
        return response
