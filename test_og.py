# coding: utf-8


import og


def test_parse_no_data():
    assert not og.parse(u'')


def test_parse_only_title():
    html = u'<head><title>Pure Title</title></head>'
    assert str(og.parse(html)) == str({u'title': u'Pure Title'})


def test_parse_uppercase():
    html = u'<head><TITLE>Pure Title</title></head>'
    assert str(og.parse(html)) == str({u'title': u'Pure Title'})


def test_parse_og_info():
    html = u'''
    <head>
    <meta property="og:title" content="Python on A Hard Wheel">
    <meta property="og:image" content="image_src">
    <meta property="og:url"
    content="http://lepture.com/en/2014/python-on-a-hard-wheel">
    <meta property="og:description" content="How to build and distribute
    binary wheels on your Mac for every Mac.">
    <meta name="twitter:creator" content="@lepture">
    </head>
    '''
    rv = og.parse(html)
    assert rv[u'title'] == u'Python on A Hard Wheel'
    assert rv[u'image'] == u'image_src'
    assert rv[u'url'] == u'http://lepture.com/en/2014/python-on-a-hard-wheel'
    assert rv[u'twitter'] == u'@lepture'
    assert u'description' in rv


def test_parse_twitter_card():
    html = u'''
    <head>
    <meta name="twitter:title" content="Python on A Hard Wheel">
    </head>
    '''
    rv = og.parse(html)
    assert rv[u'title'] == u'Python on A Hard Wheel'
