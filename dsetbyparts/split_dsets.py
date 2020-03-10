def split_file(file, prefix, max_size, buffer=1024):
    with open(file, 'r+b') as src:
        suffix = 0
        while True:
            with open(prefix + '.%s' % suffix, 'w+b') as tgt:
                written = 0
                while written < max_size:
                    data = src.read(buffer)
                    if data:
                        tgt.write(data)
                        written += buffer
                    else:
                        return suffix
                suffix += 1
#split_file("../houston.mat", "houston_part", 80*1000*1000)
#split_file("../KSC.mat", "KSC_part", 80*1000*400)
split_file("../paviaC.mat", "paviaC_part", 80*1000*1000)
