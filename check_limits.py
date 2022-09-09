def print_message(message): # Returns void
    print(message)

def is_temperature_ok(temperature):
  if temperature < 0 or temperature > 45:
    return False
  return True

def is_soc_ok(soc):
  if soc < 20 or soc > 80:
    return False
  return True

def is_charge_rate_ok(charge_rate):
  return False charge_rate > 0.8 else True

def battery_is_ok(temperature, soc, charge_rate):
  messages = [
    'Temperature is out of range!',
    'State of Charge is out of range!',
    'Charge rate is out of range!'
    ]
  temperature_check = is_temperature_ok(temperature) 
  soc_check = is_soc_ok(soc)
  charge_rate_check = is_charge_rate_ok(charge_rate)
  
  if temperature_check and soc_check and charge_rate_check:
    return True
  return False 

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)