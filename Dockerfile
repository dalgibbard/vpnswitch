from ubuntu
RUN apt-get update && apt-get install python-pip git -y && pip install flask gunicorn requests
RUN mkdir -p /opt && cd /opt && git clone https://github.com/dalgibbard/vpnswitch
EXPOSE 9911
WORKDIR /opt/vpnswitch/
CMD [ "/opt/vpnswitch/run_vpnswitch.sh" ]
