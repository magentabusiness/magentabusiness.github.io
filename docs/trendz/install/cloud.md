---
layout: docwithnav-trendz
assignees:
- vparomskiy
title: Enable Trendz Analytics in ThinsgBoard Cloud 
description: Activate Trendz Analytics Cloud

cloudPlan:
  0:
    image: /images/trendz/cloud-1.webp
    title: 'Log in to IoT Hub account and select “Plan and Billing” menu option. Press “Update Plan” button'
  1:
    image: /images/trendz/cloud-2.webp
    title: 'Choose “IoT Hub + Trendz” and select the most suitable plan for you'
  2:
    image: /images/trendz/cloud-3.webp
    title: 'Reload the page to see new “Trendz Analytics” option in your IoT Hub Menu'

---

* TOC
{:toc}

## What is Trendz Cloud

The Trendz Analytics Cloud is a fully managed, scalable and fault-tolerant version of [Trendz Analytics product](/products/trendz/). It is already integrated with IoT Hub and can be used to analyze your data from IoT Hub.

- **Improved time to market.** Save time on maintenance of the platform or configuration of the features.
- **Reduced costs.** The cost of the cluster infrastructure is shared between the users of the platform.
- **High availability.** Trendz Cloud uses microservices architecture and is deployed in multiple availability zones.
- **Data durability.** Platform uses data replication and backup procedures to make sure you don't lose the data.

## Prerequisites

You need to have active IoT Hub account to active Trendz Analytics Cloud. If you don't have IoT Hub account yet, please [sign up](https://thingsboard.cloud/signup). 

## Activate Trendz Analytics Cloud

- Log in to IoT Hub account and select [Plan and Billing (North America)](https://thingsboard.cloud/billing) / [Plan and Billing (Europe)](https://eu.thingsboard.cloud/billing) menu option.
- Press **Update Plan** button
- Choose **IoT Hub + Trendz** and select the most suitable plan for you


{% include images-gallery.html imageCollection="cloudPlan" %}

## Next steps

{% assign currentGuide = "InstallationOptions" %}{% include templates/trndz-guides-banner.md %}
