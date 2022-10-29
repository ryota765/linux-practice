FROM ubuntu:20.04

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV APP_ROOT /usr/src
WORKDIR $APP_ROOT

RUN apt-get update && \
    apt-get install -y binutils build-essential sysstat python3-matplotlib python3-pil fonts-takao fio qemu-kvm virt-manager libvirt-clients virtinst jq docker.io containerd libvirt-daemon-system strace && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*