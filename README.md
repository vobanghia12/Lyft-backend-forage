# Fleet service (Microservice)
A codebase written by Python for checking specific cars in Lyft when they need services for parts such as battery, engine and tires. 

<h2>The current detailed service data that we need to maintain:</h2>

<h4> Engines:</h4>
<ul>
  <li>Capulet Engine - should be serviced once every 30,000 miles</li>
  <li>Willoughby Engine - should be serviced once every 60,000 miles</li>
  <li>Sternman Engine - should be serviced only when the warning indicator is on</li>
</ul>

  
<h4> Batteries:</h4>
<ul>
  <li>Spindler Battery - should be serviced once every 2 years</li>
  <li>Nubbin Battery - should be serviced once every 4 years</li>
</ul>
  
<h4>Tires:</h4>
  <ul>
  <li>Carrigan Tires - need to be serviced once one or more tire wear is equal or greater than 0.9</li>
  <li>Octoprime Tires - need to be serviced once all of the sum of tires greater than or equal to 3</li>
  </ul>
  
<h2>Models of cars(included engine, battery, and tire they using)</h2>
<h4>Calliope</h4>
<ul>
  <li>Capulet Engine</li>
  <li>Spindler Battery</li>
  <li>Carrigan Tires</li>
 </ul>
<h4>Glissade</h4>
<ul>
  <li>Willoughby Engine</li>
  <li>Spindler Battery</li>
  <li>Octoprime Tires</li>
 </ul>
<h4>Palindrome</h4>
<ul>
  <li>Sternman Engine</li>
  <li>Spindler Battery</li>
  <li>Carrigan Tires</li>
  </ul>
  <h4>Rorschach</h4>
  <ul>
  <li>Willoughby Engine</li>
  <li> Nubbin Battery</li>
  <li>Octoprime Tires</li>
  </ul>
<h4>Thovex</h4>
<ul>
  <li>Capulet Engine</li>
  <li>Nubbin Battery</li>
  <li>Octoprime Tires</li>
</ul>
  
  
<h2>Archritecture Design</h2>

![Lyft Fleet Service](https://user-images.githubusercontent.com/27200158/185296227-093ee6e1-7038-486d-bb33-4d6dff5478a2.png)
