from typing import Dict, List, Union


def text(message: str) -> Dict[str, str]:
    """Simple text element"""
    return {'text': message}


def attachments(*args):
    """Simple attachments base element containing multiple attachment"""
    return {'attachments': [*args]}


def attachment(fallback: str, color: str = None, pretext: str = None,
               author_name: str = None, author_link: str = None,
               author_icon: str = None, title: str = None,
               title_link: str = None, text: str = None,
               fields: List[Dict[str, str]] = None, image_url: str = None,
               thumb_url: str = None, footer: str = None,
               footer_icon: str = None, ts: int = None
               ) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    """Attachement element"""
    element = {}
    element.update({'fallback': fallback} if fallback else {})
    element.update({'color': color} if color else {})
    element.update({'author_name': author_name} if author_name else {})
    element.update({'author_link': author_link} if author_link else {})
    element.update({'author_icon': author_icon} if author_icon else {})
    element.update({'title': title} if title else {})
    element.update({'title_link': title_link} if title_link else {})
    element.update({'text': text} if text else {})
    element.update({'fields': fields} if fields else {})
    element.update({'image_url': image_url} if image_url else {})
    element.update({'thumb_url': thumb_url} if thumb_url else {})
    element.update({'footer': footer} if footer else {})
    element.update({'footer_icon': footer_icon} if footer_icon else {})
    element.update({'ts': ts} if ts else {})
    return element
