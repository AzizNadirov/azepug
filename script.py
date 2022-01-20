
def reqs_without_versions():
    """ 
        I had a issue related with changing
        python version. So, my requirements.txt file
        didn't work. There are i delete version part of
        module names in requirements.txt
    """

    ff = open('requirements.txt', 'r')
    f_output = open('requirements2.txt', 'w')
    f = ff.readlines()
    for m in f:
        module_name = m[0:m.find("=")]
        f_output.write(module_name+'\n')
    ff.close()
    f_output.close()