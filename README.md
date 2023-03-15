# MC2DC
Simple python websocket message and whisper logger from minecraft bedrock to discord

**Log all whispers and messages from your minecraft bedrock world/realm directly to your discord webhook**

> Hosting currently only tested on windows 
>
> Must be hosted with python but can be used on any platform on bedrock


**Required Libraries:**

`websockets` `requests`

**Requirements:**

`python3.2 or higher`

**How To Set Up:**

Step 1:
    
    Download MC2DC as a zip file and extract it
    
    Make sure python is up to date
    
    Make sure all the required libraries are installed and up to date (can be done manually or by running install.bat)

Step 2:

    Open main.py
    
    Set url on line 33 to the url of the discord webhook you want to post to
    
    Set ip on line 36 to the ip/url/uri of your websocket, or leave as is if being hosted localy
    
    Set port on line 39 to the port you want to host it to, or leave as is if being hosted localy
    
    
**How To Run:**

After setting up, use start.bat or run manually
    

**How To Connect On PC:**

For local connections:

    Run commands in powershell:

        For Minecraft Bedrock: CheckNetIsolation LoopbackExempt -a -n="Microsoft.MinecraftUWP_8wekyb3d8bbwe"

        For Minecraft Bedrock Preview: CheckNetIsolation LoopbackExempt -a -n="Microsoft.MinecraftWindowsBeta_8wekyb3d8bbwe"

    Run Command in Minecraft:

        /connect 127.0.0.1:3000


For online connections:

    Run Command in Minecraft:

        /connect <WEBSOCKET IP>
        where <WEBSOCKET IP> is replaced by the websocket ip
        

**How to connect on other platforms:**

    Run Command in Minecraft:

        /connect <WEBSOCKET IP>
        where <WEBSOCKET IP> is replaced by the websocket ip
        
**Troubleshooting:**


If minecraft is failing to connect to the websocket:

    Test webhook on https://websocketking.com

    If test works and websocket is being run localy then:    
    
      Run commands in powershell:

          For Minecraft Bedrock: CheckNetIsolation LoopbackExempt -a -n="Microsoft.MinecraftUWP_8wekyb3d8bbwe"

          For Minecraft Bedrock Preview: CheckNetIsolation LoopbackExempt -a -n="Microsoft.MinecraftWindowsBeta_8wekyb3d8bbwe"
          
      More Info: https://doc.pmmp.io/en/rtfd/faq/connecting/win10localhostcantconnect.html
      
    If being hosted online, make sure you make a ws://example.com websocket and not a https://example.com.
    
**Contact:**

Discord: GalacticApricot#9601
    
    
        

