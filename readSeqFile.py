# read the sequences saved in the file
# and the seq length information should be save in seqLen file

sequenceFile = "sequences.txt"
seqLenFile = "seqLen.txt"

seqF = open(sequenceFile,'r')
lenF = open(seqLenFile,'r')

# total_len = len(seqF.read())
# print(total_len)
lines = lenF.readlines()
tmp_total_len = 0
for line in lines:
    tmp_len = int(line)
    tmp_total_len += tmp_len
    str = seqF.read(tmp_len)#.decode("utf-8")
    print(str)
    if(tmp_len != len(str)):
        print("error tmp_len :%d len(str):%d" % (tmp_len, len(str)))
    assert(tmp_len == len(str))
    print("我是分隔符~~~~~~~~~~~~~~~~~~~~~~")
    print(tmp_len)
print(tmp_total_len)
seqF.close()
lenF.close()