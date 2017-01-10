#This is an expearnment with compile(string, '', expression)
s = """
def f():
	print("I like cake!")
"""

c = compile(s, 'fakemodule', 'exec')
exec s
f()
