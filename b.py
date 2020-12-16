def test1():
    # test1 is above initial Dev Eq threshold,
    # has no modification after first commit,
    # and has in-degree of 1
    # but it lives shorter than 365 days
    if os.name != "nt":
        shutil.rmtree(top)
        return

    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)


def test2():
    # test 2 lives longer than 365 days,
    # has no modification after first commit,
    # and has an in-degree of 1
    # but its initial Dev Eq is smaller than 25
    pass
