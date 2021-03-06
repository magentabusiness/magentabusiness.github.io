* TOC
{:toc}

IoT Hub rule engine is based on two main components: the actor model and message queue.

<br/>

![image](/images/user-guide/rule-engine-2-0/rule-engine-architecture.svg)
 
### Actor model

Actor model enables high performance and concurrent processing of messages from device transport layer as long as server-side API calls. 
IoT Hub uses own Actor System implementation that is sharpened for our use case. 
There are two main actors related to the rule engine: Rule Chain Actor and Rule Node Actor.

#### Rule Chain Actor

Rule Chain actor is responsible for rule node configuration, routing messages between rule nodes, and handling queue put and ack commands.
Each Rule Chain Actor represent single rule chain configured by the user. Rule Chain Actor is parent for multiple Rule Node actors.

#### Rule Node Actor

Rule Node actor is responsible for processing of the incoming messages.
{% unless docsPrefix == 'paas/' %} The logic of message processing is highly customizable.
There are many built-in implementations of the RuleNodes and you can develop your own, custom rule node implementations as well.
See [Rule Node Development](/docs/{{docsPrefix}}user-guide/contribution/rule-node-development/) guide for more details.
{% endunless %}

## Next steps

{% assign currentGuide = "DataProcessing" %}{% include templates/multi-project-guides-banner.md %}
