def count_ip_occurances(ip_list: list) ->dict:
    """
    Counts occurances of IP addresses in a list
    """
    counts = {}
    for ip in ip_list:
        if ip in counts:
            counts[ip] += 1
        else:
            counts[ip] = 1
    return counts

if __name__ == "__main__":
    test_ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.5"]
    result = count_ip_occurances(test_ips)
    print(f"IP Counts : {result}")