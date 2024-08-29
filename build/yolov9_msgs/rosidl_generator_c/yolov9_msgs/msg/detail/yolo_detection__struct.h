// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from yolov9_msgs:msg/YoloDetection.idl
// generated code does not contain a copyright notice

#ifndef YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__STRUCT_H_
#define YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'class_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/YoloDetection in the package yolov9_msgs.
typedef struct yolov9_msgs__msg__YoloDetection
{
  rosidl_runtime_c__String class_name;
  float confidence;
  float x_min;
  float y_min;
  float x_max;
  float y_max;
  float x_center;
  float y_center;
} yolov9_msgs__msg__YoloDetection;

// Struct for a sequence of yolov9_msgs__msg__YoloDetection.
typedef struct yolov9_msgs__msg__YoloDetection__Sequence
{
  yolov9_msgs__msg__YoloDetection * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} yolov9_msgs__msg__YoloDetection__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // YOLOV9_MSGS__MSG__DETAIL__YOLO_DETECTION__STRUCT_H_
