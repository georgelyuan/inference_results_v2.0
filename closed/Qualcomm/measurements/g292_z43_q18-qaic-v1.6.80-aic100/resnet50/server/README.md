# Setup
Set up your system as detailed [here](https://github.com/krai/ck-qaic/blob/main/script/setup.docker/README.md).

# Benchmarking
```
SDK_VER=v1.6.80 POWER=no SUT=g292_z43_q18 DOCKER=yes SERVER_ONLY=yes WORKLOADS="resnet50" $(ck find ck-qaic:script:run)/run_datacenter.sh
```
