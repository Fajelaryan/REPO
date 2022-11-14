class HiddenLeaf(): 
     def Name(self):
      print("===========================================================")
      print("Name: Minato Uzumaki")
      print("===========================================================")
     def Affiliation(self): 
       print("Affiliation: Village Hidden in the Leaves") 
     def CurrentNinjaRank(self):
       print("Current Ninja Rank: Hokage") 
     def RegisteredNijaNumber(self):
       print("Registered NinJa Number: Unknown") 
     def DateOfBirth(self):
       print("Date of Birth: January 25th")
     def Age(self):
       print("Age: Deceased")  
     def ZodiacSign(self):
       print("Zodiac Sign: Aquarius") 
     def Height(self):
       print("Height: 179.2 cm") 
     def Weight(self):
       print("Weight: 66.1 kg") 
     def BloodType(self):
       print("BloodType: B") 
     def FavoriteFood(self):
       print("Favorite Food: Kushina's Home Cooking") 
     def LeastFavoriteFood(self):
       print("Least Favorite Food: Unknown") 
     def Hobby(self):
       print("Hobby: Reading Jira's novel") 
     def AssignmentCommpleted(self):
         print("Assignment Completed: 122D- Rank, 147C-Rank, 216B-Rank, 323A -Rank, 39S - Rank ")
         print("===========================================================")
         
class HiddenLeaf1(): 
     def Name(self):
      print("Name: Obito Utchiha")
      print("===========================================================")
     def Affiliation(self): 
       print("Affiliation: Konohagakure / Akatsuki") 
     def CurrentNinjaRank(self):
       print("Current NinJa Rank: S - Class missing Ninja") 
     def RegisteredNijaNumber(self):
       print("Registered Ninja Number: 010886") 
     def DateOfBirth(self):
       print("Date of Birt: Febuary 10th")
     def Age(self):
       print("Age: 31")  
     def ZodiacSign(self):
       print("Zodiac Sign: Aquarius") 
     def Height(self):
       print("Height: 165.09cm") 
     def Weight(self):
       print("Weight: 55.8 kg") 
     def BloodType(self):
       print("Blood Type: 0") 
     def FavoriteFood(self):
       print("Favorite Food: Unknown") 
     def LeastFavoriteFood(self):
       print("Least Favorite Food: Unknown") 
     def Hobby(self):
       print("Hobby: To Complete Infinite Tsukuyumi") 
     def AssignmentCommpleted(self):
         print("Assignment Commpleted: Unkon due to Third Great Ninja War ")
         print("===========================================================")
        
obj_Ninja = HiddenLeaf()
obj_Ninja1 = HiddenLeaf1() 

for Shinobi in (obj_Ninja, obj_Ninja1):
    Shinobi.Name()
    Shinobi.Affiliation()
    Shinobi.CurrentNinjaRank()
    Shinobi.RegisteredNijaNumber()
    Shinobi.DateOfBirth()
    Shinobi.Age()
    Shinobi.ZodiacSign()
    Shinobi.Height()
    Shinobi.Weight()
    Shinobi.BloodType()
    Shinobi.FavoriteFood()
    Shinobi.LeastFavoriteFood()
    Shinobi.Hobby()
    Shinobi.AssignmentCommpleted()