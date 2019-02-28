
def path2dict(path, depth):
    d = {}
    text = path.split('/')[0]
    d['text'] = text
    #depth = depth + 1
    #d['children'] = [path2dict(p, depth) for p in path.split('/')[depth:]]
    #print "This is childer: %r" % d['children']
    return d

paths = [
   "root/child1/file1",
   "root/child1/file2",
   "root/child2/file2"
]

depth = 0
for path in paths:
	print paths
    #d = path2dict(path, depth)
    # print(d)

