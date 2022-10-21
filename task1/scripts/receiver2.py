import rospy
from std_msgs.msg import Float32

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+ "Converted value %fC",data.data)

def listener():
    rospy.init_node('listener2',anonymous=True)
    rospy.Subscriber('celcius',Float32,callback)
    rospy.spin()

if __name__=='__main__':
    listener()