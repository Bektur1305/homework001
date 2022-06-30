def domain_name(url):
    s = url.find('/')
    if s != -1:
        if url[s+2]!="w":
            dot = url.find('.')
            t = url[(s+2):(dot)]
            return t
        else:
            q= url[(s+6):]
            dot = q.find('.')
            t = q[:(dot)]
            return t
    else:
        q=url[4:]
        dot = q.find('.')
        t = q[:(dot)]
        return t

print(domain_name("http://google.com"))