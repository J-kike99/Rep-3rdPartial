class Song(object):
    
    def _init_(self , lyrics):
        sel.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
            
santaclaus_its_comming = Song(["You better watch out",
                               "You better no cry",
                               "You better not pound"]) 


santaclaus_its_comming2 = Song(["I'm telling you why ",
                                "Santaclaus is comming to town"])

santaclaus_its_comming.sing_me_a_song()

santaclaus_its_comming2.sing_me_a_song()
