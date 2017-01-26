# arti
Ansible plugin for finding the latest directory in artifactory

# Usage
Say you have an artifactory web directory like:
http:/artifactory.mydomain.com/ourcoolapp

with the following directories:
- coolapp-2016-05-01
- coolapp-2016-04-07
- coolapp-2016-03-22

You can run your task like so: 

    - debug: 
        msg: "{{ item }}"
      with_arti: "http:/artifactory.mydomain.com/ourcoolapp"
      
It should return `coolapp-2016-05-01`





