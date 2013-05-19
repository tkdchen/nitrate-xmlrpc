# -*- coding: utf-8 -*-

import unittest

from nitrate.apps.management.models import Classification
from nitrate.apps.management.models import Product

from nitratexmlrpc.api.utils import pre_check_product
from nitratexmlrpc.api.utils import pre_process_ids


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.classification = Classification.objects.create(
            name='Classification 1',
            description='Description of classification 1',
            sortkey=1)
        self.product = Product(
            name='Product 1',
            description='Description of product 1',
            votes_to_confirm=True,
            classification=self.classification)
        self.product.save()

    def tearDown(self):
        self.product.delete()
        self.classification.delete()

    def test_pre_check_product(self):
        values = 'Product 1'
        product = pre_check_product(values)
        self.assertEqual(product.name, self.product.name)

        values = self.product.pk
        product = pre_check_product(values)
        self.assertEqual(product.pk, self.product.pk)

        values = object()
        self.assertRaises(ValueError, pre_check_product, values)

        values = { 'other': '', }
        product = pre_check_product(values)
        self.assertEqual(product, None,
            'product does not exist in arguments, None should be returned.')

        values = { 'other': '', 'product': self.product.pk }
        product = pre_check_product(values)
        self.assertEqual(product.pk, self.product.pk)

        values = { 'other': '', 'product': self.product.name }
        product = pre_check_product(values)
        self.assertEqual(product.name, self.product.name)

        values = { 'other': '', 'product': 'Product 1' }
        product = pre_check_product(values)
        self.assertEqual(product.name, self.product.name)

        values = { 'other': '', 'product': object() }
        self.assertRaises(ValueError, pre_check_product, values)

    def test_pre_process_ids(self):
        values = [1, 2, 3]
        ids = pre_process_ids(values)
        self.assert_(1 in ids, 'IDs does not contain 1.')
        self.assert_(2 in ids, 'IDs does not contain 2.')
        self.assert_(3 in ids, 'IDs does not contain 3.')

        values = ['1', '2', '3']
        ids = pre_process_ids(values)
        self.assert_(1 in ids, 'IDs does not contain 1.')
        self.assert_(2 in ids, 'IDs does not contain 2.')
        self.assert_(3 in ids, 'IDs does not contain 3.')

        values = ['1', 2, '3']
        ids = pre_process_ids(values)
        self.assert_(1 in ids, 'IDs does not contain 1.')
        self.assert_(2 in ids, 'IDs does not contain 2.')
        self.assert_(3 in ids, 'IDs does not contain 3.')

        values = 100
        ids = pre_process_ids(values)
        self.assert_(isinstance(ids, list), 'IDs is not an object of list.')
        self.assert_(100 in ids, 'IDs does not contain 100.')

        values = '10'
        ids = pre_process_ids(values)
        self.assert_(isinstance(ids, list), 'IDs is not an object of list.')
        self.assert_(10 in ids, 'IDs does not contain 10.')

        values = '10'
        ids = pre_process_ids(values)
        self.assert_(isinstance(ids, list), 'IDs is not an object of list.')
        self.assert_(10 in ids, 'IDs does not contain 10.')

        # Invalid input test 

        values = object()
        self.assertRaises(TypeError, pre_process_ids, values)

        values = 'n'
        self.assertRaises(ValueError, pre_process_ids, values)

        values = [1, 'x', 2]
        self.assertRaises(ValueError, pre_process_ids, values)

        values = ['1', 'x', '2']
        self.assertRaises(ValueError, pre_process_ids, values)
