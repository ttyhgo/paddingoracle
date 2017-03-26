from oracle import *
import sys

'''
if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()
'''

odata = "9F0B13944841A832B2421B9EAF6D9836813EC9D944A5C8347A7CA69AA34D8DC0DF70E343C4000A2AE35874CE75E64C31"
#data = "9F0B13944841A832B2421B9EAF6D9836813EC9D943A2CF337D7BA19DA74A8AC7DF70E343C4000A2AE35874CE75E64C31"

print int('FF',16)

databl1 = odata[:32]
databl2 = odata[32:64]
databl3 = odata[64:96]

paddlen = 16
for j in range(0, 32, 2):
    databl2 = databl2[:j] + "FF" + databl2[j+2:]

    data = databl1 + databl2 + databl3

    #print i, data
    ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
    #print ctext

    Oracle_Connect()
    rc = Oracle_Send(ctext, 3)
    Oracle_Disconnect()
    if rc == 0:
        paddlen = paddlen - j/2
        print j/2,data
        break
padd = hex(paddlen)
print paddlen, padd

databl2 = odata[32:64]

print odata
for y in range(0, paddlen):
    for x in range(32, (32-((paddlen-y)*2)), -2):
        #print hex(int(databl2[(j-2):j],16))
        #print int(padd, 16)^ (int(padd,16)+1)
        print "x", x
        databl2 = databl2[:x-2] + hex( int(databl2[(x-2):x],16) ^(int(padd, 16)^ (int(padd,16)+1)) )[2:].upper()  + databl2[x:]
        mdata = databl1 + databl2 + databl3
        #print data
    print "mm",mdata
    for j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
        flag = False
        for k in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            temp = (j + k).upper()

            data = mdata[:32] + mdata[32:30+((16-paddlen-y)*2)] + temp + mdata[32+((16-paddlen-y)*2):]
            #print data
            ctext = [(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)]
            Oracle_Connect()
            rc = Oracle_Send(ctext, 3)
            Oracle_Disconnect()
            if rc == 1:
                print "find",rc, data
                flag = True
                break
        if flag == True:
            break

    padd = hex((int(padd,16)+1))
    #print "padd", padd
    databl2 = data[32:64]
'''

for j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f']:
    flag = False
    for k in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f']:
        temp = (j+k).upper()


        data = mdata[:32]+mdata[32:40]+temp+mdata[42:]
        print data
        ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
        Oracle_Connect()
        rc = Oracle_Send(ctext, 3)
        Oracle_Disconnect()
        if rc == 1:
            print rc,data
            flag = True
            break
    if flag == True:
        break
'''


data = "9F0B13944841A832B2421B9EAF6D9836813EC9D961A2CF337D7BA19DA44A8AC7DF70E343C4000A2AE35874CE75E64C31"
ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]

print data
Oracle_Connect()
rc = Oracle_Send(ctext, 3)
Oracle_Disconnect()
print "rr", rc


for j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f']:
    flag = False
    for k in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f']:
        temp = (j+k).upper()


        data = mdata[:32]+mdata[32:38]+temp+mdata[40:]
        print data
        ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
        Oracle_Connect()
        rc = Oracle_Send(ctext, 3)
        Oracle_Disconnect()
        if rc == 1:
            print rc,data
            flag = True
            break
    if flag == True:
        break