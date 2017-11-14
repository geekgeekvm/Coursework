import math

class Vertex:
	def __init__(self):
		self.color='white'
		self.start=0
		self.num=0
		self.end=0
		self.pred=None
class Graph:
	def __init__(self,n=None):
		self.n=n
		self.treedge=[]
		self.forwedge=[]
		self.backedge=[]
		self.crossedge=[]
		self.edges=[]
		self.time=0
		self.timestamp=dict()
		self.vertexlist=[]
		self.adjlist=dict()
		for i in range(n):
			self.adjlist[i]=[]
		self.labellist=dict()
		

	def adjlistm(self,index1,index2):

		l=self.adjlist.get(index1)
		l.append(index2)
		

	def dfsmain(self,source):
		for i in range(self.n):
			x=Vertex()
			x.num=i

			self.vertexlist.append(x)
		self.dfs(source)


	def dfs(self,source):
		
		s=self.vertexlist[source]
		s.color='grey'
		self.time=self.time+1
		s.start=self.time

		a=self.adjlist[s.num]
		if(len(a)>0):
			a.sort()
		
			for i in a:
				v=self.vertexlist[i]
				
				if v.color is 'white':
					
					self.treedge.append([s.num,v.num])
					self.dfs(v.num)
					v.pred=s

			s.color='black'
		self.time=self.time+1
		s.end=self.time
		timeaaray=[s.start,s.end]
		self.timestamp[s.num]=timeaaray
		

	

		
def main():
	n=int(input())
	m=int(input("edges"))
	G=Graph(n)
	for i in range(m):
		var1, var2= input().split()
		G.edges.append([int(var1),int(var2)])
		G.adjlistm(int(var1),int(var2))
	G.dfsmain(2)
	print(G.timestamp)
	for i in G.edges:
		if i not in G.treedge:
			starta=G.timestamp.get(i[0])[0]
			startb=G.timestamp.get(i[1])[0]
			enda=G.timestamp.get(i[0])[1]
			endb=G.timestamp.get(i[1])[1]
			if(starta>startb && enda<endb):
				G.backedge.append(i)
			if(starta>endb):
				G.crossedge.append(i)
			if(startb>starta):
				G.forwedge.append(i)

main()
