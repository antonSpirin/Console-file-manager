from function import *
from library import dict_celeb
import os
import sys
import shutil
import random


def test_listdir():
    path = os.getcwd()
    # print(path)
    # print(os.listdir(path))
    assert 'folder1' in os.listdir(path)
    assert 'folder2' in os.listdir(path)
    assert 'function.py' in os.listdir(path)
    assert 'library.py' in os.listdir(path)


def test_view_folders():
    for i in range(len(view_folders())):
        assert os.path.isdir(view_folders()[i]) == True
    for i in range(len(view_folders())):
        assert os.path.isfile(view_folders()[i]) == False


def test_view_files():
    for i in range(len(view_files())):
        assert os.path.isfile(view_files()[i]) == True
    for i in range(len(view_files())):
        assert os.path.isdir(view_files()[i]) == False


def test_random_names():
    count_names = 5
    assert len(random_names(dict_celeb, count_names)) == count_names


def test_create_folder():
    assert create_folder('folder_test') == os.path.exists('folder_test')
    os.rmdir('folder_test')


def test_copy_folder_file():
    assert copy_folder_file('folder1', 'folder_copy7') == 'folder_copy7'
    shutil.rmtree('folder_copy7')
    assert copy_folder_file('library.py', 'folder_copy4') == 'folder_copy4\\library.py'
    os.remove('folder_copy4\\library.py')
