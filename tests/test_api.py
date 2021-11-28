import unittest
import pytest
from api import *
import flask
import json
from mockito import when, mock, verify, ANY


#class TestApi(unittest.TestCase):

#     def test_home(self):

#         self.assertEqual(api.home(), render_template('home.html'))

def test_home():
    when(flask).render_template(...).thenReturn([])
    _ = home()
    verify(flask, inorder=True, times=1).render_template('home.html')


# if __name__ == '__main__':
#     unittest.main()


def test_api_all():
    when(flask).jsonify(...).thenReturn([])
    _ = api_all()
    verify(flask, inorder=True, times=1).jsonify(data)


# def test_api_name():
#     when(flask).request.args(...).thenReturn({"args": ["Name"]})
#     when(flask).jsonify(...).thenReturn([])
#     _ = api_name()
#     verify(flask, inorder=True, times=1).jsonify(results)