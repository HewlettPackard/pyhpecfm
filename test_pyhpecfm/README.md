#Testing PYHPECFM

All PRs must contain matching tests and a PR will not be accepted without passing the entire
test suite.

API calls have been recorded using the vcrpy library.

Travis-CI has been used for continuous testing.

## Test environment

We acknowledge that different testing environments will have different IP addresses.
To mitigate these differences, we ask that developers place a new entry in their /etc/hosts file 
to point the hostname *cfmtest.local* to the address of their local CFM instance.

Note: It is mandatory to use the hostname cfmtest.local as the vcrpy cassette files are using this hostname
and the Travis CI integration has been setup to use this hostname as well.

Hint: You can set this host name in your /etc/hosts file.

## Exporting Environment Variables

On a macOS machines, the following commands should be used to make environmental variables available

export CFM_IP=cfmtest.local  #required
export CFM_USERNAME= %your_username%  #should match your system
export CFM_PASSWORD= %your_password%  #should match your system

If you choose to use a different name the test will fail and your PR will not be accepted.

