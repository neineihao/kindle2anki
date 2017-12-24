from abc import abstractmethod, ABCMeta
from dictionary.dict_base import DictBase
# import urllib
import urllib.request
import urllib.parse


class HJDict_Base(DictBase, metaclass=ABCMeta):
    headers = [("User-Agent",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) "
                "AppleWebKit/536.26 (KHTML, like Gecko) "
                "Version/6.0 Mobile/10A5376e Safari/8536.25")]

    def look_up(self, word):
        req_url = self.get_req_url(word)
        print(req_url)

        opener = urllib.request.build_opener()
        opener.addheaders = self.headers
        urllib.request.install_opener(opener=opener)

        with urllib.request.urlopen(req_url) as f:
            page = f.read()
            parsed_result = self.parse_page(page)
        return parsed_result

    def encode_query(self, q):
        quoted = urllib.parse.quote(q, encoding='utf-8')
        return quoted

    @abstractmethod
    def get_req_url(self, word):
        pass

    @abstractmethod
    def parse_page(self, page):
        pass