# -*- coding: utf-8 -*-
from plone import api
from plone.browserlayer.utils import registered_layers
from smdu.geosampa.config import PROJECTNAME
from smdu.geosampa.interfaces import IBrowserLayer
from smdu.geosampa.testing import INTEGRATION_TESTING

import unittest

DEPENDENCIES = (
    'plone.formwidget.geolocation',
    'plone.formwidget.masterselect',
)


class InstallTestCase(unittest.TestCase):

    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        for p in DEPENDENCIES:
            self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer_installed(self):
        self.assertIn(IBrowserLayer, registered_layers())


class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

        with api.env.adopt_roles(['Manager']):
            self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer_removed(self):
        self.assertNotIn(IBrowserLayer, registered_layers())
