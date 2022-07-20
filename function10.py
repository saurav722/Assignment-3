class Emp:
    def _init_(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def _str_(self):
        return "emp id=%d Emp name=%s Emp sal=%g"%(self.eid,self.ename,self.esal)
e1 = Emp(111,"kamal",100000.45)
print(e1)
e2 = Emp(111,"anu",200000.46)
print(e2)