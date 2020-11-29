# to read command line arguments
import sys

def url_parser(url_string):
    url_dict = dict()
    scheme = url_string[:url_string.find(':')]
    domain = url_string[url_string.find('//')+2:]
    url = url_string[url_string.find('//')+2:]

    # for fragment
    if '#' in domain: 
        fragment = domain[domain.rfind('#')+1:]
        domain = domain.split('#')[0]
        url = domain[:domain.find('#')]
    else: fragment = None

    # for domain
    if '/' in domain: path = domain[domain.find('/'):]; domain = domain[:domain.find('/')]
    else: path = None

    # for query string
    if '?' in url_string: query = url.split('?')[1]; path = path[:path.find('?')]
    else: query = None

    # TLD
    top_level_domain = domain[domain.rfind('.')+1:]
    url_dict_path= path
    url_dict_domain = domain
   
    url_dict_port = (lambda: None, lambda: url_dict_domain.split(':')[1])[':' in url_dict_domain]()

    # for port
    if ':' in url_dict_domain: url_dict_domain = url_dict_domain.split(':')[0]; top_level_domain = top_level_domain.split(':')[0]

    # for username
    username = (lambda: None, lambda: url_dict_domain.split('@')[0])['@' in url_dict_domain]()
    if '@' in url_dict_domain: url_dict_domain = url_dict_domain.split('@')[1]

    # populate the url parser dictionary with all the segments
    url_dict = {'scheme/protocol': scheme, 'username': username, 'domain': url_dict_domain, 'port': url_dict_port, 'path': url_dict_path, 'query': query, 'fragment': fragment}

    # print the segments
    print(url_dict)

    return url_dict

if __name__ == '__main__':
    url_parser(sys.argv[1])