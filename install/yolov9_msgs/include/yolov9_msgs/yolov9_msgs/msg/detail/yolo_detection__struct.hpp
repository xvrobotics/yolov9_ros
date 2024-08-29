// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from yolov9_msgs:msg/YoloDetection.idl
// generated code does not contain a copyright notice

#ifndef YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__STRUCT_HPP_
#define YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__yolov9_msgs__msg__YoloDetection __attribute__((deprecated))
#else
# define DEPRECATED__yolov9_msgs__msg__YoloDetection __declspec(deprecated)
#endif

namespace yolov9_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct YoloDetection_
{
  using Type = YoloDetection_<ContainerAllocator>;

  explicit YoloDetection_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->class_name = "";
      this->confidence = 0.0f;
      this->x_min = 0.0f;
      this->y_min = 0.0f;
      this->x_max = 0.0f;
      this->y_max = 0.0f;
      this->x_center = 0.0f;
      this->y_center = 0.0f;
    }
  }

  explicit YoloDetection_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : class_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->class_name = "";
      this->confidence = 0.0f;
      this->x_min = 0.0f;
      this->y_min = 0.0f;
      this->x_max = 0.0f;
      this->y_max = 0.0f;
      this->x_center = 0.0f;
      this->y_center = 0.0f;
    }
  }

  // field types and members
  using _class_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _class_name_type class_name;
  using _confidence_type =
    float;
  _confidence_type confidence;
  using _x_min_type =
    float;
  _x_min_type x_min;
  using _y_min_type =
    float;
  _y_min_type y_min;
  using _x_max_type =
    float;
  _x_max_type x_max;
  using _y_max_type =
    float;
  _y_max_type y_max;
  using _x_center_type =
    float;
  _x_center_type x_center;
  using _y_center_type =
    float;
  _y_center_type y_center;

  // setters for named parameter idiom
  Type & set__class_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->class_name = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__x_min(
    const float & _arg)
  {
    this->x_min = _arg;
    return *this;
  }
  Type & set__y_min(
    const float & _arg)
  {
    this->y_min = _arg;
    return *this;
  }
  Type & set__x_max(
    const float & _arg)
  {
    this->x_max = _arg;
    return *this;
  }
  Type & set__y_max(
    const float & _arg)
  {
    this->y_max = _arg;
    return *this;
  }
  Type & set__x_center(
    const float & _arg)
  {
    this->x_center = _arg;
    return *this;
  }
  Type & set__y_center(
    const float & _arg)
  {
    this->y_center = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    yolov9_msgs::msg::YoloDetection_<ContainerAllocator> *;
  using ConstRawPtr =
    const yolov9_msgs::msg::YoloDetection_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<yolov9_msgs::msg::YoloDetection_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<yolov9_msgs::msg::YoloDetection_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      yolov9_msgs::msg::YoloDetection_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<yolov9_msgs::msg::YoloDetection_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      yolov9_msgs::msg::YoloDetection_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<yolov9_msgs::msg::YoloDetection_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<yolov9_msgs::msg::YoloDetection_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<yolov9_msgs::msg::YoloDetection_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__yolov9_msgs__msg__YoloDetection
    std::shared_ptr<yolov9_msgs::msg::YoloDetection_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__yolov9_msgs__msg__YoloDetection
    std::shared_ptr<yolov9_msgs::msg::YoloDetection_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const YoloDetection_ & other) const
  {
    if (this->class_name != other.class_name) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->x_min != other.x_min) {
      return false;
    }
    if (this->y_min != other.y_min) {
      return false;
    }
    if (this->x_max != other.x_max) {
      return false;
    }
    if (this->y_max != other.y_max) {
      return false;
    }
    if (this->x_center != other.x_center) {
      return false;
    }
    if (this->y_center != other.y_center) {
      return false;
    }
    return true;
  }
  bool operator!=(const YoloDetection_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct YoloDetection_

// alias to use template instance with default allocator
using YoloDetection =
  yolov9_msgs::msg::YoloDetection_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace yolov9_msgs

#endif  // YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__STRUCT_HPP_
