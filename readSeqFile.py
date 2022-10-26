# read the sequences saved in the file
# and the seq length information should be save in seqLen file

sequenceFile = "alias-gpt2-small/sequences.txt"
seqLenFile = "alias-gpt2-small/seqLen.txt"

seqF = open(sequenceFile,'r')
lenF = open(seqLenFile,'r')


lines = lenF.readlines()
tmp_total_len = 0
# print(len(lines))
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
print("sequence number : %d " % (len(lines)))

seqF.close()
lenF.close()