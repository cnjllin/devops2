#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "SONG Xiang"


def test(**kwargs):
    return kwargs

def error(**kwargs):
    raise Exception("执行有错")
