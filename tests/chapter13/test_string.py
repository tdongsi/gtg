
import unittest

import chapter13.string as gtg


class TestString(unittest.TestCase):

    def test_pattern_matching(self):

        self.assertEqual(gtg.find_brute('ANPANMAN', 'PAN'), 2)
        self.assertEqual(gtg.find_brute('abacaabaccabacabaabb', 'abacab'), 10)

        self.assertEqual(gtg.find_boyer_moore('ANPANMAN', 'PAN'), 2)
        self.assertEqual(gtg.find_boyer_moore('abacaabaccabacabaabb', 'abacab'), 10)

        self.assertEqual(gtg.find_kmp('ANPANMAN', 'PAN'), 2)
        self.assertEqual(gtg.find_kmp('abacaabaccabacabaabb', 'abacab'), 10)


class TestTrie(unittest.TestCase):

    def test_trie(self):

        trie = gtg.Trie()

        trie.insert('abc$')
        trie.insert('abgl$')
        trie.insert('cdf$')
        trie.insert('abcd$')
        trie.insert('lmn$')

        trie.list()

        self.assertEqual(trie.search('lmn$'), True)
        self.assertEqual(trie.search('ab$'), False)
        self.assertEqual(trie.search('cdf$'), True)
        self.assertEqual(trie.search('ghi$'), False)

        print("Check Delete")
        print("Delete #1:")
        trie.delete('abc$')
        trie.list()
        print("Delete #2:")
        trie.delete('abgl$')
        trie.list()
        print("Delete #3:")
        trie.delete('abcd$')
        trie.list()

    def test_ctci_contacts(self):

        trie = gtg.Trie()

        trie.insert('hack$')
        trie.insert('hackerrank$')
        self.assertEqual(trie.search_partial('hac'), 2)
        self.assertEqual(trie.search_partial('hak'), 0)
        self.assertEqual(trie.search_partial('hack'), 2)
        self.assertEqual(trie.search_partial('hack$'), 1)

