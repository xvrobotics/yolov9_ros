// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from yolov9_msgs:msg/YoloDetection.idl
// generated code does not contain a copyright notice

#ifndef YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__TRAITS_HPP_
#define YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "yolov9_msgs/msg/detail/yolo_detection__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace yolov9_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const YoloDetection & msg,
  std::ostream & out)
{
  out << "{";
  // member: class_name
  {
    out << "class_name: ";
    rosidl_generator_traits::value_to_yaml(msg.class_name, out);
    out << ", ";
  }

  // member: confidence
  {
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << ", ";
  }

  // member: x_min
  {
    out << "x_min: ";
    rosidl_generator_traits::value_to_yaml(msg.x_min, out);
    out << ", ";
  }

  // member: y_min
  {
    out << "y_min: ";
    rosidl_generator_traits::value_to_yaml(msg.y_min, out);
    out << ", ";
  }

  // member: x_max
  {
    out << "x_max: ";
    rosidl_generator_traits::value_to_yaml(msg.x_max, out);
    out << ", ";
  }

  // member: y_max
  {
    out << "y_max: ";
    rosidl_generator_traits::value_to_yaml(msg.y_max, out);
    out << ", ";
  }

  // member: x_center
  {
    out << "x_center: ";
    rosidl_generator_traits::value_to_yaml(msg.x_center, out);
    out << ", ";
  }

  // member: y_center
  {
    out << "y_center: ";
    rosidl_generator_traits::value_to_yaml(msg.y_center, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const YoloDetection & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: class_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "class_name: ";
    rosidl_generator_traits::value_to_yaml(msg.class_name, out);
    out << "\n";
  }

  // member: confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << "\n";
  }

  // member: x_min
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_min: ";
    rosidl_generator_traits::value_to_yaml(msg.x_min, out);
    out << "\n";
  }

  // member: y_min
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_min: ";
    rosidl_generator_traits::value_to_yaml(msg.y_min, out);
    out << "\n";
  }

  // member: x_max
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_max: ";
    rosidl_generator_traits::value_to_yaml(msg.x_max, out);
    out << "\n";
  }

  // member: y_max
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_max: ";
    rosidl_generator_traits::value_to_yaml(msg.y_max, out);
    out << "\n";
  }

  // member: x_center
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_center: ";
    rosidl_generator_traits::value_to_yaml(msg.x_center, out);
    out << "\n";
  }

  // member: y_center
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_center: ";
    rosidl_generator_traits::value_to_yaml(msg.y_center, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const YoloDetection & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace yolov9_msgs

namespace rosidl_generator_traits
{

[[deprecated("use yolov9_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const yolov9_msgs::msg::YoloDetection & msg,
  std::ostream & out, size_t indentation = 0)
{
  yolov9_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use yolov9_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const yolov9_msgs::msg::YoloDetection & msg)
{
  return yolov9_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<yolov9_msgs::msg::YoloDetection>()
{
  return "yolov9_msgs::msg::YoloDetection";
}

template<>
inline const char * name<yolov9_msgs::msg::YoloDetection>()
{
  return "yolov9_msgs/msg/YoloDetection";
}

template<>
struct has_fixed_size<yolov9_msgs::msg::YoloDetection>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<yolov9_msgs::msg::YoloDetection>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<yolov9_msgs::msg::YoloDetection>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__TRAITS_HPP_
