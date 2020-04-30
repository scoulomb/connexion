# Reference is https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
# Where we can see MIME type can have optional parameter
# We can have a space or not in charset
def is_json_mimetype_v1(mimetype):
    """
    :type mimetype: str
    :rtype: bool
    """
    simple_mime_type, optional_parameter = mimetype.split(";") if \
        ";" in mimetype else \
        (mimetype, None)
    maintype, subtype = simple_mime_type.split('/')  # type: str, str

    return maintype == 'application' and \
           (
                   subtype == 'json' or
                   subtype.endswith('+json')
           ) and \
           (
                   optional_parameter is None or
                   optional_parameter.strip() == "charset=utf-8"
           )


def is_json_mimetype_v2(mimetype):
    """
    :type mimetype: str
    :rtype: bool
    """
    simple_mime_type, optional_parameter = mimetype.split(";") if \
        ";" in mimetype else \
        (mimetype, None)
    if "/" not in simple_mime_type:
        return False
    maintype, subtype = simple_mime_type.split('/')  # type: str, str

    is_valid_main_type = (maintype == 'application')
    is_valid_subtype = (subtype == 'json' or subtype.endswith('+json'))
    is_valid_optional_parameter = (
            optional_parameter is None or
            optional_parameter.strip() == "charset=utf-8"
    )

    return is_valid_main_type and is_valid_subtype and is_valid_optional_parameter


def is_json_mimetype(mimetype):
    """
    :type mimetype: str
    :rtype: bool
    """
    simple_mime_type, _, optional_parameter = mimetype.partition(";")
    maintype, _, subtype = simple_mime_type.partition("/")

    print(mimetype)
    print(f"maintype:{maintype}, subtype:{subtype}, optional_parameter:{optional_parameter}\n")

    is_valid_main_type = (maintype == 'application')
    is_valid_subtype = (subtype == 'json' or subtype.endswith('+json'))
    is_valid_optional_parameter = (
            not optional_parameter or
            optional_parameter.strip() == "charset=utf-8"
    )

    return is_valid_main_type and is_valid_subtype and is_valid_optional_parameter
    


import unittest

from mimetype import is_json_mimetype


class TestUtils(unittest.TestCase):

    def test_is_json_mimetype(self):
        self.assertTrue(is_json_mimetype("application/json"))
        self.assertTrue(is_json_mimetype("application/json; charset=utf-8"))
        self.assertTrue(is_json_mimetype("application/json;charset=utf-8"))
        self.assertTrue(is_json_mimetype("application/anything+json;charset=utf-8"))
        self.assertTrue(is_json_mimetype("application/anything+json"))

        self.assertFalse(is_json_mimetype("application"))
        self.assertFalse(is_json_mimetype("appli/json"))
        self.assertFalse(is_json_mimetype("application/xml"))
        self.assertFalse(is_json_mimetype("application/xml; charset=utf-8"))
        self.assertFalse(is_json_mimetype("app/json; charset=utf-8"))
        self.assertFalse(is_json_mimetype("application/json;charset=utf-dfdfd"))
        self.assertFalse(is_json_mimetype(""))
        
# https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty
