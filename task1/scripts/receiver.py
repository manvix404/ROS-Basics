import rospy
from std_msgs.msg import Int16, Float32
def callback(data):
    rospy.loginfo(rospy.get_caller_id()+ "Received %dF",data.data)
    degree=(data.data-32)*(5/9)
    pub=rospy.Publisher('celcius',Float32)
    rate=rospy.Rate(1)
    #while not rospy.is_shutdown():
    rospy.loginfo(degree)
    pub.publish(degree)
    rate.sleep()

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('farenhite',Int16,callback)
    rospy.spin()

if __name__=='__main__':
    listener()
