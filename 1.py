# Challenge
# Dot wants to find a connection to Europe that will give them the best value per hour of travel time. The following tickets are available for the connection:

# Vancouver - Toronto: 250 CAD, travel time 3.5 hours
# Vancouver - Ottawa: 280 CAD, travel time 4 hours
# Vancouver - Montreal: 240 CAD, travel time 4 hours
# Vancouver - Edmonton: 150 CAD, travel time 1.5 hours
# Vancouver - Calgary: 180 CAD, travel time 1 hour
# These tickets are available for the second leg of the trip:

# Ottawa - Berlin: 1350 CAD, layover: 3.5 hours, travel time 9 hours
# Montreal - London: 1300 CAD, layover: 2 hours, travel time 8 hours
# Edmonton - London: 1200 CAD, layover: 5 hours, travel time 10 hours
# Calgary - London: 1400 CAD, layover: 2.5 hours, travel time 10 hours
# Toronto - Munich: 990 CAD, layover: 1.5 hours, travel time 9.5 hours
# Using math operators in Python, find out which flight will give Dot the best value per hour of travel time.

# value = price_paid / travel_time

van_tor_price = 250
van_ott_price = 280
van_mon_price = 240
van_edm_price = 150
van_cal_price = 180

van_tor_travel_time = 3.5
van_ott_travel_time = 4
van_mon_travel_time = 4
van_edm_travel_time = 1.5
van_cal_travel_time = 1

ott_ber_price = 1350
mon_lon_price = 1300
edm_lon_price = 1290
cal_lon_price = 1400
tor_mun_price = 990

ott_layover = 3.5
mon_layover = 2
edm_layover = 5
cal_layover = 2.5
tor_layover = 1.5

ott_ber_travel_time = 9
mon_lon_travel_time = 8
edm_lon_travel_time = 10
cal_lon_travel_time = 10
tor_mun_travel_time = 9.5

# SOLUTION

print((van_tor_price + tor_mun_price) / (van_tor_travel_time + tor_layover + tor_mun_travel_time)) #85.51
print((van_ott_price + ott_ber_price) / (van_ott_travel_time + ott_layover + ott_ber_travel_time)) #98.78
print((van_mon_price + mon_lon_price) / (van_mon_travel_time + mon_layover + mon_lon_travel_time)) #110.0
print((van_edm_price + edm_lon_price) / (van_edm_travel_time + edm_layover + edm_lon_travel_time)) #87.27
print((van_cal_price + cal_lon_price) / (van_cal_travel_time + cal_layover + cal_lon_travel_time)) #117.03



# 85.51724137931035
# 98.78787878787878
# 110.0
# 87.27272727272727
# 117.03703703703704
# The flight with the best value is Vancouver -> Toronto -> Munich so we will board flight to Toronto
