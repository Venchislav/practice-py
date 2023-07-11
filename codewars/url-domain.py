def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]


print(domain_name("https://www.cnet.com"))
