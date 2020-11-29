# Write a Python script called as urlparser.py. The script parses an url into the segments that are explained in the lecture Internet vs WWW, and additionally 
# extracts top-level

#Take a screenshot of the terminal output of your script for the following URLs
# 1. https://www.facebook.com/photo.php?fbid=2068026323275211&set=a.269104153167446&type=3&theater    X
# 2. http://www.blog.google.uk:1000/path/to/myfile.html?key1=value1&key2=value2#InTheDocument        X
# 3. https://www.overleaf.com/9565720ckjijuhzpbccsd#/347876331/
# 4. ftp://root@west.uni.koblenz.de
# 5. https://west.uni-koblenz.de/studying/ws2021
# You are not allowed to use any specific libraries that help in url parsing and regular expressions.

import sys

def url_parser(url_string):

    # url_string = sys.argv[1]
    # url_string = 'https://west.uni-koblenz.de/research/projects'
    url_dict = dict()
    scheme = url_string[:url_string.find(':')]
    domain = url_string[url_string.find('//')+2:]
    url = url_string[url_string.find('//')+2:]

    if '#' in domain: 
        fragment = domain[domain.rfind('#')+1:]
        domain = domain.split('#')[0]
        url = domain[:domain.find('#')]
    else: fragment = None
    if '/' in domain:
        path = domain[domain.find('/'):]
        domain = domain[:domain.find('/')]
    else: path = None
    if '?' in url_string: query = url.split('?')[1]; path = path[:path.find('?')]
    else: query = None
    top_level_domain = domain[domain.rfind('.')+1:]
    url_dict_path= path
    url_dict_domain = domain
    # url_dict_domain = (lambda: domain, lambda: domain[:domain.find('/')])['/' in domain]()
    url_dict_port = (lambda: None, lambda: url_dict_domain.split(':')[1])[':' in url_dict_domain]()
    if ':' in url_dict_domain: url_dict_domain = url_dict_domain.split(':')[0]; top_level_domain = top_level_domain.split(':')[0]

    username = (lambda: None, lambda: url_dict_domain.split('@')[0])['@' in url_dict_domain]()
    if '@' in url_dict_domain: url_dict_domain = url_dict_domain.split('@')[1]

    url_dict = {'scheme/protocol': scheme, 'username': username, 'domain': url_dict_domain, 'port': url_dict_port, 'path': url_dict_path, 'query': query, 'fragment': fragment}

    print(url_dict)

    return url_dict

if __name__ == '__main__':
    url_parser(sys.argv[1])