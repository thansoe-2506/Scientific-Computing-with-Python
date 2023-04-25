def add_time(start, duration, day=''):
      days = {
            0:'Monday',
            1:'Tuesday',
            2:'Wednesday',
            3:'Thursday',
            4:'Friday',
            5:'Saturday',
            6:'Sunday'
      }
      day_index = 0
      str_day = ''

      
      time_ = start.split()[0]
      am_pm = start.split()[1]

      s_hour = int(time_.split(':')[0])
      s_minute = int(time_.split(':')[1])

      a_hour = int(duration.split(':')[0])
      a_minute = int(duration.split(':')[1])

      n_hour = s_hour+a_hour
      n_minute = s_minute+a_minute

      if n_minute >= 60:
            n_minute -= 60
            n_hour += 1

      if n_hour >= 12:
            circle = n_hour // 12   
            if am_pm == 'PM':
                  day_count = (circle //2 ) + 1         
            else:
                  day_count = (circle // 2)

            

            if day != '':
                  for key, value in days.items():
                        if value == day.title():
                              day_index = key
                  temp = day_count % 7
                  day_index = day_index + temp

            str_day = ''
            if day_count == 1 and am_pm == 'AM':
                  str_day = ''
                  day_count = 0
                  day_index -= 1

            elif day_count > 1 and am_pm == 'AM':
                  day_count -= 1
            if day_count == 1:
                  str_day = '(next day)'
            elif day_count > 1:
                  str_day = '('+str(day_count)+' days later)'

            if circle % 2 == 0:
                  pass
            else:
                  if am_pm == 'AM': am_pm = 'PM'
                  elif am_pm == 'PM': am_pm = 'AM'
            
            n_hour = n_hour % 12
            if n_hour == 0:
                  n_hour = 12


      str_n_minute = ''
      if n_minute < 10:
            str_n_minute = '0' + str(n_minute)
      else:
            str_n_minute = str(n_minute)

      if day_index < 0 or day == '':
            new_time = str(n_hour) + ':' + str_n_minute + ' ' + am_pm + ' ' + str_day
      else:
            new_time = str(n_hour) + ':' + str_n_minute + ' ' + am_pm + ', ' + days[day_index] + ' ' + str_day


      return new_time.strip()

print(add_time("2:59 AM", "24:00", "saturDay"))
