# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2015-2018 by Exopy Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Test templates utility functions.

"""
from configobj import ConfigObj

from exopy.tasks.utils.templates import save_template, load_template


def test_save_template(tmpdir):
    """Test saving a template.

    """
    path = str(tmpdir.join('test.template.ini'))
    save_template(path, {'test': 'é'}, 'à'*100)

    conf = ConfigObj(path)
    assert 'test' in conf
    assert len(conf.initial_comment) == 2


def test_load_template(tmpdir):
    """Test loading a template.

    """
    path = str(tmpdir.join('test.template.ini'))
    doc = 'à\nb\nc'
    save_template(path, {'test': 'é'}, doc)

    conf, docl = load_template(path)
    assert 'test' in conf
    assert docl == doc.replace('\n', ' ')
