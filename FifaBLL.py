from FifaDataAccess import accessdata

class players:
    def __init__(self):
        self.dataAccess=accessdata()
        self.records=[(1,"Leon","Goretzka","Germany","Bayern Munich","CM",87),(2,"HamidReza","Horr","Iran","Esteghlal","LW",99),(3,"Cristiano","Ronaldo","Portugal","Al Nassr","ST",90)
        ,(4,"Lionel","Messi","Argentine","PSG","RW",93),(5,"Kylian","Mbappe","France","PSG","ST",92),(6,"Karim","Benzema","France","Real Madrid","ST",92),
        (7,"Iker","Casilas","Spain","LEGEND","GK",90),(8,"Andrea","Pirlo","Italy","LEGEND","CM",89),(9,"Wayne","Rooney","England","LEGEND","ST",88),
        (10,"Abbas","Boazzar","Iran","Naft","CM",70),(11,"Vinicius","Junior","Brazil","Real Madrid","LW",87),(12,"Kevin","De bruyne","Belgium","Man City","CAM",88),
        (13,"Farhad","Majidi","Iran","Esteghlal","ST",98),(14,"Mehdi","Torabi","Iran","Long","LW",66),(15,"Vahid","Amiri","Iran","Long","RW",30),(16,"Luka","Modric","Croatia","Real Madrid","CM",88),
        (17,"Pablo","Gavi","Spain","Barcelona","CM",83),(18,"David","Alaba","Austria","Real Madrid","CB",86),(19,"Erling","Halland","Norway","Man City","ST",90),
        (20,"Bruno","Fernandes","Portugal","Man United","CAM",88),(21,"Neymar","Jr","Brazil","PSG","LW",89),(22,"Thomas","Muller","Germany","Bayern Munich","CAM",86),
        (23,"Naser","Hejazi","Iran","Esteghlal","GK",98),(24,"Mansour","Pourheidari","Iran","Esteghlal","RB",98),(25,"Gianluigi","Buffon","Italy","LEGEND","GK",90),
        (26,"Zinedine","Zidane","France","LEGEND","GK",95),(27,"Gerard","Pique","Spain","Shakira","CB",84),(28,"Eric","Cantona","France","LEGEND","ST",92),
        (29,"Paolo","Maldini","Italy","LEGEND","CB",95), (30,"Jiloyd","Samuel","England","Esteghlal","RB",75)]
    
    def createData(self):
        query="INSERT INTO tblPlayers VALUES(?,?,?,?,?,?,?)"
        self.dataAccess.insertQuery(query,self.records)
    
    def deleteData(self):
        query="DELETE FROM tblPlayers"
        self.dataAccess.deleteQuery(query)
    
    def updateData(self,playername,overall,post,nation):
        query=f"UPDATE tblPlayers SET overall={overall}  , nation = '{nation}' , position = '{post}' WHERE firstName='{playername}' "
        self.dataAccess.updateQuery(query)
    
    def deletesData(self,playername,overall,post,nation):
        query=f"DELETE FROM tblPlayers WHERE overall>={overall}  AND nation = '{nation}' AND position = '{post}' AND firstName='{playername}' "
        self.dataAccess.deleteQuery(query)
    
    def searchData(self,playername,overall,post,nation):
        if post=="" and nation=="Any" and playername=="" :
            query=f"SELECT * FROM tblPlayers WHERE overall>={overall} ORDER BY overall DESC"
        elif post=="" and nation!="Any" and playername!="":
            query=f"SELECT * FROM tblPlayers WHERE overall >= {overall} AND nation = '{nation}' AND firstName = '{playername}' ORDER BY overall DESC"
        elif nation=="Any" and post!="" and playername!="":
            query=f"SELECT * FROM tblPlayers WHERE overall>={overall} AND position = '{post}' AND firstName = '{playername}' ORDER BY overall DESC"
        elif playername=="" and nation!="Any" and post!="":
            query=f"SELECT * FROM tblPlayers WHERE overall>={overall} AND position = '{post}' AND nation = '{nation}' ORDER BY overall DESC"
        elif post=="" and nation=="Any" and playername!="":
            query=f"SELECT * FROM tblPlayers WHERE overall>={overall} AND firstName='{playername}' ORDER BY overall DESC"
        elif post=="" and playername=="" and nation!="Any":
            query=f"SELECT * FROM tblPlayers WHERE overall>={overall} AND nation = '{nation}' ORDER BY overall DESC"
        elif playername=="" and nation=="Any" and post!="":
            query=f"SELECT * FROM tblPlayers WHERE overall>={overall} AND position = '{post}' ORDER BY overall DESC"
        else:
            query=f"SELECT * FROM tblPlayers WHERE  overall>={overall}  AND nation = '{nation}' AND position = '{post}' AND firstName='{playername}' ORDER BY overall DESC"
        # query=f"SELECT * FROM tblPlayers WHERE overall >= {overall} AND position = '{post}'"
        rows=self.dataAccess.searchData(query) 
        return rows