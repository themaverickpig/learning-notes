parame = {1,2,3,3}
# parame.add(4)
parame.update([1,2,3,4,5,'hello','world'])
parame.remove(4)
parame.remove('hello')
parame.discard('world')
parame.discard(6)
parame.update('dahishdoaihs ocoashohcasca')
print(parame)
a = parame.pop()
print(a)
print(len(parame))