
(cl:in-package :asdf)

(defsystem "ros_intro-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "JoyAxis" :depends-on ("_package_JoyAxis"))
    (:file "_package_JoyAxis" :depends-on ("_package"))
  ))