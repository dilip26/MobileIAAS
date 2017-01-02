daemon():
{
tcpdump -i wlo1 icmp and icmp[icmptype]=icmp-echo -c 1
python /home/akshay/MobileIAAS/intermediate_reply_mac.py
}


#while true:
daemon()

echo "launched"

