import unittest


class MyTestCase(unittest.TestCase):

    def test_insert_head(self):
        from LL_2 import LinkedList
        ll = LinkedList()
        ll.insertHead(10)
        ll.insertHead(20)
        self.assertEqual(ll._head._element, 20)
        self.assertEqual(ll._tail._element, 10)
        self.assertEqual(len(ll), 2)

    def test_insert_tail(self):
        from LL_2 import LinkedList
        ll = LinkedList()
        ll.insertTail(30)
        ll.insertTail(40)
        self.assertEqual(ll._head._element, 30)
        self.assertEqual(ll._tail._element, 40)
        self.assertEqual(len(ll), 2)

if __name__ == '__main__':
    unittest.main()
