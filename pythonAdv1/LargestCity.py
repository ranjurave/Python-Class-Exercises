cities = {"Auckland":123456,
          "Wellington":123457,
          "Dunedin":123454}
# greatest = {}
# for k, v in cities.items():
#     if v>123456:
#         print(f"Largerst city is {k}")

greatest = {k:v for k,v in cities.items() if v > 123459}
print(greatest)