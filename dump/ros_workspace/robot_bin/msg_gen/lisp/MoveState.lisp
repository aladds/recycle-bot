; Auto-generated. Do not edit!


(cl:in-package robot_bin-msg)


;//! \htmlinclude MoveState.msg.html

(cl:defclass <MoveState> (roslisp-msg-protocol:ros-message)
  ((moving
    :reader moving
    :initarg :moving
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass MoveState (<MoveState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_bin-msg:<MoveState> is deprecated: use robot_bin-msg:MoveState instead.")))

(cl:ensure-generic-function 'moving-val :lambda-list '(m))
(cl:defmethod moving-val ((m <MoveState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_bin-msg:moving-val is deprecated.  Use robot_bin-msg:moving instead.")
  (moving m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveState>) ostream)
  "Serializes a message object of type '<MoveState>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'moving) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveState>) istream)
  "Deserializes a message object of type '<MoveState>"
    (cl:setf (cl:slot-value msg 'moving) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveState>)))
  "Returns string type for a message object of type '<MoveState>"
  "robot_bin/MoveState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveState)))
  "Returns string type for a message object of type 'MoveState"
  "robot_bin/MoveState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveState>)))
  "Returns md5sum for a message object of type '<MoveState>"
  "9104f1a32b4fbf4d3c8c80d9b9493250")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveState)))
  "Returns md5sum for a message object of type 'MoveState"
  "9104f1a32b4fbf4d3c8c80d9b9493250")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveState>)))
  "Returns full string definition for message of type '<MoveState>"
  (cl:format cl:nil "bool moving~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveState)))
  "Returns full string definition for message of type 'MoveState"
  (cl:format cl:nil "bool moving~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveState>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveState>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveState
    (cl:cons ':moving (moving msg))
))
