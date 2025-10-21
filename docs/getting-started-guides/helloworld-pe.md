---
layout: docwithnav-pe
assignees:
- ashvayka
title: Getting Started with IoT Hub
description: Getting started with IoT Hub open-source IoT platform and simulated IoT devices
redirect_from: "/docs/pe/getting-started-guides/helloworld/"
step1:
    0:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-1-1-provision-device-1-pe.png
        title: 'Login to your IoT Hub instance and go to the "Devices" page of the "Entities" section.'
    1:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-1-1-provision-device-2-pe.png
        title: 'By default, you navigate to the device group "All". Click on the "+" icon in the top right corner of the table and then select "Add new device" from drop-down menu.'
    2:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-1-1-provision-device-3-pe.png
        title: 'Enter a device name (e.g., "My New Device") No other changes required at this time. Click "Add".'
    3:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-1-1-provision-device-4-pe.png
        title: 'A window for checking the device connection will open — we&#39;ll skip this step for now and return to connection checking in the next step.'
    4:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-1-1-provision-device-5-pe.png
        title: 'Congratulations, you&#39;ve added your first device! As you add more devices, they will be added at the top of the table, as the table automatically sorts devices by their creation time, with the newest ones listed first.'

step11:
    0:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-1-1-provision-device-6-pe.png
        title: 'You will also receive a notification upon adding devices. Click the bell icon (top right) to view notifications.'

step2:
    0:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/check-connectivity-device-1-pe.png
        title: 'Click on your device, then click the "Check connectivity" button in the "Device details" window.'
    1:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/check-connectivity-device-2-pe.png
        title: 'In the opened window, choose your messaging protocol and operating system. Install any necessary client tools and copy the provided command.'
    2:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/check-connectivity-device-3-pe.png
        title: 'Execute the copied command in Terminal. Once telemetry data (e.g., temperature readings) is successfully published, the device status will change from "Inactive" to "Active," and you&#39;ll see the data displayed. You can now close the connectivity window.'

step3:
    0:
        image: /images/helloworld/hello-world-pe-step-2-item-1-magenta.png 
        title: 'Click on the device row in the table to open device details;'
    1:
        image: /images/helloworld/hello-world-pe-step-2-item-4-magenta.png
        title: 'Navigate to the telemetry tab.'
        
step31:
    0:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/create-dashboard-1-pe.png
        title: 'Navigate to the "Dashboards" page through the main menu on the left of the screen. By default, you navigate to the dashboard group "All".'
    1:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/create-dashboard-2-pe.png
        title: 'Click the "+" sign in the upper right corner of the screen, and select "Create new dashboard" from the drop-down menu.'
    2:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/create-dashboard-3-pe.png
        title: 'In the opened dialog, it is necessary to enter a dashboard title, description is optional. Click "Add".'
    3:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/create-dashboard-4-pe.png
        title: 'After creating the dashboard, it will open automatically, and you can immediately start adding widgets to it. To save the dashboard, click "Save" button in the upper right corner.'
    4:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/create-dashboard-5-pe.png
        title: 'Your first dashboard has been successfully created. As you continue to add new dashboards, they will appear at the top of the list. This default sorting is based on the creation timestamp.'

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
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-3-4-add-alarm-widget-4-pe.png
        title: 'Specify the previously created device "My New Device" as the data source in the "Device" field. Next, we will configure the filters. All alarms have specific severities and statuses. Mark those you want to see in the widget. If none are marked, all alarms will be displayed regardless of their status or severity;'
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
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-7-create-customer-3-pe.png
        title: 'If needed, you can assign a different owner for this customer. We will leave this option unchanged. Enter a name for the new group and click "Create a new one!";'
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
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-5-pe.png
        title: 'In the next window, click "Add" button to create a device group;'
    5:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-6-pe.png
        title: 'Click "Update" to add to the group and change the owner of your device. You can always change the owner back to the tenant;'
    6:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-7-pe.png
        title: 'By default, the general device list displays both tenant devices and devices of your customers. Disable "Include customer entities" to only see tenant devices in the device list;'
    7:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-8-pe.png
        title: 'Your device list should be empty now.'

step72_1:
    0:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-9-pe.png
        title: 'Navigate to "Customers" page. Find your customer in the list of customers and then click on the "Manage customer devices" icon;'
    1:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-10-pe.png
        title: 'Your device is owned by the customer and is located in the customer&#39;s device group "My Devices".'

step72_2:
    0:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-11-pe.png
        title: 'Open the "Devices" page. Click on the "+" icon in the top right corner of the table and then select "Add new device" from drop-down menu;'
    1:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-12-pe.png
        title: 'Input device name (for example, "Thermostat") and select the new owner in the "Owner" field. Then, click "Add";'
    2:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-13-pe.png
        title: 'Close check connectivity window;'
    3:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-assign-device-to-customer-14-pe.png
        title: 'The device has been created, and it immediately belongs to your customer.'

step73:
    0:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-share-the-dashboard-3-pe.png
        title: 'Open the "Dashboards" page and go to the "Groups" tab. Click the "Share" icon next to the "All" dashboard group;'
    1:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-share-the-dashboard-4-pe.png
        title: 'Select the customer you want to share the dashboard with and set the permission level. In this case, choose "Read", then click "Share".'

step73_1:
    0:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-share-the-dashboard-5-pe.png
        title: 'On the "All" tab of the "Dashboards" page, click on the "+" icon in the top right corner of the table and select "Create new dashboard" from the drop-down menu;'
    1:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-share-the-dashboard-6-pe.png
        title: 'Enter a name for the dashboard (e.g., "Thermostats"). In the "Groups" field of the "Owner and groups" section, select an existing group or enter a name for a new dashboard group (for example, "Thermostats group") and click "Create a new one!";'
    2:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-share-the-dashboard-7-pe.png
        title: 'In the "Add entity group" window that opens, click "Next: Share entity group";'
    3:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-share-the-dashboard-8-pe.png
        title: 'Check the "Share entity group" box, select the customer to share the dashboard with, and set their permissions. Then click "Add";'
    4:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-share-the-dashboard-9-pe.png
        title: 'Click "Add" again to confirm dashboard creation;'
    5:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-share-the-dashboard-10-pe.png
        title: 'The new dashboard will open automatically — click "Save" in the top-right corner;'
    6:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-71-share-the-dashboard-11-pe.png
        title: 'Your dashboard has been created and placed in the "Thermostats group". You can quickly access it by clicking the group name.'

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
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-7-5-activate-customer-user-1-pe.png
        title: 'Paste the previously copied link into a new browser tab and press the "Enter" key. Now create a password by entering it twice and clicking "Create Password".'
    1:
        image: https://img.thingsboard.io/helloworld/getting-started-pe/hello-world-7-5-activate-customer-user-2-pe.png
        title: 'You are now logged in as a customer user. Since this user has read-only access, you can view device data and its alarms, but you cannot acknowledge or clear them.'

        
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
