import matplotlib.pylab as plt
import math

plt.subplot(111, aspect=True)

seat_tube_len = 520
top_tube_len = 556
head_tube_len = 155
head_tube_angle = 73.25
seat_tube_angle = 73.5
chainstay_len = 410
wheelbase = 988
stack = 567
reach = 391
saddle_height = 800
y_rh = 70

head_tube_angle = math.radians(head_tube_angle)
seat_tube_angle = math.radians(seat_tube_angle)

plt.plot([0, chainstay_len], [y_rh, 0], 'g')
#plt.plot([chainstay_len, chainstay_len-1.2*seat_tube_len*math.cos(seat_tube_angle)],
#         [0, 1.2*seat_tube_len*math.sin(seat_tube_angle)], 'k--', alpha=0.5)
plt.plot([0, chainstay_len-seat_tube_len*math.cos(seat_tube_angle)],
         [y_rh, seat_tube_len*math.sin(seat_tube_angle)], 'g')
plt.plot([chainstay_len-seat_tube_len*math.cos(seat_tube_angle), chainstay_len+reach],
         [seat_tube_len*math.sin(seat_tube_angle), stack], 'g')
plt.plot([chainstay_len, chainstay_len-seat_tube_len*math.cos(seat_tube_angle)],
         [0, seat_tube_len*math.sin(seat_tube_angle)], 'g')
plt.plot([chainstay_len, chainstay_len+reach],
         [0, stack], 'g')
plt.plot([chainstay_len+reach, wheelbase],
         [stack, y_rh], 'g', label=r'$\mathrm{Canyon\, ULTIMATE}$')


seat_tube_len = 545
top_tube_len = 547
head_tube_len = 159
head_tube_angle = 73.3
seat_tube_angle = 73.5
chainstay_len = 415
wheelbase = 989
stack = 590
reach = 380
saddle_height = 800
y_rh = 70

head_tube_angle = math.radians(head_tube_angle)
seat_tube_angle = math.radians(seat_tube_angle)

plt.plot([0, chainstay_len], [y_rh, 0], 'b')
#plt.plot([chainstay_len, chainstay_len-1.2*seat_tube_len*math.cos(seat_tube_angle)],
#         [0, 1.2*seat_tube_len*math.sin(seat_tube_angle)], 'k--', alpha=0.5)
plt.plot([0, chainstay_len-seat_tube_len*math.cos(seat_tube_angle)],
         [y_rh, seat_tube_len*math.sin(seat_tube_angle)], 'b')
plt.plot([chainstay_len-seat_tube_len*math.cos(seat_tube_angle), chainstay_len+reach],
         [seat_tube_len*math.sin(seat_tube_angle), stack], 'b')
plt.plot([chainstay_len, chainstay_len-seat_tube_len*math.cos(seat_tube_angle)],
         [0, seat_tube_len*math.sin(seat_tube_angle)], 'b')
plt.plot([chainstay_len, chainstay_len+reach],
         [0, stack], 'b')
plt.plot([chainstay_len+reach, wheelbase],
         [stack, y_rh], 'b', label=r'$\mathrm{Canyon\, ENDURACE}$')

plt.legend(loc='best')
plt.show()