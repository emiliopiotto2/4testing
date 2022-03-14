class Hotel:
    
    def __init__(self,stars:int=0,location:int=0) -> None:      
        #Assinging
        self.stars = stars
        self.location = location
        
        print(f"Instance created!:{stars},{location}")

    def total_value(self):
        return self.stars*self.location


    def hotel_classifier(self):
        print('Running Classifier')
        if self.stars >=4:
            rating = 'Premium'
            if self.location in range(0,3):
                loc = 'Close range'
            elif self.location in range(3,7):
                loc = 'Medium range'
            elif self.location in range(7,10):
                loc = 'Long range'
        else:
            rating= 'Normal'
        return [rating,loc]