---
layout: blogpost
title:  "A Multicast Method for Swarm State Management"
date:   2020-04-29 1:20:01 -0600
categories:
---

<h2>A Multicast Method for Swarm State Management</h2>

---

To join a swarm network an agent begins by joining a predefined multicast group at an IP address within the range <code>224.0.0.0 - 224.0.0.255</code>. There can be many multicast groups, but the agent may only join one at a time. It is expected that the programmer has divided the multicast groups by purpose, for the use cases described here only one group is used, which is at the default <code>244.0.0.1</code>. Each agent has a specific state $$A_s$$ which is encoded as a byte and can be determined via a lookup table. Additionally, each agent also has an internal member struct which contains a 16 byte string from the agent's name, the agent's state byte, and the agent's 4 byte IPv4 address. These member structs are multicast to every member of the swarm network at a predefined frequency, though the programmer may change this frequency when initiating the agent. The primary purpose of the multicast group is to distribute telemetry, device information, and IPv4 information to the members of the multicast group. The most commonly shared information is the member struct, tough other telemetry can be shared. This information is delivered via a UDP packet with a payload of only 37 bytes. All agents make decisions based off of the information stored within these packets. Should the program receives a <code>SIG INT</code> or other shutdown message the swarm net manager will multicast that the agent is unavailable. If an agent has not communicated to the multicast group within a predefined amount of time, then the members of that group also consider that agent unavailable.

![N_view_diagram](/img/blog/swarmjoin.png)

Independent from the frequent state multicast, which runs in a separate thread, when an agent changes state it also multicasts the new state. This is done so that there is no delay between the agent's internal knowledge of its state change and the group's knowledge of the agent's state change. Relying only on the frequent state multicast could cause state miss-matches between the group or an agent. Additionally, it would allow for an intermediary state, which the agent is only in briefly, to be missed by the group. Thus, a new thread is created and then destroyed to handle an adhoc state multicast. Such intermediary cases are not edge cases, as I will mention briefly in the following section, and are used to synchronize agents when cooperating. When in a particular synchronization state (which are considered intermediary) an agent will open up a TCP socket for high volume data transmission.

The swarm state managment is available here: <a href="https://github.com/piepieninja/SSRL-Swarm-Net" target="_blank">https://github.com/piepieninja/SSRL-Swarm-Net</a> (to be released late june).

<br><br><br><br><br><br><br><br><br><br>
<small>This is copied from a section of my thesis. If you found this useful to your research please consider using the following bibtex:</small>

<p class="bibtex">
  @mastersthesis{CalebAdamsMSThesis, <br>
    &emsp; author={Caleb Ashmore Adams}, <br>
    &emsp; title={High Performance Computation with Small Satellites and Small Satellite Swarms for 3D Reconstruction}, <br>
    &emsp; school={The University of Georgia}, <br>
    &emsp; url={http://piepieninja.github.io/research-papers/thesis-pre-release.pdf},<br>
    &emsp; year=2020, <br>
    &emsp; month=may <br>
  }
</p>

<br><br><br><br>
