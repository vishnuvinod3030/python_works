#1800 to 2024
years=[y for y in range(1800,2025) ]
print(years)

# cen_year=[y for y in years if y%100==0]
# print(cen_year)

leap_years=[y for y in years if (y%100==0 and y%400==0) or (y%100!=0 and y%4==0)]
print(1900 in leap_years)