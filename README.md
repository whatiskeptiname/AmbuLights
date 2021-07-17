# AmbuLights

Raspberry Pi based project to notify vehicles about emergency ambulances in their route. It was developed during Hackathon organized by ITONICS Nepal. Whenever there is an emergency need of an ambulance the emergency lights in that particular route will be turned on.
## Images

**Hardware Device**

<div align="center">
   <img src="./images/led_off.jpg" width="40%" height="40%" />

   <img src="./images/led_on.jpg" width="40%" height="40%" />
</div>

<!-- **Screenshot from UserApp**

<div align="center">
   <img src="./images/screenshot.png" width="60%" height="60%" />
</div> -->

## Components Used

1. Raspberry Pi 3 Model B
2. leds *9
3. Breadboard 

## Working

User selects a route from the map, the information about the route is sent to the server. The server will match the best route by comparing the latitude and longitude of the route with pre defined ones. Once the route is matched the server will light the leds in the route notifying the vehicles about the coming ambulance.