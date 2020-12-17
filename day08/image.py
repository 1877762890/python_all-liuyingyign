
f=open("景甜.jpg","rb")#景甜前没有 ../，因为景甜这个图片是直接在day08下面，如果在day08-demo里面就需要加../
w=open("1798.jpg","wb")

data=f.read()
w.write(data)

f.close()
w.close()

