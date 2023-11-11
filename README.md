# KNFK website repo
This repo is used to host code for our main website of our club.

## Hosting and setup
Our website is hosted on our private server in faculty of physics in Warsaw
University of Technology. 

Current URL: 
```
www-knfk.fizyka.pw.edu.pl
```
Current IP:
```
194.29.174.207
```

## For developers:
Our server is virtualised into multiple pools. This site is hosted on pool
`kubit01`. Only admin has access to it (only he knows the password).

VM that is actually running the site is called `siteHostingVm`

To replicate exact state of current server following steps need to be taken:
- Create new VM
    - Bridge needs to be set to vmbr1 and VLAN to 85
    - Rest is optional but preferably a good amount of storage and memory +
      cores should be allocated.
    - Setup OS
    - Connect to internet
- Setup docker
    - install docker
    - login as user
    - pull images
    - copy docker compose
    - run docker compose 

After all this you should have a running site available from outside server.

Now, the only thing left to do is for you to beg the PW IT department to update 
DNS to map VMs IP to www-knfk.fizyka.pw.edu.pl (new VMs ip almost certainly
will have different IP than it has now but if you manage to have change it to
`194.29.174.207` then there should be no issue).

