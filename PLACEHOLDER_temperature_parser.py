# Placeholder parser, just returns a list of set temperatures so I can log them

temperatures = [10.0, 11.1, 12.2, 13.3, 14.4, 15.5, 16.6, 17.7, 18.8, 19.9]

temp_index = 0


def get_temp():
    global temp_index
    temp = temperatures[temp_index]
    temp_index = (temp_index + 1) % 10
    return temp
