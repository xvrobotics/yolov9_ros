// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from yolov9_msgs:msg/YoloDetection.idl
// generated code does not contain a copyright notice

#ifndef YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__BUILDER_HPP_
#define YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "yolov9_msgs/msg/detail/yolo_detection__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace yolov9_msgs
{

namespace msg
{

namespace builder
{

class Init_YoloDetection_y_center
{
public:
  explicit Init_YoloDetection_y_center(::yolov9_msgs::msg::YoloDetection & msg)
  : msg_(msg)
  {}
  ::yolov9_msgs::msg::YoloDetection y_center(::yolov9_msgs::msg::YoloDetection::_y_center_type arg)
  {
    msg_.y_center = std::move(arg);
    return std::move(msg_);
  }

private:
  ::yolov9_msgs::msg::YoloDetection msg_;
};

class Init_YoloDetection_x_center
{
public:
  explicit Init_YoloDetection_x_center(::yolov9_msgs::msg::YoloDetection & msg)
  : msg_(msg)
  {}
  Init_YoloDetection_y_center x_center(::yolov9_msgs::msg::YoloDetection::_x_center_type arg)
  {
    msg_.x_center = std::move(arg);
    return Init_YoloDetection_y_center(msg_);
  }

private:
  ::yolov9_msgs::msg::YoloDetection msg_;
};

class Init_YoloDetection_y_max
{
public:
  explicit Init_YoloDetection_y_max(::yolov9_msgs::msg::YoloDetection & msg)
  : msg_(msg)
  {}
  Init_YoloDetection_x_center y_max(::yolov9_msgs::msg::YoloDetection::_y_max_type arg)
  {
    msg_.y_max = std::move(arg);
    return Init_YoloDetection_x_center(msg_);
  }

private:
  ::yolov9_msgs::msg::YoloDetection msg_;
};

class Init_YoloDetection_x_max
{
public:
  explicit Init_YoloDetection_x_max(::yolov9_msgs::msg::YoloDetection & msg)
  : msg_(msg)
  {}
  Init_YoloDetection_y_max x_max(::yolov9_msgs::msg::YoloDetection::_x_max_type arg)
  {
    msg_.x_max = std::move(arg);
    return Init_YoloDetection_y_max(msg_);
  }

private:
  ::yolov9_msgs::msg::YoloDetection msg_;
};

class Init_YoloDetection_y_min
{
public:
  explicit Init_YoloDetection_y_min(::yolov9_msgs::msg::YoloDetection & msg)
  : msg_(msg)
  {}
  Init_YoloDetection_x_max y_min(::yolov9_msgs::msg::YoloDetection::_y_min_type arg)
  {
    msg_.y_min = std::move(arg);
    return Init_YoloDetection_x_max(msg_);
  }

private:
  ::yolov9_msgs::msg::YoloDetection msg_;
};

class Init_YoloDetection_x_min
{
public:
  explicit Init_YoloDetection_x_min(::yolov9_msgs::msg::YoloDetection & msg)
  : msg_(msg)
  {}
  Init_YoloDetection_y_min x_min(::yolov9_msgs::msg::YoloDetection::_x_min_type arg)
  {
    msg_.x_min = std::move(arg);
    return Init_YoloDetection_y_min(msg_);
  }

private:
  ::yolov9_msgs::msg::YoloDetection msg_;
};

class Init_YoloDetection_confidence
{
public:
  explicit Init_YoloDetection_confidence(::yolov9_msgs::msg::YoloDetection & msg)
  : msg_(msg)
  {}
  Init_YoloDetection_x_min confidence(::yolov9_msgs::msg::YoloDetection::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_YoloDetection_x_min(msg_);
  }

private:
  ::yolov9_msgs::msg::YoloDetection msg_;
};

class Init_YoloDetection_class_name
{
public:
  Init_YoloDetection_class_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_YoloDetection_confidence class_name(::yolov9_msgs::msg::YoloDetection::_class_name_type arg)
  {
    msg_.class_name = std::move(arg);
    return Init_YoloDetection_confidence(msg_);
  }

private:
  ::yolov9_msgs::msg::YoloDetection msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::yolov9_msgs::msg::YoloDetection>()
{
  return yolov9_msgs::msg::builder::Init_YoloDetection_class_name();
}

}  // namespace yolov9_msgs

#endif  // YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__BUILDER_HPP_
