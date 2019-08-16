#Testing PYHPECFM

All PRs must contain matching tests and a PR will not be accepted without passing the entire
test suite.

API calls have been recorded using the vcrpy library.

Travis-CI has been used for continous testing.

## Test environment

We acknowledge that different testing environments will have different IP addresses.
To mitigate these differences, we ask that developers place a new entry in their /etc/hosts file 
to point the hostname *cfmtest.local* to the address of their local CFM instance.

Note: It is manditory to use the hostname cfmtest.local as the vcrpy cassette files are using this hostname
and the Travis CI integration has been setup to use this hostname as well.

If you choose to use a different name the test will fail and your PR will not be accepted.

