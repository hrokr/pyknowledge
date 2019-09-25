def pass_hash(str):
    """
Password Hashes<7kyu>

Comments:
    As a side note, md5 can be exploited, so never use it for anything secure.
    The reason I used it in this kata is simply because it is a very common 
    hashing algorithm and many people will recognize the name.

Task:
    Create the function that converts a given string into an md5 hash. 
    The return value should be encoded in hexadecimal.

Notes:
    If you want to externally test a string, look at this website.
    http://www.md5hasher.net/

Input >> Output Examples
    pass_hash('password') # ==> 5f4dcc3b5aa765d61d8327deb882cf99
    pass_hash('abc123') # ==>  e99a18c428cb38d5f260853678922e03   
    """

    import hashlib
    print (hashlib.md5(str.encode('utf-8')).hexdigest())


pass_hash("password")
