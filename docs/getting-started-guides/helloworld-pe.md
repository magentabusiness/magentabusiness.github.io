---
layout: docwithnav-pe
assignees:
- ashvayka
title: Getting Started with IoT Hub
description: Getting started with IoT Hub open-source IoT platform and simulated IoT devices
redirect_from: "/docs/pe/getting-started-guides/helloworld/"
step1:
    0:
        image: /images/helloworld/hello-world-pe-step-1-item-1-magenta.png
        title: 'Login to your IoT Hub instance and open Device Groups(1) page, <br>
        Navigate to default Deivce Group "ALL"(2), <br>
        Click on the "+" icon in the top right corner of the table and then select "Add Device"(3).'
    # 1:
    #     image: /images/helloworld/hello-world-pe-step-1-item-3.png
    #     title: 'Navigate to default Device group “ALL”.'
    # 2:
    #     image: /images/helloworld/hello-world-pe-step-1-item-2.png 
    #     title: 'Click on the "+" icon in the top right corner of the table and then select "Add Device".'
    2:
        image: /images/helloworld/hello-world-pe-step-1-item-4-magenta.png
        title: 'Input device name. For example, "My New Device". No other changes are required at this time. Click "Add" to add the device.'
    3:
        image: /images/helloworld/hello-world-pe-step-1-item-5-magenta.png
        title: 'Now your device should be listed first, since the table sorts devices using the time of the creation by default. '
        
step2:
    0:
        image: /images/helloworld/hello-world-pe-step-2-item-1-magenta.png
        title: 'Click on the device row in the table to open device details;'
    1:
        image: /images/helloworld/hello-world-pe-step-2-item-2-magenta.png
        title: 'Click "Copy access token". Token will be copied to your clipboard. Save it to a safe place.'

step3:
    0:
        image: /images/helloworld/hello-world-pe-step-2-item-1-magenta.png 
        title: 'Click on the device row in the table to open device details;'
    1:
        image: /images/helloworld/hello-world-pe-step-2-item-4-magenta.png
        title: 'Navigate to the telemetry tab.'
        
step31:
    0:
        image: /images/helloworld/hello-world-pe-step-31-item-1-magenta.png
        title: 'Open Dashboard Groups page. Open default dashboard group “All”. Click on the "+" icon in the top right corner to create a new dashboard.'
    1:
        image: /images/helloworld/hello-world-pe-step-31-item-2-magenta.png
        title: 'Input dashboard name. For example, "My New Dashboard". Click "Add" to add the dashboard.'
    2:
        image: /images/helloworld/hello-world-pe-step-31-item-3-magenta.png
        title: 'Now your dashboard should be listed first, since the table sorts dashboards using the time of the creation by default. Click on the "Open dashboard" icon.'
        
step32:
    0:
        image: /images/helloworld/hello-world-pe-step-32-item-1-magenta.png 
        title: 'Enter edit mode. Click on the pencil button in the bottom right corner.'
    1:
        image: /images/helloworld/hello-world-pe-step-32-item-2-magenta.png  
        title: 'Click "Entity Aliases" icon in the top right part of the screen. You will see an empty list of Entity aliases.'
    2:
        image: /images/helloworld/hello-world-pe-step-32-item-3-magenta.png  
        title: 'Click "Add alias".'
    3:
        image: /images/helloworld/hello-world-pe-step-32-item-4-magenta.png  
        title: 'Input alias name, for example "MyDevice". Select "Single entity" Filter type. Select "Device" as Type and type "My New" to enable autocomplete. Choose your device from the auto-complete and click on the needed device.'        
    4:
        image: /images/helloworld/hello-world-pe-step-32-item-5-magenta.png  
        title: 'Click "Add" and then "Save".'        
    5:
        image: /images/helloworld/hello-world-pe-step-32-item-6-magenta.png  
        title: 'Finally, Click "Apply changes" in the dashboard editor to save the changes. Then you should enter edit mode again.'

step33:
    0:
        image: /images/helloworld/hello-world-pe-step-33-item-1-magenta.png
        title: 'Enter edit mode. Click on the "Add new widget" button. '
    1:
        image: /images/helloworld/hello-world-pe-step-33-item-2-magenta.png
        title: 'Select "Cards" widget bundle.'
    2:
        image: /images/helloworld/hello-world-pe-step-33-item-2_1-magenta.png
        title: 'Select "Entities table - Latest values" widget. '
    3:
        image: /images/helloworld/hello-world-pe-step-33-item-3-magenta.png
        title: 'Click "Add" to add the data source. Widget may have multiple data sources, but we will use only one in this case.'
    4:
        image: /images/helloworld/hello-world-pe-step-33-item-4-magenta.png 
        title: 'Select "MyDevice" entity alias. Then click on the input field to the right. The auto-complete with available data points will appear. Select "temperature" data point and click "Add".'        
    5:
        image: /images/helloworld/hello-world-pe-step-33-item-5-magenta.png
        title: 'Resize the widget to make it a little bigger. Just drag the bottom right corner of the widget. You can also play with the advanced settings if you want to edit the widget.'
        
step34:
    0:
        image: /images/helloworld/hello-world-pe-step-34-item-1-magenta.png 
        title: 'Enter Edit mode.'
    1:
        image: /images/helloworld/hello-world-pe-step-34-item-2-magenta.png 
        title: 'Click "Add new widget" icon in the bottom right corner of the screen.'
    2:
        image: /images/helloworld/hello-world-pe-step-34-item-3-magenta.png 
        title: 'Click "Create new widget" icon.'
    3:
        image: /images/helloworld/hello-world-pe-step-34-item-4-magenta.png 
        title: 'Select "Charts" bundle.' 
    4:
        image: /images/helloworld/hello-world-pe-step-34-item-4_1-magenta.png 
        title: 'Select "Timeseries Line Chart" widget.'        
    5:
        image: /images/helloworld/hello-world-pe-step-34-item-5-magenta.png  
        title: 'Click "Add datasource" button.'
    6:
        image: /images/helloworld/hello-world-pe-step-34-item-6-magenta.png
        title: 'Select "MyDevice" Alias. Select "temperature" key. Click "Add".'
    7:
        image: /images/helloworld/hello-world-pe-step-34-item-7-magenta.png
        title: 'Drag and Drop you widget to desired space. Resize the widget. Apply changes.'
    8:
        image: /images/helloworld/hello-world-pe-step-34-item-8-magenta.png  
        title: 'Publish different telemetry values multiple times Step 2. Note that the widget displays only one minute of data by default.'
    9:
        image: /images/helloworld/hello-world-pe-step-34-item-9-magenta.png  
        title: 'Enter Edit mode. Open time selection window. Change the interval and aggregation function. Update the time window and apply changes.'

step35:
    0:
        image: /images/helloworld/hello-world-pe-step-35-item-1-magenta.png 
        title: 'Enter Edit mode.'
    1:
        image: /images/helloworld/hello-world-pe-step-35-item-2-magenta.png  
        title: 'Click "Add new widget" icon in the bottom right corner of the screen.'
    2:
        image: /images/helloworld/hello-world-pe-step-35-item-3-magenta.png  
        title: 'Click "Create new widget" icon.'
    3:
        image: /images/helloworld/hello-world-pe-step-35-item-4-magenta.png  
        title: 'Select "Alarm widgets" bundle.'        
    4:
        image: /images/helloworld/hello-world-pe-step-35-item-4_1-magenta.png  
        title: 'Select "Alarm table" widget.'        
    5:
        image: /images/helloworld/hello-world-pe-step-35-item-5-magenta.png  
        title: 'Select "Entity" alarm source and "MyDevice" alias. Click "Add"'
    6:
        image: /images/helloworld/hello-world-pe-step-35-item-6-magenta.png  
        title: 'Scroll down and locate new "Alarms" widget. Drag and Drop widget to the top right corner of the dashboard.'
    7:
        image: /images/helloworld/hello-world-pe-step-35-item-7-magenta.png  
        title: 'Resize the widget and apply changes.'

step4:
    0:
        image: /images/helloworld/hello-world-pe-step-4-item-1-magenta.png 
        title: 'Navigate to the device profiles page.'
    1:
        image: /images/helloworld/hello-world-pe-step-4-item-2-magenta.png
        title: 'Click the default profile row. This will open device profile details.'
    2:
        image: /images/helloworld/hello-world-pe-step-4-item-3-magenta.png
        title: 'Select the "Alarm Rules" tab and toggle edit mode.'
    3:
        image: /images/helloworld/hello-world-pe-step-4-item-4-magenta.png
        title: 'Click "Add alarm rule".'        
    4:
        image: /images/helloworld/hello-world-pe-step-4-item-5-magenta.png 
        title: 'Specify alarm type and click the "+" icon to add alarm rule condition.'
    5:
        image: /images/helloworld/hello-world-pe-step-4-item-6-magenta.png
        title: 'Click the "Add key filter" button to specify a condition.'
    6:
        image: /images/helloworld/hello-world-pe-step-4-item-7-magenta.png 
        title: 'Select key type, input key name, select value type, and click "Add".'
    7:
        image: /images/helloworld/hello-world-pe-step-4-item-8-magenta.png
        title: 'Select operation and input threshold value. Click "Add".'
    8:
        image: /images/helloworld/hello-world-pe-step-4-item-9-magenta.png
        title: 'Click "Save".'
    9:
        image: /images/helloworld/hello-world-pe-step-4-item-10-magenta.png 
        title: 'Finally, click "Apply changes".'        

step5:
    0:
        image: /images/helloworld/hello-world-pe-step-5-item-1-magenta.png
        title: 'Notice that the new temperature telemetry causes a new active alarm.'
    1:
        image: /images/helloworld/hello-world-pe-step-5-item-2-magenta.png 
        title: 'User may acknowledge and clear the alarms.'     
        
step7:
    0:
        image: /images/helloworld/hello-world-pe-step-7-item-1-magenta.png 
        title: 'Navigate to the customer groups page.'
    1:
         image: /images/helloworld/hello-world-pe-step-7-item-2-magenta.png
         title: 'Then navigate to the default customer group "All".'
    2:
        image: /images/helloworld/hello-world-pe-step-7-item-3-magenta.png 
        title: 'Click the "+" sign to add a new customer.'
    3:
        image: /images/helloworld/hello-world-pe-step-7-item-4-magenta.png 
        title: 'Add customer title and click "Add".'
    4:
        image: /images/helloworld/hello-world-pe-step-7-item-5.png 
        title: 'Click  “Manage customer user groups”.'
    5:
        image: /images/helloworld/hello-world-pe-step-7-item-6.png 
        title: 'Open “Customer Users” group.'
    6:
        image: /images/helloworld/hello-world-pe-step-7-item-7.png 
        title: 'Click the “+” sign to add a User'
    7:
        image: /images/helloworld/hello-world-pe-step-7-item-8.png 
        title: 'Specify email that you will use to login as a customer user and click "Add".'
    8:
        image: /images/helloworld/hello-world-pe-step-7-item-9.png 
        title: 'Copy the activation link and save it to a safe place. You will use it later to set the password.'
    9:
        image: /images/helloworld/hello-world-pe-step-7-item-10.png
        title: 'Open user details'          
    10:
        image: /images/helloworld/hello-world-pe-step-7-item-11.png
        title: 'Toggle edit mode'
    11:
        image: /images/helloworld/hello-world-pe-step-7-item-12.png
        title: 'Select default dashboard and check "Always fullscreen". Apply changes.'  
    12:
        image: /images/helloworld/hello-world-pe-step-7-item-13.png 
        title: 'Use activation link to set the password. Click "Create Password". You will automatically login as a customer user.'
    13:
        image: /images/helloworld/hello-world-pe-step-7-item-14.png 
        title: 'You have logged in as a Customer User. You may browse the data and acknowledge/clear alarms.'
        
step71:
    0:
        image: /images/helloworld/hello-world-pe-step-7-item-1-magenta.png 
        title: 'Navigate to the customer groups page.'
    1:
         image: /images/helloworld/hello-world-pe-step-7-item-2-magenta.png
         title: 'Then navigate to the default customer group "All".'
    2:
        image: /images/helloworld/hello-world-pe-step-7-item-3-magenta.png 
        title: 'Click the "+" sign to add a customer.'
    3:
        image: /images/helloworld/hello-world-pe-step-7-item-4-magenta.png 
        title: 'Add customer title and click "Add".' 
        
step72:
    0:
        image: /images/helloworld/hello-world-pe-step-72-item-1-magenta.png 
        title: 'Select your device and click the "Change Owner" button.'
    1:
        image: /images/helloworld/hello-world-pe-step-72-item-2-magenta.png
        title: 'Start typing the customer name and then click on the customer item, then click the "Change owner" button.'
    # 2:
    #     image: /images/helloworld/hello-world-pe-step-72-item-3.png 
    #     title: 'Click the "Change owner" button.'
    2:
        image: /images/helloworld/hello-world-pe-step-72-item-4-magenta.png 
        title: 'Click "Yes". You can always change the owner back to the tenant.'
    3:
        image: /images/helloworld/hello-world-pe-step-72-item-5-magenta.png 
        title: 'Your device list should be empty now. This is because it displays the devices of the tenant. Navigate to the customer hierarchy to see your device.' 
    4:
        image: /images/helloworld/hello-world-pe-step-72-item-6-magenta.png 
        title: 'Your device is now in the Customers group "All".'                          
        
step73:
    0:
        image: /images/helloworld/hello-world-pe-step-73-item-1-magenta.png 
        title: 'Open "Dashboard Groups" and click the "Share" button.'
    1:
        image: /images/helloworld/hello-world-pe-step-73-item-2-magenta.png
        title: 'Select the customer and click "Share".'
        
step74:
    0:
        image: /images/helloworld/hello-world-pe-step-74-item-1-magenta.png 
        title: 'Open "Customers hierarchy", select "Customer Users" and click "Add".'
    1:
        image: /images/helloworld/hello-world-pe-step-74-item-2-magenta.png
        title: 'Specify email, first and last name. Click "Add".'
    2:
        image: /images/helloworld/hello-world-pe-step-74-item-3-magenta.png 
        title: 'Copy the activation link and save it to a safe place. Then click "OK".'
    3:
        image: /images/helloworld/hello-world-pe-step-74-item-4-magenta.png 
        title: 'Click on the user name to open user details. Toggle edit mode.' 
    4:
        image: /images/helloworld/hello-world-pe-step-74-item-5-magenta.png 
        title: 'Optionally, select the dashboard and enable "always fullscreen" mode. Apply changes.'

step75:
    0:
        image: /images/helloworld/hello-world-pe-step-75-item-1-magenta.png 
        title: 'Use activation link to set the password. Click "Create Password". You will automatically login as a customer user.'
    1:
        image: /images/helloworld/hello-world-pe-step-75-item-2-magenta.png 
        title: 'You have logged in as a Customer User. You may browse the data and acknowledge/clear alarms.'

        
mqttWindows:
    0:
        image: /images/helloworld/hello-world-pe-step-3-item-1-magenta.png
        title: 'Create new MQTT Client with the properties listed in screenshots below.' 
    1:
        image: /images/helloworld/hello-world-pe-step-3-item-2-magenta.png
        title: 'Populate the topic name and payload. Make sure the payload is a valid JSON document. Click "Publish" button.'
                           
---

{% assign docsPrefix = "pe/" %}
{% include docs/getting-started-guides/helloworld-pe.md %}
