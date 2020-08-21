#!/usr/bin/python3
import os

def createFile():
    os.mkdir('tmp/')
    if not os.path.exists('tmp/test'):
        with open('tmp/test', 'w'):
            pass
createFile()

def test_creatFile():
    assert os.path.exists('tmp/test')

