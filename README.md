# Fleet service (Microservice)
A codebase written by Python for checking specific cars in Lyft when they need services for parts such as battery, engine and tires. 

#The current detailed service data that we need to maintain:
Engines:
  Capulet Engine - should be serviced once every 30,000 miles
  Willoughby Engine - should be serviced once every 60,000 miles
  Sternman Engine - should be serviced only when the warning indicator is on
  
Batteries:
  Spindler Battery - should be serviced once every 2 years
  Nubbin Battery - should be serviced once every 4 years
  
Tires:
  Carrigan Tires - need to be serviced once one or more tire wear is equal or greater than 0.9
  Octoprime Tires - need to be serviced once all of the sum of tires greater than or equal to 3
  
Models of cars(included engine, battery, and tire they using)
Calliope
  Capulet Engine
  Spindler Battery
  Carrigan Tires
Glissade
  Willoughby Engine
  Spindler Battery
  Octoprime Tires
Palindrome
  Sternman Engine
  Spindler Battery
  Carrigan Tires
Rorschach
  Willoughby Engine
  Nubbin Battery
  Octoprime Tires
Thovex
  Capulet Engine
  Nubbin Battery
  Octoprime Tires
  
  
#Archritecture Design 

![Lyft Fleet Service](https://user-images.githubusercontent.com/27200158/185296227-093ee6e1-7038-486d-bb33-4d6dff5478a2.png)
