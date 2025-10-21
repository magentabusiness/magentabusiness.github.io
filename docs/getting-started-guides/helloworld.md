---
layout: docwithnav-pe
assignees:
- ashvayka
title: Getting Started with IoT Hub
description: Getting started with IoT Hub open-source IoT platform and simulated IoT devices
step1:
    0:
        image: /images/helloworld/getting-started-ce/hello-world-1-1-provision-device-1-ce.png 
        title: 'Log in to IoT Hub and navigate to the "Devices" page of the "Entities" section.'
    1:
        image: /images/helloworld/getting-started-ce/hello-world-1-1-provision-device-2-ce.png 
        title: 'Click on the "+" icon in the top right corner of the table and select "Add new device" from drop-down menu.'
    2:
        image: /images/helloworld/getting-started-ce/hello-world-1-1-provision-device-3-ce.png 
        title: 'Enter a device name (e.g., "My New Device") No other changes required at this time. Click "Add".'
    3:
        image: /images/helloworld/getting-started-ce/hello-world-1-1-provision-device-4-ce.png
        title: 'A window for checking the device connection will open — we&#39;ll skip this step for now and return to connection checking in the next step.'
    4:
        image: /images/helloworld/getting-started-ce/hello-world-1-1-provision-device-5-ce.png 
        title: 'Congratulations, you&#39;ve added your first device! As you add more devices, they will be added at the top of the table, as the table automatically sorts devices by their creation time, with the newest ones listed first.'

step11:
    0:
        image: /images/helloworld/getting-started-ce/hello-world-1-1-provision-device-6-ce.png 
        title: 'You will also receive a notification upon adding devices. Click the bell icon (top right) to view notifications.'

step2:
    0:
        image: /images/helloworld/getting-started-ce/check-connectivity-device-1-ce.png
        title: 'Click on your device, then click the "Check connectivity” button in the "Device details" window.'
    1:
        image: /images/helloworld/getting-started-ce/check-connectivity-device-2-ce.png
        title: 'In the opened window, choose your messaging protocol and operating system. Install any necessary client tools and copy the provided command.'
    2:
        image: /images/helloworld/getting-started-ce/check-connectivity-device-3-ce.png
        title: 'Execute the copied command in Terminal. Once telemetry data (e.g., temperature readings) is successfully published, the device status will change from "Inactive" to "Active," and you&#39;ll see the data displayed. You can now close the connectivity window.'

step3:
    0:
        image: /images/helloworld/getting-started-ce/hello-world-2-1-connect-device-3-ce.png
        title: 'Navigate to the "Latest telemetry" tab. You should see the previously published "temperature" readings.'
    1:
        image: /images/helloworld/hello-world-step-3-item-3.png 
        title: 'Navigate to the telemetry tab.'
        
step31:
    0:
        image: /images/helloworld/getting-started-ce/create-dashboard-1-ce.png
        title: 'Navigate to the "Dashboards" page through the main menu on the left of the screen. Then, click the "+" sign in the upper right corner of the screen, and select "Create new dashboard" from the drop-down menu.'
    1:
        image: /images/helloworld/getting-started-ce/create-dashboard-2-ce.png
        title: 'In the opened dialog, it is necessary to enter a dashboard title, description is optional. Click "Add".'
    2:
        image: /images/helloworld/getting-started-ce/create-dashboard-3-ce.png
        title: 'After creating the dashboard, it will open automatically, and you can immediately start adding widgets to it. To save the dashboard, click "Save" button in the upper right corner.'
    3:
        image: /images/helloworld/getting-started-ce/create-dashboard-4-ce.png
        title: 'Your first dashboard has been successfully created. As you continue to add new dashboards, they will appear at the top of the list. This default sorting is based on the creation timestamp.'
step32:
    0:
        image: /images/helloworld/hello-world-step-32-item-1.png 
        title: 'Enter edit mode. Click on the pencil button in the bottom right corner.'
    1:
        image: /images/helloworld/hello-world-step-32-item-2.png 
        title: 'Click the "Entity Aliases" icon in the top right part of the screen. You will see an empty list of Entity aliases.'
    2:
        image: /images/helloworld/hello-world-step-32-item-3.png 
        title: 'Click "Add alias".'
    3:
        image: /images/helloworld/hello-world-step-32-item-4.png 
        title: 'Input alias name, for example, "MyDevice". Select the "Single entity" Filter type. Select "Device" as Type and type "My New" to enable autocomplete. Choose your device from the auto-complete and click on it.'        
    4:
        image: /images/helloworld/hello-world-step-32-item-5.png 
        title: 'Click "Add" and then "Save".'        
    5:
        image: /images/helloworld/hello-world-step-32-item-6.png 
        title: 'Finally, click "Apply changes" in the dashboard editor to save the changes. Then you should enter edit mode again.'

step33:
    0:
        image: /images/helloworld/hello-world-step-33-item-1.png 
        title: 'Enter edit mode. Click on the "Add new widget" button. '
    1:
        image: /images/helloworld/hello-world-step-33-item-2.png 
        title: 'Select the "Cards" widget bundle. Select the "Latest values" tab. Click on the header of the Entities widget. The "Add Widget" window will appear.'
    2:
        image: /images/helloworld/hello-world-step-33-item-3.png 
        title: 'Click "Add" to add the data source. A widget may have multiple data sources, but we will use only one in this case.'
    3:
        image: /images/helloworld/hello-world-step-33-item-4.png 
        title: 'Select "MyDevice" entity alias. Then click on the input field on the right. The auto-complete with available data points will appear. Select "temperature" data point and click "Add".'        
    4:
        image: /images/helloworld/hello-world-step-33-item-5.png 
        title: 'Resize the widget to make it a little bigger. Just drag the bottom right corner of the widget. You can also play with the advanced settings if you would like to edit the widget.'
        
step34:
    0:
        image: /images/helloworld/hello-world-step-34-item-1.png 
        title: 'Enter Edit mode.'
    1:
        image: /images/helloworld/hello-world-step-34-item-2.png 
        title: 'Click the "Add new widget" icon in the bottom right corner of the screen.'
    2:
        image: /images/helloworld/hello-world-step-34-item-3.png 
        title: 'Click the "Create new widget" icon.'
    3:
        image: /images/helloworld/getting-started-ce/hello-world-3-4-add-alarm-widget-4-ce.png
        title: 'Specify the previously created device "My New Device" as the data source in the "Device" field. Next, we will configure the filters. All alarms have specific severities and statuses. Mark those you want to see in the widget. If none are marked, all alarms will be displayed regardless of their status or severity;'
    4:
        image: /images/helloworld/hello-world-step-34-item-5.png 
        title: 'Click the "Add Datasource" button.'
    5:
        image: /images/helloworld/hello-world-step-34-item-6.png 
        title: 'Select "MyDevice" Alias. Select the "temperature" key. Click "Add".'
    6:
        image: /images/helloworld/hello-world-step-34-item-7.png 
        title: 'Drag and Drop your widget to the desired space. Resize the widget. Apply changes.'
    7:
        image: /images/helloworld/hello-world-step-34-item-8.png 
        title: 'Publish different telemetry values multiple times Step 2. Note that the widget displays only one minute of data by default.'
    8:
        image: /images/helloworld/hello-world-step-34-item-9.png 
        title: 'Enter Edit mode. Open time selection window. Change the interval and aggregation function. Update the time window and apply changes.'

step35:
    0:
        image: /images/helloworld/hello-world-step-34-item-1.png 
        title: 'Enter Edit mode.'
    1:
        image: /images/helloworld/hello-world-step-34-item-2.png 
        title: 'Click the "Add new widget" icon in the bottom right corner of the screen.'
    2:
        image: /images/helloworld/hello-world-step-34-item-3.png 
        title: 'Click the "Create new widget" icon.'
    3:
        image: /images/helloworld/hello-world-step-35-item-3.png 
        title: 'Select the "Alarm widgets" bundle. Click on the "Alarms" widget header.'        
    4:
        image: /images/helloworld/hello-world-step-35-item-4.png 
        title: 'Select the "Entity" alarm source and "MyDevice" alias. Click "Add"'
    5:
        image: /images/helloworld/hello-world-step-35-item-5.png 
        title: 'Scroll down and locate the new "Alarms" widget. Drag and Drop widget to the top right corner of the dashboard.'
    6:
        image: /images/helloworld/hello-world-step-35-item-6.png 
        title: 'Resize the widget and apply changes.'

step4:
    0:
        image: /images/helloworld/hello-world-step-4-item-1.png 
        title: 'Navigate to the device profiles page.'
    1:
        image: /images/helloworld/hello-world-step-4-item-2.png 
        title: 'Click the default profile row. This will open device profile details.'
    2:
        image: /images/helloworld/hello-world-step-4-item-3.png 
        title: 'Select the "Alarm Rules" tab and toggle edit mode.'
    3:
        image: /images/helloworld/hello-world-step-4-item-4.png 
        title: 'Click "Add alarm rule".'        
    4:
        image: /images/helloworld/hello-world-step-4-item-5.png 
        title: 'Specify alarm type and click the "+" icon to add alarm rule condition.'
    5:
        image: /images/helloworld/hello-world-step-4-item-6.png 
        title: 'Click the "Add key filter" button to specify a condition.'
    6:
        image: /images/helloworld/hello-world-step-4-item-7.png 
        title: 'Select key type, input key name, select value type, and click "Add".'
    7:
        image: /images/helloworld/hello-world-step-4-item-8.png 
        title: 'Select operation and input threshold value. Click "Add".'
    8:
        image: /images/helloworld/hello-world-step-4-item-9.png 
        title: 'Click "Save".'
    9:
        image: /images/helloworld/hello-world-step-4-item-10.png 
        title: 'Finally, click "Apply changes".'        

step5:
    0:
        image: /images/helloworld/hello-world-step-5-item-1.png 
        title: 'Notice that the new temperature telemetry causes a new active alarm.'
    1:
        image: /images/helloworld/hello-world-step-5-item-2.png 
        title: 'User may acknowledge and clear the alarms.'     
        
step71:
    0:
        image: /images/helloworld/hello-world-step-7-item-1.png 
        title: 'Navigate to the Customers page.'
    1:
        image: /images/helloworld/hello-world-step-7-item-2.png 
        title: 'Click the "+" sign to add a customer.'
    2:
        image: /images/helloworld/hello-world-step-7-item-3.png 
        title: 'Add customer title and click "Add".'

step72:
    0:
        image: /images/helloworld/hello-world-step-71-item-1.png 
        title: 'Open Devices page. Click "Assign to customer" for "My New Device".'
    1:
        image: /images/helloworld/hello-world-step-71-item-2.png 
        title: 'Select "My New Customer" and click "Assign".'

step73:
    0:
        image: /images/helloworld/hello-world-step-71-item-3.png 
        title: 'Open Dashboards. Click "Manage assigned customers".'
    1:
        image: /images/helloworld/hello-world-step-71-item-4.png 
        title: 'Select "My New Customer" and click "Update".'

step74:
    0:
        image: /images/helloworld/hello-world-step-7-item-4.png 
        title: 'Navigate back to the "Customers" page and click the "manage customer users" icon.'        
    1:
        image: /images/helloworld/hello-world-step-7-item-5.png 
        title: 'Click the "Add user" icon.'        
    2:
        image: /images/helloworld/hello-world-step-7-item-6.png 
        title: 'Specify email that you will use to login as a customer user and click "Add".'
    3:
        image: /images/helloworld/hello-world-step-7-item-7.png 
        title: 'Copy the activation link and save it to a safe place. You will use it later to set the password.'
    4:
        image: /images/helloworld/hello-world-step-71-item-7.png 
        title: 'Open user details.'         
    5:
        image: /images/helloworld/hello-world-step-71-item-5.png 
        title: 'Toggle edit mode.'
    6:
        image: /images/helloworld/hello-world-step-71-item-6.png 
        title: 'Select default dashboard and check "Always fullscreen". Apply changes.'

step75:
    0:
        image: /images/helloworld/getting-started-ce/hello-world-7-5-activate-customer-user-1-ce.png
        title: 'Paste the previously copied link into a new browser tab and press the "Enter" key. Now create a password by entering it twice and clicking "Create Password".'
    1:
        image: /images/helloworld/getting-started-ce/hello-world-7-5-activate-customer-user-2-ce.png
        title: 'You are now logged in as a customer user. You may browse the data and acknowledge/clear alarms.'
mqttWindows:
    0:
        image: /images/helloworld/hello-world-step-3-item-1.png
        title: 'Create new MQTT Client with the properties listed in screenshots below.' 
    1:
        image: /images/helloworld/hello-world-step-3-item-2.png
        title: 'Populate the topic name and payload. Make sure the payload is a valid JSON document. Click "Publish" button.' 
                           
---

* TOC
{:toc}

  
This guide demonstrates basic usage of popular IoT Hub features. You will learn how to:

- Connect devices to IoT Hub
- Push data from devices to IoT Hub
- Build real-time dashboards
- Create a Customer and assign the dashboard with them.
- Define thresholds and trigger alarms
- Set up notifications via email, SMS, mobile apps, or integrate with third-party services.

For simplicity, we&#39;ll visualize data from a temperature sensor.

## Video tutorial

Prefer visual learning? Check out our step-by-step getting started video tutorial:

&nbsp;
<div id="video">  
    <div id="video_wrapper">
        <iframe src="https://www.youtube.com/embed/80L0ubQLXsc" frameborder="0" allowfullscreen></iframe>
    </div>
</div>

We will connect and visualize data from the temperature sensor to keep it simple. 
 
{% include templates/prerequisites.md %}

## Step 1. Provision Device

Let&#39;s add a device that sends temperature data to IoT Hub:

{% include images-gallery.html imageCollection="step1" showListImageTitles="true" %}

You will also receive a notification upon adding devices. Click the bell icon (top right) to view notifications.

{% include images-gallery.html imageCollection="step11" %}

[Learn more about notifications here](#step-6-alarm-notifications).

<br>
**Additional provisioning methods**
- [Bulk provisioning](/docs/user-guide/bulk-provisioning/){:target="_blank"}: Import multiple devices via CSV through the UI.
- [Device provisioning](/docs/user-guide/device-provisioning/){:target="_blank"}: Configure devices to self-register automatically. 
- [REST API](/docs/api/){:target="_blank"} provisioning: Manage devices programmatically through APIs.

## Step 2. Connect device

Let&#39;s verify your device&#39;s connection to IoT Hub:

{% include images-gallery.html imageCollection="step2" showListImageTitles="true" %}

<br>
Explore [IoT Hub API reference](/docs/{{docsPrefix}}api){:target="_blank"}. Here you will find more detailed information about all supported protocols for connecting devices.

{% capture connectdevicetogglespec %}
HTTP<small>Linux, macOS or Windows</small>%,%http%,%templates/helloworld/http.md%br%
MQTT<small>Linux or macOS</small>%,%mqtt-linux%,%templates/helloworld/mqtt-linux.md%br%
MQTT<small>Windows</small>%,%mqtt-windows%,%templates/helloworld/mqtt-windows.md%br%
CoAP<small>Linux or macOS</small>%,%coap%,%templates/helloworld/coap.md%br%
Other Protocols<small>Modbus, SNMP, LoRaWAN, etc</small>%,%other%,%templates/helloworld/other.md{% endcapture %}
{% include content-toggle.html content-toggle-id="connectdevice" toggle-spec=connectdevicetogglespec %}

Once you have successfully published the "temperature" readings, you should immediately see them in the Device Telemetry Tab:

Let&#39;s create a dashboard and add three widgets to it in order to display a list of entities and their latest values, as well as show alarm signals related to the specified entity.

## Step 3. Create Dashboard

We will create a dashboard and add the most popular widgets. See the instructions below. 

### Step 3.1 Create Empty Dashboard

{% include images-gallery.html imageCollection="step31" showListImageTitles="true" %}

### Step 3.2 Add Entity Alias

Alias is a reference to a single entity or group of entities that are used in the widgets.
Alias may be static or dynamic. For simplicity, we will use "Single entity" alias references the one and only entity ("My New Device" in our case).
It is possible to configure an alias that references multiple devices. For example, devices of a certain type or related to a certain asset. 
You may learn more about different aliases [here](/docs/user-guide/ui/aliases/).

{% include images-gallery.html imageCollection="step32" showListImageTitles="true" %}   

### Step 3.3 Add Table Widget

To add the table widget we need to select it from the widget library. Widgets are grouped into widget bundles.
Each widget has a data source. This is how the widget "knows" what data to display.
To see the latest value of our "temperature" data that we sent during step 2, we should configure the data source.

Let&#39;s add your first widget:

Congratulations! You have added the first widget. Now you can send new telemetry reading and it will immediately appear in the table. 

Congratulations! You&#39;ve added your first widget.

In the "Entities table" widget, there are two columns.
The first column displays the device&#39;s name, and the second column displays the value of the "temperature" key (device telemetry).
So, each column corresponds to an added key.

Now you are able to send a new telemetry reading (as in [Step 1](#step-1-provision-device)), and it will immediately appear in the table.

### Step 3.3 Add a Chart widget

Chart widgets allow you to display time series data with customizable line charts and bar charts.

To add the chart widget we need to select it from the widget library.
Chart widget displays multiple historical values of the same data key ("temperature" in our case).
We should also configure the time window to use the chart widget.

{% include images-gallery.html imageCollection="step34" showListImageTitles="true" %}

Now it&#39;s time to configure alarm rules and raise some alarms.

> **Note:** in this documentation, we are using a single device as a data source for the widgets. 
To use dynamic entities (for example, devices of a certain type or related to a certain asset) as data source, you should use the alias.
Alias is a reference to a single entity or a group of entities that are used in the widgets. 
You may learn more [about different aliases here](/docs/{{docsPrefix}}user-guide/ui/aliases/){:target="_blank"}.

{% include images-gallery.html imageCollection="step35" showListImageTitles="true" %}

We will use the [alarm rules](/docs/user-guide/device-profiles/#alarm-rules){:target="_blank"} feature to raise the alarm when the temperature reading exceeds 25 degrees.
To do this, we should edit the device profile and add a new alarm rule. 
The "My New Device" is using the "Default" device profile.
We recommend creating dedicated [device profiles](/docs/user-guide/device-profiles/){:target="_blank"} for each corresponding device type, but we&#39;ll skip this step here for simplicity.

{% include images-gallery.html imageCollection="step4" showListImageTitles="true" %}

## Step 5. Create Alarm

Now our alarm rule is active (see [Step 4](/docs/getting-started-guides/helloworld/#step-4-configure-alarm-rules)), 
and we should send new telemetry on behalf of the device (see [Step 2](/docs/getting-started-guides/helloworld/#step-2-connect-device)) to trigger the alarm.
Note that the temperature value should be 26 or higher to raise the alarm. Once we send a new temperature reading, we should immediately see a new alarm on our dashboard.

{% include images-gallery.html imageCollection="step5" showListImageTitles="true" %}

## Step 6. Alarm notifications

The IoT Hub [Notification center](/docs/{{docsPrefix}}user-guide/notifications/){:target="_blank"} allows personalized notifications to end-users regarding device activities, environmental changes, or events in your IoT ecosystem, and more. 
Notifications can be delivered via email, SMS, or integrated third-party systems.

## Step 7. Assign Device and Dashboard to Customer

Additionally, [ThingsBoard Mobile Application](/docs/mobile/){:target="_blank"} provides instant push notifications directly to your smartphone, ensuring you&#39;re always informed of critical events wherever you are.

Follow [this guide](/docs/mobile/getting-started/){:target="_blank"} to install the IoT Hub mobile app and set up notifications. 

Enjoy exploring IoT Hub!

## Step 7. Assign device and dashboard to customer

One of the most important IoT Hub features is the ability to assign Dashboards to Customers. 
You may assign different devices to different customers. Then, you may create a Dashboard(s) and assign it to multiple customers.
Each customer user will see his own devices and will not be able to see devices or any other data that belongs to a different customer.

We have already created a Device (see [Step 1](#step-1-provision-device)), and a Dashboard (see [Step 3](#step-3-create-dashboard)).
Now it&#39;s time to create a Customer and a Customer User and make sure they will have access to the device's data and the dashboard.

### Step 7.1 Create customer

Let&#39;s create a customer with the title "My New Customer". Please see the instruction below:

{% include images-gallery.html imageCollection="step71" showListImageTitles="true" %}

#### Step 7.2 Assign device to Customer

Let&#39;s assign device to the customer. The customer users will have ability to read and write telemetry and send commands to devices. 

{% include images-gallery.html imageCollection="step72" showListImageTitles="true" %}

#### Step 7.3 Assign dashboard to Customer

{% include images-gallery.html imageCollection="step72_1" showListImageTitles="true" %}

You can make the customer the owner of the device during its creation stage. To do this, follow this steps:

{% include images-gallery.html imageCollection="step72_2" showListImageTitles="true" %}

### Step 7.3 Assign the dashboard to customer

Let&#39;s share our dashboard with the customer. The customer users will have read-only access to the dashboard. 

{% include images-gallery.html imageCollection="step73" showListImageTitles="true" %}

#### Step 7.4 Create customer user

Now, let&#39;s create a user that will belong to the customer and will have `read-only` access both to the dashboard and the device.
You may optionally configure the dashboard to appear just after user logs in to the platform&#39;s web UI.

{% include images-gallery.html imageCollection="step74" showListImageTitles="true" %}

#### Step 7.5 Activate customer user

Finally, log in to IoT Hub as a customer user.

{% include images-gallery.html imageCollection="step75" showListImageTitles="true" %}

## Next steps

{% assign currentGuide = "GettingStartedGuides" %}{% include templates/guides-banner.md %}

## IoT Hub education course
 
 <div id="video">  
     <div id="video_wrapper">
         <iframe src="https://www.youtube.com/embed/videoseries?list=PLYEKB_XwLCZJ6T8RPLTjRwMw0eoabpEKO" frameborder="0" allowfullscreen></iframe>
     </div>
 </div>
 <p></p>


## Your feedback

Don&#39;t hesitate to star IoT Hub on [github](https://github.com/thingsboard/thingsboard){:target="_blank"} to help us spread the word. 
If you have any questions about this sample, please [contact us](/docs/contact-us/){:target="_blank"}.
