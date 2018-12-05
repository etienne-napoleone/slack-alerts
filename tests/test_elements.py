from slack_alerts import elements

TEXT = 'test'
DICTIONARY = {TEXT: 'ok'}


def test_element_text():
    assert elements.text(TEXT) == {'text': TEXT}


def test_element_attachments():
    assert elements.attachments(DICTIONARY, DICTIONARY) == {
        'attachments': [DICTIONARY, DICTIONARY]}


def test_element_attachment_minimum():
    assert elements.attachment(fallback=TEXT) == {'fallback': TEXT}


def test_element_attachment_attrs():
    assert elements.attachment(fallback=TEXT, title=TEXT) == {
        'fallback': TEXT, 'title': TEXT}
