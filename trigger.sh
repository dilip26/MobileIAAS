daemon()
{
echo 'daemon bro'
intrfc=$(ifconfig |grep "wl"|awk '{print $1}')
echo $intrfc
tcpdump -i $intrfc icmp and icmp[icmptype]=icmp-echo -c 1
python intermediate_reply_mac.py
}

daemon
echo "launched"

