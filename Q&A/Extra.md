
#Docker

1. Difference between expose & Publish 

- EXPOSE is used in the Dockerfile to document the intended ports that the container should expose, while the -p or --publish option is used during runtime to map those container ports to specific ports on the host machine. The EXPOSE instruction alone doesn't make the container's ports accessible from the host; it's more like a hint to users or developers about the expected ports.
