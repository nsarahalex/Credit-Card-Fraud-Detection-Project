import pandas as pd
  #The data frame
data = {'ip_addresses' : ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.5"]}
df = pd.DataFrame(data)

ip_counts = df['ip_addresses'].value_counts()
print(ip_counts)