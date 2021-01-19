import sys
import importlib
import urllib.request as urllib2

class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl


    def find_module(self, fullname, path=None):
        if path is None:
            baseurl = self._baseurl
        else:
            # 不是原定义的url就直接返回不存在
            if not path.startswith(self._baseurl):
                return None
            baseurl = path

        try:
            loader = UrlMetaLoader(baseurl)
        except Exception:
            return None

class UrlMetaLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self.baseurl = baseurl

    def get_code(self, fullname):
        f = urllib2.urlopen(self.get_filename(fullname))
        return f.read()

    def get_data(self):
        pass

    def get_filename(self, fullname):
        return self.baseurl + fullname + '.py'

def install_meta(address):
    finder = UrlMetaFinder(address)
    sys.meta_path.append(finder)


"""  
>>> from my_importer import install_meta
>>> install_meta('http://localhost:12800/') # 往 sys.meta_path 注册 finder 
>>> import my_info  # 打印ok，说明导入成功
ok
>>> my_info.name  # 验证可以取得到变量
"""
