## Google Home AIButler Guide
Thanks to kylpeacock@gmail.com for all his help with npm/nodejs app 

### AIButler started with my first tutorial on www.santiapps.com where we:
1. Connected a RPi2 onto a home local linksys wifi network
2. Interfaced the pi with a bluetooth-serial module hm10
3. Wrote py scripts to connect to hm10-bt-enabled (4ch) relay board and send commands to control light circuit

### AIButler now will interface with GoogleHome device
1. Install node(~v7) and npm(~v5) on rpi and go ahead and get nginx as well.  apt-get install nodejs, npm, nginx 
2. Create folder on pi home/pi/Google/ghsm and put the files from git into that folder. 
3. Open terminal in pi (or ssh into it), go to home/pi/Google/ghsm/ directory & run `(sudo) npm install` to install the required components as specified by the packages.json file included.
4. Run `touch .env` to create the .env file (or (sudo) nano .env) and add the following 3 lines:
    DEV=TRUE if you are on desktop, or FALSE if you are on your raspberry pi
    PORT=8000 for development, 80 or 443 for HTTP or HTTPS
    PASS= Whatever you want your password to be
5. Run `(sudo) npm start` to launch the server and get the listening port prompt in terminal.  Your app is listening now
6. Test your app by opening brwoser window to http://yourRPisIPaddress:8000/API/switches/sw1?password=yourpwdhere.  You should get the json string with the current values of your switches array.  Browsers make GET requests by default so the switch will not be toggled.


When you make a POST request to the server, follow this structure: 
`http://ipaddresshere/API/switches/sw1?password=yourpwdhere`

### Next Steps
You will want to configure the Python files to suit your project's needs. In my case I simply added my existing toggle-the-bt-relay-board code to each sw1_off.py and sw1_on.py so that when those files are called upon toggling the nodejs app, the code gets executed and my lights are toggled.

To add or edit a switch, go into saveState.json. Use the first switch as a guide, and add a new object to the switches array. 

You can serve your own frontend out of the public folder, and it will be accessible on the root route if you make a get request to your IP address. 

### This nodejs app runs on your rpi, now let's make it accessible from the outside.
1. First get letsencrypt installed and create your certificate files.  You will need a qualifed domain or subdomain and you'll have to create an A Record for that domain to point to your router's public IP address (usu found in the Admin section of your router) 
2. Now configure your router to re-route requests made to its publicly assigned IP.  This is done in the router's Port Forwarding section and you must specify the name of the rule, the port on the router that will get re-routed and the IP within your lan to which that re-route will go to.  If your rpi's IP is 192.168.1.53 then that is the IP that port 80 must be re-routed to in the case of http requests.  Make sure to modify your certificate files' paths to the correct path.
3. Now connect this to your nodejs app which is listening on port 8000. To do so you must configure nginx.  The included file will guide you.  The file has a server{} block to re-route http requests on port 80 to 192...53:8081 and another block to re-route https requests on port 443 to 192...53:444.
4. Start your nodejs app by navigating to its folder in home/pi/Google/ghsm/ and running (sudo) npm start.
5. Then go to Hurl.it, make a post to your domain with the /API/switches/sw1?password=yourpwdhere and look out for the response

### Connect to Google Home device
1. Create your webhook on console.api.ai from Google, create your intent and in fulfillment fill in your URL used in Hurl.it
2. Talk to Google and control your lights like a pro!

#### Not working yet ####
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
