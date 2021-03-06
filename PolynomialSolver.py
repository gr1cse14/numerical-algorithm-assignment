# ques 5
class PolynomialSolver:
	def F(self,n,L,val):
		return sum(L[i]*(val**i) for i in range(n+1))
	def Fder(self,n,L,val):
		return sum(i*L[i]*(val**(i-1)) for i in range(1,n+1))
	def solve(self,n,L,method):
		if(method=='bisection'):
			print("Input lower bound of interval in which root lies")
			l=int(input())
			print("Input upper bound of interval in which root lies")
			u=int(input())
			print("Input maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,l)-self.F(n,L,u))>0.00001 and it>0):
				m=(l+u)/2
				if(self.F(n,L,l)*self.F(n,L,m)<0):
					u=m
				else:
					l=m
				print (l,u,self.F(n,L,l),self.F(n,L,u))
				it-=1
			return([l,u])
		if(method=='secant'):
			print("Enter lower bound of interval in which root lies")
			l=int(input())
			print("Enter upper bound of interval in which root lies")
			u=int(input())
			print("Enter maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,l))>0.00001 and it>0):
				f1=self.F(n,L,l)
				f2=self.F(n,L,u)
				l,u=u,u-(((u-l)*f2)/(f2-f1))
				print (l,u,f1,f2)
				it-=1
			return(l)
		if(method=='secantRF'):
			print("Enter lower bound of interval in which root lies")
			l=int(input())
			print("Enter upper bound of interval in which root lies")
			u=int(input())
			m=l
			print("Enter maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,m))>0.00001 and it>0):
				f1=self.F(n,L,l)
				f2=self.F(n,L,u)
				m=u-(((u-l)*f2)/(f2-f1))
				fm=self.F(n,L,m)
				if(f1*fm<0):
					u=m
				else:
					l=m
				print (m)
				it-=1
			return(l)
		if(method=='newtonraphson'):
			print("Enter lower bound of interval in which root lies")
			l=int(input())
			print("Enter maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,l))>0.00001 and it>0):
				l=l-self.F(n,L,l)/self.Fder(n,L,l)
			return(l)
		else:
			return NULL
