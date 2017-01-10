#coding: utf-8


class FailedRequestException(Exception):
    def __init__(self, status_code, response_txt):
        super(FailedRequestException, self).__init__()
        self.status_code = status_code
        self.response_txt = response_txt
