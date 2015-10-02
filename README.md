Link to WebGL Globe Repo
https://github.com/dataarts/webgl-globe

Project Description:
http://googlecode.blogspot.co.uk/2011/05/visualizing-geographic-data-with-webgl.html
 This is WebGL Globe, a project by the Google Data Arts Team. We can plot data by putting in the 
correct JSON Format data. For Medidata Solutions, this can be client site location data, or it can
be the location of servers from different services.

Description of Technology Used:
Used Sumologic to obtain logs of Medidata Services
Including three key data: IP address, Name of Service, Count of Calls
Used Excel to Normalize the Count of Calls to between 0 and 1 and create csv
Used freegeoip.net api to get GEO information on IP addresses
Python libraries to process csv data into the correct JSON format
WebGL Globe Project javascript libraries including THREE.js, Tween.js and Dectector.js

Demo Description:
The demo uses the dataset *trial_category_data.json* that came from *August_13th_to_12th_ip_request.csv*.
I categorized them to three types including: Front End, Infrastructure and also Core to organise the data.

Technical Problems Experienced:
1. Problem with Data Obained
  *trial_15_days_greater_than_1000.csv* has data for 15 days of services that have greater than 1000 count of calls. The problem with this data set is that most of the IP addresses cannot be found through the freegeoip.net and therefore unable to plot.
  *finalServiceData15_days_smaller_than_1000.csv* has data for 15 days of services that have smaller than 1000 count of calls. The Geo location for this data set are mostly retrievable through the API, however, there is an error with the three.min.js that is attached as a screen shot. This can be seen if plotting dataset *trial_smaller_than_1000_new.json*. Same error shows up for other data sets.

2. Problem with Web GL Globe

*test_for_error.json* : As seen from the above screenshot, I played with this JSON data set and discovered that this error will show up if there are more than 3 Same Long Lat data group that show up. There may be other sources of this error.


Future Considerations and Usage:
1. Automate using python the normalisation process
2. More comprehensive and accurate IP to Geo data API
3. Would be nice to get Client Site Geo Data
4. Google Analytics has something similar but this can be more customised
