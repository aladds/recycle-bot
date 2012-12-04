; Auto-generated. Do not edit!


(cl:in-package ros_intro-msg)


;//! \htmlinclude JoyAxis.msg.html

(cl:defclass <JoyAxis> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (button1
    :reader button1
    :initarg :button1
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass JoyAxis (<JoyAxis>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <JoyAxis>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'JoyAxis)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_intro-msg:<JoyAxis> is deprecated: use ros_intro-msg:JoyAxis instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <JoyAxis>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_intro-msg:x-val is deprecated.  Use ros_intro-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <JoyAxis>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_intro-msg:y-val is deprecated.  Use ros_intro-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'button1-val :lambda-list '(m))
(cl:defmethod button1-val ((m <JoyAxis>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_intro-msg:button1-val is deprecated.  Use ros_intro-msg:button1 instead.")
  (button1 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <JoyAxis>) ostream)
  "Serializes a message object of type '<JoyAxis>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'button1) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <JoyAxis>) istream)
  "Deserializes a message object of type '<JoyAxis>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'button1) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<JoyAxis>)))
  "Returns string type for a message object of type '<JoyAxis>"
  "ros_intro/JoyAxis")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JoyAxis)))
  "Returns string type for a message object of type 'JoyAxis"
  "ros_intro/JoyAxis")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<JoyAxis>)))
  "Returns md5sum for a message object of type '<JoyAxis>"
  "a4d0515b204fdcee5c954ba17ec1d2fa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JoyAxis)))
  "Returns md5sum for a message object of type 'JoyAxis"
  "a4d0515b204fdcee5c954ba17ec1d2fa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JoyAxis>)))
  "Returns full string definition for message of type '<JoyAxis>"
  (cl:format cl:nil "float32 x~%float32 y~%bool button1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JoyAxis)))
  "Returns full string definition for message of type 'JoyAxis"
  (cl:format cl:nil "float32 x~%float32 y~%bool button1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JoyAxis>))
  (cl:+ 0
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JoyAxis>))
  "Converts a ROS message object to a list"
  (cl:list 'JoyAxis
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':button1 (button1 msg))
))
