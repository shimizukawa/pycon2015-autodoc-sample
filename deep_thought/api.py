"APIs"


class Request(object):
    """
    .. seqdiag::

       {
          code [label="Your Code"];
          lib  [label="Library"];
          site [label="Web Site"];

          code  -> lib          [label="Request(url)"];
          code <-- lib          [label="req"];
          code  -> lib          [label="req.open(auth_cb)"];
                   lib  -> site [label="GET"];
                   lib <-- site [label="status=401"];
                   lib => code  [label="auth_cb(realm)", return="(user, pass)"];
                   lib  -> site [label="GET/auth header"];
                   lib <-- site [label="status=200"];
          code <-- lib          [label="status"];

          span_height = 20;
       }
    """

    def __init__(self, url):
        """
        Create request object.

        :param str url: url to open
        """

    def open(self, callback):
        """
        Open website.

        :param function callback: callback function on basic auth.
        :return: status code
        :rtype: int
        """

