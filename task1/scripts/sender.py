import rospy
import random
from std_msgs.msg import Int16

def send():
    pub=rospy.Publisher('farenhite',Int16)
    rospy.init_node('sender',anonymous=True)
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        x=random.randint(0,300)
        rospy.loginfo(x)
        pub.publish(x)
        rate.sleep()

if __name__ =='__main__':
    try:
        send()
    except rospy.ROSInterruptException:
        pass