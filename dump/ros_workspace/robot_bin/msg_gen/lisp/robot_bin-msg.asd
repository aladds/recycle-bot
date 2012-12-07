
(cl:in-package :asdf)

(defsystem "robot_bin-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MoveState" :depends-on ("_package_MoveState"))
    (:file "_package_MoveState" :depends-on ("_package"))
  ))