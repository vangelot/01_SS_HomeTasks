import unittest
import pytest

from Trees import Tree


class TestTrees(unittest.TestCase):
    def test_add_list_nodes(self):
        instance = Tree(12)
        assert instance.add_list_nodes([10, 9, 11]) is None, "ОШИБКА"
        assert instance.add_list_nodes([10, 9, 'qqq']) is None, "недопустимая вершина"
        # assert instance.add_list_nodes([10, 9, 8]) is None, "ОШИБКА"

    def test_find_min(self):
        instance = Tree(12)
        instance.add_list_nodes([10, 9, 11, 'QQQ', 22, 14, 2, 24.5, 'a', 10])
        # assert instance.find_min().id_node == 2, "wrong answer"
        assert instance.find_min().id_node == 9, "wrong answer"
        # assert instance.find_min().id_node == 3, "wrong answer"
        instance = Tree(12)
        instance.add_list_nodes([-5, -6, -4, 4, 6, 5, 8, 7, -1, -2, 3, 1, 0, 2])
        assert instance.find_min().id_node == -6, "wrong"

    def test_find_max(self):
        instance = Tree(12)
        instance.add_list_nodes([-5, -6, -4, 4, 6, 5, 8, 7, -1, -2, 3, 1, 0, 2])
        assert instance.find_max().id_node == 12, "wrong"

    def test_delete_node(self):
        instance = Tree(12)
        instance.add_list_nodes([-5, -6, -4, 4, 6, 5, 8, 7, -1, -2, 3, 1, 0, 2])
        assert instance.delete_node(4) is None, "wrong"
